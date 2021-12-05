label save_reminder:
    if persistent.enable_save_reminder == False: # not None
        return # return control to whatever label that called this

    # first time player will have persistent.enable_save_reminder is None
    if persistent.enable_save_reminder: # is True
        "(Hello from your friendly {b}Save Reminder{/b}!)"

    "(Would you like to {b}Save{/b} your progress up to now?)"

    call screen confirm("Would you like to save your progress up to now?", 
        yes_action=[ShowMenu('save'), Return()], 
        no_action=Return())
    if persistent.enable_save_reminder is None: # first time player need to set this up
        "(I can also remind you to save every now and then if you like. You can turn off the reminder at any time in {icon=icon-settings} {b}Settings > Others{/b}.)"
    else:
        "(Hey, just wondering... Do you find my reminders useful? If not, feel free to turn it off. I won't be offended.)"
    call screen confirm("Would you like to receive reminders to save every now and then? You can turn it off at any time in {icon=icon-settings} Settings > Others.", 
        yes_action=[SetField(persistent, 'enable_save_reminder', True), Return(True)], 
        no_action=[SetField(persistent, 'enable_save_reminder', False), Return(False)])

    if _return:
        "(Reminder set!)"
    else:
        "(Okay. I won't bug you anymore. Just remember to save your progress often!)"

    "Now let's resume our story..."
    return