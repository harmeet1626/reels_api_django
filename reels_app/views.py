from rest_framework.response import Response
from .models import Posts, LikedBy, Comments, user_profile
from django.contrib.auth.models import User
from .serializers import serialized_post, like_reel_serializer, shared_post_serializer, comments_serializer, user_profile_serializer, Followers_serializers
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size=5
    page_query_param = 'page'
    page_size_query_param = 'size'
    max_page_size = 20
    last_page_strings = [("last_page")]
 

# class getReels(generics.ListAPIView):
#     pagination_class = CustomPagination 
#     def get(self, request, *args, **kwargs):        
#         currentUser = request.data['userId']
#         queryset = Posts.objects.all()
#         serialized = serialized_post(queryset, many=True)
#         res ={
#             "Res":self.get_paginated_response(serialized.data)
#         }
#         return Response(res)

class getReels(generics.ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = serialized_post
    pagination_class = CustomPagination




class likeReel(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        try:                
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
                totalLikes = LikedBy.objects.filter(post = postId)
                res = {"message":"post liked!","totalLikes": totalLikes.count() }
                return Response(res)
            else:
                check.delete()
                totalLikes = LikedBy.objects.filter(post = postId)
                res = {"message":"post Unliked!","totalLikes": totalLikes.count() }
                return Response(res)
        except Exception as E:
            return Response(str(E))



class shareReel(generics.ListAPIView):
    def get(self,request):
        try:                
            details = request.data
            serialized = shared_post_serializer(data = details)
            if serialized.is_valid():
                serialized.save()
                return Response("shared!")
            else:
                return Response(serialized.errors)
        except Exception as E:
            return Response(str(E))


class addComment(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        try:                
            details = request.data
            serialized = comments_serializer(data = details)
            if serialized.is_valid():
                serialized.save()
            return Response("Comment added!")        
        except Exception as E:
            return Response(str(E))   

class getComments(generics.ListAPIView):
    def get(self, request, id, *args, **kwargs):
        try:
            queryset = Comments.objects.filter(post = id)
            serialized = comments_serializer(queryset, many=True)
            return Response(serialized.data)
        except Exception as E:
            return Response(str(E))

class follow(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        dataset = request.data
        serialized= Followers_serializers(data=dataset)
        if serialized.is_valid():
            serialized.save()
            return Response("Followed")
        else:
            return Response(serialized.errors)