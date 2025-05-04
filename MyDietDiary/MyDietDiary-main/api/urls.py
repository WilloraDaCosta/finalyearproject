from django.urls import path
from .views import get_recommendations, login_user, SignupView, Page1View, Page2View, Page3View, Page4View, Page5View
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('recommendations/', get_recommendations, name='get-recommendations'),
   # path('api/login/', login_user, name='login_user'),
    path('api/login/', obtain_auth_token, name='api_token_auth'),
   # path('api/sleep/', sleep_data, name='sleep_data'),
    path('signup/', SignupView.as_view(), name='signup'),
   # path('userdata/', UserDataView.as_view(), name='userdata'),
    path('page1/', Page1View.as_view(), name='page1'),
    path('api/page2/', Page2View.as_view(), name='page2'),
    path('api/page3/', Page3View.as_view(), name='page3'),
    path('api/page4/', Page4View.as_view(), name='page4'),
    path('api/page5/', Page5View.as_view(), name='page5'),
]
