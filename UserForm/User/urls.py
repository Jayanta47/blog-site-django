from django.urls import path
from User import views as v
app_name = 'user'

urlpatterns = [
    path('test_index/', v.test_index, name='test'),
    path('register/', v.register, name='register'),
    path('profile/', v.profile, name='profile')
]
