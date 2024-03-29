""" Create posts view. """

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


# Models
from lazygram.applications.posts.models import Posts
from lazygram.applications.users.models import FollowingModel

# Settings
from config.settings.base import REST_FRAMEWORK

# Serializer
from lazygram.applications.posts.serializers import PostsSerializer
from lazygram.applications.users.models import Profile


class PostsView(ModelViewSet):
    """
    A viewset that provides default 'list()', 'create()', 'update()'
    and 'destroy()' actions for the 'Posts' model.
    """

    queryset = Posts.objects.all()
    followed_queryset = FollowingModel.objects.all()
    http_method_names = ["get", "post", "put", "patch", "delete", "head", "options"]
    serializer_class = PostsSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer, **kwargs):
        serializer.save(profile=kwargs["profile"])

    def perform_update(self, serializer):
        serializer.save()

    def list(self, request, *args, **kwargs):
        """
        List posts only from followed profiles.
        """

        profile = Profile.manager_object.get(user=request.user)
        followed = self.followed_queryset.filter(profile=profile)
        queryset = self.queryset.filter(profile_id__in=followed[0].following.all())

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):

        # Getting instances and delete usernames in string type.
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Getting profile
        profile = Profile.manager_object.get(user__username=request.user)
        self.perform_create(
            serializer, profile=profile
        )  # Send profile as a kwarg and save post

        # Headers
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def update(self, request, *args, **kwargs):

        partial = kwargs.pop("partial", True)
        instance = self.get_object()

        # Getting authenticated user.
        profile = Profile.manager_object.get(user__username=request.user)
        profile_likedit = {"profile_likedit": [profile.id]}
        serializer = self.get_serializer(
            instance, data=profile_likedit, partial=partial
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        """
        Remove a post instance and discount -1 from `posts_count` field from profile
        instance asociated with the instance deleted.
        """

        instance = self.get_object()
        # Remove -1 post
        instance.profile.posts_count -= 1
        instance.profile.save()

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProfilePost(APIView):
    """
    List all profile posts of a user.
    """

    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ["get", "post", "put", "patch", "head", "options"]
    pagination_class = REST_FRAMEWORK.get("DEFAULT_PAGINATION_CLASS")
    _paginator = None

    @property
    def paginator(self):
        """
        The paginator instance associated with the view, or `None`.
        """

        if not hasattr(self, "_paginator"):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self, queryset):
        """
        Return a single page of results, or `None` if pagination is disabled.
        """
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        """
        Return a paginated style `Response` object for the given output data.
        """
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)

    def get_serializer_class(self):
        """
        Return the class to use for the serializer.
        Defaults to using `self.serializer_class`.
        You may want to override this if you need to provide different
        serializations depending on the incoming request.
        (Eg. admins get full serialization, others get basic serialization)
        """
        assert self.serializer_class is not None, (
            "'%s' should either include a `serializer_class` attribute, "
            "or override the `get_serializer_class()` method." % self.__class__.__name__
        )

        return self.serializer_class

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {"request": self.request, "format": self.format_kwarg, "view": self}

    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = self.get_serializer_class()
        kwargs.setdefault("context", self.get_serializer_context())
        return serializer_class(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if kwargs is not None:
            queryset = self.queryset.filter(
                profile__user__username=kwargs.get("profile")
            )
            page = self.paginate_queryset(queryset)

            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data="Not found", status=status.HTTP_404_NOT_FOUND)
