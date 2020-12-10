from django import forms
from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _

from blog.post.models import Post
from blog.comment.models import Comment


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content", "author")


class ExtendedPostAdminForm(PostAdminForm):
    is_adding_comment = forms.BooleanField(
        label=_("Do you want to add a comment ?"), required=False
    )
    comment_content = forms.CharField(required=False)

    class Meta(PostAdminForm.Meta):
        fields = PostAdminForm.Meta.fields + ("is_adding_comment", "comment_content")

    def clean_comment_content(self):
        if (
            self.cleaned_data["is_adding_comment"]
            and len(self.cleaned_data["comment_content"]) == 0
        ):
            raise forms.ValidationError(
                _("You checked the input ! Please put a comment")
            )
        return self.cleaned_data["comment_content"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "comments")
    search_fields = ["title__startswith"]
    form = ExtendedPostAdminForm

    def comments(self, obj):
        count = obj.comments.count()
        url = (
            reverse("admin:comment_comment_changelist")
            + "?"
            + urlencode({"post__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Comments</a>', url, count)
        # return obj.comments.count()

    def save_model(self, request, obj, form, change):
        author = obj.author
        obj.save()
        if form.cleaned_data["is_adding_comment"] == True:
            comment_content = form.cleaned_data["comment_content"]
            new_comment = Comment(
                content=comment_content, author=author, post_id=obj.id
            )
            new_comment.save()
