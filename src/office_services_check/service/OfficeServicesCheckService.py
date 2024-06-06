import random


class OfficeServicesCheckService:

    def __init__(self):
        self._manual_sign = self.get_power_supply_status() == "OK" and self.get_internet_status() == "OK"

    def get_power_supply_status(self):
        if random.randint(1, 100) <= 5:
            return "POWER_SUPPLY_ERROR"
        return "OK"

    def get_internet_status(self):
        if random.randint(1, 100) <= 5:
            return "INTERNET_ERROR"
        return "OK"
    
    def enable_manual_sign(self):
        self._manual_sign = True

    def unable_manual_sign(self):
        self._manual_sign = False

    def is_manual_sign_enabled(self):
        return self._manual_sign