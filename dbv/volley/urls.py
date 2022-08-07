from django.urls import path

from .views import *

urlpatterns=[
    path('', VolleyHome.as_view(), name='home'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', ArticleCategory.as_view(), name='category'),
    path('tournament/', Tournament.as_view(), name='tournament'),
    path('contacts/', Contacts.as_view(), name='contacts'),
    path('feedback/', Feedback.as_view(), name='feedback'),
    path('faq/', FAQ.as_view(), name='faq'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('fotogallery2/', Fotogallery.as_view(), name='fotogallery'),
    path('fotogallery/', ShowFoto.as_view(), name='showfoto'),
    path('application/', Application.as_view(), name='application'),
    path('registered_teams/', Registered_teams.as_view(), name='registered_teams'),
    path('reklama/', Advertising.as_view(), name='advertising'),
    path('men_players/', ManPlayer.as_view(), name='players'),
    path('women_players', WomanPlayer.as_view(), name='w_players'),
    path('show_player/<slug:player_slug>', ShowPlayer.as_view(), name='show_player'),
    path('shedule/', AllShedule.as_view(), name='all_shedule'),
    path('show_shedule/<slug:shedule_slug>', ShowShedule.as_view(), name='show_shedule'),
    path('championship/', TournamentTable.as_view(), name='championship'),
    path('results/', ResultNet.as_view(), name='results'),
    path('sponsors/', OurSponsors.as_view(), name='sponsors'),
    path('translations/', LiveVideo.as_view(), name='translations'),
    path('ranking/', PlayerRanking.as_view(), name='ranking'),
    path('choose/', MenOrWomen.as_view(), name='choose_player'),

]

