from django.urls import path
from . import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='comment API')

urlpatterns = [
    path('', views.comment_list),
    path('<int:pk>/', views.comment_detail),
    path('swagger/', schema_view),
]
