screen shop_screen():
    on "show" action With(dissolve)
    on "hide" action With(dissolve)

    default item_on_display = shop_items[0]

    frame:
        xfill True
        xsize 1000
        xpadding 30
        ypadding 30
        xalign 0.5
        yalign 0.5

        background white80

        has vbox
        spacing 20

        label _("Item Shop") xalign 0.5

        text _("{icon=icon-shopping-bag} Money: $") + str(player_stats.player_stats_map[MONEY]) xalign 0.5 text_align 0.5

        hbox:
            spacing 10

            # left panel
            viewport:
                draggable True
                mousewheel True
                ymaximum 600
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
                add item_on_display.image xalign 0.5 yalign 0.5
                text item_on_display.name bold True xalign 0.5 text_align 0.5
                text _("Price: $") + str(item_on_display.price) xalign 0.5 text_align 0.5
                text _("Quantity held: ") + str(player_items[item_on_display]) xalign 0.5 text_align 0.5
                # TODO: check whether player has enough money using Function()
                textbutton "{icon=icon-shopping-cart} " + _("Purchase Item"):
                    xalign 0.5
                    text_align 0.5
                    action SetDict(
                        player_items,
                        item_on_display,
                        player_items[item_on_display] + 1
                        )

        textbutton "{icon=icon-log-out} " + _("Exit Shop"):
            action Return()
            xalign 0.5

init python:

    from collections import defaultdict

    class Item():
        def __init__(self, name, image, price, is_consumable):
            self.name = name
            self.image = image
            self.price = price
            self.is_consumable = is_consumable
            # TODO: add stats change

    shop_items = [
        Item("Water", "water", 10, True),
        Item("Soda", "soda", 20, True),
        Item("Beans", "beans", 30, True),
        Item("Chocolate", "chocolate", 50, True),
        Item("Pizza", "whole_pizza", 100, True),
        Item("Sushi", "sushi", 300, True),

        Item("Plant", "plant", 300, False),
        Item("Desk", "desk", 1000, False),
        Item("Headphones", "headphones", 3000, False),
        Item("Keyboard", "keyboard", 2000, False),
        Item("Lamp", "lamp", 1500, False),
        Item("Monitor", "monitor", 3000, False),
        
        Item("Simple chair", "chair1", 500, False),
        Item("Regular chair", "chair2", 1000, False),
        Item("Nice chair", "chair3", 2000, False),
        Item("Cool chair", "chair4", 3000, False),
        Item("Fancy chair", "chair5", 5000, False),
        Item("Simple router", "router1", 500, False),
        Item("Nice router", "router2", 1000, False),
        Item("Fancy router", "router3", 2000, False),
        Item("White Noise Machine", "white_noise_machine", 8000, False),
    ]

    player_items = defaultdict(int)

screen inventory_screen():
    vpgrid:

        cols 3
        rows len(player_items)
        spacing 10
        draggable True
        mousewheel True
        ymaximum 760

        scrollbars "vertical"
        vscrollbar_unscrollable "hide"

        # Since we have scrollbars, we have to position the side, rather
        # than the vpgrid proper.
        side_xalign 0.5

        # body rows
        for item in player_items:
            text item.name xysize cell_size
            text player_items[item] xysize cell_size xalign 0.5
            textbutton 'Consume' xysize cell_size xalign 0.5
