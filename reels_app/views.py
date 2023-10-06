from rest_framework.response import Response
from .models import Posts, LikedBy
from django.contrib.auth.models import User
from .serializers import serialized_post, like_reel_serializer, shared_post_serializer, comments_serializer
from rest_framework import generics


class getReels(generics.ListAPIView):
    def get(self, request, *args, **kwargs):        
        currentUser = request.data['userId']
        queryset = Posts.objects.all()
        serialized = serialized_post(queryset, many=True)
        res ={
            "Res":serialized.data
        }
        return Response(res)


class likeReel(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        userId=request.data['userId']
        postId=request.data['postId']
        check = LikedBy.objects.filter(user = userId, post = postId)
        
        if check.count()==0:
            dataset = {"user":userId, "post":postId}
            queryset = like_reel_serializer(data = dataset)
            if queryset.is_valid():
                queryset.save()
            else:
                print(queryset.error_messages)
            return Response("Post liked")
        else:
            check.delete()
            return Response("Post Unliked")



class shareReel(generics.ListAPIView):
    def get(self,request):
        print(request.data)
        details = request.data
        serialized = shared_post_serializer(data = details)
        if serialized.is_valid():
            serialized.save()
            return Response("shared!")
        else:
            return Response(serialized.errors)


class addComment(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):        
        post = request.data['post']
        commented_by  = request.data['commented_by']
        comment= request.data['comment']
        dataset = {"post":post,"commented_by":commented_by,"comment":comment}
        serialized = comments_serializer(dataset)
        print(serialized.data,4444444444444444444444444)

        return super().post(request, *args, **kwargs)
            
