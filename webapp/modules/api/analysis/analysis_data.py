""" CHECK DATA """
# from webapp.models import Product


class Analyze_data:

    def __init__(self):
        # LISTS OF ALL NAME AND URL TO DETECT DUPLICATIONS
        """self.p_name_list = list()
        self.p_url_list = list()
        self.unwanted_categories = ["eau", "water"]
        self.p_code_list = list()

    def check_data(self, data):
        self.data = data
        products_name = Product.objects.all()
        for row in products_name:
            self.p_name_list.append(row.product_name)
            self.p_code_list.append(row.code)
            self.p_url_list.append(row.product_url)

        check_list = list()
        duplicate_list = list()
        right_check_list = [True] * len(data)

        for field in data:
            check_list.append(self.checking_empty_field(field))

        if check_list == right_check_list:
            # ADD INTO LIST TRUE OR FALSE, FALSE WHEN IT'S IN DOUBLE
            duplicate_list.append(self.checking_duplicate_name(data[0]))
            duplicate_list.append(self.checking_duplicate_url(data[1][-15:]))
            duplicate_list.append(self.checking_duplicate_code(data[5]))

            CHECK IF DUPLICATE NAME OR URL END (15 LAST CHAR)
            if duplicate_list == [True]:
                if data[3] is str():
                    if self.checking_unwanted_cat(data[3]) is True:
                        return True
                else:
                    return True
        return False"""

    # METHOD TO RETURN TRUE OR FALSE IF THE FIELD IS EMPTY
    def checking_empty_field(self, field):
        if (field is not None) or (field == 0):
            return True
        else:
            return False

    """def checking_duplicate_name(self, product_name):

        if product_name not in self.p_name_list:
            self.p_name_list.append(product_name)
            return True
        else:
            return False"""

    # METHOD TO RETURN TRUE OR FALSE IF THE END OF URL IS IN DOUBLE
    """def checking_duplicate_url(self, product_url):
        for url in self.p_url_list:
            if url == product_url:
                print(url, product_url)
                return False
        self.p_url_list.append(product_url)
        return True

    # METHOD TO RETURN TRUE OR FALSE IF THE PRODUCT_CODE IS IN DOUBLE
    def checking_duplicate_code(self, product_code):
        for code in self.p_code_list:
            if product_code == code:
                return False

        self.p_code_list.append(product_code)
        return True

    # METHOD TO RETURN TRUE OR FALSE IF IS WANTED CATEGORY
    def checking_unwanted_cat(self, categorie):
        for unw_categ in self.unwanted_categories:
            if unw_categ in categorie:
                return False
        return True

    def del_lists(self):
        # self.p_name_list = []
        # self.p_url_list = []
        self.p_code_list = []"""
