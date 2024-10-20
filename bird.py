class bird():
    def __init__(self, colour):
        self.colour = colour
        print("The coulour of my bird is: ", self.colour)
    
    def who(self):
        print("Im a bird")

    def fly(self):
        print("I am flying!")

class penguin(bird):
    def __init__(self, colour):
        super().__init__(colour)
    
    def whoisthis(self):
        print("I am penguin")

    def run(self):
        print("I can run!")

peggy = penguin("Blue")
peggy.whoisthis()
peggy.fly()
peggy.run()
