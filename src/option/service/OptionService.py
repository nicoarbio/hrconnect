import pkgutil
import importlib
import json
from collections import defaultdict
import inspect

from src.option.model.AbstractOption import AbstractOption
from src.option.model.AbstractScheduledOption import AbstractScheduledOption
from src.utils.Logging import Logging

ROLES_CONFIG_FILEPATH = "src/config/roles.config.json"

class OptionService:

    def __init__(self):
        Logging.debug("Cargando servicio de opciones para el usuario")
        self._package_name = "src.option.model.use_cases"
        self._options = []
        self._cu_by_role = {}
        self._load_cu_by_role()

    def load_options(self):
        package = __import__(self._package_name, fromlist=[""])
        for _, module_name, _ in pkgutil.iter_modules(package.__path__):
            module = importlib.import_module(f"{self._package_name}.{module_name}")
            for attribute_name in dir(module):
                attribute = getattr(module, attribute_name)
                if inspect.isclass(attribute) and issubclass(attribute, AbstractOption) and not inspect.isabstract(attribute):
                    self._options.append(attribute())
    
    def _load_cu_by_role(self):
        with open(ROLES_CONFIG_FILEPATH, 'r') as file:
            data = json.load(file)
            cu_by_role = data['cu_by_role']
            composite_roles = data.get('composite_roles', {})
        
        cu_by_role = defaultdict(list, cu_by_role)
        
        for role, sub_roles in composite_roles.items():
            cu_list = cu_by_role[role]
            for sub_role in sub_roles:
                cu_list.extend(cu_by_role.get(sub_role, []))
            cu_by_role[role] = list(set(cu_list))  # Remove duplicates

        self._cu_by_role = cu_by_role

    def get_options_for_role(self, role):
        Logging.debug("Buscando opciones para el rol: " + role)
        cu_ids = self._cu_by_role.get(role, [])
        Logging.debug("Todas las opciones: " + str(self._cu_by_role))
        Logging.debug("Opciones disponibles para " + role + ": " + str(cu_ids))
        filtered_options = [option for option in self._options if option.get_id() in cu_ids]
        return filtered_options

    def get_schedule_options(self) -> list[AbstractScheduledOption]:
        return [option for option in self._options if hasattr(option, 'cancelThread')]
