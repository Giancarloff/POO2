

class Company:

    def __init__(self, name, catchPhrase, bs):
        self.__name = name
        self.__catchPhrase = catchPhrase
        self.__bs = bs

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_catchPhrase(self):
        return self.__catchPhrase
    
    def set_catchPhrase(self, new_catchPhrase):
        self.__catchPhrase = new_catchPhrase

    def get_bs(self):
        return self.__bs

    def set_bs(self, new_bs):
        self.__bs = new_bs

    def __str__(self):
        return f"{self.get_name()}, {self.get_catchPhrase()}, {self.get_bs()}"

        