""" SELENIUM TEST """
import sys

from selenium import webdriver


class TestUserStory():

    def __init__(self):
        # Créer une session Firefox
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        # User Data
        self.username = "fake_pseudo"
        self.first_name = "fake_first_name"
        self.last_name = "fake_last_name"
        self.mail = "fakeMail@mail.com"
        self.password = "fakePassword"

        self.user_research = "Nutella"

    def get_home_page(self):

        # Appeler l’application web
        self.driver.get("https://pur-beurre-af.herokuapp.com/")

    def click_on_btn(self, name):

        # Localiser le boutton et l'utilisé
        button = self.driver.find_element_by_name(name)
        button.click()

    def click_on_link(self, text):

        link = self.driver.find_element_by_link_text(text)
        link.click()

    def click_on_item(self, text):

        item = self.driver.find_element_by_class_name(text)
        item.click()

    def get_form_send_key(self, name, key):

        # Localiser la zone de texte
        field = self.driver.find_element_by_name(name)
        field.clear()
        field.send_keys(key)

    def research_by_enter_key(self, what):

        # Localiser la zone de texte
        search_field = self.driver.find_element_by_name('user_text')
        search_field.clear()

        # Saisir et confirmer le mot-clé
        search_field.send_keys(what)
        search_field.submit()

        # Consulter la liste des produits affichés à la suite de la recherche
        # à l’aide de la méthode find_elements_by_class_name
        lists = self.driver.find_elements_by_class_name("card")

        if len(lists) == 6:
            return True

    def research_by_clic_button(self, what):

        # Localiser la zone de texte
        search_field = self.driver.find_element_by_name('user_text')
        search_field.clear()

        # Saisir le mot-clé
        search_field.send_keys(what)

        # Localiser le boutton et l'utilisé
        self.click_on_btn("wen_logo")

        # Consulter la liste des produits affichés à la suite de la recherche
        # à l’aide de la méthode find_elements_by_class_name
        lists = self.driver.find_elements_by_class_name("card")

        if len(lists) == 6:
            return True

    def fill_and_post_signup_form(self):

        self.get_form_send_key("username", self.username)
        self.get_form_send_key("first_name", self.first_name)
        self.get_form_send_key("last_name", self.last_name)
        self.get_form_send_key("mail", self.mail)
        self.get_form_send_key("password", self.password)

        self.click_on_btn("signup_btn")

    def fill_and_post_signin_form(self, state):

        if state is True:

            self.get_form_send_key("username", self.username)
            self.get_form_send_key("password", self.password)

            self.click_on_btn("signin_btn")

            lists = self.driver.find_elements_by_tag_name("a")

            for item in lists:
                if "/myfood" in item.get_attribute("innerHTML"):
                    return True

        elif state is False:

            self.get_form_send_key("username", "false_value")
            self.get_form_send_key("password", "false_value")

            self.click_on_btn("signin_btn")

            if self.driver.current_url == (
                "https://pur-beurre-af.herokuapp.com/signin"
            ):
                return True

    def select_product(self):

        link = self.driver.find_element_by_link_text("C'est mon produit !")
        link.click()

        # Consulter la liste des produits affichés à la suite de la recherche
        # à l’aide de la méthode find_elements_by_class_name
        lists = self.driver.find_elements_by_class_name("card")

        if len(lists) == 6:
            return True

    def click_on_connect_from_result(self):

        link = self.driver.find_element_by_link_text("Se connecter")
        link.click()

    def logout(self):

        item = self.driver.find_element_by_id("disconnected")
        item.click()

    def save(self):

        item = self.driver.find_element_by_id("save")
        item.click()

    def display(self, test):
        self.driver.implicitly_wait(3)
        sys.stdout.write(
            f"\r>>>    Test: {test}/15"
        )


