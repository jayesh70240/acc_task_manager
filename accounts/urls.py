from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import ( TokenObtainPairView,TokenRefreshView, TokenVerifyView )
from .views import CustomTokenObtainPairView

urlpatterns = [
    # path('/api/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/login/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/register/', RegisterView.as_view(), name="sign_up"),
]