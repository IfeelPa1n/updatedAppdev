from django.db import models

# Create your models here.


#Student
class Student(models.Model):
    id = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.id

class Announcement(models.Model):
    publisher_id = models.CharField(max_length=100, default='DEFAULT_VALUE_HERE')
    publish_room = models.CharField(max_length=100)
    announcement_context = models.CharField(max_length=1500)
    month_content = models.CharField(max_length=2, default='01')  # Default value '01'
    day_content = models.CharField(max_length=2, default='01')  # Default value '01'
    year_content = models.CharField(max_length=4, default='2024')  # Default value '2024'

    def __str__(self):
        return f"{self.publisher_id} - {self.publish_room} - {self.announcement_context[:50]}..."

class StudentDetails(models.Model):
    student_id = models.CharField(max_length=100, default='DEFAULT_VALUE_HERE')
    name = models.CharField(max_length=100)
    year_level = models.CharField(max_length=50)
    attending_course = models.CharField(max_length=100)

    def __str__(self):
        return self.student_id
#end of Student

class RoomParticipants(models.Model):
    roomnamekey = models.CharField(max_length=100, default='DEFAULT_VALUE_HERE')
    list_of_participant = models.CharField(max_length=100)

    def __str__(self):
        return self.roomnamekey

#Teacher
class Teacher(models.Model):
    id = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.id

class TeacherRoom(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=100)
    room_code = models.CharField(max_length=50)

    class Meta:
        unique_together = [['teacher', 'room_name'], ['teacher', 'room_code']]

    def __str__(self):
        return self.room_name

class TeacherDetails(models.Model):
    teacher_id = models.CharField(max_length=100, default='DEFAULT_VALUE_HERE')
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.teacher_id
#End of Teacher

