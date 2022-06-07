""" Profile model """
# Django imports
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    """
    Model profile, extends from User model and add more information to register
    """

    # Only user for record
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    biography = models.CharField(max_length=350,
                                 null=True,
                                 blank=True,
                                 editable=True,
                                )

    picture = models.ImageField(upload_to='uploads/users_profile', null=True, blank=True)
    date_of_birth = models.DateTimeField()
    website = models.URLField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True, editable=True)
    # posts_count = models.IntegerField(blank=True, null=True, editable=True)
    # followers = models.IntegerField(blank=True, null=True, editable=True)
    # following = models.IntegerField(blank=True, null=True, editable=True)
    # Created and modified any from profile
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    # For display string in records from admin
    def __str__(self):
        return '%sf %sf' % (self.user, self.created)
    
    # Validations
    def exist_profile(self, username):
        """return true if the user is in Profile, false if not"""
        if self.objects.filter(user=username).exists():
            return True
        else:
            return False

    # FIX
    # # Validate kw and user for update
    # def validate_pk(self, user, pk):
    #     """ Return true if exist any match """
    #     if self.objects.filter(user=user, id=pk).exists():
    #         return True
    #     else:
    #         return False
    class Meta:
        verbose_name_plural = 'Profiles'

