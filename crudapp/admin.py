from django.contrib import admin
from crudapp.models import book,student,register

# Register your models here.
admin.site.register(book)
admin.site.register(student)
admin.site.register(register)