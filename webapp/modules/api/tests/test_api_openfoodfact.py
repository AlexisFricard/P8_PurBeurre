"""
TEST API OpenFoodFacts

PEP8 exeptions: (flake8) F401 - imported but unused (l.8)
"""
import json

from purbeurre import wsgi  # noqa

from webapp.modules.api.requests_library import request_categ as r_by_categ
from webapp.modules.api.requests_library import request_categories as r_categ
from webapp.modules.api.requests_library import request_code as r_code
from webapp.modules.api.requests_library import request_products as r_prod


""" HAS NOT BEEN TESTED """
# request_code ==> Wrong 'code' ==> TO BE TESTED WITH ONLINE API
# request_categ ==> Params 'to_fill' ==> TESTED IN test_db_manager.py
""" REQUEST n CATEGORIES """


def test_if_request_categories_return_exptected_datas(monkeypatch):

    # MOCK RESPONSE
    class MockResponse:
        def json(*args, **kwargs):
            mock_url = "P8_PurBeurre/webapp/modules/api/tests/mocks/mock_categories.json"  # noqa
            with open(mock_url, encoding="utf-8") as json_file:
                mock_resp = json.load(json_file)
            return mock_resp

    # PATCH URL
    def mock_requests_url_answer(url):
        return MockResponse()

    # PATCH REQUEST
    monkeypatch.setattr(
        "webapp.modules.api.requests_library.request_categories.requests.get",  # noqa
        mock_requests_url_answer,
    )

    # PATCH VARS
    number = 6

    """ TEST VALUES """
    categories = r_categ.query_categories(number)

    assert len(categories) == 6
    assert categories[0] == "Aliments et boissons à base de végétaux"
    assert categories[1] == "Aliments d'origine végétale"
    assert categories[2] == "Snacks"
    assert categories[3] == "Snacks sucrés"
    assert categories[4] == "Boissons"
    assert categories[5] == "Viandes"


def test_if_request_categories_return_None():

    """TEST 1 - WRONG VALUE"""
    categories = r_categ.query_categories("mock")
    assert categories is None

    """ TEST 2 - NO VALUE """
    categories = r_categ.query_categories(0)
    assert categories is None


""" REQUEST CODE BY GIVEN CODE AND PARAMETER """


def test_if_request_code_return_exptected_datas(monkeypatch):

    # MOCK RESPONSE
    class MockResponse:
        def json(*args, **kwargs):
            mock_url = (
                "P8_PurBeurre/webapp/modules/api/tests/mocks/mock_code.json"  # noqa
            )
            with open(mock_url, encoding="utf-8") as json_file:
                mock_resp = json.load(json_file)
            return mock_resp

    # PATCH URL
    def mock_requests_url_answer(url):
        return MockResponse()

    # PATCH REQUEST
    monkeypatch.setattr(
        "webapp.modules.api.requests_library.request_code.requests.get",  # noqa
        mock_requests_url_answer,
    )

    # PATCH VARS
    parameters = ["selection", "result"]

    """ TEST 1 - PARAMS SELECTION """

    response = r_code.by_code("mock_code", parameters[0])

    # TEST TYPE OF RESPONSE
    assert isinstance(response, dict)
    # TEST ACCESS TO DATAS
    assert response["code"] == "3330720662002"
    assert response["product"]["_id"] == "3330720662002"

    """ TEST 2 - PARAMS RESULT """

    response = r_code.by_code("mock_code", parameters[1])

    # TEST TYPE OF RESPONSE
    assert isinstance(response, dict)
    # TEST LENTH OF RESPONSE
    assert len(response) == 15
    # TEST ACCESS TO DATAS
    assert response["product_name"] == "Pâte à tartiner noisette cacao"


def test_if_request_code_return_None():

    """TEST WRONG PARAMATER"""
    response = r_code.by_code("3330720662002", "mock_paramater")

    assert response is None
    # USE_CONNECTION TO TEST "CODE" WITH ONLINE API


""" REQUEST n PRODUCTS BY GIVEN NAME & PARAMETER  """


def test_if_request_products_return_none_or_datas(monkeypatch):

    # MOCK RESPONSE TO CHECK DATAS
    class MockResponse:
        def json(*args, **kwargs):
            mock_url = (
                "P8_PurBeurre/webapp/modules/api/tests/mocks/mock_products.json"  # noqa
            )
            with open(mock_url, encoding="utf-8") as json_file:
                mock_resp = json.load(json_file)
            return mock_resp

    # MOCK RESPONSE TO TEST NO RESPONSE
    class MockNoResponse:
        def json(*args, **kwargs):
            mock_url = (
                "P8_PurBeurre/webapp/modules/api"
                + "/tests/mocks/mock_no_products.json"  # noqa
            )
            with open(mock_url, encoding="utf-8") as json_file:
                mock_resp = json.load(json_file)
            return mock_resp

    # PATCH URL
    def mock_requests_url_answer(url):
        return MockResponse()

    def mock_requests_empty_result(url):
        return MockNoResponse()

    # PATCH REQUEST
    monkeypatch.setattr(
        "webapp.modules.api.requests_library.request_products.requests.get",  # noqa
        mock_requests_url_answer,
    )

    """ TEST 1 - RESPONSE """
    response = r_prod.query_n_products("mock_name", 6)

    # TEST TYPE OF RESPONSE
    assert isinstance(response, dict)
    # TEST NUMB OF DATAS
    assert len(response) == 6

    """ TEST 2 - NO RESPONSE """

    # CHANGE PATCH REQUEST
    monkeypatch.setattr(
        "webapp.modules.api.requests_library.request_products.requests.get",  # noqa
        mock_requests_empty_result,
    )

    response = r_prod.query_n_products("mock_name", 6)

    assert response is None
    # USE_CONNECTION TO TEST ONLINE API


""" REQUEST n PRODUCTS BY GIVEN CATEGORIE """


def test_if_request_categ_return_none_or_datas(monkeypatch):

    # MOCK RESPONSE
    class MockResponse:
        def json(*args, **kwargs):
            mock_url = (
                "P8_PurBeurre/webapp/modules/api/tests/mocks/mock_by_categ.json"  # noqa
            )
            with open(mock_url, encoding="utf-8") as json_file:
                mock_resp = json.load(json_file)
            return mock_resp

    # PATCH URL
    def mock_requests_url_answer(url):
        return MockResponse()

    # PATCH REQUEST
    monkeypatch.setattr(
        "webapp.modules.api.requests_library.request_categ.requests.get",  # noqa
        mock_requests_url_answer,
    )

    # PATCH VARS
    number = 6

    """ TEST 1 - PARAMS SUBSTITUTE """

    response = r_by_categ.query_products("mock", number, ["substitute", "e"])

    # TEST TYPE OF RESPONSE
    assert isinstance(response, dict)
    # TEST NUMB OF DATAS
    assert len(response) == 6

    """ TEST 2 - WRONG PARAMS """

    response = r_by_categ.query_products(
        "mock_categorie", number, ["mock_wrong_params", "e"]
    )

    # TEST RESPONSE
    assert response is None

    """ TEST 3 - WRONG NUTRISCORE """
    # TEST VALUE ERROR
    try:
        response = r_by_categ.query_products(
            "mock_categorie", number, ["substitute", "g"]
        )
    except ValueError:
        assert response is None
