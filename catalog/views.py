from django.shortcuts import render

from catalog.models import Product


def rendering_index(request):
    context = {
        'object_list': Product.objects.all()
    }
    return render(request, 'catalog/index.html', context)


def rendering_contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        try:
            with open('callback_form.txt', 'a') as data:
                data.write(f'{name} {phone} send next message: {message}\n')
        except FileNotFoundError:
            print(f'{name} {phone} send next message: {message}')
    return render(request, 'catalog/contacts.html')


def rendering_product(request, pk):
    context = {
        'object': Product.objects.get(pk=pk)
    }
    return render(request, 'catalog/product.html', context)

