init python:

    # a change in stats or todo should always automatically trigger the showing of the stats screen
    CHANGE_DIRECTION_INC = 'inc'
    CHANGE_DIRECTION_DEC = 'dec'

    # some constants for dict keys
    SANITY = _('Sanity')
    CS_KNOWLEDGE = _('CS Knowledge')
    RENOWN = _('Renown')
    MONEY = _('Money')

    class PlayerStats():
        def __init__(self):
            # v1_skills is defined in variables.rpy

            # map string names to stats
            # DO NOT TRANSLATE THESE TWO
            self.player_stats_map = {
            SANITY: 100, 
            CS_KNOWLEDGE: 0, 
            }

            # these are translated as defined in variables.rpy
            self.subcategory_stats_map = {}

        def set_stats(self, stats_name, val):
            if stats_name == MONEY:
                clamped_val = max(0, val)
            else:
                # keep between 0 and 100 by default
                clamped_val = min(100, max(0, val))
            
            self.player_stats_map[stats_name] = clamped_val
            renpy.notify(stats_name + _(' is set to ') + str(clamped_val))

        def change_stats(self, stats_name, val):
            if stats_name in self.player_stats_map:
                map_pointer = self.player_stats_map
            elif stats_name in self.subcategory_stats_map:
                map_pointer = self.subcategory_stats_map

            new_val = map_pointer[stats_name] + val
            if stats_name == MONEY:
                # keep between 0 and 100 by default
                clamped_val = max(0, new_val)
            else:
                clamped_val = min(100, max(0, new_val))
                
            map_pointer[stats_name] = clamped_val
            
            change_direction = None
            if val > 0:
                change_direction = CHANGE_DIRECTION_INC
                val_str = str(val)
                renpy.sound.play('audio/sfx/stats_change_boop.wav')
                if stats_name in self.subcategory_stats_map: # skill name + the word `knowledge`
                    renpy.notify(stats_name + _(' knowledge increased by ') + val_str)
                else: # just plain string `Sanity` or `CS Knowledge`
                    renpy.notify(stats_name + _(' increased by ') + val_str)
            elif val < 0:
                change_direction = CHANGE_DIRECTION_DEC                    
                val_str = str(-val)
                renpy.sound.play('audio/sfx/stats_change_buzz.wav')
                if stats_name in self.subcategory_stats_map:
                    renpy.notify(stats_name + _(' knowledge decreased by ') + val_str)
                else:
                    renpy.notify(stats_name + _(' decreased by ') + val_str)

            renpy.show_screen('player_stats_todo_screen', 
                _layer='transient', changed_stats=stats_name, change_direction=change_direction)

            if stats_name in self.subcategory_stats_map:
                # check if max out
                if self.subcategory_stats_map[stats_name] == 100 and \
                not plot_stats_full in persistent.achievements:
                    persistent.achievements.add(plot_stats_full)
                    renpy.call_screen('confirm_and_share_screen', 
                        title=plot_stats_full, tweet_content_url=all_tweet_map[plot_stats_full])

                self.compute_cs_knowledge()

        def change_stats_random(self, stats_name, min_val, max_val):
            # renpy.random.randint([min], [max]) both ends inclusive
            val = renpy.random.randint(min_val, max_val)
            self.change_stats(stats_name, val)

        def is_sanity_low(self):
            return self.player_stats_map[SANITY] < 50

        def compute_cs_knowledge(self):
            # total
            val = sum(self.subcategory_stats_map.values())
            
            # check if max out
            if val == 100 * len(self.subcategory_stats_map) and \
            not plot_stats_all in persistent.achievements:
                persistent.achievements.add(plot_stats_all)
                renpy.call_screen('confirm_and_share_screen', 
                        title=plot_stats_all, tweet_content_url=all_tweet_map[plot_stats_all])

            # take average
            val /= float(len(self.subcategory_stats_map))
            # round to int
            val = int(round(val))
            clamped_val = min(100, max(0, val))
            self.player_stats_map[CS_KNOWLEDGE] = clamped_val

    class ToDoList():
        def __init__(self):
            self.incomplete = []
            self.completed = []

        def add_todo(self, todo):
            self.incomplete.append(todo)
            if not renpy.get_screen('player_stats_todo_screen', layer='transient'):
                renpy.show_screen('player_stats_todo_screen', _layer='transient', show_todo=True)
            if not renpy.sound.is_playing():
                renpy.sound.play('audio/sfx/smartphone_typing.wav')

        def complete_todo(self, todo):
            if todo in self.incomplete:
                self.incomplete.remove(todo)
                self.completed.append(todo)
                if not renpy.get_screen('player_stats_todo_screen', layer='transient'):
                    renpy.show_screen('player_stats_todo_screen', _layer='transient', show_todo=True)
                if not renpy.sound.is_playing():
                    renpy.sound.play('audio/sfx/todo_complete.wav')

    def get_stats_change_direction_icon(stats, changed_stats, change_direction):
        if stats == changed_stats:
            if change_direction == CHANGE_DIRECTION_INC:
                return '{icon=icon-chevrons-up}'
            elif change_direction == CHANGE_DIRECTION_DEC:
                return '{icon=icon-chevrons-down}'
        return ''

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0

