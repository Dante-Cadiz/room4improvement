from . import views
from django.urls import path

urlpatterns = [
    path('', views.CategoryListView.as_view(), name='home'),
    path('<slug:slug>/', views.CategoryView.as_view(), name='category'),
    path('booking/<slug:slug>/<int:pk>', views.MakeBooking.as_view(),
         name='make_booking'),
]