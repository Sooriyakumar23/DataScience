class Facebook:
    def __init__(self):
        self.is_logged_in = False
    def login(self, user_name, password):
        if (self.user_name == user_name and self.password == password):
            self.is_logged_in = True
            print("Success: Facebook Login Done !")
        else:
            self.is_logged_in = False
            print(f"Failed: Facebook Login failed for user_name = {user_name} and password = {password}")
    def signup(self, user_name, password):
        self.user_name = user_name
        self.password = password
        self.is_logged_in = False
    def view_post(self):
        if (self.is_logged_in):
            print ("Success: You can View Post")
        else:
            print ("Failed: You need to Login to View Post")

user1 = Facebook()
user1.signup("Alice", "12345")
user1.view_post()
user1.login("Alice", "54321")
user1.view_post()
user1.login("Alice", "12345")
user1.view_post()