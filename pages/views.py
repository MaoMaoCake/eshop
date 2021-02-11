from django.shortcuts import render

# Create your views here.
def home_page_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "home.html", {})


def about_page_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "about.html", {})


def contact_page_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "contact.html", {})