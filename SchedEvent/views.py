from django.shortcuts import render, redirect
from django.views.generic import View  # Correct import
from django.http import HttpResponse, JsonResponse
from .models import Student, Teacher, StudentDetails, TeacherDetails, TeacherRoom, RoomParticipants, Announcement
from django.contrib import messages
from django.http import JsonResponse

# Debugging import
print("Import successful: django.views.generic.View")

class WelcomeView(View):
    template_name = "welcome_page.html"  # Correct attribute name

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)  # Correct attribute usage

#End of WelcomeView


#Student
class VerifyStud(View):
    template = "verificationStudent.html"

    def get(self, request):
        context = {}
        return render(request, self.template, context)

    def post(self, request):
        id = request.POST.get('id')
        action = request.POST.get('action')

        if action == 'login':
            if Student.objects.filter(id=id).exists():
                return redirect('SchedEvent:StudentMainPage', id=id)  # Pass id in the URL
            else:
                messages.error(request, 'Invalid ID or non-existing')
        elif action == 'create':
            if Student.objects.filter(id=id).exists():
                messages.error(request, 'ID already exists. Please choose a different ID.')
            else:
                # Create a new Student object
                Student.objects.create(id=id)
                return redirect('SchedEvent:StudentMainPage', id=id)  # Pass id in the URL

        return render(request, self.template)

def index(responce):
    return HttpResponse("welcome_page.html")

class Studentdomain(View):
    template = "student_domain.html"

    def get(self, request, id=None):
        context = {'id': id}
        return render(request, self.template, context)

class StudentDetailsView(View):
    template_name = "studentDetails.html"

    def get(self, request, id):
        current_details = self.currInfo(id)

        context = {'id': id, 'current_details': current_details}
        return render(request, self.template_name, context)

    def currInfo(self, student_id):
        student_details = StudentDetails.objects.filter(student_id=student_id).first()
        return student_details

    def post(self, request, id):
        name = request.POST.get('name')
        year_level = request.POST.get('year_level')
        attending_course = request.POST.get('attending_course')

        student_details = StudentDetails.objects.filter(student_id=id).first()
        if student_details:
            student_details.name = name
            student_details.year_level = year_level
            student_details.attending_course = attending_course
            student_details.save()
            message = "Details have been successfully updated."
        else:
            StudentDetails.objects.create(student_id=id, name=name, year_level=year_level, attending_course=attending_course)
            message = "Details have been successfully saved."

        context = {'id': id, 'message': message}
        return render(request, self.template_name, context)

class StudentApplyView(View):
    template_name = "studentApplicationRoom.html"

    def get(self, request, id):
        current_details = self.currInfo(id)
        rooms = TeacherRoom.objects.all()
        context = {'id': id, 'current_details': current_details, 'rooms': rooms}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        room_code = request.POST.get('applicationCode')
        room_name = request.POST.get('applicationName')
        student_id = request.POST.get('id')  # Ensure to get 'id' from POST data, not kwargs

        # Check if the room with the provided name and code exists
        room = TeacherRoom.objects.filter(room_name=room_name, room_code=room_code).first()
        if room:
            # Check if the student has already applied to the room
            if not RoomParticipants.objects.filter(roomnamekey=room_name, list_of_participant=student_id).exists():
                # If not, create a new entry in RoomParticipants
                RoomParticipants.objects.create(roomnamekey=room_name, list_of_participant=student_id)
                message = f"Applied Successfully"
            else:
                message = f"You are already enrolled in this room"
        else:
            message = f"Invalid Room Code"

        return JsonResponse({'message': message})

    def currInfo(self, student_id):
        student_details = StudentDetails.objects.filter(student_id=student_id).first()
        return student_details

class StudentSchedAnnouncement(View):
    template_name = "studentSchedAnnounce.html"

    def get(self, request, id):
            # Fetch rooms where the user is a participant
        rooms = RoomParticipants.objects.filter(list_of_participant=id).values_list('roomnamekey', flat=True)
        context = {'id': id,'rooms': rooms}
        return render(request, self.template_name, context)

    def post(self, request, id):
        room_clicked = request.POST.get('room_clicked')
        announcements = Announcement.objects.filter(publish_room=room_clicked)
        return JsonResponse({'announcements': list(announcements.values())})
