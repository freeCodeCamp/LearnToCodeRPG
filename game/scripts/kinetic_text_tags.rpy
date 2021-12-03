"""
 Kinetic Text Tags Ren'Py Module
 2021 Daniel Westfall <SoDaRa2595@gmail.com>

 http://twitter.com/sodara9
 I'd appreciate being given credit if you do end up using it! :D Would really
 make my day to know I helped some people out!
 Really hope this can help the community create some really neat ways to spice
 up their dialogue!
 http://opensource.org/licenses/mit-license.php
 Github: https://github.com/SoDaRa/Kinetic-Text-Tags
 itch.io: https://wattson.itch.io/kinetic-text-tags
 Forum Post: https://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=60527&sid=75b4eb1aa5212a33cbfe9b0354e5376b
"""
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

### UPDATE ###
# With the new ATL text tag, a handful of effects I've made have become redundant.
# Namely the bounce (bt), fadein (fi) and rotation (rotat) effects.
# However, I'll leave them in here for posterity and in case someone would like
# to reuse some of the code for whatever purpose.
# Plus the bounce and fadein may be faster to type for some. And I'd probably
# break some code if I did. Though feel free to remove them if you find them
# to be clutter.

##### Our preference to disable the chaos text #####
default preferences.chaos_on = False  # You can change this to be gui.chaos_text or persistent.chaos_text if you'd prefer.

