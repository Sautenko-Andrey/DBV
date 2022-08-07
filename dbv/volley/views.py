from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *




class VolleyHome(DataMixin, ListView):
    model = Article
    template_name = 'volley/index.html'
    context_object_name = 'posts'


    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        c_def=self.get_user_context(title='Главная страница')
        return dict(list(context.items())+list(c_def.items()))


    def get_queryset(self):
        return Article.objects.filter(is_published=True).select_related('cat')


class ManPlayer(DataMixin,ListView):
    model = Player
    template_name = 'volley/players.html'
    context_object_name = 'players'

    def get_queryset(self):
        return Player.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Игроки/Мужчины')
        return dict(list(context.items()) + list(c_def.items()))


class WomanPlayer(DataMixin,ListView):
    model = Player
    template_name = 'volley/woman_players.html'
    context_object_name = 'players'

    def get_queryset(self):
        return Player.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Игроки/Женщины')
        return dict(list(context.items()) + list(c_def.items()))



class ShowFoto(DataMixin,ListView):
    model = Fotos
    template_name = 'volley/showfoto.html'
    context_object_name = 'album'


    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        c_def=self.get_user_context(title='Фото')
        return dict(list(context.items())+list(c_def.items()))


class Fotogallery(DataMixin, ListView):
    model = Tournament
    template_name = 'volley/fotogallery.html'
    context_object_name = 'tour'


    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Альбомы')
        return dict(list(context.items()) + list(c_def.items()))


# def index(request):
#     posts=Article.objects.all()
#     context={
#         'posts':posts,
#         'menu':menu,
#         'title':'Главная страница',
#         'cat_selected':0,
#     }
#     return render(request,'volley/index.html', context=context)


# def categories(request, catid):
#     if int(catid)>100:
#         return redirect('home', permanent=True)
#     return HttpResponse(f'Статьи по категориям {catid}')


class ShowPost(DataMixin, DetailView):
    model = Article
    template_name = 'volley/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class ShowPlayer(DataMixin, DetailView):
    model = Player
    template_name = 'volley/player_post.html'
    slug_url_kwarg = 'player_slug'
    context_object_name = 'player'

    def get_queryset(self):
        return Player.objects.filter(slug=self.kwargs['player_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['player'])
        return dict(list(context.items()) + list(c_def.items()))



# def show_post(request, post_slug):
#     post=get_object_or_404(Article,slug=post_slug)
#
#     context={
#         'post':post,
#         'menu':menu,
#         'title':post.title,
#         'cat_selected':post.cat_id
#     }
#     return render(request, 'volley/post.html', context=context)


class ArticleCategory(DataMixin, ListView):
    model=Article
    template_name = 'volley/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Article.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')


    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        c=Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Категория-' + str(c.name),
                                      cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))


# def show_category(request, cat_slug):
#     posts=Article.objects.filter(cat__slug=cat_slug)
#
#     context = {
#             'posts':posts,
#             'menu':menu,
#             'title':'Отображение по рубрикам',
#             'cat_selected':cat_slug,
#         }
#
#     return render(request, 'volley/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class Tournament(DataMixin, ListView):
    model=Application
    template_name = 'volley/season_overview.html'
    context_object_name = 'teams'


    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Сезон 2022')
        return dict(list(context.items()) + list(c_def.items()))


class Registered_teams(DataMixin,ListView):
    model = Application
    template_name = 'volley/season.html'
    context_object_name = 'teams'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Зарегестрированные команды')
        return dict(list(context.items()) + list(c_def.items()))


class Contacts(DataMixin, ListView):
    model = Organizators
    template_name = 'volley/contacts.html'
    context_object_name = 'organizators'


    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Контакты организаторов')
        return dict(list(context.items()) + list(c_def.items()))



    def get_queryset(self):
        return Organizators.objects.filter(is_published=True)


