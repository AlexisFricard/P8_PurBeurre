"""
Test webapp/views.py

PEP8 exeptions: (flake8) F401 - imported but unused (l.6)
"""
from purbeurre import wsgi

from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase

from webapp.views import index, selection, result, save


class TemplateTest(TestCase):

    def test_index(self):

        request = RequestFactory().get('index')
        view = index(request)
        assert view.status_code == 200

    def test_selection(self):

        request = RequestFactory().post('/selection')
        request.POST = {"user_text": "nutella"}

        view = selection(request)
        assert view.status_code == 200

    def test_result(self):

        request = RequestFactory().get('/result')
        request.GET = {"query": "3330720662002"}

        view = result(request)
        assert view.status_code == 200

    def test_save(self):

        # BUILD REQUEST
        request = RequestFactory().get('/save')
        request.GET = {"query": "3330720662002,4028491400907"}

        """ TEST 1 - WITH UNCONNECTED USER """
        request.user = AnonymousUser()

        view = save(request)

        # 302 - REDIRECT TO Signin/
        assert view.status_code == 302
        assert view.url == "/signin"

        """ TEST 2 - WITH CONNECTED USER """
        request.user = User.objects.get(username='JeanLouis')

        view = save(request)

        # 302 - REDIRECT TO MyFood/
        assert view.status_code == 302
        assert view.url == "/myfood"
