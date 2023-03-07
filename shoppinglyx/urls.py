from django.contrib import admin
from django.urls import path, include
admin.site.site_header = "MINOR PROJECT"
admin.site.site_title = "Minor Projct Portal"
admin.site.index_title = "Welcome to Minor Project Developer"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]
