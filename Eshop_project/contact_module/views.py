from django.shortcuts import render

def contact_us_page(request):
    return render(request, 'contact_module/contact_us_page.html', {})
