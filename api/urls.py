from django.urls import path
from .views import UserView, CourseView, AssignmentView, GradeView

urlpatterns = [
    path('api/users/', UserView.as_view(), name='users'),
    path('api/courses/', CourseView.as_view(), name='courses'),
    path('api/assignments/', AssignmentView.as_view(), name='assignments'),
    path('api/grades/', GradeView.as_view(), name='grades'),
     path('api/register/', RegisterView.as_view(), name='register'),
    path('api/submissions/', AssignmentSubmissionView.as_view(), name='submissions'),
]
