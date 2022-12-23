init python:
    import re
    import random # renpy.random doesn't have sample
    import urllib.parse # for tweet intent generation

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
    'Cruising for a Musing': 'audio/bgm/Cruising for a Musing.mp3',
    'Crystalize That Inner Child': "audio/bgm/Crystalize That Inner Child.mp3",
    'From the Ground Up': 'audio/bgm/From the Ground Up.mp3',
    'Never Not Favored': "audio/bgm/Never Not Favored.mp3",
    'Press Your Advantage': "audio/bgm/Press Your Advantage.mp3",
    'Scratching The Surface': 'audio/bgm/Scratching The Surface.mp3',
    'Still Learning': 'audio/bgm/Still Learning.mp3',
    'We Are Going to Make it': 'audio/bgm/We Are Going to Make it.mp3',
    'Alone With the City': "audio/bgm/Alone With the City.mp3",
    'The Surest Way Out is Through': "audio/bgm/The Surest Way Out is Through.mp3",
    "Can't Stay Down": "audio/bgm/Can't Stay Down.mp3",
    'Walking on Air': "audio/bgm/Walking on Air.mp3",
    'Collider in My Head': "audio/bgm/Collider in My Head.mp3",
    }

    all_music_files = list(all_music_tracks.values())

    # music room
    music_room = MusicRoom(fadeout=1.0)

    for track in all_music_tracks:
        file = all_music_tracks[track]
        music_room.add(file, always_unlocked=True)

    ## images

    renpy.image('main_menu_v1', 'gui/main_menu_v1.png')

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
            image_name = re.match(r'images/bg/(.+).png', file, re.I).group(1) # ex. images/bg/(bg living_room).png
            renpy.image(image_name + ' night', im.MatrixColor(image_path, tint_dark))
            renpy.image(image_name + ' dusk', im.MatrixColor(image_path, tint_sunset))
        # npc sprites
        if file.startswith('images/chara/npc'):
            image_path = re.sub(r'images/', '', file) # remove the `images/` prefix
            image_name = re.match(r'images/chara/npc/(.+).png', file, re.I).group(1) # ex. images/bg/(bg living_room).png
            renpy.image(image_name + ' red', im.MatrixColor(image_path, tint_red))
            renpy.image(image_name + ' orange', im.MatrixColor(image_path, tint_orange))
            renpy.image(image_name + ' blue', im.MatrixColor(image_path, tint_blue))
            renpy.image(image_name + ' purple', im.MatrixColor(image_path, tint_purple))

            renpy.image(image_name + ' red flipped', im.MatrixColor(im.Flip(image_path, horizontal=True), tint_red))
            renpy.image(image_name + ' orange flipped', im.MatrixColor(im.Flip(image_path, horizontal=True), tint_orange))
            renpy.image(image_name + ' blue flipped', im.MatrixColor(im.Flip(image_path, horizontal=True), tint_blue))
            renpy.image(image_name + ' purple flipped', im.MatrixColor(im.Flip(image_path, horizontal=True), tint_purple))

    # blink
    charas = [
    'player',
    'annika',
    'layla',
    'marco',
    'goro',
    'iris',
    'mala',
    'adaku',
    'darius',
    'josephine',
    'maria',
    'oliver',
    'raj',
    'rishi',
    'rohit',
    'suits'
    ]
    '''
    image player_eyes_blink = DynamicBlink(
        "images/chara/player/player_eyes_open.png",
        "images/chara/player/player_eyes_closed.png"
        )
    '''
    for chara in charas:
        renpy.image(chara + '_eyes_blink', DynamicBlink(
            f"images/chara/{chara}/{chara}_eyes_open.png",
            f"images/chara/{chara}/{chara}_eyes_closed.png"
            )
        )

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
    article_url = 'https://www.freecodecamp.org/news/learn-to-code-rpg-1-5-update/'

    # ref: https://tech.cymi.org/tweet-intents
    def generate_tweet_intent(tweet_content, url=article_url):
        content_enc = urllib.parse.quote(tweet_content, safe='')
        url_enc = urllib.parse.quote(url, safe='')
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

    # ATL transition
    eyeopen = ImageDissolve("others/eye.png", 2, ramplen=128, reverse=False, time_warp=eyewarp)
    eyeclose = ImageDissolve("others/eye.png", 2, ramplen=128, reverse=True, time_warp=eyewarp)

