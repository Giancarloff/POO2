
class IncompleteData(Exception):

    def __init__(self, datas):
        super().__init__(f"Faltam os seguintes {datas}!")        


class User:

    def __init__(self, id, name, username, email, address, phone, website, company):
        self.__id = id
        self.__name = name
        self.__username = username
        self.__email = email
        self.__address = address
        self.__phone = phone
        self.__website = website
        self.__company = company

    def get_id(self):
        return self.__id

    def set_id(self, new_id):
        self.__id = new_id

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_username(self):
        return self.__username

    def set_username(self, new_username):
        self.__username = new_username

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        self.__email = new_email

    def get_address(self):
        return self.__address

    def set_address(self, new_address):
        self.__address = new_address

    def get_phone(self):
        return self.__phone

    def set_phone(self, new_phone):
        self.__phone = new_phone

    def get_website(self):
        return self.__website

    def set_website(self, new_website):
        self.__website = new_website

    def get_company(self):
        return self.__company

    def set_company(self, new_company):
        self.__company = new_company

    def __str__(self):
        addres = str(self.get_address())
        company = str(self.get_company())
        return f"{self.get_id()}, {self.get_name()}, {self.get_username()}, {self.get_email()}, {addres}, {self.get_phone()}, {self.get_website()}, {company}"

