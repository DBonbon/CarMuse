from django.urls import path
from . import views
from .views import SearchResultsView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name="index"),
    # path('paintings/', views.painting_index, name="paintings"),
    # path('painting<int:pk>/', views.painting_detail, name="painting_detail"),
    path('painters/', views.painter_index, name="painters"),
    path('painter<int:pk>/', views.painter_detail, name="painter_detail"),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    # path("art_search/", views.art_search, name="art_search"),
    path('paintings/', views.PaintingListView.as_view(), name='paintings'),
    path('painting/<int:pk>/', views.PaintingDetailView.as_view(), name='painting_detail'),
]

"""path('', views.index, name='index'),
    path('paintings/', views.PaintingListView.as_view(), name='paintings')"""