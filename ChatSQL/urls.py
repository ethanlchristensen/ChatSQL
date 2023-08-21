from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

from users import views as user_views

urlpatterns = [
    path("", include("chat.urls")),
    path("admin/", admin.site.urls),
    path("chatsql/register/", user_views.register, name="register"),
    path(
        "chatsql/login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "chatsql/logout/",
        auth_views.LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
    path(
        "chatsql/password-reset",
        view=auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"),
        name="password-reset",
    ),
    path(
        "chatsql/password-reset/done",
        view=auth_views.PasswordResetDoneView.as_view(
            template_name="users/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "chatsql/password-reset/complete",
        view=auth_views.PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path(
        "chatsql/password-reset-confirm/<uidb64>/<token>/",
        view=auth_views.PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path("chatsql/profile/", user_views.profile, name="profile")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)