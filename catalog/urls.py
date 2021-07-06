from django.urls import path,  include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="catalog"),
    path('paintings/', views.painting_index, name="paintings"),
    path('painting<int:pk>/', views.painting_detail, name="painting_detail"),
    path('painters/', views.painter_index, name="painters"),
    path('painter<int:pk>/', views.painter_detail, name="painter_detail"),
    path("art_search/", views.art_search, name="art_search"),


    # /appimageprocessing-CLOUDINARY/
    path('', views.index, name='catalog.views.index'),

    path('predefined_delivery_urls/', views.painting_index_sample1, name='catalog.views.painting_index_sample1'),

    path('cloudinary_delivery_urls/', views.painting_index_sample2, name='catalog.views.painting_index_sample2'),

    path('cloudinary_template_urls/', views.painting_index_sample3, name='catalog.views.painting_index_sample3'),

]

"""path('', views.index, name='index'),
    path('paintings/', views.PaintingListView.as_view(), name='paintings')"""