screen bonus_screen():
    tag menu
    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Bonus"), scroll="viewport"):
        style_prefix "bonus"
        # Build your screen here

style bonus_label is gui_label
style bonus_label_text is gui_label_text
style bonus_text is gui_text

style bonus_label_text:
    size gui.label_text_size