from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'get_html_for_pic', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title','slug', 'cat', 'content','photo', 'get_html_for_pic', 'is_published','time_create','time_update')
    readonly_fields = ('time_create','time_update','get_html_for_pic')
    save_on_top = True


    def get_html_for_pic(self,object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=60>")

    get_html_for_pic.short_description='Картинка'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'email')
    list_display_links = ('id', 'title')
    search_fields = ('title',)



class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'team_name', 'tour_category', 'player_1', 'player_2', 'city', 'phone', 'rank', 'team_id')
    list_display_links = ('id', 'team_name')
    search_fields = ('team_name',)


class OrganizatorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'content', 'photo', 'phone', 'email', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published',)


class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer', 'is_published')
    list_display_links = ('id', 'question')
    search_fields = ('question',)
    list_editable = ('is_published',)
    list_filter = ('is_published',)


class ImageInLine(admin.TabularInline):
    model = Fotos


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    inlines = [
        ImageInLine
    ]


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_html_for_photo', 'rank', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    list_editable = ('is_published',)
    list_filter = ('is_published',)
    prepopulated_fields = {'slug': ('name',)}
    fields = ('name', 'slug', 'sex', 'photo', 'get_html_for_photo','rank','content','height','city','age','value','instagram','facebook','is_published')
    readonly_fields = ('get_html_for_photo',)
    save_on_top = True


    def get_html_for_photo(self,object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=60>")

    get_html_for_photo.short_description='Фото'


class SexAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class SheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_html_for_background', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    list_editable = ('is_published',)
    list_filter = ('is_published',)
    prepopulated_fields = {'slug': ('name',)}
    fields = ('name', 'slug', 'picture', 'get_html_for_background', 'content', 'date', 'location', 'event_format',
              'money_prize', 'is_published')
    readonly_fields = ('get_html_for_background',)
    save_on_top = True

    def get_html_for_background(self, object):
        if object.picture:
            return mark_safe(f"<img src='{object.picture.url}' width=60>")

    get_html_for_background.short_description = 'Картинка'


class TablePointsAdmin(admin.ModelAdmin):
    list_display = ('id', 'team_name', 'second_names', 'set_difference', 'count_tours', 'points')
    list_display_links = ('id', 'team_name', 'second_names', 'points')
    search_fields = ('team_name', 'second_names')
    list_filter = ('team_name', 'second_names')


class TranslationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','info','picture', 'get_html_for_picture','name_2','name_3','is_published')
    list_display_links = ('name',)
    list_editable = ('is_published',)
    search_fields = ('name',)
    list_filter = ('name', 'is_published')



    def get_html_for_picture(self,object):
        if object.picture:
            return mark_safe(f"<img src='{object.picture.url}' width=60>")

    get_html_for_picture.short_description='Картинка'







admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Organizators, OrganizatorsAdmin)
admin.site.register(Question_Answer, FAQAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Shedule, SheduleAdmin)
admin.site.register(TablePoints, TablePointsAdmin)
admin.site.register(Translation, TranslationAdmin)

admin.site.site_title='Админ-панель сайта DBV'
admin.site.site_header='Админ-панель сайта DBV'