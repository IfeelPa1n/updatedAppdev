from django.urls import path
from . import views
from .views import StudentApplyView

print("Import successful: .views")

app_name = 'SchedEvent'

urlpatterns = [
    path("", views.WelcomeView.as_view(), name="welcomepage"),
    path("StudentVerify/", views.VerifyStud.as_view(), name="StudentVerificationStop"),
    path("Studentdomain/<str:id>/", views.Studentdomain.as_view(), name="StudentMainPage"),
    path("Studentdetails/<str:id>/",views.StudentDetailsView.as_view(), name="StudentDetailPage"),
    path("StudentApplyRoom/<str:id>/", views.StudentApplyView.as_view(), name="ApplicationRoomPage"),
    path("StudentAnnounceRoom/<str:id>/", views.StudentSchedAnnouncement.as_view(), name="SchedAnnouncePage"),
    path('apply-room/<str:id>/', StudentApplyView.as_view(), name='apply_room'),

    path("TeacherVerify/", views.VerifyTeach.as_view(), name="TeacherVerificationStop"),
    path("Teacherdomain/<str:id>/", views.Teacherdomain.as_view(), name="TeacherMainPage"),
    path("Teacherdetails/<str:id>/", views.Teacherdetails.as_view(), name="TeacherDetailPage"),
    path("TeacherCreateRoom/<str:id>/", views.TeacherCreateRoom.as_view(), name="TeacherRoomCreatePage"),
    path("TeacherInventory/<str:id>/", views.TeacherInvRoom.as_view(), name="TeacherMyRoomsPage"),
]