init python:
    class Picker(object):
        def __init__(self, options):
            self.options =  [ i.split() for i in options ]

        def __call__(self, attributes):
            rv = set(attributes)

            for i in self.options:
                if i[0] in attributes:
                    rv.update(i[1:])

            return rv

    # make a meow sound when the cat speaks
    def meow_sound_callback(event, **kwargs):
        if event == "show":
            renpy.sound.play("audio/sfx/meow.wav", loop=False)

init:
    # major characters
    define player = Character("[persistent.player_name]", image="player")
    define annika = Character("Annika", image="annika")
    define ryan = Character("Ryan")
    define becca = Character("Becca")

    # minor characters
    define kid = Character("High Schoool Kid")
    define mom = Character("Mom")
    define dad = Character("Dad")
    define mint = Character("Mint", callback=meow_sound_callback) # player's cat

    # expressions
    # player
    define player_expressions = [
    "neutral eyes_blink face_no_eyes_neutral",
    "happy eyes_blink face_no_eyes_happy",
    "confused eyes_blink face_no_eyes_confused",
    "awe face_awe",
    "cry face_cry",
    "distress face_distress",
    "laugh face_laugh",
    ]
    # major characters except player
    define expressions = [
    "neutral eyes_blink face_no_eyes_neutral",
    "happy eyes_blink face_no_eyes_happy",
    "confused eyes_blink face_no_eyes_confused",
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

    # layered character sprites
    # player should always appear as a side image
    layeredimage player:
        always "player_base"

        group eyes auto prefix "eyes"
        group face_no_eyes auto prefix "face_no_eyes"
        group face auto prefix "face"

        group expressions:
            # need null b/c no prefix
            attribute neutral default null
            attribute happy null
            attribute confused null
            attribute awe null
            attribute cry null
            attribute distress null
            attribute laugh null

        attribute_function Picker(player_expressions)

    image side player = LayeredImageProxy("player")

    layeredimage annika:
        always "annika_base"

        group eyes auto prefix "eyes"
        group face_no_eyes auto prefix "face_no_eyes"
        group face auto prefix "face"

        group expressions:
            attribute neutral default null
            attribute happy null
            attribute confused null

        attribute_function Picker(expressions)

    # text displayables
    define freeCodeCamp = '{a=https://www.freecodecamp.org/}{font=fonts/saxmono.ttf}{color=#002ead}freeCodeCamp{/color}{/font}{/a}'

    # transitions
    define longfade = Fade(3.0)