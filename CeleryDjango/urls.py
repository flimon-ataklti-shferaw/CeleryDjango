from django.contrib import admin
from django.urls import path

from demo.views import ReviewEmailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ReviewEmailView.as_view(), name='reviews')
]
