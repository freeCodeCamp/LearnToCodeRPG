screen save_reminder_screen(message, yes_action, no_action):
    # based on the confirm screen
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _("Would you like to get future reminders to save your progress?"):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                style_prefix "radio"
                textbutton _("Keep reminding me to save"):
                    action ToggleField(persistent, 'enable_save_reminder')
                    xsize 250
                textbutton _("Turn off future reminders"):
                    action InvertSelected(ToggleField(persistent, 'enable_save_reminder'))
                    xsize 250

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action

label save_reminder:
    if persistent.enable_save_reminder == False: # not None
        return # return control to whatever label that called this

    # first time player will have persistent.enable_save_reminder is None
    if persistent.enable_save_reminder: # is True
        "(Hello from your friendly {b}Save Reminder{/b}!)"

    "(Would you like to {b}Save{/b} your progress up to now?)"

    call screen save_reminder_screen("Would you like to save your progress up to now?", 
        yes_action=[ShowMenu('save'), Return()], 
        no_action=Return())

    "Thanks for entertaining your friendly {b}Save Reminder{/b}! Now let's get back to our story..."
    return
