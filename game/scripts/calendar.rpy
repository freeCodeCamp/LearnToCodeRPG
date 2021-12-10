init python:
    from datetime import date

    class Calendar():
        def __init__(self, day=1, month=8, year=2021):
            self.is_daytime = True
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
            renpy.call_screen('text_over_black_bg_screen', _('The next day...'))

        def next_week(self):
            self.day += 7
            if self.day > self.days_count[self.month]:
                self.month += 1 # new month
                self.day = self.day - self.days_count[self.month] - 1
                if self.month > 12: 
                    self.month = 1 # back to January
                    self.year += 1 # increment year
            renpy.call_screen('text_over_black_bg_screen', _('Fast-forwarding a week...'))

        def next_month(self):
            self.month += 1
            if self.month > 12: 
                self.month = 1 # back to January
                self.year += 1 # increment year
            renpy.call_screen('text_over_black_bg_screen', _('Fast-forwarding a month...'))

        def get_month_string(self):
            return self.month_names[self.month]

        def get_day_string(self):
            return str(self.day)

default calendar_enabled = True # similar to quick_menu boolean
# this screen should always show
screen calendar_screen():
    ## Ensure this appears on top of other screens like quick_menu and player_stats
    zorder 101
    if calendar_enabled:
        frame:
            xpos 20
            ypos 20
            xpadding 30
            ypadding 30
            background white80
            hbox:
                spacing 15
                text '{icon=icon-calendar}'
                text calendar.get_month_string():
                    color gui.accent_color
                    font gui.interface_text_font
                    size gui.name_text_size
                    bold True
                    underline True
                text calendar.get_day_string():
                    font gui.interface_text_font
                    size gui.name_text_size
                    bold True

# this can be used as calendar transition, chapter transition, etc.
screen text_over_black_bg_screen(title_text):
    ## Ensure this appears on top of other screens like quick_menu and player_stats
    zorder 102
    modal True
    add black
    text title_text at text_dissolve:
        xalign 0.5
        yalign 0.5
        size gui.chapter_title_text_size
        color white

    timer 3.0 action [
    Hide('text_over_black_bg_screen', dissolve),
    Return()
    ]

transform text_dissolve:
    on show:
        alpha 0.0
        linear 1.0 alpha 1.0
    on hide:
        linear 0.2 alpha 0.0