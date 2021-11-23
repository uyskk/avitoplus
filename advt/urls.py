from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views


urlpatterns = [
    path('advt/', login_required(views.AdvtListView.as_view(), login_url='login'), name='advt-list'),
    path('advt/<int:pk>', login_required(views.AdvtDetailView.as_view(), login_url='login'), name='advt-detail'),
    path('advt/create/', login_required(views.AdvtCreateView.as_view(), login_url='login'), name='advt-create'),
    path('advt/like/<int:pk>', views.LikeView.as_view(), name='advt-like'),
    path('advt/dislike/<int:pk>', views.DislikeView.as_view(), name='advt-dislike'),
    path('comment/create/<int:pk>', login_required(views.CommentCreateView.as_view(), login_url='login'), name='comment-create')

]
