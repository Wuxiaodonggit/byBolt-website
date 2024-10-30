from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Website
from .forms import WebsiteForm

@login_required
def website_list(request):
    websites = Website.objects.filter(owner=request.user)
    return render(request, 'websites/website_list.html', {'websites': websites})

@login_required
def website_create(request):
    if request.method == 'POST':
        form = WebsiteForm(request.POST)
        if form.is_valid():
            website = form.save(commit=False)
            website.owner = request.user
            website.save()
            messages.success(request, '网站添加成功！')
            return redirect('website_list')
    else:
        form = WebsiteForm()
    return render(request, 'websites/website_form.html', {'form': form, 'title': '添加网站'})