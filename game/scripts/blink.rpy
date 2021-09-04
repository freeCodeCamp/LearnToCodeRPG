init python:

    class DynamicBlink(renpy.display.layout.DynamicDisplayable):
        """
        A dynamic image that blinks every now and then
        """

        def __init__(self, *args, **kwargs):
            self.current_image = args[1]
            self.blink_st = -1.0 # arbitrary number to force normal start

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

                    # XXX: renpy.python.rng.random() is too CPU-heavy
                    # self.blink_st = st + 2.0 + ( renpy.python.rng.random() * 5.0 )
                    self.blink_st = st + 2.0

                    self.current_image = args[0]

            else:

                # normal image

                if st > self.blink_st:

                    # time to blink

                    self.blink_st = st + 0.1 

                    self.current_image = args[1]

            return self.current_image, 0


        def predict_images(self):

            return self.used_images