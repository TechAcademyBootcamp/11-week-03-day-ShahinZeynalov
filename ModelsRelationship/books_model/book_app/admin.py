from django.contrib import admin
from book_app.models import Book,Author,Category

# Register your models here.

admin.site.register([Book,Author,Category])
