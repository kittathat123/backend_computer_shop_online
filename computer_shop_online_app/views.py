# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_requireddjango
from django.contrib.auth import login, logout, authenticate

# this import will allow the server to response to the client when they request from a certain URL
from django.http import HttpResponse
from django.template import loader
from .models import New_arrival_product
from .forms import Register_Form, Login_Form


# Create your views here.


def main_page(request):
    # return HttpResponse("Hello, world. You're at the polls ind") not the template just Http text
    new_arrival_product = New_arrival_product.objects.all()

    context = {"new_arrival_product": new_arrival_product}
    return render(request, "web_page/main.html", context)


def promotion_page(request):
    # return HttpResponse("It is your promotion_page")
    return render(request, "web_page/promotion-page.html")


def register_page(request):
    # return render(request, 'web_page/register-page.html')
    if request.method == "POST":
        form = Register_Form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("computer_shop_online_app:main_page")
    else:
        form = Register_Form()
    return render(request, "web_page/register-page.html", {"form": form})


def login_page(request):
    # return render(request, 'web_page/login-page.html')
    if request.method == "POST":
        print("MA YOUNG")
        form = Login_Form(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print("KO CHECK NOI : ", user)
            login(request, user)
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect("computer_shop_online_app:main_page")
    else:
        form = Login_Form()
    return render(request, "web_page/login-page.html", {"form": form})


def logout_page(request):
    if request.method == "POST":
        logout(request)
        print("LOGOUT LEAW NA : ", request)
        return redirect("computer_shop_online_app:main_page")
