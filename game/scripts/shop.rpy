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
            self.tag = tag
            self.tag_priority = tag_priority

    # TODO
    # class ShopEntry():
    #     self.item

    food_items = [
        Item('Water', 'water', 'Plain water. Tastes refreshing. Boost Energy by 5.', 10, { ENERGY: 5 }),
        Item('Soda', 'soda', 'Soda water. No added sugar. Boost Energy by 10.', 20, { ENERGY: 10 }),
        Item('Beans', 'beans', 'Canned beans. A savory snack. Boost Energy by 15.', 30, { ENERGY: 15 }),
        Item('Chocolate', 'chocolate', "Who doesn't like chocolate? Boost Energy by 25.", 50, { ENERGY: 25 }),
        Item('Pizza', 'whole_pizza', 'An entire pizza. Smells like delicious bread and cheese. Boost Energy by 50.', 100, { ENERGY: 50 }),
        Item('Sushi', 'sushi', 'Sushi rolls with real crab meat (or could it be imitation crab?) and cucumber. Boost Energy by 100.', 300, { ENERGY: 100 }),
    ]

    home_shop_items = food_items + [
        RoomItem('Refurbished Desk', 'desk_nice', 
            'The thrift store nearby said this was a steal. The legs seem to have been gnawed on by someone’s cat, but that just means Mint has a head start.', 
            1000, DESK, 2),

        RoomItem('Second-hand Office Chair', 'chair_second_hand', 
            "You’re not sure what those stains are, but your neighbor was about to throw it out. It’s still got most of its stuffing!", 
            500, CHAIR, 2),
        RoomItem('Comforta Office Chair', 'chair_nice', 
            "A brand new, more upgraded version of your neighbor’s old chair. The seat is firm and good for your back.", 
            1000, CHAIR, 3),
        RoomItem('Executive Gamer', 'chair_fancy', 
            'This chair is for the busy professional who means BUSINESS… Except when they’re playing the latest MMORPG. With incredible upper and lower back support, this chair takes the stress out of long hours in your IDE.', 
            2000, CHAIR, 4),

        RoomItem('Stock Router', 'router_simple', 
            'You were finally able to convince your old-school parents to let you get the family some wifi. This router came with the installation.', 
            500, ROUTER, 2),
        RoomItem('Upgraded router', 'router_nice', 
            'Mom and Dad are getting with the times, and have laptops too. Upgrading to a new wifi speed comes with a better router to handle it!', 
            1000, ROUTER, 3),
        RoomItem('Web Nexus', 'router_fancy', 
            'Stock routers only tap into a fraction of the potential of something built for speed. With a range of 2000 feet, you can access the web blocks away from the house.', 
            2000, ROUTER, 4),

        RoomItem('Used Netbook', 'pc_used', 
            'Your old high school is finally getting rid of its netbooks. It’s almost 10 years old, but these were clearly built to last.', 
            1000, PC, 2),
        RoomItem('Basik Bild Laptop', 'pc_student', 
            'It’s got that “new laptop” smell! Containing all of the basics any developer should need, you’re basically guaranteed an increase in your productivity.', 
            3000, PC, 3),
        RoomItem('Custom PC Build', 'pc_custom', 
            'You’re not sure what you need 800GB of RAM for, but you feel like you do. The rainbow LEDs create an awesome glow in your bedroom at night.', 
            5000, PC, 4),

        RoomItem('Monstera Deliciosa', 'plant', 
            'So you Shmoogled it, and there isn’t really anything DELICIOUS about this plant, but it does add some life to your home office.', 
            300),
        RoomItem('Poster 1', 'poster1', 
            'You’re not sure if that’s what his name is, but it’s what Mom has been calling him since you brought him home. This poster gives your room a jazzy feeling.', 
            200),
        RoomItem('Poster 2', 'poster2', 
            'You’ve always wanted to go to the rainforest. This poster gives your room an adventurous feeling.', 
            200),
        RoomItem('Poster 3', 'poster3', 
            "You’ve been wanting to take a vacation for AGES. Maybe with this in your room, you’ll feel more motivated.", 
            200),
        RoomItem('Cat lamp', 'cat_lamp', 
            'The glow from this lamp is as warm as Mint’s fur.', 
            400),
        RoomItem('Cat bed', 'cat_bed', 
            'Mint always sleeps on the floor next to your feet while you work. Why not keep a cat bed there instead?', 
            600),
    ]

    # TODO: refactor this lookup
    all_items = { item.name: item for item in home_shop_items }

    vending_machine_items = deepcopy(food_items)
    for item in vending_machine_items:
        item.price *= 2

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
                text item_on_display.description xalign 0.5 text_align 0.5
                text _('Price: $') + str(item_on_display.price) xalign 0.5 text_align 0.
                if not isinstance(item_on_display, RoomItem):
                    text _('Quantity held: ') + str(player_stats.food_inventory[item_on_display.name]) xalign 0.5 text_align 0.5
                textbutton '{icon=icon-shopping-cart} ' + _('Purchase Item'):
                    xalign 0.5
                    text_align 0.5
                    if player_stats.can_purchase_item(item_on_display):
                        action Function(player_stats.purchase_item, item_on_display)

        textbutton '{icon=icon-log-out} ' + _('Exit Shop'):
            action Return()
            xalign 0.5

# inventory for food
screen inventory_screen():
    # no need for vpgrid because it's already inside a viewport
    grid 4 len(player_stats.food_inventory):
        xspacing 10
        yspacing 5

        # body rows
        for item_name in player_stats.food_inventory:
            $ item = all_items[item_name]

            text item_name
            text item.description size gui.quick_button_text_size
            text str(player_stats.food_inventory[item_name]) xalign 0.5

            textbutton _('Use'):
                if player_stats.food_inventory[item_name] > 0:
                    action Function(player_stats.use_item, item)