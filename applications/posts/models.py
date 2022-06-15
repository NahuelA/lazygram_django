""" Posts model """
# Django imports
from django.db import models
from applications.users.models import Profile
# Create your models here.

# Posts for the user
class Posts(models.Model):

    # Model profile from users app
    profile_name = models.ForeignKey(
                                Profile,
                                on_delete=models.DO_NOTHING,
                                null=True,
                            )

    description = models.CharField(
                                   max_length=250,
                                   blank=True,
                                   null=True,
                                   db_index=True,
                                )

    created = models.DateTimeField(
                                   auto_now_add=True,
                                   editable=False,
                                   auto_created=True,
                                   db_index=True,
                                )

    last_modified = models.DateTimeField(
                                         auto_now=True,
                                         editable=False,
                                         db_index=True,
                                        )

    post_image = models.ImageField(
                                upload_to='uploads/pictures_posted',
                                null=True,
                            )

    def __str__(self):
        return '%sf %sf' % (self.profile, self.created)

    class Meta:

        verbose_name_plural = 'Posts'
        # Return first name and last name in string format
        
