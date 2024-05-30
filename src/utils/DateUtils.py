from datetime import datetime

class DateUtils:

    @staticmethod
    def get_formatted_current_date_time():
        return DateUtils.get_formatted_date_time(datetime.now())
    
    @staticmethod
    def get_formatted_date_time(date_time):
        return date_time.strftime("%Y-%m-%d %H:%M:%S")
