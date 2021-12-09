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

            text "{b}[company_name]{/b} is hiring for a candidate with the following skills:"

            null height 20

            for skill in skill_names:
                hbox:
                    null width 40
                    text "•  " + skill

            null height 40

            hbox:
                spacing 100
                xalign .5
                textbutton '{icon=icon-minus-circle} ' + _("Pass") action Return(False) # boolean return indicating whether the player decides to apply
                textbutton '{icon=icon-send} ' + _("Apply") action Return(True)

# see confirm_and_share.rpy
screen company_email_screen(company_name, message, ok_text, tweet_content_url=None):
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

            if tweet_content_url:
                textbutton "{icon=icon-twitter} " + _("Tweet this"):
                    xalign 0.5
                    action OpenURL(tweet_content_url)

            null height 20

            textbutton ok_text:
                xalign 0.5
                action Return()

screen company_interview_email_screen(company_name):
    use company_email_screen(
        company_name,
        """
        Hey [persistent.player_name],

        Thanks for applying to our job posting.

        We've received your application and thought your experience is a good fit for the role. We'd like to invite you to an interview with us. Please click {b}Confirm Interview{/b} below to confirm.

        Best,
        [company_name]
        """,
        'Confirm Interview'
        )

screen company_rejection_email_screen(company_name):
    use company_email_screen(
        company_name,
        """
        Hey [persistent.player_name],

        Thanks for taking the time to interview with us.

        We are writing to let you know that we've reviewed your interview results and have decided to move on with other candidates. We look forward to seeing your application in the future.

        Best,
        [company_name]
        """,
        "Okay, I guess [company_name] isn't my muse",
        )

screen company_offer_email_screen(company_name):
    use company_email_screen(
        company_name,
        """
        Hey [persistent.player_name],

        You did great in our interivew and we'd like to extend you this offer for an entry-level software engineer role.

        Please click {b}Accept Offer{/b} below to confirm. We look forward to your joining us!
        
        Best,
        Your future colleagues at [company_name]
        """,
        'Accept Offer',
        tweet_content_url=tweet_first_offer
        )
