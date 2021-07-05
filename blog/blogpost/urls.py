from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from .views import HomeView, PostView

urlpatterns = [
    path('', HomeView.as_view() , name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('posts/<str:slug>',PostView.as_view, name='post')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#added manually
#urlpatterns += staticfiles_urlpatterns()