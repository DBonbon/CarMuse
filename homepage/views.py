from django.shortcuts import render
from .models import Cover

def home_page(request):
    covers = Cover.objects.all()
    context ={'covers': covers}
    return render(request, 'homepage/home_page.html', context)

