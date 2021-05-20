"""
Test usermanage/views.py

PEP8 exeptions: (flake8) F401 - imported but unused (l.8)
"""
import django

from purbeurre import wsgi

from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase

from usermanage.views import signup, log_out, account, signin, myfood


class TemplateTest(TestCase):

    def test_signup(self):

        """ TEST 1 - FROM signin """

        request = RequestFactory().get('/signup')

        view = signup(request)

        # 302 - REDIRECT TO Signin to login
        assert view.status_code == 200

        """ TEST 2 - WHEN USER POST FORM REGISTER' """

        request = RequestFactory().post('/signup')

        request.POST = {
            "username": "Test_signup",
            "password": "Test_pw",
            "email": "Test_email@mail.com",
            "first_name": "Test_fn",
            "last_name": "Test_ln"
        }

        view = signup(request)

        # 302 - REDIRECT TO Signin to login
        assert view.status_code == 302
        assert view.url == "/signin"

    def test_signin(self):

        """ TEST 1 - WITH A CONNECTED USER """
        request = RequestFactory().get('/signin')
        request.user = User.objects.get(username='JeanLouis')

        view = signin(request)

        # 302 - REDIRECT TO Signin to account
        assert view.status_code == 302
        assert view.url == "/account"

        """ TEST 2 - TO LOGIN WITH ANONYMOUS USER """

        request = RequestFactory().post('/signin')

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        request.user = AnonymousUser()

        request.POST = {
            'username': 'JeanLouis',
            'password': 'jeanjean'
        }

        view = signin(request)

        # 302 - Home page
        assert view.status_code == 302
        assert view.url == "/"

        """ TEST 3 - WITH UNCONNECTED CLIENT FROM RESULT """

        request = RequestFactory().post("/signin")

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        request.user = AnonymousUser()

        request.POST = {
            'username': 'JeanLouis',
            'password': 'jeanjean'
        }
        request.GET = {
            "query": '80177173'
        }

        view = signin(request)

        # 302 - Result page
        assert view.status_code == 302
        assert view.url == "/result?query=80177173"

        """ TEST 4 - WITH UNCONNECTED CLIENT FROM HOMEPAGE """

        request = RequestFactory().get('/signin')
        request.user = AnonymousUser()

        view = signin(request)

        # 200 - Signin again
        assert view.status_code == 200

    def test_account(self):

        """ TEST 1 - WITH A CONNECTED USER """
        request = RequestFactory().get('/account')
        request.user = User.objects.get(username='JeanLouis')

        view = account(request)

        # 302 - REDIRECT TO Signin to account
        assert view.status_code == 200

        """ TEST 2 - WITH ANONYMOUS USER """
        # IN FACT, USER UNCONNECTED CAN'T ACCES TO 'account.html'
        request = RequestFactory().post('/account')
        request.user = AnonymousUser()

        try:
            view = account(request)
        except django.core.exceptions.DisallowedHost:
            assert True

    def test_my_food(self):
        # IN FACT, USER UNCONNECTED CAN'T ACCES TO 'myfood.html'
        request = RequestFactory().get('/myfood')
        request.user = User.objects.get(username='JeanLouis')

        view = myfood(request)

        # 200 - In myfood
        assert view.status_code == 200

    def test_log_out(self):

        request = RequestFactory().post('/log_out')
        request.user = User.objects.get(username='JeanLouis')

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        view = log_out(request)

        assert view.status_code == 302
        assert view.url == "/"
