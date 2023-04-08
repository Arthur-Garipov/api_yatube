from rest_framework import viewsets

from posts.models import Post, Group, Comment
from .serializers import PostSerializer, GroupSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from posts.models import Post, Group, Comment
# from .serializers import PostSerializer, CommentSerializer, GroupSerializer
# from django.shortcuts import get_object_or_404
# from django.db.models import Q


# @api_view(['GET', 'POST'])
# def api_posts(request):
#     if request.method == 'POST':
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(author=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     posts = Post.objects.all()
#     serializer = PostSerializer(posts, many=True)
#     return Response(serializer.data)


# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def api_posts_id(request):
#     post = get_object_or_404(Post, id=id)
#     if request.method == 'GET':
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#     user = request.user
#     if user != post.author:
#         return Response(status=status.HTTP_403_FORBIDDEN)
#     if request.method == 'PUT' or request.method == 'PATCH':
#         serializer = PostSerializer(post, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET'])
# def api_groups(request):
#     posts = Post.objects.all()
#     groups = Group.objects.filter(Q(posts__in=posts)).distinct()
#     serializer = GroupSerializer(groups, many=True)
#     return Response(serializer.data)


# @api_view(['GET', 'POST'])
# def api_groups_id(request, slug):
#     group = get_object_or_404(Group, id=slug)
#     serializer = GroupSerializer(group)
#     return Response(serializer.data)


# @api_view(['GET', 'POST'])
# def api_comments(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     if request.method == 'POST':
#         serializer = CommentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(author=request.user, post=post)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     comments = Comment.objects.filter(post=post)
#     serializer = CommentSerializer(comments, many=True)
#     return Response(serializer.data)


# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def api_comments_id(request, comment_id):
#     comment = get_object_or_404(Comment, id=comment_id)
#     if request.method == 'GET':
#         serializer = CommentSerializer(comment)
#         return Response(serializer.data)
#     elif request.method == 'PUT' or request.method == 'PATCH':
#         if not request.user.is_authenticated:
#             return Response(status=status.HTTP_401_UNAUTHORIZED)
#         if not request.user == comment.author:
#             return Response(status=status.HTTP_403_FORBIDDEN)
#         serializer = CommentSerializer(
#             comment, data=request.data, partial=True
#         )
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         if not request.user.is_authenticated:
#             return Response(status=status.HTTP_401_UNAUTHORIZED)
#         if not request.user == comment.author:
#             return Response(status=status.HTTP_403_FORBIDDEN)
#         comment.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
