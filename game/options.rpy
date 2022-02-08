## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.

## Custimization

# uncomment this to show non-selectable options as well
# define config.menu_include_disabled = True

## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Learn to Code RPG")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = False


## The version of the game.

define config.version = "1.0"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define intro = _p("""
{b}Learn to Code RPG{/b} is a game where you teach yourself to code, make friends in the tech industry, and pursue your dream to become a developer.
""")

define about = _p("""
This game was made possible by all the kind people who donate to support freeCodeCamp.org. You can help support our nonprofit's mission {a=https://www.freecodecamp.org/news/how-to-donate-to-free-code-camp/}here{/a}.

This project is open source and is currently in beta. If you notice any bugs or have suggestions about accessibility, the interface, the story, or anything at all, please report them on our {a=https://github.com/freeCodeCamp/LearnToCodeRPG}GitHub repo{/a}.

If you are enjoying this game, please {icon=icon-thumbs-up} rate and review us on {a=https://freecodecamp.itch.io/learn-to-code-rpg}itch.io{/a}.
""")

define credits = _p("""
Creative Lead:
    {a=https://ruolinzheng08.github.io/}Lynn Zheng (Ruolin Zheng){/a}
    {a=https://github.com/RuolinZheng08/}{icon=icon-github}{/a}
    {a=https://www.youtube.com/channel/UCZ2MeG5jTIqgzEMiByrIzsw}{icon=icon-youtube}{/a}
    {a=https://www.linkedin.com/in/ruolin-zheng/}{icon=icon-linkedin}{/a}
    {a=https://twitter.com/lynnzheng08}{icon=icon-twitter}{/a}

Coding & Writing & Misc. Art:
    {a=https://ruolinzheng08.github.io/}Lynn Zheng (Ruolin Zheng){/a}
    
Music:
    {a=https://twitter.com/ossia}Quincy Larson{/a}

Character Art:
    {a=https://layerto.carrd.co}Layerto (Noa Trinh){/a}

Quiz Questions & Proofreading:
    {a=https://twitter.com/abbeyrenn}Abbey Rennemeyer{/a},
    {a=https://github.com/ojeytonwilliams/}Oliver Eyton-Williams{/a},
    {a=https://twitter.com/EstefaniaCassN}Estefania Cassingena Navone{/a},
    {a=https://twitter.com/codergirl1991}Jessica Wilkins{/a},
    {a=https://twitter.com/deniselemonaki}Dionysia Lemonaki{/a}

Playtesting:
    {a=https://twitter.com/ieahleen}Ilenia Magoni{/a},
    {a=https://twitter.com/EstefaniaCassN}Estefania Cassingena Navone{/a},
    {a=https://twitter.com/nhcarrigan}Naomi Carrigan{/a},
    {a=https://twitter.com/_sidemt}Yoko Matsuda{/a},
    {a=https://twitter.com/Daniel__Rosa}Daniel Rosa{/a},
    {a=https://twitter.com/beaucarnes}Beau Carnes{/a}
    
And thank you for playing the game :)
""")

## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "LearnToCodeRPG"


## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by
## default. Setting one of these to False will hide the appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = False


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

define config.sample_sound = "audio/sfx/stats_change_boop.wav"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

define config.main_menu_music = "audio/bgm/Crystalize That Inner Child.mp3"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = dissolve


## Used when entering the main menu after the game has ended.

define config.end_game_transition = dissolve

define config.end_splash_transition = dissolve


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 60


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "LearnToCodeRPG-1629849682"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"

# define config.mouse_displayable = MouseDisplayable(Text('{color=#000}{size=50}{icon=icon-mouse-pointer}{/size}{/color}'), 0, 0)