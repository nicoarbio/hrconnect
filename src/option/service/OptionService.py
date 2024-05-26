import pkgutil
import importlib

from src.option.model.AbstractOption import AbstractOption


class OptionService:

    def __init__(self):
        self._package_name = "src.option.use-cases"
        self._options = []
        self._load_options()

    def _load_options(self):
        package = __import__(self._package_name, fromlist=[""])
        for _, module_name, _ in pkgutil.iter_modules(package.__path__):
            module = importlib.import_module(f"{self._package_name}.{module_name}")
            for attribute_name in dir(module):
                attribute = getattr(module, attribute_name)
                if isinstance(attribute, type) and issubclass(attribute, AbstractOption) and attribute is not AbstractOption:
                    self._options.append(attribute())

    def get_options(self):
        return self._options

#    def get_all_options_for_user(self, user):
#        return self._option_dao.get_all_options_for_user(user)
