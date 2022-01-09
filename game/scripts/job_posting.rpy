init 998 python:
    easter_egg_skill_achievement_map = {
    _('Brewing coffee'): plot_skill_coffee,
    _('Fixing fax machines'): plot_skill_fax,
    _('Handling angry customers'): plot_skill_customer,
    _('Fusing cables'): plot_skill_cable,
    _('Retrieving lost passwords'): plot_skill_password,
    _('Pacifying office pets'): plot_skill_pet,
    }

    easter_egg_skills = list(easter_egg_skill_achievement_map.keys())

    # company logo files are named as images/others/company/avocado.png etc.
    # DO NOT TRANSLATE THE COMPANY NAMES
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

screen job_posting_screen(company_name, skill_names, easter_egg_skill=None):
    frame:
        style_prefix "confirm"

        xfill True
        xsize 1000
        xmargin 50
        ypadding 30
        yalign .25

        vbox:
            xfill True

            label company_name xalign 0.5

            $ company_logo = 'images/others/company/%s.png' % all_company_names[company_name]
            add company_logo xalign 0.5

            text _("{b}[company_name]{/b} is hiring for a candidate with the following skills:")

            null height 20

            vbox:
                xfill True
                xoffset 200
                for skill in skill_names:
                    text "•  [skill!t]"
                if easter_egg_skill:
                    $ achievement_name = easter_egg_skill_achievement_map[easter_egg_skill]
                    textbutton "•  [easter_egg_skill!t]":
                        activate_sound 'audio/sfx/confirm_and_share.wav'
                        hovered [
                        Notify(_('Wait, is this a technical skill?')),
                        Function(persistent.achievements.add, achievement_name)
                        ]
                        action [
                        OpenURL(all_tweet_map[achievement_name]),
                        ]
                        text_font gui.text_font
                        xoffset -7 # XXX: tweak alignment

            null height 40

            hbox:
                spacing 100
                xalign .5
                textbutton _("{icon=icon-minus-circle} Pass") action Return(False) # boolean return indicating whether the player decides to apply
                textbutton _("{icon=icon-send} Apply") action Return(True)

# see confirm_and_share.rpy
screen company_email_screen(company_name, message, ok_text):
    frame:
        style_prefix "confirm"

        xfill True
        xsize 1000
        xmargin 50
        ypadding 25
        yalign .25

        vbox:
            xfill True

            label company_name xalign 0.5

            $ company_logo = 'images/others/company/%s.png' % all_company_names[company_name]
            add company_logo xalign 0.5

            text _(message)

            null height 20

            textbutton ok_text:
                xalign 0.5
                action Return()

screen company_interview_email_screen(company_name):
    use company_email_screen(
        company_name,
        _("""
        Hey [player_name],

        Thanks for applying to our job posting.

        We've received your application and thought your experience is a good fit for the role. We'd like to invite you to an interview with us. Please click {b}Confirm Interview{/b} below to confirm.

        Best,
        [company_name]
        """),
        _('Confirm Interview')
        )

screen company_rejection_email_screen(company_name):
    use company_email_screen(
        company_name,
        _("""
        Hey [player_name],

        Thanks for taking the time to interview with us.

        We are writing to let you know that we've reviewed your interview results and have decided to move on with other candidates. We look forward to seeing your application in the future.

        Best,
        [company_name]
        """),
        _("Okay, I guess [company_name] isn't my muse"),
        )

screen company_offer_email_screen(company_name):
    use company_email_screen(
        company_name,
        _("""
        Hey [player_name],

        You did great in our interview and we'd like to extend you this offer for an entry-level software engineer role.

        Please click {b}Accept Offer{/b} below to confirm. We look forward to your joining us!
        
        Best,
        Your future colleagues at [company_name]
        """),
        _('Accept Offer'),
        )
