from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, reverse, get_object_or_404


from products.models import Product, Category


def all_products(request):
    """
    A view to show all products, including sorting and search queries.
    """

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if "category" in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if "query" in request.GET:
            query = request.GET["query"]
            if not query:
                messages.error(
                    request, ("You didn't enter any search criteria!")
                )
                return redirect(reverse("all_products"))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query
            ) | Q(
                category__friendly_name__icontains=query
            )
            products = products.filter(queries)

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
    }

    return render(request, "products/products.html", context)


def product_detail(request, product_slug):
    """
    A view to show an individual product from the product slug.
    """

    product = get_object_or_404(Product, slug=product_slug)

    context = {
        "product": product,
    }

    return render(request, "products/product_detail.html", context)
