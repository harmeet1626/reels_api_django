from django.contrib import admin
from .models import user_profile,LikedBy, Posts, Tags, Followers

admin.site.register(user_profile)
admin.site.register(LikedBy)
admin.site.register(Posts)
admin.site.register(Tags)
admin.site.register(Followers)
