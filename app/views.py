from django.shortcuts import render
from .tasks import go_to_sleep


def progress_view(request):
    result = go_to_sleep.delay(1)
    return render(request, 'index.html', context={'task_id': result.task_id})
