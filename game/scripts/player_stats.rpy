init python:
    class PlayerStats():
        def __init__(self):
            self.day_counter = 1

            # map string names to stats
            self.player_stats_map = {
                'Sanity': 100,
                'CS Knowledge': None,
                'Curriuclum Progress': None,
                'Interview Skills': None,
                'Dev Skills': None,
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

        def set_stats(self, stats_name, val):
            # keep between 0 and 100
            if stats_name in self.player_stats_map:
                clamped_val = min(100, max(0, val))
                self.player_stats_map[stats_name] = clamped_val

init:            
    screen player_stats_screen(player_stats):
        ## Ensure this appears on top of other screens.
        # zorder 100

        frame:
            # top left of screen
            xalign 0
            yalign 1
            xpadding 30
            ypadding 30

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
                                bar value player_stats.player_stats_map[stats_name] range 100 xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve

                    # right column shows the stats value in numbers
                    vbox:
                        spacing 10
                        for stats_name in player_stats.player_stats_name_list:
                            # if None, not yet initialized/unlocked
                            if player_stats.player_stats_map[stats_name] is not None:
                                text str(player_stats.player_stats_map[stats_name])

    transform alpha_dissolve:
        alpha 0.0
        linear 0.5 alpha 1.0