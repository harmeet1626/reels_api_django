from rest_framework.response import Response
from rest_framework import serializers
from .models import Posts, LikedBy, user_profile, SharedPost, Comments, Followers


class serialized_post(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    liked = serializers.SerializerMethodField()
    shares = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    profilePic = serializers.SerializerMethodField()
    isfollowing = serializers.SerializerMethodField()
    class Meta:
        model = Posts
        fields = ('id','user','caption', 'video', 'likes', 'liked', 'shares', 'comments','isfollowing','profilePic')

    def get_likes(self, id):
        likes = LikedBy.objects.filter(post=id).values()
        return likes.count()
    
    def get_liked(self, id):
        current_user = 1
        liked = liked = LikedBy.objects.filter(post_id = id, user_id = current_user).values()        
        if liked.count() == 0 :
            return False
        else:
            return True
        
    def get_shares(self, id):
        totalShares = SharedPost.objects.filter(post = id)
        return totalShares.count()

    def get_comments(self, id):
        totalComments = Comments.objects.filter(post = id)
        return totalComments.count()
    
    def get_profilePic(self, id):
        post_id = id.id
        post = Posts.objects.filter(id = post_id).values('user__id')
        user_id = post[0]['user__id']
        picture = user_profile.objects.filter(id = user_id).values()
        return picture[0]['ProfilePicture']
    
    def get_isfollowing(self, id):
        post_id = id.id
        my_id = 1
        post = Posts.objects.filter(id = post_id).values('user__id')
        user_id = post[0]['user__id']
        following = Followers.objects.filter(user = user_id, followed_by=my_id)        
        if following.count()==0:
            return False
        else:
            return True
    



class like_reel_serializer(serializers.ModelSerializer):
    class Meta:
        model = LikedBy
        fields = "__all__" 


class shared_post_serializer(serializers.ModelSerializer):
    class Meta:
        model = SharedPost
        fields='__all__'


class comments_serializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields='__all__'



class user_profile_serializer(serializers.ModelSerializer):
    class Meta:
        model = user_profile
        fields='__all__'



class Followers_serializers(serializers.ModelSerializer):
    class Meta:
        model = Followers
        fields='__all__'