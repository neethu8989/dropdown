from django.contrib import admin

from dependapp.models import Districts, Branches, Person

# Register your models here.
admin.site.register(Districts)
admin.site.register(Branches)
admin.site.register(Person)
