init python:
    from datetime import date, timedelta

    class Calendar():
        def __init__(self):
            self.date = date.today() # system date
            self.weekday_names = [_('Monday'), _('Tuesday'), _('Wednesday'), _('Thursday'), _('Friday'), _('Saturday'), _('Sunday')]

        def is_weekday(self):
            return self.date.weekday() < 5 # 5 Sat, 6 Sun

        def get_weekday_string(self):
            return self.weekday_names[self.date.weekday()]

        def next(self):
            self.date += timedelta(days=1)
            renpy.call_screen('text_over_black_bg_screen', _('The next day...'))

        def next_weekday(self):
            if self.is_weekday():
                return
            days_before_weekday = 7 - self.date.weekday()
            self.date += timedelta(days=days_before_weekday)
            renpy.call_screen('text_over_black_bg_screen', _('Fast-forwarding to a work day...'))

        def next_week(self):
            self.date += timedelta(days=7)
            renpy.call_screen('text_over_black_bg_screen', _('Fast-forwarding a week...'))

        def next_month(self):
            self.date += timedelta(days=30)
            renpy.call_screen('text_over_black_bg_screen', _('Fast-forwarding a month...'))

        def get_year(self):
            return self.date.year

        def get_month(self):
            return self.date.month

        def get_day(self):
            return self.date.day

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
                text calendar.date.isoformat():
                    color gui.accent_color
                    font gui.interface_text_font
                    size gui.name_text_size
                text calendar.get_weekday_string():
                    font gui.interface_text_font
                    size gui.name_text_size

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