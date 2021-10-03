init:
    screen job_posting_screen():
        frame:
            # center of screen
            xalign 0.5
            yalign 0.5
            xpadding 30
            ypadding 30

            vbox:
                spacing 40
                # job title
                text "BiscuitBinaryTree" color gui.accent_color font gui.interface_text_font size gui.name_text_size bold True
                # description
                text "We are hiring a candidate with the following qualities"
