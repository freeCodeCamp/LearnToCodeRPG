init python:
    stats_unlocked = False
    todo_unlocked = False

    study_session_questions = general_questions

    annika_open_source_visited = False
    annika_open_source_first_visit = False

    has_had_study_session_today = False
    has_done_job_search_today = False

    # player_stats.player_stats_map['CS Knowledge'] >= 80
    has_completed_curriculum = False

    # TODO: refactor
    has_met_marco = False

    # TODO: definitely refactor
    interview_company_name = None
    days_before_interview = None

    offer_company_name = None
    days_before_offer = None

    has_received_offer = False
    # TODO: beyond demo version, can do negotiation
    has_accepted_offer = False

    # TODO: more day counters, more refactoring
    day_completed_curriculum = None
    # day counter of the first offer, subtract this from the other day counters
    day_of_first_offer = None

    # player can meet Layla at Hacker Space
    has_met_layla = False

    # topics to ask Annika, Marco, and Layla
    topics_to_ask = set()

    ## Non-mutable

    # see sanity_events.rpy
    # initially there are only events with player themself and Annika
    # eventually the plot will unlock those with Ryan and the community
    sanity_event_labels = [
        'sanity_event_player',
        'sanity_event_mint',
        'sanity_event_annika_boba',
    ]