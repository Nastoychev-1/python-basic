from django.contrib import admin
from .models import Category, Exercise, Card, Part_of_the_body

# Register your models here.
admin.site.register(Category)
admin.site.register(Exercise)
admin.site.register(Card)
admin.site.register(Part_of_the_body)