#End of Student
#End of Student
#End of Student
#End of Student
#End of Student

#Teacher
class VerifyTeach(View):
    template = "verificationTeacher.html"

    def get(self, request):
        context = {}
        return render(request, self.template, context)

    def post(self, request):
        id = request.POST.get('id')
        action = request.POST.get('action')

        if action == 'login':
            if Teacher.objects.filter(id=id).exists():
                return redirect('SchedEvent:TeacherMainPage', id=id)  # Redirect with id parameter
            else:
                messages.error(request, 'Invalid ID or non-existing')
        elif action == 'create':
            if Teacher.objects.filter(id=id).exists():
                messages.error(request, 'ID already exists. Please choose a different ID.')
            else:
                # Create a new Teacher object
                Teacher.objects.create(id=id)
                return redirect('SchedEvent:TeacherMainPage', id=id)  # Redirect with id parameter

        return render(request, self.template)

class Teacherdomain(View):
    template = "teacher_domain.html"

    def get(self, request, id=None):
        context = {'id': id}
        return render(request, self.template, context)

class Teacherdetails(View):
    template_name = "teacherDetails.html"

    def get(self, request, id):
        current_details = self.currInfo(id)

        context = {'id': id, 'current_details': current_details}
        return render(request, self.template_name, context)

    def currInfo(self, teacher_id):
        teacher_details = TeacherDetails.objects.filter(teacher_id=teacher_id).first()
        return teacher_details

    def post(self, request, id):
        name = request.POST.get('name')
        department = request.POST.get('department')
        course = request.POST.get('course')

        teacher_details = TeacherDetails.objects.filter(teacher_id=id).first()
        if teacher_details:
            teacher_details.name = name
            teacher_details.department = department
            teacher_details.course = course
            teacher_details.save()
            message = "Details have been successfully overwritten."
        else:
            TeacherDetails.objects.create(teacher_id=id, name=name, department=department, course=course)
            message = "Details have been successfully saved."

        context = {'id': id, 'message': message}
        return render(request, self.template_name, context)

class TeacherCreateRoom(View):
    template = "teacherCreationRoom.html"

    def get(self, request, id):
        context = {'id': id}
        return render(request, self.template, context)

    def post(self, request, id):
        room_name = request.POST.get('room_name')
        room_code = request.POST.get('room_code')

        teacher = Teacher.objects.get(id=id)

        # Check if a room with the same name or code already exists for the teacher
        if TeacherRoom.objects.filter(teacher=teacher, room_name=room_name).exists() or \
                TeacherRoom.objects.filter(teacher=teacher, room_code=room_code).exists():
            message = "Try a Different Name and Code"
        elif TeacherRoom.objects.filter(room_name=room_name, room_code=room_code).exists():
            message = "Room Name and Code combination have been taken. Please choose a different one."
        else:
            # Create a new TeacherRoom object
            TeacherRoom.objects.create(teacher=teacher, room_name=room_name, room_code=room_code)
            message = "Room Successfully Created"

        context = {'id': id, 'message': message}
        return render(request, self.template, context)

class TeacherInvRoom(View):
    template = "teacherInventoryRoom.html"

    def get(self, request, id):
        teacher_rooms = TeacherRoom.objects.filter(teacher__id=id)
        participants = RoomParticipants.objects.all()  # Fetch all RoomParticipants
        context = {'id': id, 'teacher_rooms': teacher_rooms, 'participants': participants}
        return render(request, self.template, context)

    def post(self, request, id):
        publisher_id = id
        publish_room = request.GET.get('publish_room', '')  # Assuming room_name is sent from the form
        announcement_context = request.POST.get('announcement', '')
        month_content = request.POST.get('default0', '')
        day_content = request.POST.get('default1', '')
        year_content = request.POST.get('default2', '')

        Announcement.objects.create(
            publisher_id=publisher_id,
            publish_room=publish_room,
            announcement_context=announcement_context,
            month_content=month_content,
            day_content=day_content,
            year_content=year_content
        )

        return HttpResponse("Announcement has been posted and schedule is on the go!")
#End of Teacher
