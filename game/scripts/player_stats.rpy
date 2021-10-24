init python:
    class PlayerStats():
        def __init__(self):
            self.day_counter = 1

            # map string names to stats
            self.player_stats_map = {
                'Sanity': 100,
                'CS Knowledge': None,
            }

            # to loop over the dictionary deterministically
            self.player_stats_name_list = list(self.player_stats_map.keys())

        def init_stats(self, stats_name):
            if stats_name in self.player_stats_map:
                self.player_stats_map[stats_name] = 0
            # TODO: play sound

        def change_stats(self, stats_name, val):
            # keep between 0 and 100
            if stats_name in self.player_stats_map and self.player_stats_map[stats_name] is not None:
                new_val = self.player_stats_map[stats_name] + val
                clamped_val = min(100, max(0, new_val))
                self.player_stats_map[stats_name] = clamped_val
                # TODO: play different sound depending on the stats and direction of change
                if not renpy.sound.is_playing():
                    renpy.sound.play('audio/sfx/stats_change_boop.wav')

        def change_stats_random(self, stats_name, min_val, max_val):
            # renpy.random.randint([min], [max]) both ends inclusive
            val = renpy.random.randint(min_val, max_val)
            self.change_stats(stats_name, val)

        def set_stats(self, stats_name, val):
            # keep between 0 and 100
            if stats_name in self.player_stats_map:
                clamped_val = min(100, max(0, val))
                self.player_stats_map[stats_name] = clamped_val

        def is_sanity_low(self):
            return self.player_stats_map['Sanity'] > 50

    class ToDoList():
        def __init__(self):
            self.todo_keys = [] # a list of keys for traversing the dict deterministically
            self.todo_dict = {} # maps str todo to boolean indicating completion

        def add_todo(self, todo):
            self.todo_keys.append(todo)
            self.todo_dict[todo] = False
            # TODO: show and collapse screen

init:

    transform alpha_dissolve:
        alpha 0.0
        linear 0.5 alpha 1.0

    $ player_stats_screen_width = 620

    screen player_stats_screen:
        ## Ensure this appears on top of other screens.
        # zorder 100
        default todo_expanded = False

        on "show" action With(Dissolve(1.0))
        on "hide" action With(Dissolve(1.0))

        frame:
            # top left of screen
            xsize player_stats_screen_width
            xalign 0.0
            yalign 0.0
            xpadding 30
            ypadding 30

            background Solid("#ffffffcc") # 80% opacity

            vbox:
                spacing 20
                # calendar
                hbox:
                    spacing 10
                    text 'Day' color gui.accent_color font gui.interface_text_font size gui.name_text_size bold True
                    text str(player_stats.day_counter) font gui.interface_text_font size gui.name_text_size bold True

                hbox:
                    spacing 40
                    # left column shows the stats name
                    vbox:
                        spacing 10
                        # iterate over the list instead of the map for deterministicity
                        for stats_name in player_stats.player_stats_name_list:
                            # if None, not yet initialized/unlocked
                            if player_stats.player_stats_map[stats_name] is not None:
                                text stats_name color gui.accent_color
                    # middle column shows the stats bar
                    vbox:
                        spacing 10
                        for stats_name in player_stats.player_stats_name_list:
                            # if None, not yet initialized/unlocked
                            if player_stats.player_stats_map[stats_name] is not None:
                                bar value player_stats.player_stats_map[stats_name] range 100 xalign 0.5 yalign 0.9 xmaximum 200 at alpha_dissolve

                    # right column shows the stats value in numbers
                    vbox:
                        spacing 10
                        for stats_name in player_stats.player_stats_name_list:
                            # if None, not yet initialized/unlocked
                            if player_stats.player_stats_map[stats_name] is not None:
                                text str(player_stats.player_stats_map[stats_name])

                if todo_unlocked:
                    null height 10
                    hbox:
                        spacing 40
                        if todo_unlocked:
                            textbutton '{icon=list}To-Do' action ToggleScreenVariable('todo_expanded', true_value=True, false_value=False)

                    if todo_expanded:
                        use todo_listview

    screen todo_listview:
        viewport:
            xsize player_stats_screen_width
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
                for todo in todo_list.todo_keys:
                    if not todo_list.todo_dict[todo]: # a boolean indicating completion
                        text '{icon=circle} ' + todo
                    else:
                        text '{icon=circle-check} ' + todo color gui.idle_color

