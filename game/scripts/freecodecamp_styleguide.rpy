# https://design-style-guide.freecodecamp.org/

## The init offset statement causes the initialization statements in this file
## to run before init statements in gui.rpy
init offset = -3

init:
    # color pairs
    define gray00 = u'#ffffff'
    define gray90 = u'#0a0a23'

    define gray05 = u'#f5f6f7'
    define gray85 = u'#1b1b32'

    define gray10 = u'#dfdfe2'
    define gray80 = u'#2a2a40'

    define gray15 = u'#d0d0d5'
    define gray75 = u'#3b3b4f'

    # accent
    # primary, to be used on a dark bg
    define purple = u'#dbb8ff'
    define yellow = u'#f1be32'
    define blue = u'#99c9ff'
    define light_green = u'#acd157'

    # secondary, to be used on a light bg
    define dark_purple = u'#5a01a7'
    define dark_yellow = u'#4d3800'
    define dark_blue = u'#002ead'
    define dark_green = u'#00471b'

    image gray90 = gray90
    image gray05 = gray05

    define red = u'#f00'
    define white = u'#fff'
    define black = u'#000'

    image black = black

    # https://gist.github.com/lopspower/03fb1cc0ac9f32ef38f4
    define white80 = u'#fffc' # 80% opacity
    image white80 = white80