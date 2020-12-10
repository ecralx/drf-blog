from django.db import models


class Comment(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        "authentication.CustomUser", related_name="comments", on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        "post.Post", related_name="comments", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["created"]
