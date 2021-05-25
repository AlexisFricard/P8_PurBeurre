"""
TEST ANALYZE DB

PEP8 exeptions: (flake8) F401 - imported but unused (l.8)
"""
import json

from purbeurre import wsgi  # noqa
from webapp.management.commands.analyze_db import update_db


def test_if_update_db_responde_correctly(monkeypatch):
    # MOCK RESPONSE
    class MockResponse:
        def json(*args, **kwargs):
            mock_url = (
                "P8_PurBeurre/webapp/modules/api/tests/mocks/mock_code.json"  # noqa
            )
            with open(mock_url, encoding="utf-8") as json_file:
                mock_resp = json.load(json_file)
            return mock_resp

    # MOCK RESPONSE TO TEST NO RESPONSE
    class MockNoResponse:
        def json(*args, **kwargs):
            mock_url = (
                "P8_PurBeurre/webapp/modules/api/tests/mocks/mock_no_code.json"  # noqa
            )
            with open(mock_url, encoding="utf-8") as json_file:
                mock_resp = json.load(json_file)
            return mock_resp

    # PATCH URL
    def mock_requests_url_answer(url):
        return MockResponse()

    def mock_requests_empty_result(url):
        return MockNoResponse()

    """ TEST 1 - WITH GOOD RESPONSE """

    # PATCH REQUEST
    monkeypatch.setattr(
        "webapp.modules.api.requests_library.request_code.requests.get",
        mock_requests_url_answer,
    )
    # TEST
    assert update_db() is None

    """ TEST 2 - WITH NO RESPONSE """

    # CHANGE PATCH REQUEST
    monkeypatch.setattr(
        "webapp.modules.api.requests_library.request_code.requests.get",
        mock_requests_empty_result,
    )

    # TEST
    assert update_db() is None
