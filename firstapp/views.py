from django.shortcuts import render
from django.http import HttpResponse
from . import forms


def index(request):
    return render(request, "firstapp/index.html")


def form_view(request):
    form = forms.formname()
    if request.method == "POST":
        form = forms.formname(request.POST)

        if form.is_valid():
            print("Validation ok")
            print("Name: " + form.cleaned_data["name"])
            print("Email: " + form.cleaned_data["email"])
            print("Text: " + form.cleaned_data["text"])

    return render(request, "firstapp/formv.html", {"form": form})


def userform(request):
    form = forms.userinfo()
