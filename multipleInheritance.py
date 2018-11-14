class OperatingSystem:
    multitasking = True
    name = "Mac OS"

class Apple:
    website = "apple.com"
    name = "Apple"

class MacBook(OperatingSystem, Apple):
    def __init__(self):
        if self.multitasking is True:
            print("This is multitasking system. Visit {}".format(self.website))
            print("Name: ",self.name) #Mac OS comes first!

macBook = MacBook()
