from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Article(models.Model):
    title=models.CharField(max_length=255, verbose_name='Заголовок')
    slug=models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    content=models.TextField(blank=False, verbose_name='Текст статьи')
    photo=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Картинка')
    time_create=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update=models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_published=models.BooleanField(default=True, verbose_name='Опубликовано')
    cat=models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug':self.slug})


    class Meta:
        verbose_name='статьи'
        verbose_name_plural = 'Статьи'
        ordering=['-time_create', 'title']


class Comments(models.Model):
    article=models.ForeignKey('Article', on_delete=models.CASCADE, verbose_name='Статья', blank=True, null=True,
                              related_name='comments_article')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария', blank=True, null=True)
    create_date=models.DateTimeField(auto_now=True, verbose_name='Дата создания комментария')
    text=models.TextField(verbose_name='Текст комментария')
    status=models.BooleanField(verbose_name='Видимость комментария', default=False)


class Comment(models.Model):
    name=models.CharField(max_length=80, verbose_name='Имя')
    email=models.EmailField(max_length=254, verbose_name='Эмейл')
    body=models.TextField(verbose_name='Комментарий')
    create_on=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    active= models.BooleanField(default=False, verbose_name='Активен/Неактивен')
    post= models.ForeignKey('Article', on_delete=models.CASCADE, related_name='comments',
                       verbose_name='Пост')


    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Коментарии'
        ordering = ['create_on']



class Category(models.Model):
    name=models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


    class Meta:
        verbose_name='категорию'
        verbose_name_plural = 'Категория'
        ordering=['-id']



class Feedback(models.Model):
    title = models.CharField(blank=False, max_length=50, db_index=True, verbose_name='Тема')
    content = models.TextField(blank=False, verbose_name='Текст')
    email=models.CharField(blank=False, max_length=30, verbose_name='Email')


    def __str__(self):
        return self.title


    class Meta:
        verbose_name='сообщение'
        verbose_name_plural = 'Обратная связь'
        ordering=['-id']



class Application(models.Model):
    team_name = models.CharField(blank=False, max_length=30, db_index=True, verbose_name='Команда')
    tour_category = models.CharField(blank=False, max_length=30, db_index=True, verbose_name='Категория')
    player_1 = models.CharField(blank=False, max_length=30, db_index=True, verbose_name='Игрок №1')
    player_2 = models.CharField(blank=False, max_length=30, db_index=True, verbose_name='Игрок №2')
    city = models.CharField(blank=False, max_length=20, db_index=True, verbose_name='Город')
    phone=models.CharField(blank=False, max_length=12, db_index=True, verbose_name='Телефон')
    rank=models.CharField(null=True,max_length=5,verbose_name='Рейтинг')
    team_id=models.ForeignKey('TablePoints', on_delete=models.PROTECT, null=True, verbose_name='ID команды')


    def __str__(self):
        return self.team_name


    class Meta:
        verbose_name='заявку'
        verbose_name_plural = 'Заявка участника'
        ordering=['id']


