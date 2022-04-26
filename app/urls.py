from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('', views.progress_view, name='index'),
    re_path(r'^celery-progress/', include('celery_progress.urls')),  # the endpoint is configurable
]
