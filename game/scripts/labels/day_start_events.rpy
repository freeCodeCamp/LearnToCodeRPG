label day_start:
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