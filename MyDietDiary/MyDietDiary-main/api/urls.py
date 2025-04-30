from django.urls import path
from .views import get_recommendations

urlpatterns = [
    path('recommendations/', get_recommendations, name='get-recommendations'),
    path('api/login/', login_user, name='login_user'),
]
