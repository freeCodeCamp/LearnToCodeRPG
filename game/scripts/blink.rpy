init python:

    class DynamicBlink(renpy.display.layout.DynamicDisplayable):
        """
        A dynamic image that blinks every now and then
        """

        def __init__(self, *args, **kwargs):
            self.current_image = args[1]
            self.blink_st = -1.0 # arbitrary number to force normal start

            # cache a random duration b/c calling random on each frame is too heavy
            # but we don't want multiple on-screen sprites to be always blinking at the same moment
            self.time_till_next_blink = 2.0 + renpy.random.random() * 5.0

            self.used_images = args
            kwargs.update( {
                '_predict_function' : self.predict_images } )

            super(DynamicBlink, self).__init__( self.get_blink_image, 
                                                *args, 
                                                **kwargs )

        def get_blink_image(self, st, at, *args, **kwargs):

            if self.current_image == args[1]:

                # the blink image

                if st > self.blink_st:

                    # time to swap to normal

                    self.blink_st = st + self.time_till_next_blink

                    self.current_image = args[0]

            else:

                # normal image

                if st > self.blink_st:

                    # time to blink

                    self.blink_st = st + 0.2 

                    self.current_image = args[1]

            return self.current_image, 0


        def predict_images(self):

            return self.used_images