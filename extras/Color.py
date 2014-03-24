# an example of how a class is created, passes in object            

class Color(object):
    '''An RGB color, with red, green and blue components.'''

    def lightness(self):
        '''Calculate the lightness of this color.'''

        strongest = max(self.red, self.green, self.blue)
        weakest   = min(self.red, self.green, self.blue)
        return 0.5 * (strongest + weakest) / 255

print 'purple = Color()'
print  'purple.red = 255'
print  'purple.green = 0'
print  'purple.blue = 255'
print  'purple.lightness()'
