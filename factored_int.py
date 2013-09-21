class factored_int(int):

    def __new__(cls, *argv):
        
        value = 1
        for i in argv:
            value = value * i

        return int.__new__(cls, value)

    def __init__(self, *argv):
        
        self.factors = argv



doit = factored_int
print doit(3)

print doit() #should be 1

print doit(2, 3, 5)
