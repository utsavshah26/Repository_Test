from POM.home import home

class LoginPage:

    def __init__(self,page):
        self.page = page

        self.__username = page.get_by_role("textbox", name="Username")
        self.__password = page.get_by_role("textbox", name="Password")
        self.__LoginButton = page.get_by_role("button", name="Login")

    def enter_usernamne(self, uname):
        
        self.__username.fill(uname)
        

    def enter_password(self, upass):
        
        self.__password.fill(upass)


    # def click_login(self):
    #     self.__LoginButton.click()
    
    #OR

    def click_login(self):
        self.__LoginButton.click()
        return home(self.page)

    def do_login(self, uname, upass):
        self.enter_usernamne(uname)
        self.enter_password(upass)
        self.click_login()
        return home(self.page)



