init python:
    annika_open_source_visited = False
    annika_open_source_first_visit = False

    has_had_study_session_today = False

    # player_stats.player_stats_map['CS Knowledge'] >= 80
    has_completed_curriculum = False

    # if the player is half-way through the curriculum and some days have elapsed
    # player_stats.player_stats_map['CS Knowledge'] >= 40 and player_stats.day_counter > 8
    has_met_marco = False

    days_before_interview = None

    has_received_offer = False

    # day counter of the first offer
    day_of_first_offer = None

    # TODO: beyond demo version, can do negotiation
    has_accepted_offer = False

    # player can meet Layla at Hacker Space
    has_met_layla = False

    # see sanity_events.rpy
    # initially there are only events with player themself and Annika
    # eventually the plot will unlock those with Ryan and the community
    sanity_event_labels = [
        'sanity_event_player',
        'sanity_event_mint',
        'sanity_event_annika_boba',
    ]