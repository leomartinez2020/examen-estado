from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'preguntas'
urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('preguntas/', views.index, name='index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
