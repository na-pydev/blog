from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list' ),
    path("<int:year>/<int:month>/<int:day>/<str:post>", views.post_detail_view, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share')
]
