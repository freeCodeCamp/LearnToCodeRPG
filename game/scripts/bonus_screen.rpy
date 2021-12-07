screen bonus_screen():
    tag menu
    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Bonus"), scroll="viewport"):
        style_prefix "bonus"
        vbox:
            spacing 15
            
            label 'Bonus Contents'
            textbutton '{icon=icon-award} ' + _("Achievements") action Show('achievements_screen')
            textbutton '{icon=icon-headphones} ' + _("Music Gallery") action NullAction()
            textbutton '{icon=icon-book-open} ' + _("Glossary") action Show('glossary_screen')
            textbutton '{icon=icon-code} ' + _("Quiz Collection") action Show('quiz_screen')

            null height 20

            label 'Movies'
            # TODO: play game trailer from YouTube
            textbutton '{icon=icon-film} ' + _("Game Trailer") action NullAction()
            textbutton '{icon=icon-youtube} ' + _("Learn to Code RPG: The Making of") action NullAction()

            null height 20
            label 'Mini Games'
            textbutton '{icon=icon-music} ' + _("Rhythm Game") action Call('rhythm_game_entry_from_bonus_screen')
            # TODO: more mini games, quiz speedrun survival mode etc.

screen achievements_screen():
    tag menu
    use game_menu(_("Achievements"), scroll="viewport"):
        style_prefix "bonus"
        vbox:
            spacing 50
            for category in [plot_achievement, plot_bonus, quiz_bonus, ending_achievement]:
                vbox:
                    spacing 15
                    label category

                    $ achievement_to_tweet_map = achievement_labels_map[category]
                    grid 2 len(achievement_to_tweet_map):
                        xspacing 60

                        for achievement in sorted(achievement_to_tweet_map.keys()):
                            $ is_unlocked = (achievement in persistent.achievements)

                            if is_unlocked:
                                $ tweet = achievement_to_tweet_map[achievement]
                                text '{icon=icon-unlock} [achievement]'
                                textbutton '{icon=icon-twitter} Tweet this' action OpenURL(tweet)
                            else:
                                text '{icon=icon-lock} ???'
                                null

# TODO: v2
screen glossary_screen():
    tag menu
    use game_menu(_("Glossary"), scroll="viewport"):
        style_prefix "bonus"
        text "Coming in v2!"

# TODO: v2
screen quiz_screen():
    tag menu
    use game_menu(_("Quiz Questions"), scroll="viewport"):
        style_prefix "bonus"
        text "Coming in v2!"

style bonus_label is gui_label
style bonus_label_text is gui_label_text
style bonus_text is gui_text

style bonus_label_text:
    size gui.label_text_size