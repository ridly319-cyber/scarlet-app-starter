"""
Views: one Python function per page.

A view takes the request and returns a response. render() fills a template with a
context dictionary and wraps the result in an HttpResponse.
"""

from django.shortcuts import render
from operations.models import Product


def home(request):
    featured = (
        Product.objects.filter(active=True, size="12 oz bag")
        .select_related("coffee")
        .order_by("sku")[:4]
    )
    return render(request, "pages/home.html", {"featured": featured})


def catalog(request):
    products = (
        Product.objects.filter(active=True)
        .select_related("coffee")
        .order_by("sku")
    )
    return render(
        request,
        "pages/catalog.html",
        {"products": products, "count": products.count()},
    )


def about(request):
    return render(request, "pages/about.html")


def contact(request):
    return render(request, "pages/contact.html")
