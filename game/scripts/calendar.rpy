init python:
    from datetime import date

    class Calendar():
        def __init__(self, day=1, month=8, year=2021):
            self.day = day
            self.month = month
            self.year = year
            
            self.month_names = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July',
                                               'August', 'September', 'October', 'November', 'December']
            self.days_count = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                        
        def next(self):
            self.day += 1
            if self.day > self.days_count[self.month]:
                self.month += 1 # new month
                self.day = 1 # first day of new month
                if self.month > 12: 
                    self.month = 1 # back to January
                    self.year += 1 # increment year

        def next_week(self):
            for _ in range(7):
                self.next()

        def next_month(self):
            self.month += 1
            if self.month > 12: 
                self.month = 1 # back to January
                self.year += 1 # increment year

        def get_month_string(self):
            return self.month_names[self.month]

        def get_day_string(self):
            return str(self.day)