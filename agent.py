from validation import get_valid_input
import random


class Property:
    """
    Represents a superclass for House and Apartment, the common arguments
    for both are square footage, number of bedrooms and number of bathrooms
    """

    def __init__(self, square_feet='', beds='', baths='', **kwargs):
        """
        Initialise square footage, number of bedrooms and number of bathrooms
        :param square_feet: str
        :param beds: str
        :param baths: str
        :param kwargs: additional keyword arguments
        """
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        """
        A method to display characteristics of the property
        """

        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():
        """
        This is a static method, the value for each key is prompted with a
        call to input
        :return: dictionary that has all the main parameters
        """
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths: "))

    prompt_init = staticmethod(prompt_init)


class Apartment(Property):
    """
    Represents the apartment, class extends Property
    """
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        """
        Initialise common characteristics of property using kwargs and add
        the special arguments of apartment
        :param balcony: str
        :param laundry: str
        :param kwargs: additional keywords arguments
        """
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        """
        A method to display main characteristics of the property adding
        additional arguments for apartment
        """
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: {}".format(self.laundry))  # i've used format
        print("has balcony: {}".format(self.balcony))  # here instead of %

    def prompt_init():
        """
        Static method that gets common arguments using method prompt_init
        from the
        parent class and updates it with additional arguments
        :return: dictionary with all the characteristics of the apartment
        """
        # in this method I have changed the validation using the additional
        # function get_valid_input
        parent_init = Property.prompt_init()
        laundry = get_valid_input(
            "What laundry facilities does the property have?",
            Apartment.valid_laundries)
        balcony = get_valid_input("Does the property have a balcony? ",
                                  Apartment.valid_balconies)
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


class House(Property):
    """
    Represents the house, class extends Property
    """
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='',
                 garage='', fenced='', **kwargs):
        """
        Initialise common characteristics of property using kwargs and add
        the special arguments of house
        :param num_stories: str
        :param garage: str
        :param fenced: str
        :param kwargs: additional keywords arguments
        """
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        """
        A method to display main characteristics of the property adding
        additional arguments for house
        """
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        """
        Static method that gets common arguments using method
        prompt_init from the parent class and updates it with additional
        arguments
        :return: dictionary with all the characteristics of the house
        """
        # in this method I have changed the validation using the additional
        # function get_valid_input
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ",
                                 House.valid_fenced)
        garage = get_valid_input("Is there a garage? ",
                                 House.valid_garage)
        num_stories = input("How many stories? ")
        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


class Purchase:
    """
    Represent a purchase, the class is going to be combined with the other
    classes
    """

    def __init__(self, price='', taxes='', **kwargs):
        """
        Initialise the arguments:the selling price, the estimated taxes and
        additional keyword arguments
        :param price: str
        :param taxes: str
        :param kwargs: additional arguments
        """
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        """
        A method to display purchase details
        """
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        """
        Static method that gets the data about price and taxes
        :return: dictionary with price and taxes as keys and input strings
        as values
        """
        return dict(
            price=input("What is the selling price? "),
            taxes=input("What are the estimated taxes? "))

    prompt_init = staticmethod(prompt_init)


class Rental:
    """
    Represent a purchase, the class is going to be combined with the other
    classes
    """

    def __init__(self, furnished='', utilities='',
                 rent='', **kwargs):
        """
        Initialise the arguments for rent, furniture, estimated utilities
        and additional keyword arguments
        :param furnished: str
        :param utilities: str
        :param rent: str
        :param kwargs: additional arguments
        """
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        """
        A method to display rental details
        """
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(
            self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        """
        Static method that gets the data about rent, furniture and estimated
        utilities
        :return: dictionary with rent, furniture, estimated utilities as
        keys and input
        strings as values
        """
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input(
                "What are the estimated utilities? "),
            furnished=get_valid_input(
                "Is the property furnished? ",
                ("yes", "no")))

    prompt_init = staticmethod(prompt_init)


class HouseRental(Rental, House):
    """
    Represent a subclass that combines the functionality of classes Rental
    and House
    """

    def prompt_init():
        """
        method to combine the prompt_init methods of the classes Rental and
        House
        :return: dictionary
        """
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentRental(Rental, Apartment):
    """
    Represent a subclass that combines the functionality of classes Rental
    and Apartment
    """

    def prompt_init():
        """
        method to combine the prompt_init methods of the classes
        Rental and Apartment
        :return: dictionary
        """
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Purchase, Apartment):
    """
    Represent a subclass that combines the functionality of classes Purchase
    and Apartment
    """

    def prompt_init():
        """
       method to combine the prompt_init methods of the classes
       Purchase and Apartment
       :return: dictionary
       """
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class HousePurchase(Purchase, House):
    """
    Represent a subclass that combines the functionality of classes Purchase
    and House
    """

    def prompt_init():
        """
       method to combine the prompt_init methods of the classes
       Purchase and House
       :return: dictionary
       """
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class Agent:
    """
    Represent an agent. Method is responsible for creating new listings and
    displaying
existing ones
    """
    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }

    def __init__(self):
        """
        Initialise the property list
        """
        self.property_list = []

    def display_properties(self):
        """
        method to display the properties in the property list
        """
        for property in self.property_list:
            property.display()

    def del_property(self):
        """
        method to delete property from the list, for example if it was sold out
        """
        count = 1
        for property in self.property_list:
            "Available properties"
            print("{}: ".format(count))
            print(property.display())
            count += 1
        del self.property_list[
            (int(input(
                "Chose the property that isn't available anymore: ")) - 1)]

    def add_property(self):
        """
        Method to add the property to the list of properties
        """
        property_type = get_valid_input(
            "What type of property? ",
            ("house", "apartment")).lower()

        payment_type = get_valid_input(
            "What payment type? ",
            ("purchase", "rental")).lower()
        PropertyClass = self.type_map[
            (property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))

    def bargain(self):
        """
        method to trade with buyer
        in this variant is used random, but it can be easily made to a real
        answer
        """
        user_price = int(
            input("Time for a deal!!! Do you have any price proposals?"))
        if random.randint(0, 1) == 1:
            print("Okey, your price satisfies me!")
        else:
            print("No, I don't adree with this proposal!")
