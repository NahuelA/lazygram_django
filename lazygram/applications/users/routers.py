""" Urls from users app. """

from django.urls import path, include

# Token blacklist
from rest_framework_simplejwt.views import TokenBlacklistView

# User views
from lazygram.applications.users.api_views import (
    UserView,
    LogoutView,
    TokenRefreshView,
    TokenObtainPairView,
    TokenValidationRegister,
    ProfileView,
    ProfilesSearchView,
    FollowingView,
    FollowersView,
    IsFollowedView,
    ForgotPassword,
    ValidateSetPassword,
    SetNewPassword,
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(prefix=r"profiles", viewset=ProfileView, basename="profiles")

router.register(prefix=r"users", viewset=UserView, basename="users")

router.register(prefix=r"followers", viewset=FollowersView, basename="followers")

router.register(prefix=r"followings", viewset=FollowingView, basename="followings")


# Crud
urlpatterns = [
    # Add all routers
    path("", include(router.urls)),
]

# Utils
urlpatterns += [
    # Logout
    path(
        route="logout/",
        view=LogoutView.as_view(),
        name="logout",
    ),
    # Refresh token
    path(
        route="refresh-token/",
        view=TokenRefreshView.as_view(),
        name="refresh-token",
    ),
    # Obtain tokens
    path(
        route="login/",
        view=TokenObtainPairView.as_view(),
        name="token",
    ),
    # Validation register token
    path(
        route="validation-register-token/",
        view=TokenValidationRegister.as_view(),
        name="token",
    ),
    # Token blacklist
    path(
        route="blacklist/",
        view=TokenBlacklistView.as_view(),
        name="token_blacklist",
    ),
    # Isfollowed
    path(
        route="isfollowed/<str:profile>",
        view=IsFollowedView.as_view(),
        name="isfollowed",
    ),
    # Search profile
    path(
        route="profiles/search/<str:search_profiles>",
        view=ProfilesSearchView.as_view(),
        name="search_profile",
    ),
    # Forgot password
    path(
        route="forgot-password",
        view=ForgotPassword.as_view(),
        name="forgot_password",
    ),
    # Validate access token to change password
    path(
        route="forgot-password-validation",
        view=ValidateSetPassword.as_view(),
        name="forgot_password_validation",
    ),
    # Set new password
    path(
        route="set-new-password",
        view=SetNewPassword.as_view(),
        name="set_new_password",
    ),
]
