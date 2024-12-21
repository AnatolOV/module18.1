from django.shortcuts import render

# Create your views here.
def platform_view(request):
    return render(request, 'fouth_task/menu.html')

def shop_view(request):
    products = {'games': ['Atomic Heart', "Cyberpunk 2077"]}
    context = {
        'products': products
    }
    return render(request, 'fouth_task/shop.html', context)


def cart_view(request):
    return render(request, 'fouth_task/cart.html')

