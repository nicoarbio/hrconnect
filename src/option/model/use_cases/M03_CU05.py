import datetime
from src.option.model.AbstractOption import AbstractOption
from src.utils.Logging import Logging
from src.config.BeanManager import BeanManager
from src.utils.IOUtils import IOUtils
from src.staff_sign.model.StaffSign import StaffSign


class M03_CU05(AbstractOption):
    """
    Descripción: El sistema permite a un ColaboradorRRHH cargar manualmente las fichadas  de los empleados en caso de haber registrado las mismas a mano.
    """

    def get_id(self):
        return "M03_CU05"

    def get_description(self):
        office_services_check_service = BeanManager.get_OfficeServicesCheckService()
        status = " (HABILITADO)" if office_services_check_service.is_manual_sign_enabled() else " (DESHABILITADO)"
        return "Cargar Fichada Manualmente" + status

    def execute_option_use_case(self):
        Logging.clear()
        Logging.print(self.get_option_name())
        office_services_check_service = BeanManager.get_OfficeServicesCheckService()
        if not office_services_check_service.is_manual_sign_enabled():
            Logging.print("Los servicios manuales de fichada no están habilitados. El suministro de energía e internet se encuentran estables")
            input("Presione Enter para continuar...")
            Logging.clear()
            return

        staff_sign_dao = BeanManager.get_StaffSignDAO()
        user_dao = BeanManager.get_UserDAO()

        inputs_ok = False
        Logging.print("Nota: ingrese 'q' para salir en cualquier momento.")
        while inputs_ok == False:
            employee_email = IOUtils.input_string("> Email del empleado: ")
            if employee_email.lower() == "q":
                Logging.clear()
                return
            time_now = datetime.datetime.now().time().strftime("%H:%M:%S")
            time_in = IOUtils.input_string("> Hora de llegada [" + time_now + "]: ") or time_now
            if time_in.lower() == "q":
                Logging.clear()
                return
            date_now = datetime.datetime.now().date().strftime("%Y-%m-%d")
            date = IOUtils.input_string("> Fecha [" + date_now + "]: ") or date_now
            if date.lower() == "q":
                Logging.clear()
                return

            user = user_dao.get_by_email(employee_email)
            # Validación de formato de hora
            try:
                datetime.datetime.strptime(time_in, "%H:%M:%S")
                time_valid = True
            except ValueError:
                time_valid = False
            
            # Validación de formato de fecha
            try:
                datetime.datetime.strptime(date, "%Y-%m-%d")
                date_valid = True
            except ValueError:
                date_valid = False

            if user is None:
                Logging.print("Error. No se encontró nignun empleado con el email ingresado.")
            elif not time_valid or not date_valid:
                Logging.print("Error. Verifique el formato provisto.")
            else:
                inputs_ok = True
            
        sign = StaffSign(_employee_id = user.get_employee_id(), _date = date, _time_in = time_in)
        staff_sign_dao.create(sign)
