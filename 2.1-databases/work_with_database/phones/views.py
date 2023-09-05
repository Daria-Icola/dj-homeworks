from django.shortcuts import render, redirect, get_object_or_404

from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    context = {'phones': []}
    get_sort = request.GET.get('sort')
    phones = Phone.objects.all()

    if get_sort == 'name':
        phones = phones.order_by('name')
    elif get_sort == 'min_price':
        phones = phones.order_by('price')
    elif get_sort == 'max_price':
        phones = phones.order_by('-price')

    context['phones'] = phones

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {"phone": {
        "name": phone.name,
        "image": phone.image,
        "price": phone.price,
        "release_date": phone.release_date,
        "lte_exists": phone.lte_exists
    }}
    return render(request, template, context)