screen player_stats_todo_screen(show_todo=False, changed_stats=None, change_direction=None):
    ## Ensure this appears on top of other screens.
    # zorder 100
    on "show" action With(dissolve)
    on "hide" action With(dissolve)

    default show_todo_local = show_todo

    frame:
        # center of screen
        xalign 0.5
        yalign 0.25
        xpadding 30
        ypadding 30

        background white80

        has vbox
        spacing 10

        hbox:
            spacing 30
            xalign 0.5
            style_prefix "radio"
            textbutton _("Show Stats"):
                action ToggleScreenVariable(name='show_todo_local', true_value=False, false_value=True)
            textbutton _("Show To-Do"):
                action [
                SensitiveIf(todo_unlocked),
                ToggleScreenVariable(name='show_todo_local', true_value=True, false_value=False)
                ]

        viewport:
            xsize 620
            ymaximum 550
            child_size (None, 4000)
            scrollbars 'vertical'
            spacing 5
            draggable True
            mousewheel True
            arrowkeys True
            vscrollbar_xsize 5
            vscrollbar_unscrollable "hide"
                
            if show_todo_local:
                use todo_screen()
            else: # show stats by default
                use player_stats_screen(changed_stats, change_direction)

screen player_stats_screen(changed_stats, change_direction):
    $ num_rows = len(player_stats.player_stats_map) + len(player_stats.subcategory_stats_map)

    grid 3 num_rows:
        xspacing 10
        yspacing 5

        # Money
        if MONEY in player_stats.player_stats_map:
            $ val = player_stats.player_stats_map[MONEY]
            text _('{icon=icon-shopping-bag} Money') color gui.accent_color
            text '$' + str(val) + '  ' + get_stats_change_direction_icon(MONEY, changed_stats, change_direction)
            null width 200

        # Sanity
        $ val = player_stats.player_stats_map[SANITY]
        text _('{icon=icon-zap} Sanity') color gui.accent_color
        bar value val range 100 xalign 0.5 yalign 0.9 xmaximum 200 at alpha_dissolve
        text str(val) + '  ' + get_stats_change_direction_icon(SANITY, changed_stats, change_direction)

        # Renown
        if RENOWN in player_stats.player_stats_map:
            $ val = player_stats.player_stats_map[RENOWN]
            text _('{icon=icon-award} Renown') color gui.accent_color
            bar value val range 100 xalign 0.5 yalign 0.9 xmaximum 200 at alpha_dissolve
            text str(val) + '  ' + get_stats_change_direction_icon(RENOWN, changed_stats, change_direction)

        # CS Knowledge
        if CS_KNOWLEDGE in player_stats.player_stats_map:
            $ val = player_stats.player_stats_map[CS_KNOWLEDGE]
            text _('{icon=icon-terminal} CS Knowledge') color gui.accent_color
            bar value val range 100 xalign 0.5 yalign 0.9 xmaximum 200 at alpha_dissolve
            text str(val) + '  ' + get_stats_change_direction_icon(CS_KNOWLEDGE, changed_stats, change_direction)

        # Subcategory CS Stats
        if player_stats.subcategory_stats_map:
            for skill in player_stats.subcategory_stats_map:
                $ val = player_stats.subcategory_stats_map[skill]
                text "    {icon=icon-code} [skill!t]" color gui.accent_color
                bar value val range 100 xalign 0.5 yalign 0.9 xmaximum 200 at alpha_dissolve
                text str(val) + '  ' + get_stats_change_direction_icon(skill, changed_stats, change_direction)

screen todo_screen():
    vbox:
        spacing 5
        for todo in todo_list.incomplete:
            text '    {icon=icon-square}    ' + todo
        for todo in todo_list.completed:
            text '    {icon=icon-check-square}    ' + todo color gui.insensitive_color