from django.contrib import admin
from django.urls import path


from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', views.StudentAPI.as_view()),
    # path('student/', views.student),
]
