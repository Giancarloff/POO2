from models.geo import Geo
from models.address import Address
from models.company import Company
from models.user import User

class UserController:

    def __init__(self, users=[]):
        self.__users = users

    def get_all(self):
        return self.__users[:]

    def create_user(self, dict_user):
        try:
            geo = Geo(dict_user['address']['geo']['lat'], dict_user['address']['geo']['lng'])
            address = Address(dict_user['address']['street'], dict_user['address']['suite'], dict_user['address']['city'], dict_user['address']['zipcode'], geo)
            company = Company(dict_user['company']['name'], dict_user['company']['catchPhrase'], dict_user['company']['bs'])
            user = User(dict_user['id'], dict_user['name'], dict_user['username'], dict_user['email'], address, dict_user['phone'], dict_user['website'], company)
            self.__users.append(user)
        except KeyError as ke:
            print(f"In create_user at UserController: {ke}")
            return None

    def delete_user(self, id):
        for user in self.__users:
            if user.get_id() == id:
                self.__users.remove(user)
                return

    def update_user(self, dict_user):
        pass