init python:
    import random
    import math

    # This will maintain what styles we want to apply and help us apply them
    class DispTextStyle():
        # Notes:
        #   - "" denotes a style tag. Since it's usually {=user_style} and we partition
        #     it over the '=', it ends up being an empty string
        #   - If you want to add your own tags to the list, I recommend adding them
        #     before the ""
        #   - Self-closing tags should not be added here and should be handled
        #     in the text tag function.
        custom_tags = ["omega", "bt", "fi", "sc", "rotat", "chaos", "move"]
        accepted_tags = ["", "b", "s", "u", "i", "color", "alpha", "font",  "size", "outlinecolor", "plain"]
        custom_cancel_tags = ["/" + tag for tag in custom_tags]
        cancel_tags = ["/" + tag for tag in accepted_tags]
        def __init__(self):
            self.tags = {}

        # For setting style properties. Returns false if it accepted none of the tags
        def add_tags(self, char):
            tag, _, value = char.partition("=") # Separate the tag and its info
            # Add tag to dictionary if we accept it
            if tag in self.accepted_tags or tag in self.custom_tags:
                if value == "":
                    self.tags[tag] = True
                else:
                    self.tags[tag] = value
                return True
            # Remove mark tag as cleared if should no longer apply it
            if tag in self.cancel_tags or tag in self.custom_cancel_tags:
                tag = tag.replace("/", "")
                self.tags.pop(tag)
                return True
            return False # If we got any other tag, tell the function to let it pass

        # Applies all style properties to the string
        def apply_style(self, char):
            new_string = ""
            # Go through and apply all the tags
            new_string += self.start_tags()
            # Add the character in the middle
            new_string += char
            # Now close all the tags we opened
            new_string += self.end_tags()
            return new_string

        # Spits out start tags. Primarily used for SwapText
        def start_tags(self):
            new_string = ""
            # Go through the custom tags
            for tag in self.custom_tags:
                if tag in self.tags:
                    if self.tags[tag] == True:
                        new_string += "{" + tag + "}"
                    else:
                        new_string += "{" + tag + "=" +self.tags[tag] + "}"
            # Go through the standard tags
            for tag in self.accepted_tags:
                if tag in self.tags:
                    if self.tags[tag] == True:
                        new_string += "{" + tag + "}"
                    else:
                        new_string += "{" + tag + "=" +self.tags[tag] + "}"
            return new_string

        # Spits out ending tags. Primarily used for SwapText
        def end_tags(self):
            new_string = ""
            # The only tags we are required to end are any custom text tags.
            # And should also end them in the reverse order they were applied.
            reversed_cancels = [tag for tag in self.custom_cancel_tags]
            reversed_cancels.reverse()
            for tag in reversed_cancels:
                temp = tag.replace("/", "")
                if temp in self.tags:
                    new_string += "{" + tag + "}"
            return new_string


    ### TEXT WRAPPER CLASSES ###
    # Basic text displacement demonstration
    class BounceText(renpy.Displayable):
        def __init__(self, child, char_offset, bounce_height=20, **kwargs):

            # Pass additional properties on to the renpy.Displayable
            # constructor.
            super(BounceText, self).__init__(**kwargs) # REMEMBER TO RENAME HERE TO YOUR CLASS

            # For all of my classes, I assume I am being passed a displayable
            # of class Text. If you might not, I recommend going with the default of
            # self.child = renpy.displayable(child)
            self.child = child

            self.bounce_height = bounce_height # The amplitude of the sine wave
            self.char_offset = char_offset # The offset into the sine wave
            self.freq = 4.0 # How fast the text moves up and down

        def render(self, width, height, st, at):
            # Where the current offset is calculated
            # (self.char_offset * -.1) makes it look like the left side is leading
            # We use st to allow this to change over time
            curr_height = math.sin(self.freq*(st+(float(self.char_offset) * -.1))) * float(self.bounce_height)

            ####  A Transform can be used for several effects   ####
            # t = Transform(child=self.child,  alpha = curr_height)

            # Create a render from the child.
            # Replace self.child with t to include an alpha or zoom transform
            child_render = renpy.render(self.child, width, height, st, at)

            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)

            # This will position our child's render. Replacing our need for an offset Transform
            render.subpixel_blit(child_render, (0, curr_height))

            renpy.redraw(self, 0) # This lets it know to redraw this indefinitely
            return render

        def event(self, ev, x, y, st):
            return self.child.event(ev, x, y, st)

        def visit(self):
            return [ self.child ]

    # Simple fade in. Helps show some ideas for timing
    # May want to modify to allow it to skip to the end if the user clicks.
    # Otherwise plays for the full time given.
    class FadeInText(renpy.Displayable):
        def __init__(self, child, char_num, fade_time, **kwargs):
            super(FadeInText, self).__init__(**kwargs)

            # The child.
            self.child = child
            self.fade_time = fade_time
            self.display_time = .01
            self.slide_distance = 100
            # This is to get seconds per character on screen for later
            # Allowing this effect to scale with the player's desired text speed
            cps = 0.0
            if preferences.text_cps is not 0: # Avoid division by 0.0
                cps = (1.0 / preferences.text_cps)
            self.time_offset = char_num * cps  # How long to wait before doing things

        def render(self, width, height, st, at):
            curr_alpha = 0.0
            xoff = 5.0
            if st > self.time_offset:
                adjust_st = st - self.time_offset # Adjust for time delay
                curr_alpha = adjust_st/self.fade_time
                xoff = max(self.slide_distance - ((adjust_st/self.fade_time) * self.slide_distance), 0)
            # Example of using transform to adjust alpha
            t = Transform(child=self.child,  alpha = curr_alpha)
            child_render = renpy.render(t, width, height, st, at)

            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)
            render.subpixel_blit(child_render, (xoff, 0))
            # Stop redrawing when the animation is finished.
            if st <= self.fade_time + self.time_offset:
                renpy.redraw(self, 0)
            return render

        def visit(self):
            return [ self.child ]

    # Simple random motion effect
    class ScareText(renpy.Displayable):
        def __init__(self, child, square=2, **kwargs):
            super(ScareText, self).__init__(**kwargs)

            self.child = child

            self.square = square # The size of the square it will wobble within.
            # Include more variables if you'd like to have more control over the positioning.

        def render(self, width, height, st, at):
            # Randomly move the offset of the text's render.
            xoff = (random.random()-.5) * float(self.square)
            yoff = (random.random()-.5) * float(self.square)

            child_render = renpy.render(self.child, width, height, st, at)
            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)

            render.subpixel_blit(child_render, (xoff, yoff))
            renpy.redraw(self, 0)
            return render

        def visit(self):
            return [ self.child ]

    # Demonstration of changing text styles on the fly
    # Could also predefine some styles and swap between those as well!
    # Also for this effect in particular, I ---HIGHLY--- advise building in some way to disable it
    # as it can be pretty harsh on the eyes.
    # An example of how you can make this a preference option is included below.
    class ChaosText(renpy.Displayable):
        # Some may want to have this list be more of a global variable than baked into the class.
        font_list = ["FOT-PopJoyStd-B.otf", "GrenzeGotisch-VariableFont_wght.ttf", "Pacifico-Regular.ttf", "RobotoSlab-ExtraBold.ttf",\
                     "RobotoSlab-Medium.ttf", "SyneTactile-Regular.ttf", "TurretRoad-Bold.ttf", "TurretRoad-ExtraBold.ttf", "TurretRoad-ExtraLight.ttf", \
                     "TurretRoad-Light.ttf", "TurretRoad-Medium.ttf", "TurretRoad-Regular.ttf"]
        #Just a list so we can pull any hex value randomly
        color_choice = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
        def __init__(self, orig_text, **kwargs):

            super(ChaosText, self).__init__(**kwargs) #REMEMBER TO RENAME HERE TO YOUR CLASS

            # Create our child
            self.child = renpy.text.text.Text(orig_text)
            self.orig_text = orig_text
            self.last_style = None # This will be used for renders if the user wants to stop chaos text

        def render(self, width, height, st, at):
            if not preferences.chaos_on:                # This preference is defined near the top of this file.  And can be set in the preferences screen (see line 783-787 in screens.rpy)
                if self.last_style is not None: # If this is our first render, then should do that first
                    # Rest of this is just a repeat of what's below.
                    self.child.set_text(self.last_style.apply_style(self.orig_text))
                    child_render = renpy.render(self.child, width, height, st, at)
                    self.width, self.height = child_render.get_size()
                    render = renpy.Render(self.width, self.height)
                    render.subpixel_blit(child_render, (0, 0))
                    return render

            # We'll create a new text style for this render
            new_style = DispTextStyle()
            new_color = ""
            # Create a random color using hex values
            for i in range(0,6):
                new_color += renpy.random.choice(self.color_choice)
            new_color = "#" + new_color
            new_style.add_tags("color=" + str(new_color))
            # Random size
            rand_size = renpy.random.randint(0,50)
            new_style.add_tags("size="+str(rand_size))
            # Random font
            rand_font = renpy.random.choice(self.font_list)
            new_style.add_tags("font="+rand_font)
            #Apply our style to our Text child
            self.child.set_text(new_style.apply_style(self.orig_text))
            # Create a render from the child.
            child_render = renpy.render(self.child, width, height, st, at)
            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)
            render.subpixel_blit(child_render, (0, 0))
            renpy.redraw(self,0)

            self.last_style = new_style # Save the current style for if the user wishes to turn off the Chaos tag
            return render

        def visit(self):
            return [ self.child ]

    # Demonstration of using a Transform on the text and applying rotation
    class RotateText(renpy.Displayable):
        def __init__(self, child, speed=300, **kwargs):
            super(RotateText, self).__init__(**kwargs)

            self.child = child

            self.speed = speed # The speed of our rotation

        def render(self, width, height, st, at):

            theta = math.radians(st * float(self.speed))
            t = Transform(child=self.child,  rotate=st*float(self.speed))
            child_render = renpy.render(t, width, height/2, st, at)

            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height/2)

            # Problem with using a Transform though is that each character will be padded
            # Because the rotation may make it wider or taller depending on the character and angle.
            # How best to tackle this though may vary depending on how you'd like to implement it.
            render.blit(child_render, (0,0))
            renpy.redraw(self, 0)
            return render

        def visit(self):
            return [ self.child ]

    # The following is an alternative version of rotate that allows for rotation in the x and y axis
    # Functionally equivalent to using a Transform and flipping it using ATL xzoom and yzoom constrained between 0 and 1
    # Using a Transform might be better in some cases, but I'll leave this here for anyone who'd prefer to work with angles
    # for this kind of effect.
    # Other matrix functions of note include
    # renpy.display.matrix.perspective(w,h,n,p,f)
    # renpy.display.matrix.screen_projection(w,h) < Renpy space to OpenGL viewport
    # renpy.display.matrix.texture_projection(w,h) < Renpy space to OpenGL render-to-texture
    # You can look up more about them in the renpy\display\matrix_functions.pyx file
    # Credit to the FancyText module creator yukinogatari for the idea.
    # FancyText module can be found at https://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=59587
    """
    class RotateText(renpy.Displayable):
        def __init__(self, child, speed=100, **kwargs):
            super(RotateText, self).__init__(**kwargs)

            self.child = child
            self.speed = speed # The speed of our rotation

        def render(self, width, height, st, at):
            angle = st * self.speed
            # Which parameter you put the 'angle' into will affect which axis the render rotates on.
            # Try moving it around and seeing what happens.
            rotation_m = renpy.display.matrix.rotate(angle,0,0)

            child_render = renpy.render(self.child, width, height, st, at)
            c_width, c_height = child_render.get_size()
            # This applies the rotation to our child's render.
            child_render.reverse = rotation_m

            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)

            # Math nerds might realize I'm not offsetting the transform.
            # While renpy.display.matrix.offset(x,y,z) is a thing, it won't change much
            # The real place to apply the offset is in your final blit. Which is what we'll calculate here

            # Rotations on x axis
            theta2 = math.radians(st * float(self.speed) + 180)
            c = math.cos(theta2) + 1.0
            xoff = 0
            yoff = c * self.height
            if yoff > self.height:
                yoff = self.height

            render.subpixel_blit(child_render, (xoff,yoff))
            renpy.redraw(self, 0)
            return render

        def visit(self):
            return [ self.child ]
    """

    # Simple text swap effect
    # It can be prone to having letters out of place when part of a larger string
    # I recommended you pass it the entire line to avoid this issue.
    # Can also just define every line it'll need in advance and just tell it which
    # ones to swap to to be extra sneaky. Then the text won't be in your script at all!
    class SwapText(renpy.Displayable):
        def __init__(self, start_tags, text1, text2, end_tags, swap_time, **kwargs):
            super(SwapText, self).__init__(**kwargs)
            #Style tags we'll need as well as the text
            self.start_tags = start_tags
            self.text1 = text1
            self.text2 = text2
            self.end_tags = end_tags
            # How long between swapping text
            self.s_time = swap_time
            # An internal timer to keep track of when to swap
            self.timer = 0.0
            # Determines if we swap to text1 or text2 next
            self.swap_to_1 = False
            self.child = Text(start_tags + text1 + end_tags)
            self.st = 0.0


        def render(self, width, height, st, at):
            delta = st - self.st # How long since last update
            self.timer += delta
            if self.timer > self.s_time:
                # If time to swap, determine which one to swap to.
                if self.swap_to_1:
                    self.child.set_text(self.start_tags + self.text1 + self.end_tags)
                    self.swap_to_1 = False
                    self.timer = 0.0
                else:
                    self.child.set_text(self.start_tags + self.text2 + self.end_tags)
                    self.swap_to_1 = True
                    self.timer = 0.0

            child_render = renpy.render(self.child, width, height, st, at)
            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)
            render.subpixel_blit(child_render, (0,0))
            renpy.redraw(self, 0)

            self.st = st # So we can check how long since last update
            return render

        def visit(self):
            return [ self.child ]

    # An example of text that moves and reacts to the mouse.
    # Sidenote: The position the mouse is distorted if the screen is resized.
    # I did try to find a way to counteract this, but didn't have much luck.
    # Seems to only happen on the x component though. No clue why.
    # If anyone can pinpoint the issue, please let me know and I'll be happy to fix it.
    class MoveText(renpy.Displayable):
        def __init__(self, child, **kwargs):
            super(MoveText, self).__init__(**kwargs)
            self.affect_distance = 150
            self.child = child
            self.mouse_pos = (1000,1000)
            self.pos = (0,0)

        def render(self, width, height, st, at):
            child_render = renpy.render(self.child, width, height, st, at)
            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)
            # x and y we get in the event function are relative to the top left corner of the displayable initially.
            # So we'll want to update it to reflect the actual position of our text
            trans_x = self.mouse_pos[0] - self.pos[0] - (self.width / 2)
            trans_y = self.mouse_pos[1] - self.pos[1] - (self.height / 2)

            vl = math.hypot(trans_x,trans_y)
            xpos, ypos = self.pos
            # Can skip calculation if vector length is further than our specified effect distance
            if vl < self.affect_distance:
                distance = 3.0 * (self.affect_distance-vl) / self.affect_distance
                xpos -= distance * trans_x / vl
                ypos -= distance * trans_y / vl
                self.pos = (xpos, ypos) # Preserve the new pos
            # Use our child's position as determined by the event function
            render.subpixel_blit(child_render, (xpos, ypos))
            renpy.redraw(self, 0)
            return render

        def event(self, ev, x, y, st):
            self.mouse_pos = (x,y)
            # Pass the event to our child.
            return self.child.event(ev, x, y, st)

        def visit(self):
            return [ self.child ]


    ### CUSTOM TAG FUNCTIONS ###
    # dummy func that doesn't do anything
    def dummy_tag_func(tag, argument, contents):
        return contents

    # Letters move in a sine wave.
    # height: (int) The amplitude of the text's sine wave motion. How high and low it'll go from it's default position in pixels. Good for jubilent and floaty text.
    # Example: {bt=[height]}Text{/bt}
    def bounce_tag(tag, argument, contents):
        new_list = [ ] # The list we will be appending our displayables into
        if argument == "": # If the argument received is blank, insert a default value
            argument = 10
        char_offset = 0  # Since we want our text to move in a wave,
                         # we want to let each character know where it is in the wave.
                         # So they move in harmony. Otherwise they rise and fall all together.
        my_style = DispTextStyle() # This will keep track of what tags and styling to add to each letter
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:                                            # Extract every character from the string
                    char_text = Text(my_style.apply_style(char))             # Create a Text displayable with our styles applied
                    char_disp = BounceText(char_text, char_offset, argument) # Put the Text into the Wrapper
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))     # Add it back in as a displayable
                    char_offset += 1
            elif kind == renpy.TEXT_TAG:
                # Filter for every kind of tag we accept
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            # I honestly never got around to testing this. Not often the text
            # already has a displayable in it. Let me know if it breaks though.
            elif kind == renpy.TEXT_DISPLAYABLE:
                char_disp = BounceText(text, char_offset, argument)
                new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
                char_offset += 1
            else: # Don't touch any other type of content
                new_list.append((kind,text))

        return new_list

    # Letters will start off to the right & invisible. And will then move left while increasing their opacity. Good for meditation and calm text.
    # offset: (int) Offset within the line. Needed to help time start of fade-in with other slow text characters.
    # time: (float) How long in seconds the animation lasts.
    # Example: {fi=[offset]-[time]}Text{/fi}
    def fade_in_tag(tag, argument, contents):
        new_list = [ ]
        if argument == "":
            my_index = 0
            fade_time = 5.0
        else: # Note: if you include one argument, you should include both
            my_index_str, _, fade_time_str = argument.partition('-')
            my_index = int(my_index_str)
            fade_time = float(fade_time_str)
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    if char == ' ':
                        new_list.append((renpy.TEXT_TEXT, ' ')) # Skips blank space since looks weird counting it
                        continue
                    char_text = Text(my_style.apply_style(char))
                    char_disp = FadeInText(char_text, my_index, fade_time)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
                    my_index += 1
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))
        return new_list

    # Letters change position every frame randomly. Good for very angry or quivering dialogue.
    # range: (int) Letters are confined to a square around their default location. Range determines length of the sides of that square.
    #              Higher values will make it very chaotic while smaller values will make it quite minimal.
    # Example: {sc=[range]}Text{/sc}
    def scare_tag(tag, argument, contents):
        new_list = [ ]
        if argument == "":
            argument = 5
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    char_text = Text(my_style.apply_style(char))
                    char_disp = ScareText(char_text, argument)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))

        return new_list

    # Letters change their font, color and size every frame.
    # Example: {chaos}Text{/chaos}
    # Honestly more a demonstration of what can be done than useful in it's own right.
    # If you create tags this chaotic, please include a way to turn it off for people with epilepsy.
    def chaos_tag(tag, argument, contents):
        new_list = [ ]
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    char_disp = ChaosText(my_style.apply_style(char))
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))

        return new_list

    # Letters rotate in place. Good for stylized intros or UI
    # Speed: (int) How fast the rotation will be.
    # Example: {rotat=[speed]}Text{/rotat}
    def rotate_tag(tag, argument, contents):
        new_list = [ ]
        # Argument here will reprsent the desired speed of the rotation.
        if argument == "":
            argument = 400
        else:
            argument = int(argument)
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    char_text = Text(my_style.apply_style(char))
                    char_disp = RotateText(char_text, argument)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))

        return new_list

    # Causes letters to change between two strings every couple of seconds.
    # text1:     (String) First set of characters to display. Should be equal to the length of the characters we're replacing
    # text2:     (String) Second set of characters to display. Should be equal to the length of text1
    # swap_time: (int) Length of time between character swap
    # Arguments are separated by '@'. Length of strings should not exceed length of text they are replacing.
    # Example: {swap=Text@Four@0.5}Text{}
    # This is a pretty static way of doing it mostly made to demonstrate the concept.
    # Included for others to build upon for their needs.
    def swap_tag(tag, argument, contents):
        new_list = [ ]
        if argument == "":
            return contents
        text1, _, argument = argument.partition("@")
        text2, _, argument = argument.partition("@")
        if len(text1) != len(text2):
            new_list.append((renpy.TEXT_TEXT, "ERROR!"))
        swap_time = float(argument)

        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                # This one replaces the whole text rather than extracting over letters
                # That way it can take up this whole block with its own Text displayable
                char_disp = SwapText(my_style.start_tags(), text1, text2, my_style.end_tags(), swap_time)
                new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))
        return new_list

    # Makes it so the text within moves away from the mouse. More example of what can be done than useful
    # Example: {move}Text{/move}
    def move_tag(tag, argument, contents):
        new_list = [ ]
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    char_text = Text(my_style.apply_style(char))
                    char_disp = MoveText(char_text)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))
        return new_list

    # Some text effects won't allow for a paragraph break if applied to a whole line
    # Which can cause your text to just continue straight off the screen.
    # To amend this, you can insert the {para} tag.
    # This will let the Text displayable holding us know when to wrap.
    # Can also use \n in most cases. But leaving this for people who may already be using it
    # or for cases where \n doesn't work.
    def paragraph_tag(tag, argument):
        return [(renpy.TEXT_PARAGRAPH, "")]

    # This tag is made to automatically wrap several Classes inside one another
    # This is to reduce strain on the render pipeline and memory from nested classes
    # Notes:
      # GradientText and GlitchText are omitted because they were made after the 1.0 release.
      # SwapText and MoveText are omitted for possible issues.
      # SwapText because is not included in this due to it replacing whole sections rather than
      # individual letters. Would be better to embed an Omega inside a SwapText.
      # MoveText because of potential issues of having things like BounceText affect
      # affecting the position of the letter visually.
      # Would be better to have an event call attached to one of those so it can account
      # for the transformations of other tags
    # Argument Notes (all tag args accept same arguments as original tag):
      # BT: BounceText
      # SC: ScareText
      # FI: FadeInText
      # ROT: RotateText
      # CH: ChaosText
    # All tag arguments are seperated by @.
    # Example: {omega=BT=[bt_arg]@SC=[sc_arg]@FI=[fi_arg1]-[fi_arg2]@ROT=[rot_arg]@CH}Text{/omega}
    def omega_tag(tag, argument, contents):
        new_list = [ ]
        if argument == "": # This tag must have arguments
            return contents
        # Variable for each of our tags. None if it takes one argument.
        # Boolean if 0 or many arguments.
        bt_tag = None
        sc_tag = None
        fi_tag = False
        rot_tag = None
        chao_tag = False
        fi_arg_1 = None
        fi_arg_2 = None

        args = [ ]
        arg_count = argument.count('@') # Count how many partitions we will need to make
        for x in range(arg_count):      # Extract all the tags and arguments with them
            new_arg, _, argument = argument.partition('@')
            args.append(new_arg)
        args.append(argument)
        # Determine what tags we'll need to apply and the arguments associated with them
        for arg in args:
            tag, _, value = arg.partition('=')
            if tag == "BT":
                if value is not "":
                    bt_tag = value
                else:
                    bt_tag = 10
            elif tag == "SC":
                if value is not "":
                    bt_tag = value
                else:
                    bt_tag = 5
            # Multiargument tag example. Be sure to use different partitions for these
            elif tag == "FI":
                fi_tag = True
                str1, _, str2 = value.partition('-')
                fi_arg_1 = int(str1)
                fi_arg_2 = float(str2)
            elif tag == "ROT":
                rot_tag = value
            elif tag == "CH":
                chao_tag = True

        my_style = DispTextStyle()
        my_index = 0 # Some Classes will need an index
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    # Apply base Wrappers to letter
                    if chao_tag:
                        char_disp = ChaosText(my_style.apply_style(char))
                    else:
                        char_disp = Text(my_style.apply_style(char))
                    # Apply further Wraps
                        # Be sure to consider if the order will be important to you
                    if bt_tag is not None:
                        char_disp = BounceText(char_disp, my_index, bt_tag)
                    if sc_tag is not None:
                        char_disp = ScareText(char_disp, sc_tag)
                    if fi_tag:
                        char_disp = FadeInText(char_disp, my_index + fi_arg_1, fi_arg_2)
                    if rot_tag is not None:
                        char_disp = RotateText(char_disp, rot_tag)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))

        return new_list

    """
    # Template tag function to copy off of.
    def TEMPLATE_tag(tag, argument, contents):
        new_list = [ ]
        if argument == "":
            argument = 5
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    char_text = Text(my_style.apply_style(char))
                    char_disp = TEMPLATEText(char_text, argument)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))
        return new_list
    """

    # Define our new text tags
    # if persistent.enable_moving text is False, leave them undefined
    def configure_text_tags():
        if persistent.enable_moving_text:
            config.custom_text_tags["bt"] = bounce_tag
            config.custom_text_tags["fi"] = fade_in_tag
            config.custom_text_tags["sc"] = scare_tag
            config.custom_text_tags["rotat"] = rotate_tag
            config.custom_text_tags["chaos"] = chaos_tag
            config.custom_text_tags["swap"] = swap_tag
            config.custom_text_tags["move"] = move_tag
            config.custom_text_tags["omega"] = omega_tag
            config.self_closing_custom_text_tags["para"] = paragraph_tag
        else:
            for tag in ["omega", "bt", "fi", "sc", "rotat", "chaos", "move", "swap"]:
                config.custom_text_tags[tag] = dummy_tag_func
    # Template tag function
    #config.custom_text_tags[""] = _tag

    # first call this function to make sure the tags get defined
    configure_text_tags()

init:
    default persistent.enable_moving_text = True