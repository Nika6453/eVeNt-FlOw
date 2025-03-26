from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('home2/', views.home2_page, name='home2_page'),
    path('description/<int:pk>/', views.description_page, name='description_page'),
    path('privatedesc/<int:pk>/', views.privatedesc_page, name='privatedesc_page'),
    path('create/', views.create_page, name='create_page'),
    path('about/', views.about_page, name='about_page'),
    path('settings/', views.settings_page, name='settings_page'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('page_category/<slug:slug>/', views.page_by_category, name='page_by_category'),
    path('page_category_private/<slug:slug>/', views.page_by_category_private, name='page_by_category_private'),
    path('search/', views.search, name='search')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)