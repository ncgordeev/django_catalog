from django.shortcuts import render


def rendering_index(request):
    return render(request, 'catalog/index.html')


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
