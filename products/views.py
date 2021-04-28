from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.shortcuts import render, redirect, reverse, get_object_or_404


from products.models import Product, Category


def all_products(request):
    """
    A view to show all products, including sorting and search queries.
    """

    products = Product.objects.filter(active=True)
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if "query" in request.GET:
            query = request.GET["query"]
            if not query:
                messages.error(
                    request, ("You didn't enter any search criteria!")
                )
                return redirect(reverse("all_products"))

            queries = (
                Q(name__icontains=query)
                | Q(description__icontains=query)
                | Q(category__friendly_name__icontains=query)
            )
            products = products.filter(queries)

    current_sorting = f"{sort}_{direction}"

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting,
    }

    return render(request, "products/products.html", context)


def product_detail(request, product_slug):
    """
    A view to show an individual product from the product slug.
    """

    product = get_object_or_404(Product, slug=product_slug)

    if product.active is False:
        messages.info(request, 'Sorry, that product is no '
                      'longer for sale. Please check back in the future.')
        return(redirect('all_products'))

    context = {
        "product": product,
    }

    return render(request, "products/product_detail.html", context)
