# creators should use priorities in the range -999 to 999
# run last
init 998:
    default stats_unlocked = False
    default stats_knowledge_unlocked = False # cs knowledge
    default stats_subcategory_unlocked = False # subcategory of cs knowledge
    default todo_unlocked = False

    # alternative endings
    default has_triggered_ending_barista = False
    default has_triggered_ending_cat = False
    default has_triggered_ending_tutor = False
    default has_triggered_ending_office = False

    default num_times_sanity_low = 0
    default has_triggered_ending_farmer = False

    default has_triggered_ending_today = False

    # set question type during study session
    # default study_session_questions = general_questions
    default study_session_questions = css_questions

    default has_visited_hacker_space_with_annika = False

    # unlocks Marco's topics_to_ask
    default has_met_marco = False

    # major characters and plot have been introduced, unlocks alternative endings
    default has_met_layla = False

    # once this is True, trivia guy no longer appears, and player can get a first round interview w/ CupCakeCPU
    default has_won_hacker_space_trivia = False
    default has_applied_to_cupcakecpu = False

    define cs_knowledge_threshold = 60 # need 60 CS Knowledge to pass the curriculum
    # player_stats.player_stats_map['CS Knowledge'] >= cs_knowledge_threshold
    default has_completed_curriculum = False

    default num_jobs_applied = 0
    default num_jobs_interviewed = 0
    default num_jobs_rejected = 0
    default num_offers = 0 # v2

    default has_received_offer = False
    # TODO: beyond demo version, can do negotiation
    default has_accepted_offer = False # v2

    default day_activity = None # set in day_activity_choice.rpy

    # interview and offer
    default interview_company_name = None # set in day_activity_choice.rpy
    default offer_company_name = None # set in quiz_session.rpy

    # seen labels
    default seen_hacker_space_events = set()
    default seen_barista_events = set()

    default persistent.enable_save_reminder = None

