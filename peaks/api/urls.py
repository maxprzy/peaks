from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.PeaksListCreateAPIView.as_view()),
    path('<int:pk>/', views.PeaksDetailAPIView.as_view()),
    path('<int:pk>/update/', views.PeaksUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.PeaksDestroyAPIView.as_view()),
    path('precise/', views.get_precise_list)
    #path('get_events/', views.get_events),
    #path('store_events/', views.store_events)
]