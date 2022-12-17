screen shop_screen(shop_items):
    on 'show' action With(dissolve)
    on 'hide' action With(dissolve)

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

        label _('Item Shop') xalign 0.5

        text _('{icon=icon-shopping-bag} Money: $') + str(player_stats.player_stats_map[MONEY]) xalign 0.5 text_align 0.5

        hbox:
            spacing 10

            # left panel
            viewport:
                draggable True
                mousewheel True
                ymaximum 600
                xsize 300

                scrollbars 'vertical'

                # Since we have scrollbars, we have to position the side, rather
                # than the vpgrid proper.
                side_xalign 0.5

                vbox:
                    for item in shop_items:
                        textbutton item.name:
                            action SetScreenVariable('item_on_display', item)

            # right panel
            vbox:
                add item_on_display.image xalign 0.5 yalign 0.5
                text item_on_display.name bold True xalign 0.5 text_align 0.5
                text _('Price: $') + str(item_on_display.price) xalign 0.5 text_align 0.
                if not isinstance(item_on_display, RoomItem):
                    text _('Quantity held: ') + str(player_stats.food_inventory[item_on_display]) xalign 0.5 text_align 0.5
                textbutton '{icon=icon-shopping-cart} ' + _('Purchase Item'):
                    xalign 0.5
                    text_align 0.5
                    if player_stats.can_purchase_item(item_on_display):
                        action Function(player_stats.purchase_item, item_on_display),

        textbutton '{icon=icon-log-out} ' + _('Exit Shop'):
            action Return()
            xalign 0.5

init python:

    from copy import deepcopy

    class Item():
        def __init__(self, name, image, description, price, stats_change=None):
            self.name = name
            self.image = image
            self.description = description
            self.price = price
            self.stats_change = stats_change

    class RoomItem(Item):
        def __init__(self, name, image, description, price, tag=None, tag_priority=None, stats_change=None):
            '''
            tag: whether the item is a chair, a laptop, etc.
            tag_priority: bigger number means the item will be displayed with priority
            '''
            super().__init__(name, image, description, price, stats_change)
            self.image_room_display = 'room ' + self.image
            self.tag = tag
            self.tag_priority = tag_priority

    food_items = [
        Item('Water', 'water', '', 10, { SANITY: 5 }),
        Item('Soda', 'soda', '', 20, { SANITY: 10 }),
        Item('Beans', 'beans', '', 30, { SANITY: 15 }),
        Item('Chocolate', 'chocolate', '', 50, { SANITY: 25 }),
        Item('Pizza', 'whole_pizza', '', 100, { SANITY: 50 }),
        Item('Sushi', 'sushi', '', 300, { SANITY: 100 }),
    ]

    home_shop_items = food_items + [
        RoomItem('Nice desk', 'desk_nice', '', 1000, DESK, 2),

        RoomItem('Second-hand chair', 'chair_second_hand', '', 500, CHAIR, 2),
        RoomItem('Nice chair', 'chair_nice', '', 1000, CHAIR, 3),
        RoomItem('Fancy chair', 'chair_fancy', '', 2000, CHAIR, 4),

        RoomItem('Simple router', 'router_simple', '', 500, ROUTER, 2),
        RoomItem('Nice router', 'router_nice', '', 1000, ROUTER, 3),
        RoomItem('Fancy router', 'router_fancy', '', 2000, ROUTER, 4),

        RoomItem('Used laptop', 'pc_used', '', 1000, PC, 2),
        RoomItem('Student laptop', 'pc_student', '', 3000, PC, 3),
        RoomItem('Custom PC', 'pc_custom', '', 5000, PC, 4),

        RoomItem('Plant', 'plant', '', 300),
        RoomItem('Poster 1', 'poster1', '', 200),
        RoomItem('Poster 2', 'poster2', '', 200),
        RoomItem('Poster 3', 'poster3', '', 200),
        RoomItem('Cat lamp', 'cat_lamp', '', 400),
        RoomItem('Cat bed', 'cat_bed', '', 600),
    ]

    vending_machine_items = deepcopy(food_items)
    for item in vending_machine_items:
        item.price *= 2

# inventory for food
screen inventory_screen():
    vpgrid:

        cols 3
        rows len(player_stats.food_inventory)
        spacing 10
        draggable True
        mousewheel True
        ymaximum 760

        scrollbars 'vertical'
        vscrollbar_unscrollable 'hide'

        # Since we have scrollbars, we have to position the side, rather
        # than the vpgrid proper.
        side_xalign 0.5

        # body rows
        for item in player_stats.food_inventory:
            text item.name xysize cell_size
            text player_stats.food_inventory[item] xysize cell_size xalign 0.5
            textbutton 'Consume':
                xysize cell_size
                xalign 0.5
                if player_stats.food_inventory[item] > 0:
                    action Function(player_stats.use_item, item)