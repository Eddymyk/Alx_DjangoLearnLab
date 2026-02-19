from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from .models import Post, Like
from .serializers import PostSerializer
from notifications.models import Notification


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def feed(request):
    following_users = request.user.following.all()
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

    paginator = PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(posts, request)
    serializer = PostSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)  

    like, created = Like.objects.get_or_create(user=request.user, post=post) 
    if not created:
        return Response({'detail': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

    if post.author != request.user:
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked',
            target=post
        )

    return Response({'detail': 'Post liked.'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk) 
    try:
        like = Like.objects.get(user=request.user, post=post) 
    except Like.DoesNotExist:
        return Response({'detail': 'Like not found.'}, status=status.HTTP_404_NOT_FOUND)

    like.delete()
    return Response({'detail': 'Post unliked.'}, status=status.HTTP_200_OK)
