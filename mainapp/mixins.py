from django.views.generic.detail import SingleObjectMixin
from .models import Category


class CategoryDetailMixin(SingleObjectMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['category'] = Category.objects.all()
        return context
