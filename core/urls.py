from django.urls import path
from core.views.auth_view import LoginView
from core.views.thesaurus_view import ThesaurusView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('thesaurus/', ThesaurusView.as_view(), name='thesaurus'),
]
