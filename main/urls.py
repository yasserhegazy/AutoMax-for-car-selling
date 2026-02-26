from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='main'),
    path('home/', views.home_view, name='home'),
    path('list/', views.list_view, name='list'), 
    path('listing/<str:id>/', views.listing_view, name='listing'),
    path('listing/<str:id>/edit/', views.edit_view, name='edit'),
    path('listing/<str:id>/delete/', views.delete_listing_view, name='delete_listing'),
    path('listing/<str:id>/like/', views.like_listing_view, name='like_listing'),
    path('listing/<str:id>/inquire/', views.inquire_listing_using_email, name='inquire_listing'),
]
