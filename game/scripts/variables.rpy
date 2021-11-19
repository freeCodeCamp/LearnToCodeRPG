init python:
    stats_unlocked = False
    todo_unlocked = False

    study_session_questions = general_questions

    has_visited_hacker_space_with_annika = False

    # unlocks Marco's topics_to_ask
    has_met_marco = False

    # once this is True, trivia guy no longer appears, and player can get a first round interview w/ CupCakeCPU
    has_won_hacker_space_trivia = False
    has_applied_to_cupcakecpu = False

    # player_stats.player_stats_map['CS Knowledge'] >= 80
    has_completed_curriculum = False

    has_received_offer = False
    # TODO: beyond demo version, can do negotiation
    has_accepted_offer = False

    day_activity = None # set in day_activity_choice.rpy
    interview_company_name = None # set in day_activity_choice.rpy
    offer_company_name = None # set in quiz_session.rpy

    topics_to_ask = set()
    npc = annika
    npc_sprite = 'annika'

    seen_hacker_space_events = set()

    seen_barista_events = set()

    seen_company_names = set()

    ## Non-mutable

    # to-do strings
    todo_check_fcc = 'Check out [freeCodeCamp]'
    todo_ask_curriculum = 'Ask Annika about CS curriculum'
    todo_learn_cs = 'Ramp up CS knowledge'
    todo_apply_cupcakecpu = 'Apply to CupcakeCPU'
    todo_apply_to_jobs = 'Start applying to jobs'
    todo_interview_prep = 'Start preparing for coding interviews'
    todo_get_job = 'Get a developer job'
    todo_ask_hackathon = 'Learn about Hackathon'
    todo_ask = 'Learn about ' # should be concatenated with vocabs from barista story

    day_acitivity_study = 'Study CS Fundamentals' # will later change into todo_interview_prep

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
