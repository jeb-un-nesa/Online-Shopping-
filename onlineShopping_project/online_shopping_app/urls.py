from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # path('', views.detail, name='detail'),
    path('', views.homePage, name='homePage'), #homepage
    path('details/<int:p_id>/', views.productdetail, name='productdetail'), #product details page url
    path('invoice/', views.invoice, name='invoice'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
