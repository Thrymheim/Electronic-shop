from django.shortcuts import render

def index_page(request):
    return render(request, 'home_module/index_page.html')

def conatact_page(request):
    return render(request, 'home_module/contact_page.html')

def site_header_partial(request):
    context = {
        'link' : 'آموزش جنگو'
    }
    return render(request, 'shared/site_header_partial.html', context)

def site_footer_partial(request):
    return render(request, 'shared/site_footer_partial.html')