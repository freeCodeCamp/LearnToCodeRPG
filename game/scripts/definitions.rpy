init python:
    import re
    import random # renpy.random doesn't have sample
    import urllib # for tweet intent generation

    class Picker(object):
        def __init__(self, options):
            self.options =  [ i.split() for i in options ]

        def __call__(self, attributes):
            rv = set(attributes)

            for i in self.options:
                if i[0] in attributes:
                    rv.update(i[1:])

            return rv

    meow_sounds = [
    "audio/sfx/meow1.wav",
    "audio/sfx/meow2.wav",
    "audio/sfx/meow3.wav",
    "audio/sfx/meow4.wav",
    ]

    # make a meow sound when the cat speaks
    def meow_sound_callback(event, **kwargs):
        if event == "show":
            meow = renpy.random.choice(meow_sounds)
            renpy.sound.play(meow, loop=False)

    # play music random looping
    # continue_looping_music = False

    all_music_tracks = {
    "Can't Stop Me. Can't Even Slow Me Down": "audio/bgm/Can't Stop Me. Can't Even Slow Me Down.mp3",
    'Chasing That Feeling': "audio/bgm/Chasing That Feeling.mp3",
    # 'Cruising for a Musing': 'audio/bgm/Cruising for a Musing.mp3',
    'Crystalize That Inner Child': "audio/bgm/Crystalize That Inner Child.mp3",
    'From the Ground Up': 'audio/bgm/From the Ground Up.mp3',
    'Never Not Favored': "audio/bgm/Never Not Favored.mp3",
    'Press Your Advantage': "audio/bgm/Press Your Advantage.mp3",
    'Scratching The Surface': 'audio/bgm/Scratching The Surface.mp3',
    'Still Learning': 'audio/bgm/Still Learning.mp3',
    'We Are Going to Make it': 'audio/bgm/We Are Going to Make it.mp3',
    }

    # UNUSED FUNCTION
    # continue_looping_music = False
    def loop_music():
        if continue_looping_music:
            music = renpy.random.choice(all_music_tracks.keys())
            renpy.music.queue(all_music_tracks[music], loop=False, fadein=1.0, tight=True)
            # if not renpy.in_rollback():
            #     renpy.notify('Now playing: ' + music)

    # renpy.music.set_queue_empty_callback(loop_music)
  
    # to stop, set the following
    # continue_looping_music = False
    # stop music

    # music room
    music_room = MusicRoom(fadeout=1.0)

    for track in all_music_tracks:
        file = all_music_tracks[track]
        music_room.add(file, always_unlocked=True)

    ## images

    renpy.image('main_menu', 'gui/main_menu.png')
    renpy.image('main_menu sepia', im.Sepia('gui/main_menu.png'))
    renpy.image('main_menu overlay', Composite(
        (1920, 1080), # size of main_menu.png
        (0, 0), 'main_menu', 
        (0, 0), 'white80')
    )

    # day-night effects
    # https://www.twoandahalfstudios.com/2019/08/tds-making-of-3-day-night-and-sunset-reshading-images-in-renpy-with-im-matrixcolor

    tint_dark = im.matrix.tint(0.44, 0.44, 0.75) * im.matrix.brightness(-0.02)
    tint_sunset = im.matrix.tint(0.85, 0.60, 0.45) * im.matrix.brightness(0.10)
    # late night in front of computer
    tint_dim = im.matrix.tint(0.90, 0.90, 1) * im.matrix.brightness(-0.1)

    # tint for gray NPC sprites
    tint_red = im.matrix.tint(1, 0.6, 0.6)
    tint_orange = im.matrix.tint(0.9, 0.6, 0.4)
    tint_blue = im.matrix.tint(0.7, 0.8, 1)
    tint_purple = im.matrix.tint(0.8, 0.6, 1)
    
    # programmatically apply effects
    for file in renpy.list_files():
        # bg images inside game/images/bg 
        if file.startswith('images/bg'):
            image_path = re.sub(r'images/', '', file) # remove the `images/` prefix
            image_name = re.match(r'images/bg/(.+).png', file).group(1) # ex. images/bg/(bg living_room).png
            renpy.image(image_name + ' night', im.MatrixColor(image_path, tint_dark))
            renpy.image(image_name + ' dusk', im.MatrixColor(image_path, tint_sunset))
        # npc sprites
        if file.startswith('images/chara/npc'):
            image_path = re.sub(r'images/', '', file) # remove the `images/` prefix
            image_name = re.match(r'images/chara/npc/(.+).png', file).group(1) # ex. images/bg/(bg living_room).png
            renpy.image(image_name + ' red', im.MatrixColor(image_path, tint_red))
            renpy.image(image_name + ' orange', im.MatrixColor(image_path, tint_orange))
            renpy.image(image_name + ' blue', im.MatrixColor(image_path, tint_blue))
            renpy.image(image_name + ' purple', im.MatrixColor(image_path, tint_purple))

            renpy.image(image_name + ' red flipped', im.MatrixColor(im.Flip(image_path, horizontal=True), tint_red))
            renpy.image(image_name + ' orange flipped', im.MatrixColor(im.Flip(image_path, horizontal=True), tint_orange))
            renpy.image(image_name + ' blue flipped', im.MatrixColor(im.Flip(image_path, horizontal=True), tint_blue))
            renpy.image(image_name + ' purple flipped', im.MatrixColor(im.Flip(image_path, horizontal=True), tint_purple))

    ## font replacement
    # font file, boldness, italics
    config.font_replacement_map["fonts/lato/Lato-Regular.ttf", True, False] = ("fonts/lato/Lato-Bold.ttf", False, False)
    config.font_replacement_map["fonts/lato/Lato-Regular.ttf", False, True] = ("fonts/lato/Lato-Italic.ttf", False, False)

    all_dinner_images = [
    'pizza',
    'gyoza',
    'chicken'
    ]

    def show_random_dinner_image():
        image = renpy.random.choice(all_dinner_images)
        renpy.show(image, at_list=[truecenter])
        renpy.pause(4.0)
        renpy.hide(image)

    # config.side_image_tag = 'player'

    # tweets generated by https://tech.cymi.org/tweet-intents
    # this game's url on itch
    itch_url = 'https://freecodecamp.itch.io/learn-to-code-rpg'
    github_url = 'https://github.com/freeCodeCamp/LearnToCodeRPG'

    # ref: https://tech.cymi.org/tweet-intents
    def generate_tweet_intent(tweet_content, url=itch_url):
        content_enc = urllib.quote(tweet_content, safe='')
        url_enc = urllib.quote(url, safe='')
        # append url to the end
        ret = 'https://twitter.com/intent/tweet?url=' + url_enc + '&text=' + content_enc
        return ret

    def add_achievement(achievement_name, title=None, **kwargs):
        persistent.achievements.add(achievement_name)
        if title is None:
            title = achievement_name
        kwargs['tweet_content_url'] = all_tweet_map[achievement_name]

        # play sound, cannot play on screen show b/c screen code results in multiple plays
        renpy.sound.play('audio/sfx/confirm_and_share.wav')

        renpy.call_screen('confirm_and_share_screen', title=title, **kwargs)

    # first-person blink
    def eyewarp(x):
        return x ** 1.33

    eyeopen = ImageDissolve("others/eye.png", 2, ramplen=128, reverse=False, time_warp=eyewarp)

