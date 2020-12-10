from rest_framework import serializers
from blog.post.models import Post
from blog.comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    content = serializers.CharField(required=True, min_length=1)
    author = serializers.ReadOnlyField(source="author.username")
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    post_title = serializers.ReadOnlyField(source="post.title")

    class Meta:
        model = Comment
        fields = ["id", "content", "created", "author", "post_title", "post"]