if __name__ == "__main__":

    tests = TestUserStory()
    tests.get_home_page()

    list_of_tests = list()

    """ ---------------------------------------------------------------- """
    """ TEST NAV BAR """

    # Img Pur Beurre
    tests.display(1)
    tests.click_on_item("navbar-brand")
    if tests.driver.current_url == "https://pur-beurre-af.herokuapp.com/":
        list_of_tests.append(True)
    else:
        list_of_tests.append(False)

    # Text Pur Beurre
    tests.display(2)
    tests.click_on_link("Pur Beurre")
    if tests.driver.current_url == "https://pur-beurre-af.herokuapp.com/":
        list_of_tests.append(True)
    else:
        list_of_tests.append(False)

    # Item account
    tests.display(3)
    tests.click_on_item("nav-link")
    if tests.driver.current_url == (
        "https://pur-beurre-af.herokuapp.com/signin"
    ):
        list_of_tests.append(True)
    else:
        list_of_tests.append(False)

    # Search Bar by enter hey
    tests.display(4)
    list_of_tests.append(tests.research_by_enter_key("Nutella"))

    # Search Bar by enter hey
    tests.display(5)
    list_of_tests.append(tests.research_by_clic_button("Nutella"))

    """ ---------------------------------------------------------------- """
    """ USER STORY 1 - User want to create an account """

    # Item account
    tests.display(6)
    tests.click_on_item("nav-link")

    tests.driver.implicitly_wait(3)

    # Click on signup
    tests.click_on_item("pt-20px")
    if tests.driver.current_url == (
        "https://pur-beurre-af.herokuapp.com/signup"
    ):
        list_of_tests.append(True)
    else:
        list_of_tests.append(False)

    # Create account
    tests.display(7)
    tests.fill_and_post_signup_form()
    if tests.driver.current_url == (
        "https://pur-beurre-af.herokuapp.com/signup"
    ):
        list_of_tests.append(True)
    else:
        list_of_tests.append(False)

    """ ---------------------------------------------------------------- """
    """ USER STORY 2 - User want to connect and disconnect """

    # Item account
    tests.click_on_item("nav-link")

    # Try to connect
    tests.display(8)
    list_of_tests.append(tests.fill_and_post_signin_form(False))

    # Connect account
    tests.display(9)
    list_of_tests.append(tests.fill_and_post_signin_form(True))

    # Logout
    tests.display(10)
    tests.logout()
    if tests.driver.current_url == "https://pur-beurre-af.herokuapp.com/":
        list_of_tests.append(True)
    else:
        list_of_tests.append(False)

    """ ---------------------------------------------------------------- """
    """ USER STORY 3 - User research a substitute of nutella and add it"""

    tests.driver.implicitly_wait(3)

    # Search Bar by clic_button
    tests.research_by_clic_button("Nutella")

    """ CASE 1 - IS NOT CONNECTED """

    # Test if they have 6 products
    tests.display(11)
    list_of_tests.append(tests.select_product())

    # Test url return after connect link from result
    tests.display(12)
    tests.click_on_connect_from_result()
    if tests.driver.current_url == (
        "https://pur-beurre-af.herokuapp.com/signin?query=80177173"
    ):
        list_of_tests.append(True)
    else:
        list_of_tests.append(False)

    # Test url return after connect from result
    tests.display(13)
    tests.fill_and_post_signin_form(True)
    if tests.driver.current_url == (
        "https://pur-beurre-af.herokuapp.com/result?query=80177173"
    ):
        list_of_tests.append(True)
    else:
        list_of_tests.append(False)

    """ CASE 2 - IS CONNECTED """

    # Test save logo
    tests.display(14)

    tests.save()
    if tests.driver.current_url == (
        "https://pur-beurre-af.herokuapp.com/myfood"
    ):
        list_of_tests.append(True)
    else:
        list_of_tests.append(False)

    # Test account
    tests.display(15)
    tests.click_on_item("nav-link")
    if tests.driver.current_url == (
        "https://pur-beurre-af.herokuapp.com/account"
    ):
        list_of_tests.append(True)
    else:
        list_of_tests.append(False)

    tests.driver.close()

    if False not in list_of_tests:
        print("\n>>>    Selenium tests success")
    else:
        print("\n>>>    There is an error in Selenium tests")
        print("\n>>>    Please consults README.md")
