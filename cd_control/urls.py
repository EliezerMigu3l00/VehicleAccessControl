from django.urls import path
from cd_control.views import EntryExitView

urlpatterns = [
    path('entry-exit/', EntryExitView.as_view(), name='entry_exit'),
]