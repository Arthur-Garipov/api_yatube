from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet


v1_router = SimpleRouter()
v1_router.register(r'v1/groups', GroupViewSet)
v1_router.register(r'v1/posts', PostViewSet)
v1_router.register(
    r'v1/posts/(?P<post_id>\d+)/comments', CommentViewSet, basename="comments"
)

urlpatterns = [
    path('', include(v1_router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
# from rest_framework import routers
# from django.urls import path, include
# from rest_framework.authtoken import views
# from api.views import PostViewSet, GroupViewSet, CommentViewSet

# v1_router = routers.DefaultRouter()

# v1_router.register(r'posts', PostViewSet)
# v1_router.register(r'groups', GroupViewSet)
# v1_router.register(
#     r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
# )

# urlpatterns = [
#     path('api/v1/api-token-auth/', views.obtain_auth_token),
#     path('v1/', include(v1_router.urls)),
#     path('v1/', include('djoser.urls')),
#     path('v1/', include('djoser.urls.jwt')),
# ]

# from django.urls import path
# from .views import api_comments_id
# from .views import api_comments
# from .views import api_groups_id
# from .views import api_groups
# from .views import api_posts_id
# from .views import api_posts
# from rest_framework.authtoken import views


# urlpatterns = [
#     path('api/v1/api-token-auth/', views.obtain_auth_token),
#     path('api/v1/posts/', api_posts),
#     path('api/v1/posts/<int:pk>/', api_posts_id),
#     path('api/v1/groups/', api_groups),
#     path('api/v1/groups/<int:group_id>/', api_groups_id),
#     path('api/v1/posts/<int:pk>/comments/', api_comments),
#     path('api/v1/posts/<int:pk>/comments/<int:comment_id>/', api_comments_id),
# ]
