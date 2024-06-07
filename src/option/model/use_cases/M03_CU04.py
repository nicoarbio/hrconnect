import datetime
from src.option.model.AbstractScheduledOption import AbstractScheduledOption
from src.config.BeanManager import BeanManager
from src.notifications.model.Notification import Notification


class M03_CU04(AbstractScheduledOption):
    """El tiempo, cada 5 minutos, solicita la comprobación del estado del suministro eléctrico e internet, para determinar el modo del fichaje."""

    def get_period_in_seconds(self):
        return 5 * 60 # 5 minutos
        #return 10 # 10 segundos para pruebas

    def get_id(self):
        return "M03_CU04"

    def get_description(self):
        return "Notificar llegadas tardes/ausencias"

    def execute_option_use_case(self):
        office_services_check_service = BeanManager.get_OfficeServicesCheckService()

        power_status = office_services_check_service.get_power_supply_status()
        internet_status = office_services_check_service.get_internet_status()

        if power_status == "OK" and internet_status == "OK":
            office_services_check_service.unable_manual_sign()
            user_dao = BeanManager.get_UserDAO()
            staff_sign_dao = BeanManager.get_StaffSignDAO()
            now = datetime.datetime.now()
            today_date = now.date()
            for employee in user_dao.get_today_start():
                employee_id = employee.get("_employee_id")
                daily_start_str = employee.get("_daily_start")  # formato "09:00:00"
                today_start_time = datetime.datetime.strptime(daily_start_str, '%H:%M:%S').time()
                today_start_datetime = datetime.datetime.combine(today_date, today_start_time) # Combinar la fecha de hoy con la hora de inicio del empleado
                
                daily_start_plus_30 = today_start_datetime + datetime.timedelta(minutes=30) # Calcular la hora de inicio más 30 minutos
                
                # Obtener la fichada del empleado
                staff_sign = staff_sign_dao.get_by_employeeid_and_date(employee_id, today_date.strftime('%Y-%m-%d'))
                time_in = None
                if staff_sign:
                    time_in = staff_sign.get_time_in()  # formato "2024-06-04 09:10:05"
                
                # Verificar si la hora actual es mayor o igual a la hora de inicio más 30 minutos y no hay fichada
                if now >= daily_start_plus_30 and not time_in:
                    mensaje = "Ya han pasado 30 minutos de su horario de fichaje y aún no lo ha realizado"
                    notifications_dao = BeanManager.get_NotificationDAO()
                    notifications_dao.create(Notification(employee_id, mensaje))
        else:
            office_services_check_service.enable_manual_sign()
            return