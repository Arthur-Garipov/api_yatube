from rest_framework import serializers
from posts.models import Group, Post, Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class PostSerialiser(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    post = serializers.SlugRelatedField(read_only=True, slug_field='id')

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')


# from rest_framework import serializers
# from rest_framework.relations import SlugRelatedField, PrimaryKeyRelatedField
# from posts.models import Comment, Post, Group


# class GroupSerializer(serializers.ModelSerializer):
#     author = SlugRelatedField(slug_field='username', read_only=True)
#     group = SlugRelatedField(slug_field='slug', read_only=True)

#     class Meta:
#         model = Group
#         fields = '__all__'


# class PostSerializer(serializers.ModelSerializer):
#     author = SlugRelatedField(slug_field='username', read_only=True)
#     group = serializers.SlugRelatedField(
#         slug_field='slug', queryset=Group.objects.all(), required=False
#     )

#     class Meta:
#         fields = '__all__'
#         model = Post


# class CommentSerializer(serializers.ModelSerializer):
#     author = SlugRelatedField(slug_field='username', read_only=True)
#     post = PrimaryKeyRelatedField(read_only=True)

#     class Meta:
#         fields = '__all__'
#         model = Comment
