from . import views
from django.urls import path

urlpatterns = [
    path('', views.CategoryListView.as_view(), name='home'),
    path('<slug:slug>/', views.CategoryView.as_view(), name='category'),
    path('calendar/<int:year>/<str:month>', views.CalendarView.as_view(), name='calendar')
]