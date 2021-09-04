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

init:
    # major characters
    define mc = Character("[persistent.player_name]")
    define annika = Character("Annika")
    define ryan = Character("Ryan")
    define becca = Character("Becca")

    # minor characters
    define kid = Character("Kid")

    # expressions for all characters
    define expressions = [
            "neutral eyes_blink face_neutral",
            "happy eyes_blink face_happy",
            "confused eyes_blink face_confused",
        ]

    # blink
    image annika_eyes_blink = DynamicBlink(
        "images/chara/annika/annika_eyes_open.png",
        "images/chara/annika/annika_eyes_closed.png"
        )

    # layered character sprites
    layeredimage annika:
        always "annika_base"

        group eyes auto prefix "eyes"
        group face auto prefix "face"

        group expressions:
            attribute neutral default null
            attribute happy null
            attribute confused null

        attribute_function Picker(expressions)
