def property_from_class(cls):
    '''From a suitable class constructs a property.'''

    class_dict = cls.__dict__
    kwargs = dict(
        fset = class_dict.get('fset'),
        fget = class_dict.get('fget'),
        fdel = class_dict.get('fdel'),
        doc = class_dict.get('__doc__'),
    )

    return property(**kwargs)


class Rectangle(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

        # Namespace mechanism.
        # Afterwards, area = property_from_class(area)
    @property_from_class
    class area(object):
        '''This is to be the doc string for the property.'''

        def fget(self):
            return self.x * self.y

        def fset(self, area):
            self.y = area / self.x

        def xxfdel(self):
            self.x = self.y = 0


w = Rectangle(3, 4)

