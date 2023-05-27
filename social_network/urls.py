
from django.contrib import admin
from django.urls import path
from accounts.views import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register', RegisterView.as_view())
]
