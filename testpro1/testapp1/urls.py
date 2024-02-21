from django.urls import path
from .views import details_api, stud_view, get_carts

urlpatterns = [
    path('v1/', stud_view),
    path('v1/<int:pk>/', details_api),
    path('carts/', get_carts),
]
