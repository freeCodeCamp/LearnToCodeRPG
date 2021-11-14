init python:
    # we have javascript_questions, web_questions, algorithm_questions, and system_questions
    all_skill_names = ['JavaScript', 'Web Development', 'Algorithm', 'System Design']

    # company logo files are named as images/others/company/avocado.png etc.
    all_company_names = {
    'AvocadoAPI': 'avocado',
    'AioliAI': 'aioli',
    'AnkoAnalytics': 'anko',
    'ButterscotchBytes': 'butterscotch',
    'BobaBandwidth': 'boba',
    'BrownieBenchmark': 'brownie',
    'CasseroleCompiler': 'casserole',
    'CupcakeCPU': 'cupcake',
    'GelatoGPU': 'gelato',
    'GingerbreadGUI': 'gingerbread',
    'PopsiclePy': 'popsicle',
    'HoneydewHeap': 'honeydew',
    'SconeSys': 'scone',
    'SundaeSoft': 'sundae',
    'MochiML': 'mochi',
    'TiramisuTPU': 'tiramisu',
    'ToffeeTerminal': 'toffee',
    'WaffleWireless': 'waffle',
    'VanillaVM': 'vanilla',
    }

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
                # job title and logo
                hbox:
                    text company_name:
                        color gui.accent_color
                        font gui.interface_text_font
                        size gui.name_text_size
                        bold True
                    $ company_logo = 'images/others/company/%s.png' % all_company_names[company_name]
                    add company_logo
                # description
                text "We are hiring for a candidate with the following skills:"
                vbox:
                    for skill in skill_names:
                        hbox:
                            text "{icon=circle-check}  "
                            text skill