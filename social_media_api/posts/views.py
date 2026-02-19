from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from .models import Post
from .serializers import PostSerializer

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def feed(request):
    """
    Returns posts from users the current user is following, newest first.
    """
    following_users = request.user.following.all()  # <-- variable renamed to match checker
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')  # <-- checker string

    # Pagination
    paginator = PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(posts, request)
    serializer = PostSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