init:
    # major characters
    define player = Character("[persistent.player_name]", image='player')
    define annika = Character("Annika", image='annika')
    define marco = Character("Marco", image='marco')
    define layla = Character("Layla", image='layla')

    # minor characters
    define kid = Character("High School Kid")
    define boy = Character("High School Boy")
    define girl = Character("High School Girl")
    define college_boy = Character("College Boy")
    define college_girl = Character("College Girl")
    define male = Character("Young Male")
    define female = Character("Young Female")
    define trivia_guy = Character("Trivia Guy") # trivia guy at hacker space
    define mom = Character("Mom")
    define dad = Character("Dad")
    define mint = Character("Mint", callback=meow_sound_callback) # player's cat
    define interviewer = Character("Interviewer")
    define host = Character("Host")
    define journalist = Character("Journalist")
    define cafe_manager = Character("Cafe Manager")
    define office_worker = Character("Office Worker")

    # text displayables
    define freeCodeCamp = '{a=https://www.freecodecamp.org/}{font=fonts/saxmono.ttf}{color=#002ead}freeCodeCamp.org{/color}{/font}{/a}'
    define developerquiz = '{a=https://www.freecodecamp.org/}{font=fonts/saxmono.ttf}{color=#002ead}http://developerquiz.org/{/color}{/font}{/a}'
    define learn_to_code_rpg_on_itch = '{a=https://freecodecamp.itch.io/learn-to-code-rpg}{font=fonts/saxmono.ttf}{color=#002ead}Learn to Code RPG on itch.io{/color}{/font}{/a}'
    define learn_to_code_rpg_on_github = '{a=https://github.com/freeCodeCamp/LearnToCodeRPG}{font=fonts/saxmono.ttf}{color=#002ead}Learn to Code RPG on itch.io{/color}{/font}{/a}'

    # transitions
    define fadehold = Fade(0.5, 1.0, 0.5)

    ## images
    # mint
    image mint:
        "others/mint/mint1.png" # can simply use `mint1`
        1.0
        "others/mint/mint2.png"
        1.0
        "others/mint/mint3.png"
        1.0
        "others/mint/mint2.png"
        1.0
        repeat

    image mint_with_pixel_sunglasses = Composite(
        (782, 782), # size of mint.png
        (0, 0), 'mint', 
        (0, 0), 'others/mint/mint_pixelsunglasses.png')

    # cookie
    image cookie:
        "others/cookie/cookie1.png"
        0.5
        "others/cookie/cookie2.png"
        0.5
        "others/cookie/cookie3.png"
        0.5
        "others/cookie/cookie4.png"
        0.5
        "others/cookie/cookie5.png"

    # toast
    image toast:
        'others/toast/toast1.png'
        0.8
        'others/toast/toast2.png'
        0.8
        'others/toast/toast3.png'
        0.8
        'others/toast/toast4.png'
        0.8
        'others/toast/toast5.png'

    # coffee
    image coffee:
        'others/coffee/coffee1.png'
        0.8
        'others/coffee/coffee2.png'
        0.8
        'others/coffee/coffee3.png'
        0.8
        repeat

    # pizza
    image pizza:
        'others/pizza/pizza1.png'
        0.8
        'others/pizza/pizza2.png'
        0.8
        'others/pizza/pizza3.png'
        0.8
        'others/pizza/pizza4.png'
        0.8
        'others/pizza/pizza5.png'

    # gyoza
    image gyoza:
        'others/gyoza/gyoza1.png'
        1.0
        'others/gyoza/gyoza2.png'
        1.0
        'others/gyoza/gyoza3.png'

    # chicken
    image chicken:
        'others/chicken/chicken1.png'
        0.8
        'others/chicken/chicken2.png'
        0.8
        'others/chicken/chicken3.png'
        0.8
        'others/chicken/chicken4.png'

    # red warning flash light
    image red_flash:
        '#f00'
        alpha 0.0
        linear 1.0 alpha 0.8  
        linear 1.0 alpha 0.1
        repeat

    # TODO: tint sprites in code
    # unused tinted sprites
    # image side player dark = im.MatrixColor('chara/player/player.png', tint_dark)
    # image side player sunset = im.MatrixColor('chara/player/player.png', tint_sunset)
    # image side player dim = im.MatrixColor('chara/player/player.png', tint_dim)
    
    ## expressions
    # player
    define player_expressions = [
    "neutral eyes_blink brows_neutral mouth_frown",
    "smile eyes_blink brows_raised mouth_smile",
    "happy eyes_blink brows_raised mouth_laugh",
    "surprised eyes_blink brows_raised mouth_oh",
    "laugh eyes_laugh brows_neutral mouth_laugh",
    "worry eyes_blink brows_lowered mouth_frown",
    "pout eyes_blink brows_lowered mouth_pout",
    "relieved eyes_closed brows_neutral mouth_oh"
    ]
    # major characters except player
    define expressions = [
    "neutral eyes_blink brows_neutral mouth_smile",
    "serious eyes_blink brows_neutral mouth_frown",
    "laugh eyes_laugh brows_raised mouth_laugh",
    ]

    # blink
    image player_eyes_blink = DynamicBlink(
        "images/chara/player/player_eyes_open.png",
        "images/chara/player/player_eyes_closed.png"
        )

    image annika_eyes_blink = DynamicBlink(
        "images/chara/annika/annika_eyes_open.png",
        "images/chara/annika/annika_eyes_closed.png"
        )

    image layla_eyes_blink = DynamicBlink(
        "images/chara/layla/layla_eyes_open.png",
        "images/chara/layla/layla_eyes_closed.png"
        )

    image marco_eyes_blink = DynamicBlink(
        "images/chara/marco/marco_eyes_open.png",
        "images/chara/marco/marco_eyes_closed.png"
        )

    # layered character sprites
    default player_base = 'player_base' # 'player_overall' or 'player_apron'
    default player_glasses = 'player_glasses' # 'player_pixelsunglasses' or None
    # player should always appear as a side image
    layeredimage player:
        if player_base == 'player_base':
            'player_base'
        elif player_base == 'player_apron':
            'player_apron'
        elif player_base == 'player_overall':
            'player_overall'

        group eyes auto prefix "eyes"
        group brows auto prefix "brows"
        group mouth auto prefix "mouth"

        group expressions:
            # need null b/c no prefix
            attribute neutral default null
            attribute smile null
            attribute happy null
            attribute surprised null
            attribute laugh null
            attribute worry null
            attribute pout null
            attribute relieved null

        if player_glasses == 'player_pixelsunglasses':
            "player_pixelsunglasses"
        elif player_glasses == 'player_glasses':
            "player_glasses"

        attribute_function Picker(player_expressions)

    image side player = LayeredImageProxy("player")

    layeredimage annika:
        always "annika_base"

        group eyes auto prefix "eyes"
        group brows auto prefix "brows"
        group mouth auto prefix "mouth"

        group expressions:
            attribute neutral default null
            attribute serious null
            attribute laugh null

        attribute_function Picker(expressions)

    layeredimage layla:
        always "layla_base"

        group eyes auto prefix "eyes"
        group brows auto prefix "brows"
        group mouth auto prefix "mouth"

        group expressions:
            attribute neutral default null
            attribute serious null
            attribute laugh null

        attribute glasses default

        attribute_function Picker(expressions)

    layeredimage marco:
        always "marco_base"

        group eyes auto prefix "eyes"
        group brows auto prefix "brows"
        group mouth auto prefix "mouth"

        group expressions:
            attribute neutral default null
            attribute serious null
            attribute laugh null

        attribute glasses default

        attribute_function Picker(expressions)