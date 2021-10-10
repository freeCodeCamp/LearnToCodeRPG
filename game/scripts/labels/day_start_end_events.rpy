label day_start:
    # this label should end up jumping to day_end

    $ player_stats.day_counter += 1
    scene bg bedroom day with fade

    # play sound of alarm
    # play sound of bird chirping
    player "A new day!"
    mint "Meow meow"
    player "Okay, what shall we do for the day?"
    jump day_activity_choices

# TODO: different text
label start_of_day_1:
    pass

label start_of_day_2:
    pass

label start_of_day_3:
    pass

label day_end:
    # this label either return or jump
    # when it returns, it returns to script.rpy, where we check 
    scene bg bedroom dusk with dissolve
    player "Phew... That was a long day."
    # TODO: different text
    dad "[persistent.player_name], dinner's ready!"
    player "Coming, dad!"

    scene bg bedroom night with dissolve
    player "Tomorrow will be another day. Right, Mint?"
    mint "Meow"
    player "Haha good night Mint."

    scene black with dissolve

    # at the end of the day, since we've just learned something

    # we check whether we can show the congrats screen
    # although other activities can increase CS knowledge as well
    # only a same-day study session will trigger this congrats
    if has_had_study_session_today and player_stats.player_stats_map['CS Knowledge'] >= 80:
        $ has_completed_curriculum = True
        call screen confirm_and_share(
            title="{bt}Congratulations!{/bt}",
            message="You completed the coding curriculum in {b}[player_stats.day_counter]{/b} days.\nNow you are ready to rock the coding interview and realize your dream of becoming a software engineer.\n Feel free to share your progress with the world!",
            ok_text="Let's go!", okay_action=Jump('stage8')
        )

    # check whether to proceed to the next stage
    # if the player is half-way through the curriculum and some days have elapsed
    if not has_met_marco and \
    player_stats.player_stats_map['CS Knowledge'] >= 40 and \
    player_stats.day_counter > 8:
        jump stage7 # Marco
    
    # check whether the next day will have a sanity event
    if player_stats.player_stats_map['Sanity'] <= 60:
        python:
            label = renpy.random.choice(seq=sanity_event_labels)
            renpy.call(label)

            # restore some sanity when we return from the sanity event
            player_stats.change_stats_random('Sanity', 5, 20)

    # check whether the next day has an interview
    if days_before_interview == 0:
        call day_activity_interview

    # return to script.rpy
    return