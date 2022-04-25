from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('category/<slug:slug>/', views.PostListByCategoryView.as_view(), name='post_list_by_category'),
    path('detail/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),

]

