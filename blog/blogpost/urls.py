from django.urls import path
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from .views import HomeView,LikeView 



urlpatterns = [
    path('', HomeView.as_view() , name='index'),
    path('model', views.model , name='model'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('posts/<str:slug>',views.posts, name='post'),
    path('like/<str:slug>',LikeView, name='like_post'),  
    url(r'^favicon\.ico$',RedirectView.as_view(url='static/fevicon.ico')),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#added manually
#urlpatterns += staticfiles_urlpatterns()