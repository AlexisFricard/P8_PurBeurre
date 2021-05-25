"""
TEST BUILDER therefore API_MANAGER

CAREFULL - Builder use api_manager.py to doing requests
"""
import json

from webapp.modules.tools.builder import build_data


""" TARGET - CODE """


def test_if_builder_by_code_return_expected_datas(monkeypatch):

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
        "webapp.modules.api.requests_library.request_code.requests.get",
        mock_requests_url_answer,
    )

    """ TEST - WITH CODE """
    test_products = build_data("mock_code", "code")

    assert isinstance(test_products, dict)
    assert len(test_products["products"][0]) == 15


""" TARGET - PROD_NAME """


def test_if_builder_by_name_return_expected_datas(monkeypatch):

    # MOCK RESPONSE
    class MockProducts:
        def json(*args, **kwargs):
            mock_url = (
                "P8_PurBeurre/webapp/modules/api/tests/mocks/mock_products.json"  # noqa
            )
            with open(mock_url, encoding="utf-8") as json_file:
                mock_resp = json.load(json_file)
            return mock_resp

    # PATCH URL
    def mock_requests_url_answer_prod(url):
        return MockProducts()

    # PATCH REQUEST
    monkeypatch.setattr(
        "webapp.modules.api.requests_library.request_products.requests.get",  # noqa
        mock_requests_url_answer_prod,
    )

    """ TEST - WITH NAME """
    test_products = build_data("mock_name", "prod_name")

    # TEST TYPE OF RESPONSE
    assert isinstance(test_products, dict)
    # TEST NUMB OF PRODUCT IN RESPONSE
    assert len(test_products["products"]) == 6


""" TARGET - SUBSTITUTE """


def test_if_builder_by_substitute_return_expected_datas(monkeypatch):

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
        "webapp.modules.api.requests_library.request_categ.requests.get",
        mock_requests_url_answer,
    )

    response = build_data(["mock_categorie", "e"], "substitute")
    # TEST TYPE OF RESPONSE
    assert isinstance(response[0], dict)
    # TEST NUMB OF DATAS
    assert len(response) == 6


""" WRONG DATAS """


def test_if_builder_return_None():

    response = build_data("mock_data", "mock_wrong_parameter")
    assert response is None