# def contacts(request):
#     organizators = Organizators.objects.all()
#     context={
#         'organizators':organizators,
#         'menu':menu,
#         'title':'Наши контакты',
#     }
#     return render(request, 'volley/contacts.html', context=context)


class Feedback(LoginRequiredMixin, DataMixin, CreateView):
    form_class = FeedbackForm
    template_name = 'volley/feedback.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')


    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Обратная связь')
        return dict(list(context.items()) + list(c_def.items()))


# def feedback(request):
#     if request.method=='POST':
#         form=FeedbackForm(request.POST)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#     else:
#         form=FeedbackForm()
#     return render(request, 'volley/feedback.html', {'form':form, 'menu':menu, 'title':'Обратная связь'})


class FAQ(DataMixin, ListView):
    model = Question_Answer
    template_name = 'volley/faq.html'
    context_object_name = 'question_answer'


    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Вопрос/Ответ')
        return dict(list(context.items()) + list(c_def.items()))


    def get_queryset(self):
        return Question_Answer.objects.filter(is_published=True)


# def faq(request):
#     return HttpResponse('Здесь будут собраны ответы на самые распространенный вопросы')


# def login(request):
#     return HttpResponse('Авторизация')


class Application(DataMixin, CreateView):
    form_class = ApplicationForm
    template_name = 'volley/application.html'
    success_url = reverse_lazy('home')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Заявка на участие')
        return dict(list(context.items()) + list(c_def.items()))



class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'volley/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))


    def form_valid(self, form):
        user=form.save()
        login(self.request,user)
        return redirect('home')


class Login(DataMixin,LoginView):
    form_class = LoginForm
    template_name = 'volley/login.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))


    def get_success_url(self):
        return reverse_lazy('home')


class Advertising(DataMixin, TemplateView):
    template_name = 'volley/advertising.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Реклама')
        return dict(list(context.items()) + list(c_def.items()))


def logout_user(request):
    logout(request)
    return redirect('login')


class AllShedule(DataMixin, ListView):
    model = Shedule
    template_name = 'volley/all_shedule.html'
    context_object_name = 'mutual_shedule'


    def get_queryset(self):
        return Shedule.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Туры')
        return dict(list(context.items()) + list(c_def.items()))


class ShowShedule(DataMixin, DetailView):
    model = Shedule
    template_name = 'volley/show_shedule.html'
    slug_url_kwarg = 'shedule_slug'
    context_object_name = 'particular_shedule'

    def get_queryset(self):
        return Shedule.objects.filter(slug=self.kwargs['shedule_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['particular_shedule'])
        return dict(list(context.items()) + list(c_def.items()))


class TournamentTable(DataMixin,ListView):
    model = TablePoints
    template_name = 'volley/table_points.html'
    context_object_name = 'info'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Турнирная таблица')
        return dict(list(context.items()) + list(c_def.items()))


class ResultNet(DataMixin, ListView):
    model=TablePoints
    template_name = 'volley/results.html'
    context_object_name = 'teams'


    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Результаты игр')
        return dict(list(context.items()) + list(c_def.items()))


class OurSponsors(DataMixin, TemplateView):
    template_name = 'volley/sponsors.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Наши спонсоры')
        return dict(list(context.items()) + list(c_def.items()))


class LiveVideo(DataMixin, ListView):
    model = Translation
    template_name = 'volley/translation.html'
    context_object_name = 'video'


    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Трансляции игр')
        return dict(list(context.items()) + list(c_def.items()))


    def get_queryset(self):
        return Translation.objects.filter(is_published=True)


class PlayerRanking(DataMixin, ListView):
    model = Player
    template_name = 'volley/ranking.html'
    context_object_name = 'player'

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        c_def=self.get_user_context(title='Рейтинги игроков')
        return dict(list(context.items()) + list(c_def.items()))


class MenOrWomen(DataMixin, TemplateView):
    template_name = 'volley/men_or_women.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Игроки')
        return dict(list(context.items()) + list(c_def.items()))

