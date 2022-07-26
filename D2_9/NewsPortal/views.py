from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Product


class ProductsList(ListView):
