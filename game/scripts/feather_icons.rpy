init -202 python:

    # Feather Icon (C) Cole Bemis. License MIT
    # Delete persistent if you made a change!
    
    font_ui_ico = 'fonts/feather-icons/fonts/feather-ramen2-icon.ttf'

    if persistent.icon is None:

        persistent.icon = {
            'alert': u'\x21', 
            'arrow-down': u'\x77', 
            'arrow-down-left': u'\x65', 
            'arrow-down-right': u'\x72', 
            'arrow-left': u'\x74', 
            'arrow-right': u'\x79', 
            'arrow-up': u'\x75', 
            'arrow-up-left': u'\x69', 
            'arrow-up-right': u'\x6f', 
            'chevron-left': u'\x26', 
            'chevron-right': u'\x2a', 
            'chevrons-down': u'\x70', 
            'chevrons-left': u'\x61', 
            'chevrons-right': u'\x73', 
            'chevrons-up': u'\x64', 
            'circle': u'\x66', 
            'circle-check': u'\x67', 
            'click-left': u'\x68', 
            'click-right': u'\x6a', 
            'close': u'\x6b', 
            'folder': u'\x6c', 
            'folder-qload': u'\x7a', 
            'folder-qsave': u'\x78', 
            'ico-archive': u'\x63', 
            'ico-bag': u'\x76', 
            'ico-box': u'\x62', 
            'ico-box2': u'\x6e', 
            'ico-briefcase': u'\x6d', 
            'ico-bulb': u'\x51', 
            'ico-cart': u'\x57', 
            'ico-cash': u'\x24', 
            'ico-coins': u'\x45', 
            'ico-disk': u'\x52', 
            'ico-map': u'\x25', 
            'ico-phone': u'\x40', 
            'ico-settings': u'\x54', 
            'ico-tool': u'\x59', 
            'ico-wallet': u'\x23', 
            'inbox': u'\x55', 
            'key-back': u'\x49', 
            'key-fast': u'\x4f', 
            'key-forward': u'\x50', 
            'key-pause': u'\x41', 
            'key-play': u'\x53', 
            'list': u'\x7c', 
            'log-down': u'\x44', 
            'log-in': u'\x29', 
            'log-in2': u'\x46', 
            'log-out': u'\x28', 
            'log-out2': u'\x47', 
            'log-up': u'\x48', 
            'logo-python': u'\x3f', 
            'logo-ramen': u'\x4a', 
            'logo-renpy': u'\x71', 
            'menu': u'\x4b', 
            'menu-small': u'\x4c', 
            'menu1': u'\x5a', 
            'moon1': u'\x58', 
            'moon2': u'\x43', 
            'moon3': u'\x56', 
            'more-horizontal': u'\x42', 
            'more-vertical': u'\x4e', 
            'msg-forward': u'\x3d', 
            'msg-reply': u'\x2b', 
            'phone': u'\x4d', 
            'phone-call': u'\x2c', 
            'phone-incoming': u'\x2e', 
            'phone-outgoing': u'\x2f', 
            'phone-x': u'\x27', 
            'sliders': u'\x3b', 
            'square': u'\x5b', 
            'square-check': u'\x5d', 
            'square-edit': u'\x5e', 
            'square-minus': u'\x31', 
            'square-plus': u'\x32', 
            'square-x': u'\x33', 
            'star': u'\x34', 
            'sun1': u'\x35', 
            'sun2': u'\x36', 
            'sun3': u'\x37', 
            'terminal': u'\x5c', 
            'toggle-left': u'\x38', 
            'toggle-right': u'\x39', 
            'trash-0': u'\x5f', 
            'trash-1': u'\x2d', 
            'volume-off': u'\x30', 
            'volume-on': u'\x60', 
            'volume-x': u'\x7e',
            'logo-facebook': u'\x7b',
            'logo-instagram': u'\x7d',
            'logo-twitter': u'\x22',
       }

    def ico(what=None, say=False):
        r""" Translate Ramen Icon Webfont, see demo.html in the 'theme\icons' for the list"""

        if what is None:
            return sorted(persistent.icon)
        else:
            try:
                if say:
                    return "{font=" + font_ui_ico + "}" + \
                        persistent.icon[what] + "{/font}"
                else:
                    return persistent.icon[what]
            except BaseException:
                return " "

    def icon_tag(tag, icon='logo-ramen'):
        """
        put icons as renpy text_tag

        ``` python
        e " {icon=alert} Warning "
        ```
        """
        return [(renpy.TEXT_TAG, "font=" + font_ui_ico),
                (renpy.TEXT_TEXT, ico(icon)), (renpy.TEXT_TAG, "/font")]

    config.self_closing_custom_text_tags["icon"] = icon_tag


style ramen_icon is button
style ramen_icon_text:
    font font_ui_ico
    size 24
    antialias True

screen demoicon():

    modal True
    zorder 1000
    frame background "#111" xsize 1.0 ysize 1.0:
    
        vpgrid xpos 0 ypos 0:
            cols 14
            spacing 5
            scrollbars 'vertical'            
            
            for i in sorted(persistent.icon.keys()):
                vbox xsize 85 ysize 70:
                    text ico(i) style 'ramen_icon_text' color "#fff"  xalign 0.5
                    text i color "#ccc" size 12  xalign 0.5
                
                