init:
    # major characters
    define player = Character("[player_name]", image='player')
    define annika = Character(_("Annika"), image='annika')
    define marco = Character(_("Marco"), image='marco')
    define layla = Character(_("Layla"), image='layla')
    # v2 characters
    define receptionist = Character(_("Receptionist"), image='maria')
    define maria = Character(_("Maria"), image='maria')
    define iris = Character(_("Iris"), image='iris')
    define goro = Character(_("Goro"), image='goro')
    define oliver = Character(_("Oliver"), image='oliver')
    define mala = Character(_("Mala"), image='mala')
    define mike = Character(_("Mike"))
    define motormouth_mike = Character(_("Motormouth Mike"))
    define darius = Character(_("Darius"), image='darius')
    define greg = Character(_("Greg"))
    define adaku = Character(_('Adaku'), image='adaku')
    define josephine = Character(_('Josephine'), image='josephine')
    define raj = Character(_('Raj'), image='raj')
    define rishi = Character(_('Rishi'), image='rishi')
    define rohit = Character(_('Rohit'), image='rohit')
    define suits = Character(_('Suits'), image='suits')

    # minor characters
    define kid = Character(_("High School Kid"))
    define boy = Character(_("High School Boy"))
    define girl = Character(_("High School Girl"))
    define college_boy = Character(_("College Boy"))
    define college_girl = Character(_("College Girl"))
    define male = Character(_("Young Male"))
    define female = Character(_("Young Female"))
    define trivia_guy = Character(_("Trivia Guy")) # trivia guy at hacker space
    define mom = Character(_("Mom"))
    define dad = Character(_("Dad"))
    define mint = Character(_("Mint"), callback=meow_sound_callback) # player's cat
    define interviewer = Character(_("Interviewer"))
    define host = Character(_("Host"))
    define journalist = Character(_("Journalist"))
    define cafe_manager = Character(_("Cafe Manager"))
    define office_worker = Character(_("Office Worker"))
    define high_school_student = Character(_("High School Student"))
    define developer1 = Character(_("Developer 1"))
    define developer2 = Character(_("Developer 2"))
    define teen = Character(_("Teen"))
    define salesperson1 = Character(_("Salesperson 1"))
    define salesperson2 = Character(_("Salesperson 2"))
    define salesperson3 = Character(_("Salesperson 3"))

    # text displayables
    define freeCodeCamp = '{a=https://www.freecodecamp.org/}{font=fonts/saxmono.ttf}{color=#002ead}freeCodeCamp.org{/color}{/font}{/a}'
    define developerquiz = 'https://developerquiz.org/'
    define learn_to_code_rpg_on_itch = '{a=https://freecodecamp.itch.io/learn-to-code-rpg}{font=fonts/saxmono.ttf}{color=#002ead}' + _("Learn to Code RPG on itch.io") + '{/color}{/font}{/a}'
    define learn_to_code_rpg_on_github = '{a=https://github.com/freeCodeCamp/LearnToCodeRPG}{font=fonts/saxmono.ttf}{color=#002ead}' + _("Learn to Code RPG on GitHub") + '{/color}{/font}{/a}'

    # transitions
    define fadehold = Fade(0.5, 1.0, 0.5)
    # NOTE: use fadehold for bigger location change
    # location change within a company/space should use blinds
    # changing time of the day should use dissolve

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
        'coffee1'
        0.8
        'coffee2'
        0.8
        'coffee3'
        0.8
        'coffee4'
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
    "relieved eyes_closed brows_neutral mouth_oh",
    ]

    # major characters except player
    define expressions = [
    "neutral eyes_blink brows_neutral mouth_smile",
    "serious eyes_blink brows_neutral mouth_frown",
    "laugh eyes_laugh brows_raised mouth_laugh",
    ]

    # other charas
    define goro_expressions = [
    "neutral eyes_blink brows_1 mouth_2",
    "smile eyes_blink brows_1 mouth_1",
    "sad eyes_blink brows_4 mouth_2",
    "fearful eyes_blink brows_4 mouth_6",
    "angry eyes_blink brows_3 mouth_2",
    "disgust eyes_blink brows_5 mouth_4",
    "laugh eyes_narrowblink brows_2 mouth_5",
    ]

    define iris_expressions = [
    "neutral eyes_blink brows_1 mouth_1",
    "smile eyes_blink brows_1 mouth_2",
    "angry eyes_blink brows_2 mouth_1",
    "disgust eyes_narrowblink brows_2 mouth_3",
    "confused eyes_narrowblink brows_3 mouth_1",
    ]

    define mala_expressions = [
    "neutral eyes_blink brows_1 mouth_2",
    "smile eyes_blink brows_1 mouth_1",
    "angry eyes_blink brows_2 mouth_2",
    "laugh eyes_blink brows_1 mouth_3",
    ]

    define adaku_expressions = [
    'neutral eyes_blink brows_1 mouth_1',
    'smile eyes_blink brows_1 mouth_2',
    'laugh eyes_laugh brows_1 mouth_3',
    'confused eyes_blink brows_2 mouth_1',
    ]

    define darius_expressions = [
    'neutral eyes_blink brows_1 mouth_1',
    'smile eyes_blink brows_1 mouth_2',
    'laugh eyes_laugh brows_1 mouth_2',
    'sad eyes_blink brows_2 mouth_3',
    'fearful eyes_blink brows_2 mouth_5',
    'confused eyes_blink brows_3 mouth_4'
    ]

    define josephine_expressions = [
    'neutral eyes_blink brows_1 mouth_1',
    'smile eyes_blink brows_1 mouth_2',
    'sad eyes_blink brows_2 mouth_1',
    'fearful eyes_blink brows_2 mouth_3',
    'confused eyes_blink brows_3 mouth_1',
    ]

    define maria_expressions = [
    'neutral eyes_blink brows_1 mouth_1',
    'smile eyes_blink brows_1 mouth_2',
    'sad eyes_blink brows_2 mouth_1',
    'fearful eyes_blink brows_2 mouth_4',
    'laugh eyes_laugh brows_1 mouth_3'
    ]

    define oliver_expressions = [
    'neutral eyes_blink brows_1 mouth_1',
    'smile eyes_blink brows_1 mouth_2',
    'laugh eyes_blink brows_1 mouth_3'
    ]

    define raj_expressions = [
    'neutral eyes_blink brows_1 mouth_1',
    'smile eyes_blink brows_1 mouth_2',
    'sad eyes_blink brows_3 mouth_1',
    'angry eyes_blink brows_2 mouth_3',
    'laugh eyes_blink brows_1 mouth_4',
    'confused eyes_blink brows_4 mouth_1'
    ]

    define rishi_expressions = [
    'neutral eyes_blink brows_1 mouth_1',
    'smile eyes_blink brows_1 mouth_2',
    'confused eyes_blink brows_4 mouth_1',
    'disgust eyes_blink brows_3 mouth_3'
    ]

    define rohit_expressions = [
    'neutral eyes_blink brows_1 mouth_1',
    'smile eyes_blink brows_1 mouth_2',
    'angry eyes_blink brows_2 mouth_1'
    ]

    define suits_expressions = [
    'neutral eyes_blink brows_1 mouth_1',
    'smile eyes_blink brows_1 mouth_2',
    'angry eyes_blink brows_2 mouth_1',
    'disgust eyes_blink brows_2 mouth_3',
    'confused eyes_blink brows_3 mouth_1'
    ]

    # more blink
    image goro_eyes_narrowblink = DynamicBlink(
        "images/chara/goro/goro_eyes_narrow.png",
        "images/chara/goro/goro_eyes_closed.png"
        )

    image iris_eyes_narrowblink = DynamicBlink(
        "images/chara/iris/iris_eyes_narrow.png",
        "images/chara/iris/iris_eyes_closed.png"
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

        attribute sweat

        # glasses are on top of the face layers
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

    # charas with custom Picker(chara_expressions)
    layeredimage goro:
        always "goro_base"

        group eyes auto prefix "eyes"
        group brows auto prefix "brows"
        group mouth auto prefix "mouth"

        group expressions:
            attribute neutral default null
            attribute smile null
            attribute sad null
            attribute fearful null
            attribute angry null
            attribute disgust null
            attribute laugh null

        attribute sweat

        attribute_function Picker(goro_expressions)

    layeredimage iris:
        always "iris_base"

        group eyes auto prefix "eyes"
        group brows auto prefix "brows"
        group mouth auto prefix "mouth"

        group expressions:
            attribute neutral default null
            attribute smile null
            attribute angry null
            attribute disgust null
            attribute confused null

        attribute sweat

        attribute_function Picker(iris_expressions)

    layeredimage mala:
        always "mala_base"

        group eyes auto prefix "eyes"
        group brows auto prefix "brows"
        group mouth auto prefix "mouth"

        group expressions:
            attribute neutral default null
            attribute smile null
            attribute angry null
            attribute laugh null

        attribute sweat

        attribute_function Picker(mala_expressions)

    layeredimage adaku:
        always "adaku_base"

        group eyes auto prefix "eyes"
        group brows auto prefix "brows"
        group mouth auto prefix "mouth"

        group expressions:
            attribute neutral default null
            attribute smile null
            attribute laugh null
            attribute confused null

        attribute sweat

        attribute_function Picker(adaku_expressions)

    layeredimage darius:
        always "darius_base"

        group eyes auto prefix "eyes"
        group brows auto prefix "brows"
        group mouth auto prefix "mouth"

        group expressions:
            attribute neutral default null
            attribute smile null
            attribute laugh null
            attribute sad null
            attribute fearful null
            attribute confused null

        attribute glasses default
        attribute sweat

        attribute_function Picker(darius_expressions)

    layeredimage josephine:
        always "josephine_base"

        group eyes auto prefix "eyes"
        group brows auto prefix "brows"
        group mouth auto prefix "mouth"

        group expressions:
            attribute neutral default null
            attribute smile null
            attribute sad null
            attribute fearful null
            attribute confused null

        attribute sweat
        attribute blush

        attribute_function Picker(josephine_expressions)

    layeredimage maria:
        always "maria_base"

        group eyes auto prefix "eyes"
        group brows auto prefix "brows"
        group mouth auto prefix "mouth"

        group expressions:
            attribute neutral default null
            attribute smile null
            attribute sad null
            attribute fearful null
            attribute laugh null

        attribute glasses default
        attribute sweat

        attribute_function Picker(maria_expressions)

    layeredimage oliver:
        always "oliver_base"

        group eyes auto prefix "eyes"
        group brows auto prefix "brows"
        group mouth auto prefix "mouth"

        group expressions:
            attribute neutral default null
            attribute smile null
            attribute laugh null

        attribute sweat

        attribute_function Picker(oliver_expressions)

    layeredimage raj:
        always "raj_base"

        group eyes auto prefix "eyes"
        group brows auto prefix "brows"
        group mouth auto prefix "mouth"

        group expressions:
            attribute neutral default null
            attribute smile null
            attribute sad null
            attribute angry null
            attribute laugh null
            attribute confused null

        attribute sweat

        attribute_function Picker(raj_expressions)

    layeredimage rishi:
        always "rishi_base"

        group eyes auto prefix "eyes"
        group brows auto prefix "brows"
        group mouth auto prefix "mouth"

        group expressions:
            attribute neutral default null
            attribute smile null
            attribute confused null
            attribute disgust null

        attribute sweat

        attribute_function Picker(rishi_expressions)

    layeredimage rohit:
        always "adaku_base"

        group eyes auto prefix "eyes"
        group brows auto prefix "brows"
        group mouth auto prefix "mouth"

        group expressions:
            attribute neutral default null
            attribute smile null
            attribute angry null

        attribute sweat
        attribute blush

        attribute_function Picker(rohit_expressions)

    layeredimage suits:
        always "suits_base"

        group eyes auto prefix "eyes"
        group brows auto prefix "brows"
        group mouth auto prefix "mouth"

        group expressions:
            attribute neutral default null
            attribute smile null
            attribute angry null
            attribute disgust null
            attribute confused null

        attribute sweat

        attribute_function Picker(suits_expressions)

    # player's bedroom
    image bg bedroom = LiveComposite(
        (1920, 1080), # size of displayable
        (0, 0), 'bg bedroom_empty',

        # decorations
        (0, 0), ConditionSwitch(
            "'plant' in player_stats.room_display_tagless", 'room plant',
            True, Null()
            ),
        (0, 0), ConditionSwitch(
            "'poster1' in player_stats.room_display_tagless", 'room poster1',
            True, Null()
            ),
        (0, 0), ConditionSwitch(
            "'poster2' in player_stats.room_display_tagless", 'room poster2',
            True, Null()
            ),
        (0, 0), ConditionSwitch(
            "'poster3' in player_stats.room_display_tagless", 'room poster3',
            True, Null()
            ),
        (0, 0), ConditionSwitch(
            "'cat_lamp' in player_stats.room_display_tagless", 'room cat_lamp',
            True, Null()
            ),
        (0, 0), ConditionSwitch(
            "'cat_bed' in player_stats.room_display_tagless", 'room cat_bed',
            True, Null()
            ),

        # desk
        (0, 0), ConditionSwitch(
            "player_stats.room_display_tagged[DESK].image == 'desk'", 'room desk',
            "player_stats.room_display_tagged[DESK].image == 'desk_nice'", 'room desk_nice',
            True, Null()
            ),

        # PC needs to be above the desk
        (0, 0), ConditionSwitch(
            "player_stats.room_display_tagged[PC].image == 'pc_old'", 'room pc_old',
            "player_stats.room_display_tagged[PC].image == 'pc_used'", 'room pc_used',
            "player_stats.room_display_tagged[PC].image == 'pc_student'", 'room pc_student',
            "player_stats.room_display_tagged[PC].image == 'pc_custom'", 'room pc_custom',
            True, Null()
            ),

        # chair might be hiding the PC
        (0, 0), ConditionSwitch(
            "player_stats.room_display_tagged[CHAIR].image == 'chair_wooden'", 'room chair_wooden',
            "player_stats.room_display_tagged[CHAIR].image == 'chair_second_hand'", 'room chair_second_hand',
            "player_stats.room_display_tagged[CHAIR].image == 'chair_nice'", 'room chair_nice',
            "player_stats.room_display_tagged[CHAIR].image == 'chair_fancy'", 'room chair_fancy',
            True, Null()
            ),

        # router needs to be above the desk
        (0, 0), ConditionSwitch(
            "player_stats.room_display_tagged[ROUTER].image == 'hotspot'", 'room hotspot',
            "player_stats.room_display_tagged[ROUTER].image == 'router_simple'", 'room router_simple',
            "player_stats.room_display_tagged[ROUTER].image == 'router_nice'", 'room router_nice',
            "player_stats.room_display_tagged[ROUTER].image == 'router_fancy'", 'room router_fancy',
            True, Null()
            ),
        )

## translation styles
# https://www.renpy.org/doc/html/gui.html#translation-and-gui-variables
translate simplified_chinese python:
    gui.text_font = "fonts/simplified_chinese/NotoSansSC-Regular.otf"
    gui.name_text_font = "fonts/simplified_chinese/NotoSansSC-Regular.otf"
    gui.interface_text_font = "fonts/simplified_chinese/NotoSansSC-Regular.otf"
    gui.button_text_font = "fonts/simplified_chinese/NotoSansSC-Regular.otf"
    gui.choice_button_text_font = "fonts/simplified_chinese/NotoSansSC-Regular.otf"
