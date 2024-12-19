from django.shortcuts import render

# Create your views here.
def platform_view(request):
    return render(request, 'third_task/platform.html')

def shop_view(request):
    products = {
        'product1': 'Товар 1',
        'product2': 'Товар 2',
        'product3': 'Товар 3'
    }
    context = {
        'products': products
    }
    return render(request, 'third_task/shop.html', context)


def cart_view(request):

    return render(request, 'third_task/cart.html')