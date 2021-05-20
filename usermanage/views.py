"""
VIEWS FILE FOR MANAGE USER

PEP8 exeptions: (flake8) E722 - Do not use bare 'exept'
"""

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User

from webapp.modules.tools.builder import build_data
from webapp.models import Save
from usermanage.forms import RegistrationForm


@login_required
def myfood(request):

    products = Save.objects.filter(user__iregex=f"{request.user.email}")
    list_of_products = list()
    list_of_substitute = list()
    dict_product = {}

    for product in products:
        prod_code = product.substitute
        datas = build_data(prod_code, "code")
        list_of_products.append(datas["products"][0])

        sub_code = product.product_substitued
        datas = build_data(sub_code, "code")
        list_of_substitute.append(datas["products"][0])

    dict_product["products"] = list_of_products
    dict_product["substitutes"] = list_of_substitute

    return render(request, "myfood.html", dict_product)


@login_required
def log_out(request):

    logout(request)
    return redirect("index")


@login_required
def account(request):

    data = {"form": RegistrationForm()}

    return render(request, 'account.html', data)


def signin(request):
    # IF USER COME FROM result.html and wasn't connected
    from_result = 0
    code = request.GET.get('query')
    if code:
        from_result = 1

    if request.user.is_authenticated:
        return redirect("account")

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.user_cache)
            if request.user.is_authenticated:
                if not from_result:
                    return HttpResponseRedirect("/")
                elif from_result:
                    return HttpResponseRedirect(f"/result?query={code}")
    else:
        form = AuthenticationForm(request)

    return render(request, 'signin.html')


def signup(request):

    if request.method == "POST":

        User.objects.create_user(
            username=request.POST.get('username'),
            password=request.POST.get('password'),
            email=request.POST.get('mail'),
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name')
        )

        return redirect("signin")

    data = {"form": RegistrationForm()}

    return render(request, 'signup.html', data)
