from django.contrib import admin
from django.urls import path
from reels_app.views import getReels, likeReel, shareReel, addComment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getreels/', getReels.as_view()),
    path('likeReel/', likeReel.as_view()),
    path('shareReel/', shareReel.as_view()),
    path('addcomment/', addComment.as_view()),
]