from django.urls import path,include


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/',SignupView.as_view(), name = 'signup')
]