from django.urls import include, path 

urlpatterns = [
    path('', include('get_info.urls')),
]