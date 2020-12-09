from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255, null=False, default="Title")
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        "authentication.CustomUser", related_name="posts", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["created"]
