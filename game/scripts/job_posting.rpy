init python:
    # we have javascript_questions, web_questions, algorithm_questions, and system_questions
    all_skill_names = ['JavaScript', 'Web Development', 'Algorithm', 'System Design']

    all_company_names = [
    'AvocadoAPI',
    'AioliAI',
    'AnkoAnalytics',
    'ButterscotchBytes',
    'BobaBandwidth',
    'BrownieBenchmark',
    'CasseroleCompiler',
    'CupcakeCPU',
    'GelatoGPU',
    'GingerbreadGUI',
    'PopsiclePy',
    'HoneydewHeap',
    'SconeSys',
    'SundaeSoft',
    'MochiML',
    'TiramisuTPU',
    'ToffeeTerminal',
    'WaffleWireless',
    'VanillaVM'
    ]

init:
    screen job_posting_screen(company_name, skill_names):
        frame:
            # center of screen
            xalign 0.5
            yalign 0.5
            xpadding 30
            ypadding 30

            vbox:
                spacing 40
                # job title
                text company_name color gui.accent_color font gui.interface_text_font size gui.name_text_size bold True
                # description
                text "We are hiring for a candidate with the following skills:"
                vbox:
                    for skill in skill_names:
                        hbox:
                            text "{icon=circle-check}  "
                            text skill
