class Address:

    def __init__(self, street, suite, city, zipcode, geo):
        self.__street = street
        self.__suite = suite
        self.__city = city
        self.__zipcode = zipcode
        self.__geo = geo

    def get_street(self):
        return self.__street

    def set_street(self, new_street):
        self.__street = new_street

    def get_suite(self):
        return self.__suite

    def set_suite(self, new_suite):
        self.__suite = new_suite

    def get_city(self):
        return self.__city

    def set_city(self, new_city):
        self.__city = new_city

    def get_zipcode(self):
        return self.__zipcode
    
    def set_zipcode(self, new_zipcode):
        self.__zipcode = new_zipcode

    def get_geo(self):
        return self.__geo
    
    def set_geo(self, new_geo):
        self.__geo = new_geo

    def __str__(self):
        geo = str(self.get_zipcode())
        return f"{self.get_street()}, {self.get_suite()}, {self.get_city()}, {self.get_zipcode()}, {geo}"
