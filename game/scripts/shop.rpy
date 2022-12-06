screen shop_screen():
    on "show" action With(dissolve)
    on "hide" action With(dissolve)

    default item_on_display = shop_items[0]

    frame:
        xfill True
        xsize 1000
        ysize 800
        xpadding 30
        ypadding 30
        xalign 0.5
        yalign 0.5

        background white80

        has hbox
        spacing 10

        # left panel
        viewport:
            draggable True
            mousewheel True
            ymaximum 900
            xsize 300

            scrollbars "vertical"

            # Since we have scrollbars, we have to position the side, rather
            # than the vpgrid proper.
            side_xalign 0.5

            vbox:
                for item in shop_items:
                    textbutton item.name:
                        action SetScreenVariable("item_on_display", item)

        # right panel
        vbox:
            add item_on_display.image
            text item_on_display.name:
                bold True
            text _("Price: $") + str(item_on_display.price)
            text _("Quantity held: ") + str(player_items[item_on_display])
            # TODO: check whether player has enough money using Function()
            textbutton _("Purchase Item"):
                action SetDict(
                    player_items,
                    item_on_display,
                    player_items[item_on_display] + 1
                    )

        # close button
        textbutton "{icon=icon-x}":
            action Return()
            xalign 1.0
            text_align 1.0

init python:

    from collections import defaultdict

    class Item():
        def __init__(self, name, image, price, is_stackable, is_consumable):
            self.name = name
            self.image = image
            self.price = price
            self.is_stackable = is_stackable
            self.is_consumable = is_consumable

    shop_items = [
        Item("Instant noodle", "cupnoodle", 30, True, True),
        Item("Mac n cheese", "macncheese", 30, True, True),

    ]

    player_items = defaultdict(int)