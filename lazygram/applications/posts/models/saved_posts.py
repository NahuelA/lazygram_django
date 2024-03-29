""" Post saves model. """

# Django
from django.db import models

# Local
from lazygram.applications.posts.models import Posts
from lazygram.applications.users.models import Profile


class SavedPosts(models.Model):
    """Saved posts model."""

    profile = models.ForeignKey(
        to=Profile,
        on_delete=models.DO_NOTHING,
        verbose_name="Profile ID",
        related_name="profile_id",
        null=True,
    )

    saved_post = models.ManyToManyField(
        to=Posts,
        null=True,
        verbose_name="Saved post",
        related_name="saved_posts",
    )

    # Validations
    def validate_post_exist(self, postid):
        """If post exist, return true, else false"""
        return Posts.objects.filter(id=postid).exists()
