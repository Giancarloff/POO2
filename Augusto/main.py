from controllers.userController import UserController
import json, urllib.request

class App:

    def __init__(self):

        self.__controller = UserController([])
        for dict_user in self.get_from_json():
            self.__controller.create_user(dict_user)

    def get_all(self):
        return self.__controller.get_all()

    def create_user(self, dict_user):
        return self.__controller.create_user(dict_user)

    def delete_user(self, dict_user):
        return self.__controller.delete_user(dict_user)

    def update_user(self, dict_user):
        return self.__controller.update_user(dict_user)

    def get_from_json(self):
        url = "https://jsonplaceholder.typicode.com/users"
        with urllib.request.urlopen(url) as openUrl:
            data = json.load(openUrl)
        i = 0
        
        for e in data:
            i += 1
            
        self.__lastID = i
        print(self.__lastID)
        return data

    def make_user_form(self):
        dict_user = {}
        
        dict_user['id'] = self.__lastID + 1
        dict_user['name'] = input("Name: ")
        dict_user['username'] = input("Username: ")
        dict_user['email'] = input("Email: ")
        
        print("Address: ")
        dict_user['address'] = dict()
        dict_user['address']['street'] = input("- Street: ")
        dict_user['address']['suite'] = input("- Suite: ")
        dict_user['address']['city'] = input("- City: ")
        dict_user['address']['zipcode'] = input("- Zipcode: ")
        
        dict_user['address']['geo'] = dict()
        dict_user['address']['geo']['lat'] = input("- Latitude: ")
        dict_user['address']['geo']['lng'] = input("- Longitude: ")
        
        dict_user['phone'] = input("Phone: ")
        dict_user['website'] = input("Website: ")
        
        print("Company: ")
        dict_user['company'] = dict()
        dict_user['company']['name'] = input("- Name: ")
        dict_user['company']['catchPhrase'] = input("- Catch Phrase: ")
        dict_user['company']['bs'] = input("- BS: ")
        
        self.__lastID += 1 # essa linha aqui corre o risco de atualizar o ID sem criar um user novo
        return dict_user

    def make_user_id(self):
        id = int(input("ID: "))
        return id

    def menu(self):
        print("""
            1. Consultar
            2. Criar
            3. Deletar
            4. Atualizar
            0. Sair 
        """)

    def get_option(self):
        return int(input("Opcao: "))

    def run(self):

        while True:
            self.menu()
            option = self.get_option()
            if option == 1:
                for user in self.get_all():
                    print(user)
                    print()
            elif option == 2:
                form = self.make_user_form()
                self.create_user(form)
            elif option == 3:
                pass
                id = self.make_user_id()
                self.delete_user(id)
            elif option == 4:
                pass
                form = self.make_user_form()
                self.update_user(form)
            else:
                break


App().run()