class Organizators(models.Model):
    name=models.CharField(blank=False, max_length=50, db_index=True, verbose_name='Имя/Фамилия')
    content = models.TextField(blank=False, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    phone=models.CharField(blank=False, max_length=12, verbose_name='Телефон')
    email = models.CharField(blank=False, max_length=30, verbose_name='Email')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name='организатора'
        verbose_name_plural = 'Организаторы'
        ordering=['id']


class Question_Answer(models.Model):
    question = models.CharField(blank=False, max_length=50, db_index=True, verbose_name='Вопрос')
    answer = models.TextField(blank=False, verbose_name='Ответ')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')


    def __str__(self):
        return self.question


    class Meta:
        verbose_name='организатора'
        verbose_name_plural = 'Вопросы/Ответы'
        ordering=['id']


class Tournament(models.Model):
    name=models.CharField(max_length=100)
    title_photo = models.ImageField(verbose_name='Картинка', null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name='фотографию'
        verbose_name_plural = 'Фотогаллерея'


def upload_gallery_image(instance, filename):
    return f'images/{instance.tournament.name}/gallery/{filename}'


class Fotos(models.Model):
    image=models.ImageField(upload_to=upload_gallery_image)
    tournament=models.ForeignKey(Tournament, on_delete=models.CASCADE)


class Player(models.Model):
    name=models.CharField(max_length=30, db_index=True, blank=False, verbose_name='Имя игрока')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    photo=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=False, verbose_name='Фото')
    content=models.TextField(blank=False, verbose_name='Текст статьи', null=True)
    height=models.CharField(max_length=6, blank=False, verbose_name='Рост')
    city=models.CharField(max_length=20, blank=False, verbose_name='Город')
    age=models.CharField(max_length=2, blank=False, verbose_name='Возраст')
    value=models.CharField(max_length=30, blank=True, verbose_name='Спортивное звание')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    sex = models.ForeignKey('Sex', on_delete=models.PROTECT, null=True, verbose_name='Пол')
    instagram=models.CharField(max_length=255, null=True, verbose_name='Инстаграм')
    facebook = models.CharField(max_length=255, null=True, verbose_name='Фейсбук')
    rank=models.CharField(max_length=100, null=True, verbose_name='Рейтинг игрока' )


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('show_player', kwargs={'player_slug':self.slug})


    class Meta:
        verbose_name='игрока'
        verbose_name_plural = 'Игроки'
        ordering=['-rank', 'name']


class Sex(models.Model):
    name=models.CharField(max_length=7,db_index=True, blank=False, verbose_name='Категория')
    slug=models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('sex', kwargs={'sex_slug': self.slug})


    class Meta:
        verbose_name='категорию'
        verbose_name_plural = 'Категория'
        ordering=['id']


class Shedule(models.Model):
    name=models.CharField(max_length=50, verbose_name='Название тура', blank=False)
    slug = models.SlugField(max_length=70, unique=True, db_index=True, verbose_name='Слаг')
    picture=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Картинка', blank=False)
    content=models.TextField(verbose_name='Описание',blank=False)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    date=models.CharField(max_length=50, verbose_name='Дата проведения')
    location=models.CharField(max_length=100, null=True, verbose_name='Локация')
    event_format=models.CharField(max_length=100, null=True, verbose_name='Формат турнира')
    money_prize=models.CharField(max_length=100, null=True, verbose_name='Призовой фонд')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('show_shedule', kwargs={'shedule_slug':self.slug})


    class Meta:
        verbose_name='тур'
        verbose_name_plural = 'Календарь'
        ordering=['id']


class TablePoints(models.Model):
    team_name=models.CharField(max_length=30, null=True, verbose_name='Название команды',  db_index=True)
    second_names=models.CharField(max_length=70, null=True, verbose_name='Фамилии игроков')
    set_difference=models.CharField(max_length=10, null=True, verbose_name='Выигранные/Проигранные партии')
    count_tours=models.CharField(max_length=2, null=True, verbose_name='Туров сыграно')
    points=models.CharField(max_length=3, null=True, verbose_name='Очки')


    def __str__(self):
        return self.team_name

    class Meta:
        verbose_name='турнирную таблицу'
        verbose_name_plural = 'Турнирная таблица'
        ordering=['-points']


class Translation(models.Model):
    name=models.CharField(max_length=50, db_index=True, verbose_name='Название трансляции', null=True)
    refer=models.CharField(max_length=255, verbose_name='Ссылка  на трансляцию', null=True)
    name_2 = models.CharField(max_length=50, db_index=True, verbose_name='Название трансляции #2', null=True)
    refer_2 = models.CharField(max_length=255, verbose_name='Ссылка  на трансляцию #2', null=True)
    name_3 = models.CharField(max_length=50, db_index=True, verbose_name='Название трансляции #3', null=True)
    refer_3 = models.CharField(max_length=255, verbose_name='Ссылка  на трансляцию #3', null=True)
    info=models.TextField(max_length=255, null=True, verbose_name='Информация о трансляции')
    picture=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Картинка',null=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')


    def __str__(self):
        return self.name


    class Meta:
        verbose_name='трансляцию'
        verbose_name_plural = 'Трансляция'
        ordering=['id']



