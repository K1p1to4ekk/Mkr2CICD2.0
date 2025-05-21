from django.shortcuts import render
from .models import Category


def main(request):
    categories = Category.objects.all()
    return render(request, 'main.html', context={'categories': categories})
