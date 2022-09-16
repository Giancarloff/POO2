
class Geo:

    def __init__(self, lat, lng):
        self.__lat = lat
        self.__lng = lng

    def get_lat(self):
        return self.__lat

    def set_lat(self, new_lat):
        self.__lat = new_lat

    def get_lng(self):
        return self.__lng

    def set_lng(self, new_lng):
        self.__lng = new_lng

    def __str__(self):
        return f"{self.get_lat()}, {self.get_lng()}"
        