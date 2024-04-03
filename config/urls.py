from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path("", home_page_view),
    path("<team_name>/", team_details_view),
    path("admin/", admin.site.urls),
]
