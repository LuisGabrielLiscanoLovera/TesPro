class Tesla:
    #creating a class variable and making it a global variable
    global speed
    speed = 60

    print("Accessing speed variable within the class:", speed)

    def __init__(self, speed):
        self.speed = speed

        def display_speed():

            print("Speed of the Tesla is:", speed)


print("Accessing the class variable", speed)


class Lucid:
    print("Accessing the speed variable from a different class:", speed)

    def __init__(self, speed):
        self.speed = speed

    def display_tesla_speed(self):
        print("Accessing the speed variable from a method in another class:", speed)


lucid_object = Lucid(speed)
lucid_object.display_tesla_speed()
