init python:

    # a change in stats or todo should always automatically trigger the showing of the stats screen

    class PlayerStats():
        def __init__(self):
            # map string names to stats
            self.player_stats_map = {
            'Sanity': 100, 
            'CS Knowledge': 0, 
            }

        def set_stats(self, stats_name, val):
            # keep between 0 and 100
            if stats_name in self.player_stats_map:
                clamped_val = min(100, max(0, val))
                self.player_stats_map[stats_name] = clamped_val
                renpy.notify(stats_name + ' is set to ' + str(clamped_val))
                if not renpy.get_screen('player_stats_screen'):
                    renpy.show_screen('player_stats_screen', _layer='transient', show_todo=False)

        def change_stats(self, stats_name, val):
            # keep between 0 and 100
            if stats_name in self.player_stats_map:
                new_val = self.player_stats_map[stats_name] + val
                clamped_val = min(100, max(0, new_val))
                self.player_stats_map[stats_name] = clamped_val
                
                # TODO: play different sound depending on the stats and direction of change
                if val > 0:
                    if not renpy.sound.is_playing():
                        renpy.sound.play('audio/sfx/stats_change_boop.wav')
                    renpy.notify(stats_name + ' increased by ' + str(val))
                else:
                    renpy.notify(stats_name + ' decreased by ' + str(-val))

                # show the stats screen
                if not renpy.get_screen('player_stats_screen'):
                    renpy.show_screen('player_stats_screen', _layer='transient', show_todo=False)

        def change_stats_random(self, stats_name, min_val, max_val):
            # renpy.random.randint([min], [max]) both ends inclusive
            val = renpy.random.randint(min_val, max_val)
            self.change_stats(stats_name, val)

        def is_sanity_low(self):
            return self.player_stats_map['Sanity'] < 50

    class ToDoList():
        def __init__(self):
            self.incomplete = []
            self.completed = []

        def add_todo(self, todo):
            self.incomplete.append(todo)
            if not renpy.get_screen('player_stats_screen'):
                renpy.show_screen('player_stats_screen', _layer='transient')
            if not renpy.sound.is_playing():
                renpy.sound.play('audio/sfx/smartphone_typing.wav')

        def complete_todo(self, todo):
            if todo in self.incomplete:
                self.incomplete.remove(todo)
                self.completed.append(todo)
                if not renpy.get_screen('player_stats_screen'):
                    renpy.show_screen('player_stats_screen', _layer='transient')
                if not renpy.sound.is_playing():
                    renpy.sound.play('audio/sfx/todo_complete.wav')

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0

screen player_stats_screen(show_stats=True, show_todo=True):
    ## Ensure this appears on top of other screens.
    # zorder 100
    on "show" action With(dissolve)
    on "hide" action With(dissolve)

    frame:
        # center of screen
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30

        background "#fffc" # 80% opacity

        vbox:
            spacing 20

            text _("Stats") bold True underline True
            hbox:
                spacing 40
                # left column shows the stats name
                vbox:
                    spacing 10
                    text "{icon=icon-zap}  " + _('Sanity') color gui.accent_color

                    if stats_knowledge_unlocked:
                        text "{icon=icon-terminal}  " + _('CS Knowledge') color gui.accent_color

                # middle column shows the stats bar
                vbox:
                    spacing 10
                    $ sanity = player_stats.player_stats_map['Sanity']
                    bar value sanity range 100 xalign 0.5 yalign 0.9 xmaximum 200 at alpha_dissolve

                    if stats_knowledge_unlocked:
                        $ cs_knolwedge = player_stats.player_stats_map['CS Knowledge']
                        bar value cs_knolwedge range 100 xalign 0.5 yalign 0.9 xmaximum 200 at alpha_dissolve

                # right column shows the stats value in numbers
                vbox:
                    spacing 10
                    $ sanity = player_stats.player_stats_map['Sanity']
                    text str(sanity)
                    if stats_knowledge_unlocked:
                        $ cs_knolwedge = player_stats.player_stats_map['CS Knowledge']
                        text str(cs_knolwedge)

            if todo_unlocked and show_todo:
                null height 10
                text _("To-Do") bold True underline True

                viewport:
                        xsize 620
                        ymaximum 200
                        child_size (None, 4000)
                        scrollbars 'vertical'
                        spacing 5
                        draggable True
                        mousewheel True
                        arrowkeys True
                        vscrollbar_xsize 5
                        vscrollbar_unscrollable "hide"

                        vbox:
                            spacing 5
                            for todo in todo_list.incomplete:
                                text '    {icon=icon-square}    ' + todo
                            for todo in todo_list.completed:
                                text '    {icon=icon-check-square}    ' + todo color gui.idle_color
    
