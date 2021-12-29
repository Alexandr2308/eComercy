from django.forms import ModelChoiceField
from django.contrib import admin

from .models import *


# class ShortsCategoryChoiceField(forms.ModelChoiceField):
#     pass


class ShortsAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='shorts'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


# class JacketCategoryChoiceField(forms.ModelChoiceField):
#     pass


class JacketAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='jackets'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Shorts, ShortsAdmin)
admin.site.register(Jacket, JacketAdmin)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Customer)