init python:
    if persistent.achievements is None:
        persistent.achievements = set()

    # npc Q and A
    topics_to_ask = set()
    npc = annika
    npc_sprite = 'annika'

    ## Non-mutable

    ## Note to proofreader: please proofread these; they show up as To-Do items
    # to-do strings
    todo_check_fcc = 'Check out [freeCodeCamp]'
    todo_ask_curriculum = 'Ask Annika about CS curriculum'
    todo_learn_cs = 'Bump {b}CS Knowledge{/b} to [cs_knowledge_threshold]+'
    todo_apply_cupcakecpu = 'Apply to CupcakeCPU'
    todo_apply_to_jobs = 'Start applying to jobs'
    todo_interview_prep = 'Start preparing for coding interviews'
    todo_get_job = 'Get a developer job'
    todo_ask_hackathon = 'Learn about Hackathon'
    todo_ask = 'Learn about ' # should be concatenated with vocabs from barista story

    ## Note to proofreader: please do not change these labels
    # story labels for hacker space and barista
    hacker_space_event_labels = [
    'hacker_space_tech_talk',
    'hacker_space_playtest',
    'hacker_space_project',
    'hacker_space_open_source',
    ]

    barista_event_labels = [
    'barista_fullstack',
    'barista_devops',
    'barista_conference',
    'barista_versioncontrol',
    'barista_machinelearning',
    'barista_agile',
    'barista_api',
    'barista_userexperience',    
    ]

    # map topic to label name
    ask_npc = {
    'Hackathon': 'ask_hackathon',
    'Full-Stack': 'ask_fullstack',
    'DevOps': 'ask_devops',
    'Conference': 'ask_conference',
    'Version Control': 'ask_versioncontrol',
    'Machine Learning': 'ask_machinelearning',
    'Agile': 'ask_agile',
    'API': 'ask_api',
    'User Experience': 'ask_userexperience',
    }

    # VIP names and profile links
    # TODO: add other contributors
    vip_names = {
    'Quincy': 'https://twitter.com/ossia', 
    'Lynn': 'https://ruolinzheng08.github.io/',
    'Abbey': 'https://twitter.com/abbeyrenn', 
    'Estefania': 'https://twitter.com/EstefaniaCassN',
    'Jessica': 'https://twitter.com/codergirl1991',
    'Oliver': 'https://github.com/ojeytonwilliams/',
    'Ilenia': 'https://twitter.com/ieahleen'
    }

    # Note to proofreader: please proofread the tweet content
    tweet_default = 'I just discovered this cool game called #LearnToCodeRPG. Play the game here: '

    # Note to proofreader: these are achievement strings displayed on the Achievements screen. Please proofread
    # Please check the casing of the title
    ## milestone
    milestone_start_curriculum = '3, 2, 1, Learn to Code, Action!'
    milestone_complete_curriculum = 'Nailed the Curriculum!'
    milestone_start_interview_prep = 'Gotta Crush Those Technical Interviews!'
    milestone_first_application = 'Submitted My First Dev Job Application!'
    milestone_first_interview = 'Got My First Interview!'
    milestone_first_offer = 'Got My First Offer!'
    # TODO: v2 can have multiple offers
    milestone_onboarding = 'Now Streaming: My Dream Dev Job'

    tweet_start_curriculum = 'I just started teaching myself to code in #LearnToCodeRPG. Play the game here: '
    tweet_complete_curriculum = 'I nailed the CS curriculum in #LearnToCodeRPG. Play the game here: '
    tweet_start_interview_prep = 'I just started prepping for coding interviews in #LearnToCodeRPG. Play the game here: '
    tweet_first_application = 'I just submitted my first application for a dev job in #LearnToCodeRPG. Play the game here: '
    tweet_first_interview = 'I got my first technical interview in #LearnToCodeRPG. Play the game here: '
    tweet_first_offer = 'I got my first dev job in #LearnToCodeRPG. Play the game here: '
    tweet_onboarding = 'I started the onboarding process for my dream dev job in #LearnToCodeRPG. Play the game here: '

    milestone_to_tweet_map = {
        milestone_start_curriculum: generate_tweet_intent(tweet_start_curriculum),
        milestone_complete_curriculum: generate_tweet_intent(tweet_complete_curriculum),
        milestone_start_interview_prep: generate_tweet_intent(tweet_start_curriculum),
        milestone_first_application: generate_tweet_intent(tweet_first_application),
        milestone_first_interview: generate_tweet_intent(tweet_first_interview),
        milestone_first_offer: generate_tweet_intent(tweet_first_offer),
        milestone_onboarding: generate_tweet_intent(tweet_onboarding)
    }

    ## plot easter eggs
    plot_vip = 'Referred by a VIP Member'
    plot_cookie = 'Late-night Cookie Crunch'
    plot_quiz_all = 'Nailed All Quizzes in a Session'
    plot_quiz_none = 'Flunked All Quizzes in a Session'
    plot_stats_full = 'Maxed Out One CS Knowledge Stats'
    plot_stats_all = 'Maxed Out ALL CS Knowledge Stats'
    # application rejections
    plot_rejection = 'Rejected? Well, The First One Seldom Works Out'
    plot_third_rejection = 'Rejected Again? I Thought Third Time Was the Charm'
    # first time barista
    plot_barista_discover = 'Barista is My Undercover for Collecting Buzzwords'
    plot_buzzword_ask = 'Asked My Tech-Savvy Friends about Tech Buzzwords'
    # collected all tech buzzwords, no need to ask all
    plot_all_buzzwords = 'Tech Buzzword Encyclopedia'
    # first time hackerspace
    plot_hackerspace_discover = 'Hanging Out at the Hacker Space'
    plot_hackerspace_all_events = 'The Hacker Space is My Second Home Now'
    plot_trivia = 'Tech Trivia Guru'
    plot_cupcakecpu = 'Applied to CupcakeCPU Through a Recruiter'
    plot_win_pong = 'Beat Up AI at Pong'
    plot_lose_pong = 'Got Beaten Up by AI at Pong'
    # first time music room
    plot_music_discover = 'Chill Beats to Code to'
    # first time rhythm game
    plot_rhythm_discover = 'Chill Beats to Smash Keyboard to'
    plot_rhythm_highscore = 'Set a New High Score in the Rhythm Game'
    plot_rhythm_perfect = 'Got a Nearly Perfect Score on My Favorite Music Track'
    plot_rhythm_perfect_all = 'Got a Nearly Perfect Score on ALL Music Tracks' # super hard
    # first time park
    plot_park = 'I Might Get a Puppy Just So I Can Go to the Park'

    plot_skill_coffee = 'This Job Needs Me to Brew Coffee?'
    plot_skill_fax = 'This Job Needs Me to Fix Fax Machiens?'
    plot_skill_customer = 'This Job Needs Me to Handle Angry Customers?'
    plot_skill_cable = 'This Job Needs Me to Fuse Cables?'
    plot_skill_password = 'This Job Needs Me to Retrieve Lost Passwords?'
    plot_skill_pet = 'This Job Needs Me to Pacify Office Pets?'

    plot_double_check = 'You Can Never Be Too Careful with Prod'

    plot_rewind_time = 'Travel in Time and SAVE the World'

    # tweets
    tweet_vip = 'I got referred by a VIP member in #LearnToCodeRPG. Play the game here: '
    tweet_cookie = 'I snuck out of a late-night coding session for a cookie in #LearnToCodeRPG. Play the game here: '
    tweet_quiz_all = 'I nailed all quiz questions in #LearnToCodeRPG. Play the game here: '
    tweet_quiz_none = 'I flunked all quiz questions in #LearnToCodeRPG. Play the game here: '
    tweet_stats_full = 'I maxed out my CS knowledge in #LearnToCodeRPG. Play the game here: '
    tweet_stats_all = 'I maxed out my CS knowledge in topics like HTML, CSS, JavaScript, Python, and more in #LearnToCodeRPG. Play the game here: '
    tweet_rejection = 'I got rejected by the first dev job I applied to in #LearnToCodeRPG. Can you do better? Play the game here: '
    tweet_third_rejection = 'I got rejected from dev jobs for the third time in #LearnToCodeRPG. Can you do better? Play the game here: '
    tweet_barista_discover = 'I just took up a barista gig to collect tech buzzwords in #LearnToCodeRPG. Play the game here: '
    tweet_buzzword_ask = 'I just hung out with my tech-savvy friend and asked about tech buzzwords in #LearnToCodeRPG. Play the game here: '
    tweet_all_buzzwords = 'I learned tons of tech buzzwords during my barista gig in #LearnToCodeRPG. Play the game here: '
    tweet_hackerspace_discover = 'I just discovered the Hacker Space in #LearnToCodeRPG. Play the game here: '
    tweet_hackerspace_all_events = 'I participated in all Hacker Space events in #LearnToCodeRPG. Play the game here: '
    tweet_trivia = 'I nailed all the tech trivia questions in #LearnToCodeRPG. Play the game here: '
    tweet_cupcakecpu = 'I applied to a company called CupcakeCPU through a recruiter in #LearnToCodeRPG. Play the game here: '
    tweet_win_pong = 'I just won against the AI in a Pong game in #LearnToCodeRPG. Play the game here: '
    tweet_lose_pong = 'I just lost against the AI in a Pong game in #LearnToCodeRPG. Play the game here: '
    tweet_music_discover = 'I just discovered the Music Room in #LearnToCodeRPG. Play the game here: '
    tweet_rhythm_discover = 'I just discovered the Rhythm Game in #LearnToCodeRPG. Play the game here: '
    tweet_rhythm_highscore = 'I just set a new high score in the Rhythm Game in #LearnToCodeRPG. Play the game here: '
    tweet_rhythm_perfect = 'I got a perfect score on a song in the Rhythm Game in #LearnToCodeRPG. Play the game here: '
    # Dev note: if anyone is actually capable of getting all perfect. wow
    tweet_rhythm_perfect_all = 'I got a perfect score on every song in the Rhythm Game in #LearnToCodeRPG. Play the game here: '
    tweet_park = 'I just discovered the perfect park for hanging out in #LearnToCodeRPG. Play the game here: '
    tweet_skill_coffee = 'I saw a dev job that requires the skill of brewing coffee in #LearnToCodeRPG. Play the game here: '
    tweet_skill_fax = 'I saw a dev job that requires the skill of fixing fax machines in #LearnToCodeRPG. Play the game here: '
    tweet_skill_customer = 'I saw a dev job that requires the skill of handling angry customers in #LearnToCodeRPG. Play the game here: '
    tweet_skill_cable = 'I saw a dev job that requires the skill of fusing cables in #LearnToCodeRPG. Play the game here: '
    tweet_skill_password = 'I saw a dev job that requires the skill of retrieving lost passwords in #LearnToCodeRPG. Play the game here: '
    tweet_skill_pet = 'I saw a dev job that requires the skill of pacifying office pets in #LearnToCodeRPG. Play the game here: '
    tweet_double_check = 'I double-checked, triple-cheked, and quadruple-checked my code until I lost count in #LearnToCodeRPG. Play the game here: '
    tweet_rewind_time = 'I went back in time to discover all of the alternative endings in #LearnToCodeRPG. Play the game here: '

    plot_bonus_to_tweet_map = {
        plot_vip: generate_tweet_intent(tweet_vip),
        plot_cookie: generate_tweet_intent(tweet_cookie), 
        plot_quiz_all: generate_tweet_intent(tweet_quiz_all), 
        plot_quiz_none: generate_tweet_intent(tweet_quiz_none), 
        plot_stats_full: generate_tweet_intent(tweet_stats_full),
        plot_stats_all: generate_tweet_intent(tweet_stats_all),
        plot_rejection: generate_tweet_intent(tweet_rejection),
        plot_third_rejection: generate_tweet_intent(tweet_third_rejection),
        plot_barista_discover: generate_tweet_intent(tweet_barista_discover), 
        plot_buzzword_ask: generate_tweet_intent(tweet_buzzword_ask),
        plot_all_buzzwords: generate_tweet_intent(tweet_all_buzzwords), 
        plot_hackerspace_discover: generate_tweet_intent(tweet_hackerspace_discover), 
        plot_hackerspace_all_events: generate_tweet_intent(tweet_hackerspace_all_events), 
        plot_trivia: generate_tweet_intent(tweet_trivia), 
        plot_cupcakecpu: generate_tweet_intent(tweet_cupcakecpu),
        plot_win_pong: generate_tweet_intent(tweet_win_pong), 
        plot_lose_pong: generate_tweet_intent(tweet_lose_pong), 
        plot_music_discover: generate_tweet_intent(tweet_music_discover), 
        plot_rhythm_discover: generate_tweet_intent(tweet_rhythm_discover), 
        plot_rhythm_highscore: generate_tweet_intent(tweet_rhythm_highscore), 
        plot_rhythm_perfect: generate_tweet_intent(tweet_rhythm_perfect), 
        plot_rhythm_perfect_all: generate_tweet_intent(tweet_rhythm_perfect_all), 
        plot_park: generate_tweet_intent(tweet_park), 
        plot_skill_coffee: generate_tweet_intent(tweet_skill_coffee), 
        plot_skill_fax: generate_tweet_intent(tweet_skill_fax), 
        plot_skill_customer: generate_tweet_intent(tweet_skill_customer), 
        plot_skill_cable: generate_tweet_intent(tweet_skill_cable), 
        plot_skill_password: generate_tweet_intent(tweet_skill_password), 
        plot_skill_pet: generate_tweet_intent(tweet_skill_pet), 
        plot_double_check: generate_tweet_intent(tweet_double_check),
        plot_rewind_time: generate_tweet_intent(tweet_rewind_time),
    }

    ## quiz
    quiz_fcc_launch = "The Launch of freeCodeCamp"
    quiz_fcc_mission = "The Mission of freeCodeCamp"
    quiz_code_radio = "Hello, Earth to Code Radio!"
    quiz_devdocs = "Dr. DevDocs.io"
    quiz_fcc_opensource = 'Contribute to Open Source with freeCodeCamp!'
    quiz_fcc_language = 'The Tech Stack of freeCodeCamp'
    quiz_fcc_inspiration = 'What inspired freeCodeCamp?'
    quiz_fcc_forum = 'freeCodeCamp Has a Forum? Neat!'
    quiz_fcc_chat = 'freeCodeCamp Has a Chat Server? Fancy!'
    quiz_fcc_mascot = 'freeCodeCamp Has a Mascot? Cute!'

    tweet_fcc_launch = 'I got an Easter Egg quiz question about the launch year of freeCodeCamp in #Learning. Play the game here: '
    tweet_fcc_mission = 'I got an Easter Egg quiz question about the mission of freeCodeCamp in #Learning. Play the game here: '
    tweet_code_radio = 'I got an Easter Egg quiz question about freeCodeCamp's Code Radio in #Learning. Play the game here: '
    tweet_devdocs = 'I got an Easter Egg quiz question about Devdocs.io in #Learning. Play the game here: '
    tweet_fcc_opensource = 'I got an Easter Egg quiz question about freeCodeCamp and Open Source in #Learning. Play the game here: '
    tweet_fcc_language = 'I got an Easter Egg quiz question asking what coding language the freeCodeCamp site is built with in #Learning. Play the game here: '
    tweet_fcc_inspiration = 'I got an Easter Egg quiz question asking what project inspired freeCodeCamp in #Learning. Play the game here: '
    tweet_fcc_forum = 'I got an Easter Egg quiz question about the freeCodeCamp Forum in #Learning. Play the game here: '
    tweet_fcc_chat = 'I got an Easter Egg quiz question about freeCodeCamp Chat in #Learning. Play the game here: '
    tweet_fcc_mascot = 'I got an Easter Egg quiz question about the freeCodeCamp Mascot in #Learning. Play the game here: '

    quiz_bonus_to_tweet_map = {
        quiz_fcc_launch: generate_tweet_intent(tweet_fcc_launch),
        quiz_fcc_mission: generate_tweet_intent(tweet_fcc_mission),
        quiz_code_radio: generate_tweet_intent(tweet_code_radio),
        quiz_devdocs: generate_tweet_intent(tweet_devdocs),
        quiz_fcc_opensource: generate_tweet_intent(tweet_fcc_opensource),
        quiz_fcc_language: generate_tweet_intent(tweet_fcc_language),
        quiz_fcc_inspiration: generate_tweet_intent(tweet_fcc_inspiration),
        quiz_fcc_forum: generate_tweet_intent(tweet_fcc_forum),
        quiz_fcc_chat: generate_tweet_intent(tweet_fcc_chat),
        quiz_fcc_mascot: generate_tweet_intent(tweet_fcc_mascot),
    }

    ## endings
    ending_barista = 'Now serving {font=fonts/saxmono.ttf}0xc0ffee{/font}'
    ending_cat = 'Cat Who Codes'
    ending_tutor = 'Coding It Forward'
    ending_office = 'Just Another Day at the Office'
    ending_farmer = 'Nature Lover at Heart'
    ending_dev = 'Dev Who Brought Down Prod on the First Day'

    tweet_end_barista = 'I ended up becoming a barista instead of a developer in #LearnToCodeRPG. Play the game here: '
    tweet_end_cat = 'I found my cat coding on my laptop in the middle of the night in #LearnToCodeRPG. Play it here: '
    tweet_end_tutor = 'I ended up becoming a CS teacher instead of a developer in #LearnToCodeRPG. Play the game here: '
    tweet_end_office = 'I ended up becoming an office worker instead of a developer in #LearnToCodeRPG. Play the game here: '
    tweet_end_farmer = 'I ended up working on a farm to embrace my nature-loving self instead of becoming a developer in #LearnToCodeRPG. Play the game here: '
    tweet_end_dev = 'I taught myself to code, got a tech job, and brought down prod on my first day of work in #LearnToCodeRPG. Play the game here: '

    ending_to_tweet_map = {
        ending_barista: generate_tweet_intent(tweet_end_barista),
        ending_cat: generate_tweet_intent(tweet_end_cat),
        ending_tutor: generate_tweet_intent(tweet_end_tutor),
        ending_office: generate_tweet_intent(tweet_end_barista),
        ending_farmer: generate_tweet_intent(tweet_end_farmer),
        ending_dev: generate_tweet_intent(tweet_end_dev),
    }

    ## master labels and maps
    plot_achievement = 'Story Milestones'
    plot_bonus = 'Story Easter Eggs'
    quiz_bonus = 'Quiz Question Easter Eggs'
    ending_achievement = 'Endings'

    achievement_labels_map = {
        plot_achievement: milestone_to_tweet_map,
        plot_bonus: plot_bonus_to_tweet_map,
        quiz_bonus: quiz_bonus_to_tweet_map,
        ending_achievement: ending_to_tweet_map
    }

    # master map for easy lookup in script.rpy, sanity check len(all_tweet_map) == num of achievements
    all_tweet_map = {}
    for tweet_map in achievement_labels_map.values():
        all_tweet_map.update(tweet_map)

    total_num_achievements = len(all_tweet_map)
    # all achievements unlocked
    tweet_all_achievements_unlocked = generate_tweet_intent('Hooray! I unlocked all of the achievements in #LearnToCodeRPG, bagging all alternative endings, Easter Eggs, and minigame high scores. Play the game here: ')

    # skills
    all_questions_map = {
    'CSS': css_questions,
    'HTML': html_questions,
    'Git': git_questions,
    'IT': it_questions,
    'JavaScript': javascript_questions,
    'Linux': linux_questions,
    'Python': python_questions,
    'SQL': sql_questions
    }

    # assign category to questions
    for category in all_questions_map:
        for question in all_questions_map[category]:
            question.category = category

    # master list of questions for mix-and-match
    all_quiz_questions = []
    for question_list in all_questions_map.values():
        all_quiz_questions.extend(question_list)

    # the order is important
    all_skills = [
    'HTML',
    'CSS',
    'JavaScript',
    'Python',
    'Linux',
    'Git',
    'SQL',
    'IT',
    ]
