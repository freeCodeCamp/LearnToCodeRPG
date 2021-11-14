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
                    text_align 0.5
                    xalign 0.5
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

screen company_email_screen(company_name, message, ok_text, has_social_media=False):

    frame:
        style_prefix "confirm"

        xfill True
        xsize 1000
        xmargin 50
        ypadding 25
        yalign .25

        vbox:
            xfill True
            spacing 25

            hbox:
                text company_name:
                    color gui.accent_color
                    font gui.interface_text_font
                    size gui.name_text_size
                    bold True
                $ company_logo = 'images/others/company/%s.png' % all_company_names[company_name]
                add company_logo

            text _(message):
                text_align 0.5
                xalign 0.5

            if has_social_media:
                hbox:
                    spacing 100
                    xalign .5
                    textbutton "{icon=logo-facebook}" action OpenURL('https://www.facebook.com')
                    textbutton "{icon=logo-instagram}" action OpenURL('https://www.instagram.com')
                    textbutton "{icon=logo-twitter}" action OpenURL('https:///www.twitter.com')

            hbox:
                spacing 100
                xalign .5
                textbutton ok_text action Return()

screen company_interview_email_screen(company_name):
    use company_email_screen(
        company_name,
        "Hey [persistent.player_name]! We've received your application and thought your experience is awesome! We'd like to invite you to an interview with us. Please click {b}Confirm Interview{/b} below to confirm.",
        'Confirm Interview',
        )

screen company_rejection_email_screen(company_name):
    use company_email_screen(
        company_name,
        "Hey [persistent.player_name]. We are writing to let you know that we've reviewed your interview results and have decided to move on with other candidates. We look forward to seeing your application in the future. Stay in touch.",
        "Okay, I guess [company_name] isn't my muse",
        )

screen company_offer_email_screen(company_name):
    use company_email_screen(
        company_name,
        "Hey [persistent.player_name]! You did great in our interivew and we'd like to extend you this offer for an entry-level software engineer role. Please click {b}Accept Offer{/b} below to confirm and feel free to share this exciting news on social media! We look forward to your joining us!",
        'Accept Offer',
        has_social_media=True
        )
