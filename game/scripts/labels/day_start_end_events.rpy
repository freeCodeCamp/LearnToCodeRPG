label day_start:
    # this label should end up jumping to day_end, which then returns control to the main game
    $ calendar.next()

    if days_before_interview is not None:
        $ days_before_interview -= 1

    if days_before_offer is not None:
        $ days_before_offer -= 1

    scene bg bedroom with fade

    play sound 'audio/sfx/alarm.wav'
    pause 2.0
    play sound 'audio/sfx/birds.wav'
    pause 3.0

    # randomly choose a start-of-day label to call
    python:
        day_start_text = renpy.random.choice(seq=[
            'day_start_text1',
            'day_start_text2',
            'day_start_text3',
            ])
        renpy.call(day_start_text)
    
    jump day_activity_choices

# TODO: special text on days of interview
label day_start_text1:
    player "A new day!"
    show mint
    mint "Meow meow~"
    player "Good morning, Mint."
    hide mint
    player "Hmmm, I don't feel like eating a big breakfast today. I guess a cookie will do."

    scene bg kitchen with blinds
    show cookie at truecenter
    pause 0.2
    play sound 'audio/sfx/chew_food.wav'
    player "Yum yum."
    hide cookie

    scene bg bedroom with blinds
    player "Mom's homemade cookies never fail to kick-start my morning."
    return

label day_start_text2:
    mom "[persistent.player_name], breakfast's ready!"
    player "Okay, I'm up!"

    scene bg kitchen with blinds
    show toast at truecenter
    pause 0.2
    play sound 'audio/sfx/chew_food.wav'
    player "Yum yum."
    hide toast
    player "I'm done. Gotta go and prepare for the day."
    player "Have a good day at work!"
    dad "You too, [persistent.player_name]!"
    mom "See you later, honey!"
    
    scene bg bedroom with blinds
    player "Alright, moving on from the most important meal of the day."
    return

label day_start_text3:
    show mint
    mint "Meow!"
    player "Yawwwwwn..."
    player "(I feel like hitting snooze on my alarm...)"
    mint "Meow!"
    player "Ahhh... Mint, are you hungry? Okay I'm getting up and getting you breakfast."

    scene bg bedroom with fadehold
    show mint
    play sound 'audio/sfx/chew_food.wav'
    pause 4.0
    hide mint

    player "Haha Mint, thanks for waking me up."
    player "Now let's get on with the day."
    return

label day_end:
    # this label either return or jump
    # when it returns, it returns to script.rpy, where we check 
    scene bg bedroom dusk with dissolve
    player "Phew... That was a long day."

    # TODO: different text if the player has had an interview
    # they will talk with parents during dinner about the interview

    # TODO: different text
    dad "[persistent.player_name], dinner's ready!"
    player "Coming, dad!"

    scene bg bedroom night with dissolve
    player "Tomorrow will be another day. Right, Mint?"
    mint "Meow"
    player "Haha good night Mint."

    scene black with dissolve
    return

    # at the end of the day, since we've just learned something

    # check whether to proceed to the next stage
    # if the player is half-way through the curriculum and some days have elapsed
    if not has_met_marco and \
    player_stats.player_stats_map['CS Knowledge'] >= 40:
        jump stage7 # Marco

    # we check whether we can show the congrats screen
    # although other activities can increase CS knowledge as well
    # only a same-day study session will trigger this congrats
    if not has_completed_curriculum and \
    has_had_study_session_today and \
    player_stats.player_stats_map['CS Knowledge'] >= 80:
        player "Hey... I just got this email..."
        $ has_completed_curriculum = True
        $ completed_curriculum_date = date(calendar.year, calendar.month, calendar.day)
        $ days_between_start_and_curriculum_completion = (completed_curriculum_date - start_date).days
        call screen confirm_and_share(
            title="{bt}Congratulations!{/bt}",
            message="You completed the coding curriculum in {b}[days_between_start_and_curriculum_completion]{/b} days.\nNow you are ready to rock the coding interview and realize your dream of becoming a software engineer.\n Feel free to share your progress with the world!",
            ok_text="Let's crunch 'em interviews!", 
            ok_action=Jump('stage8')
        )
    
    # check whether the next day will have a sanity event
    if player_stats.player_stats_map['Sanity'] <= 60:
        python:
            label = renpy.random.choice(seq=sanity_event_labels)
            renpy.call(label)

        # restore some sanity when we return from the sanity event
        $ player_stats.change_stats_random('Sanity', 5, 20)

    # two days before an interview, the player should receive an email alert
    if days_before_interview == 2:
        player "Oh hey. Here's an email from {b}[interview_company_name]{/b}. They've looked at my resume and want to interview me in two days. I better get prepared."

    # check whether the next day has an interview
    if days_before_interview == 0:
        call day_activity_interview from _call_day_activity_interview
        $ days_before_interview = None

    # check whether the next day has an offer
    if not has_accepted_offer and days_before_offer == 0:
        player "Oh hey. Here's an email from {b}[offer_company_name]{/b}."
        player "... {w}Did I read that correctly? {sc}An offer?{/sc}"
        player happy "I made it!"

        $ has_received_offer = True
        $ has_accepted_offer = True
        $ first_offer_date = date(calendar.year, calendar.month, calendar.day)
        $ days_between_start_and_offer = (first_offer_date - start_date).days
        $ days_between_curriculum_and_offer = (completed_curriculum_date - start_date).days
        call screen confirm_and_share(
            title="{bt}Congratulations!{/bt}",
            message="You taught yourself to become a developer in {b}[days_between_start_and_offer]{/b} days, [days_between_curriculum_and_offer] days after you've completed the coding curriculum.\nNow you are ready to rock your new job!\n Feel free to share your progress with the world!",
            ok_text="Let's rock my new job!", 
            ok_action=Jump('stage14')
        )

    $ has_done_job_search_today = False

    return # should return control to script.rpy