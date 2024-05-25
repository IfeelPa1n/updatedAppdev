from django.contrib import admin
from .models import Student, StudentDetails, Teacher, TeacherDetails, TeacherRoom, RoomParticipants, Announcement
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('id',)

@admin.register(StudentDetails)
class StudentDetailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_level', 'attending_course')
    search_fields = ('name', 'year_level', 'attending_course')

@admin.register(RoomParticipants)
class RoomParticipantsAdmin(admin.ModelAdmin):
    list_display = ('roomnamekey', 'list_of_participant')
    search_fields = ('roomnamekey', 'list_of_participant')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('id',)

@admin.register(TeacherRoom)
class TeacherRoomAdmin(admin.ModelAdmin):
    list_display = ('room_name', 'room_code', 'teacher')
    search_fields = ('room_name', 'room_code', 'teacher__id')

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('publisher_id', 'publish_room',  'announcement_context', 'month_content', 'day_content',
                    'year_content')
    search_fields = ('publisher_id', 'publish_room',  'announcement_context', 'month_content', 'day_content',
                     'year_content')

admin.site.register(TeacherDetails)