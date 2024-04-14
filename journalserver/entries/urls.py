from django.urls import path
from . import views

urlpatterns = [
    path('questions/', views.questions, name='questions'),
    path('user-entries/<str:username>/', views.allUserEntries, name='all_user_entries'),

]