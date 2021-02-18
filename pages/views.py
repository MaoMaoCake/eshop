from django.shortcuts import render

# Create your views here.
def home_page_view(request, *args, **kwargs):
    print(request.user)
    context = {
        'nbar': 'home'
    }
    return render(request, "home-page.html", context)


def about_page_view(request, *args, **kwargs):
    print(request.user)
    context = {
        'nbar': 'about'
    }
    return render(request, "about.html", context)


def contact_page_view(request, *args, **kwargs):
    print(request.user)
    context = {
        'nbar': 'contact'
    }
    return render(request, "contact.html", context)

def product_page_view(request, *args, **kwargs):
    print(request.user)
    context = {
        'nbar': 'product'
    }
    return render(request, "products.html", context)

def gallery_page_view(request, *args, **kwargs):
    print(request.user)
    context = {
        'nbar':'gallery'
    }
    return render(request, "gallery.html", context)