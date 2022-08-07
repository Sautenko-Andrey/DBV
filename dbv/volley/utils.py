from django.db.models import Count

from .models import *

menu=[
    {'title': 'СЕЗОН 2022', 'url_name': 'tournament'},
    {'title': 'КОНТАКТЫ', 'url_name': 'contacts'},
    {'title': 'ОБРАТНАЯ СВЯЗЬ', 'url_name': 'feedback'},
    {'title': 'FAQ', 'url_name': 'faq'},
    {'title': 'РЕКЛАМА', 'url_name': 'advertising'}
]

class DataMixin:
    paginate_by=10
    def get_user_context(self, **kwargs):
        context=kwargs
        cats=Category.objects.annotate(Count('article'))
        context['menu']=menu
        context['cats']=cats
        if 'cat_selected' not in context:
            context['cat_selected']=0
        return context