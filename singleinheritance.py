class Apple:
    manufacturer = "Apple Inc."
    contactWebsite = "www.apple.com/contact"

    def contactDetails(self):
        print("You can contact", self.contactWebsite)

class Macbook(Apple):
    def __init__(self):
        self.yearOfManufacture = 2017

    def manufactureDetails(self):
        print("This Mac was manufactured in {} by {}".format(yearOfManufacture, self.manufacturer))
        #instance attribute -> class attribute


macBook = Macbook()
macBook.manufactureDetails()
macBook.contactDetails()

#successfull inherited!
