from django.db import models
from django.contrib.auth.models import User


class user_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE ,blank=True, null=True)
    ProfilePicture = models.CharField(max_length=255,blank=True, null=True)    


class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=2000, blank=True, null=True)
    video = models.CharField(max_length=1000, blank=True, null=True)    
    class Meta:
        db_table = "posts"    


class Tags(models.Model):
    taged_user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    class Meta:
        db_table = "tags"


class LikedBy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    class Meta:
        db_table = "likedby"


class SharedPost(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    shared_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shared_by", blank=True, null=True)
    shared_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shared_to", blank=True, null=True)
    class Meta:
        db_table = "sharedPost"


class Comments(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000, blank=True, null=True)
    class Meta:
        db_table = "comments"