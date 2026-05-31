class SwimMixin:
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")


# Testing
draco = Dragon()

draco.swim()   # The creature swims!
draco.fly()    # The creature flies!
draco.roar()   # The dragon roars!
