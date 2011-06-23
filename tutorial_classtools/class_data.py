special_keys = set([
        '__dict__', 
        '__doc__',
        '__metaclass__',
        '__module__', 
        '__slots__',
        '__weakref__',
])


about_keys = set([
        'doc',
        'name',
        'module',
        'slots',
])


def class_data_from_class(cls):

    metaclass = type(cls)
    body = dict(
        (key, value) 
        for (key, value) in cls.__dict__.items()
        if key not in special_keys
        )

    
    about = {}
    for key in about_keys:
        under_under_key = '__%s__' % key
        value = getattr(cls, under_under_key, None)
        if value is not None:
            about[key] = value

    return metaclass, body, about


if __name__ == '__main__':

    print class_data_from_class(type('aaa', (), dict(a=3)))
