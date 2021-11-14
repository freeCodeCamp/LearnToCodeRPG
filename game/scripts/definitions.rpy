init python:
    import re

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
    continue_looping_music = False

    all_music = [
    "audio/bgm/Chasing That Feeling.mp3",
    "audio/bgm/Never Not Favored.mp3",
    "audio/bgm/Crystalize That Child in Me.mp3",
    "audio/bgm/Press Your Advantage.mp3",
    ]

    def loop_music():
        if continue_looping_music:
            music = renpy.random.choice(all_music)
            renpy.music.queue(music, loop=False, fadein=1.0, tight=True)

    renpy.music.set_queue_empty_callback(loop_music)
  
    # to stop, set the following
    # continue_looping_music = False
    # stop music

    # day-night effects
    # https://www.twoandahalfstudios.com/2019/08/tds-making-of-3-day-night-and-sunset-reshading-images-in-renpy-with-im-matrixcolor

    tint_dark = im.matrix.tint(.44, .44, .75) * im.matrix.brightness(-0.02)
    tint_sunset = im.matrix.tint(.85, .60, .45) * im.matrix.brightness(0.10)
    # late night in front of computer
    tint_dim = im.matrix.tint(.90, .90, 1) * im.matrix.brightness(-0.1)

    # programmatically apply effects to all bg images inside game/images/bg
    for file in renpy.list_files():
        if file.startswith('images/bg'):
            image_path = re.sub(r'images/', '', file) # remove the `images/` prefix
            image_name = re.match(r'images/bg/(.+).png', file).group(1) # ex. images/bg/(bg living_room).png
            renpy.image(image_name + ' night', im.MatrixColor(image_path, tint_dark))
            renpy.image(image_name + ' dusk', im.MatrixColor(image_path, tint_sunset))

    ## font replacement
    # font file, boldness, italics
    config.font_replacement_map["fonts/lato/Lato-Regular.ttf", True, False] = ("fonts/lato/Lato-Bold.ttf", False, False)
    config.font_replacement_map["fonts/lato/Lato-Regular.ttf", False, True] = ("fonts/lato/Lato-Italic.ttf", False, False)


init:
    # major characters
    define player = Character("[persistent.player_name]", image='player')
    define annika = Character("Annika", image='annika')
    define marco = Character("Marco")
    define layla = Character("Layla")

    # minor characters
    define kid = Character("High Schoool Kid")
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

    # text displayables
    define freeCodeCamp = '{a=https://www.freecodecamp.org/}{font=fonts/saxmono.ttf}{color=#002ead}freeCodeCamp{/color}{/font}{/a}'
    define developerquiz = '{a=https://www.freecodecamp.org/}{font=fonts/saxmono.ttf}{color=#002ead}http://developerquiz.org/{/color}{/font}{/a}'

    # transitions
    define fadehold = Fade(0.5, 1.0, 0.5)

    ## images

    ## temporary
    image side player = 'chara/player/player.png'
    image side player dark = im.MatrixColor('chara/player/player.png', tint_dark)
    image side player sunset = im.MatrixColor('chara/player/player.png', tint_sunset)
    image side player dim = im.MatrixColor('chara/player/player.png', tint_dim)
    ## end

    # mint
    image mint:
        "others/mint/mint1.png"
        1.0
        "others/mint/mint2.png"
        1.0
        "others/mint/mint3.png"
        1.0
        "others/mint/mint2.png"
        1.0
        repeat

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

    # red warning flash light
    image red_flash:
        '#f00'
        alpha 0.0
        linear 1.0 alpha 0.8  
        linear 1.0 alpha 0.1
        repeat
    
    # expressions
    # player
    # define player_expressions = [
    # "neutral eyes_blink face_no_eyes_neutral",
    # "happy eyes_blink face_no_eyes_happy",
    # "confused eyes_blink face_no_eyes_confused",
    # "awe face_awe",
    # "cry face_cry",
    # "distress face_distress",
    # "laugh face_laugh",
    # ]
    # # major characters except player
    # define expressions = [
    # "neutral eyes_blink face_no_eyes_neutral",
    # "happy eyes_blink face_no_eyes_happy",
    # "confused eyes_blink face_no_eyes_confused",
    # ]

    # blink
    image player_eyes_blink = DynamicBlink(
        "images/chara/player/player_eyes_open.png",
        "images/chara/player/player_eyes_closed.png"
        )
    image annika_eyes_blink = DynamicBlink(
        "images/chara/annika/annika_eyes_open.png",
        "images/chara/annika/annika_eyes_closed.png"
        )

    # layered character sprites
    # player should always appear as a side image
    # layeredimage player:
    #     always "player_base"

    #     group eyes auto prefix "eyes"
    #     group face_no_eyes auto prefix "face_no_eyes"
    #     group face auto prefix "face"

    #     group expressions:
    #         # need null b/c no prefix
    #         attribute neutral default null
    #         attribute happy null
    #         attribute confused null
    #         attribute awe null
    #         attribute cry null
    #         attribute distress null
    #         attribute laugh null

    #     attribute_function Picker(player_expressions)

    # image side player = LayeredImageProxy("player")

    # layeredimage annika:
    #     always "annika_base"

    #     group eyes auto prefix "eyes"
    #     group face_no_eyes auto prefix "face_no_eyes"
    #     group face auto prefix "face"

    #     group expressions:
    #         attribute neutral default null
    #         attribute happy null
    #         attribute confused null

    #     attribute_function Picker(expressions)