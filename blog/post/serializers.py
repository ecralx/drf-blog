from rest_framework import serializers
from blog.post.models import Post


class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True, min_length=1)
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Post
        fields = ["id", "title", "content", "created", "author"]
