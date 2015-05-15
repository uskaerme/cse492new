import uuid
import json
from network.forms import RegistrationForm, AuthenticationForm,  StudentForm, \
    UniversityForm, FacultyForm, DepartmentForm, CourseForm, FeedCreateForm, \
    LecturerForm, SectionForm, CommentForm, AcademicForm, PublicationForm, CourseWorkForm

from network.models import Lecturer, CustomUser, Student, Course, Section, \
    Feed, University, Faculty, Department, CourseWork, Academic, Publication, Professional
from django.shortcuts import redirect, render_to_response, render
from django.contrib.auth import login as django_login, logout as django_logout, authenticate
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from easy_thumbnails.files import get_thumbnailer


def generate_random():
    random = str(uuid.uuid4())
    random = random.lower()
    random = random.replace("-", "")
    return random[0:10]


def user_academic(request, user_id):

    user = CustomUser.objects.get(user_id=user_id)

    if request.method == 'POST':
        u_form = AcademicForm(request.POST)
        if u_form.is_valid():
            uni = u_form.save()
            uni.user = user
            uni.save()
            c = "/network/user/"+user_id+"/"
            return redirect(c)
        else:
            print(u_form.errors)
    else:
        u_form = AcademicForm()


def test2(request):
    context_dict = {}
    if request.user.is_lecturer:
        lecturer = Lecturer.objects.get(user=request.user)

        feed = Feed.objects.filter(section=Lecturer.objects.get(user=request.user).sections.all()).order_by('-creation_date')
        #c_work = CourseWork.objects.filter(section=Lecturer.objects.get(user=request.user).sections.all())

        course_list = []
        for section in lecturer.sections.all():
            if section.course not in course_list:
                course_list.append(section.course)
        context_dict['course_list'] = course_list
        context_dict['comment_form'] = CommentForm()
        context_dict['feed_form'] = FeedCreateForm()
        context_dict['feed'] = feed

    return render_to_response('network/main4.html', context_dict,
                              context_instance=RequestContext(request))
    #return render(request, 'network/main4.html')




def test(request):
    context_dict = {}
    lecturer = Lecturer.objects.get(user=request.user)
    course_list = []
    for section in lecturer.sections.all():
        if section.course not in course_list:
            course_list.append(section.course)

    coursework = CourseWork.objects.filter(section=Lecturer.objects.get(user=request.user).sections.all())
    context_dict['comment_form'] = CommentForm()
    context_dict['course_list'] = course_list
    context_dict['coursework'] = coursework
    context_dict['form'] = CourseWorkForm()
    return render_to_response('network/main3.html', context_dict,
                              context_instance=RequestContext(request))


def index(request):
    context_dict = {}
    if request.user.is_authenticated():
        if request.user.is_lecturer:
            lecturer = Lecturer.objects.get(user=request.user)

            feed = Feed.objects.filter(section=Lecturer.objects.get(user=request.user).sections.all()).order_by('-creation_date')
            #c_work = CourseWork.objects.filter(section=Lecturer.objects.get(user=request.user).sections.all())

            course_list = []
            for section in lecturer.sections.all():
                if section.course not in course_list:
                    course_list.append(section.course)
            context_dict['course_list'] = course_list
            context_dict['comment_form'] = CommentForm()
            context_dict['feed_form'] = FeedCreateForm()
            context_dict['feed'] = feed
    else:
        pass

    return render_to_response('network/main2.html', context_dict,
                              context_instance=RequestContext(request))


def university(request, university_slug):
    context_dict = {}
    try:
        university = University.objects.get(university_slug=university_slug)
        context_dict['university'] = university
        context_dict['p_pic'] = get_thumbnailer(university.profile_picture)['avatar-lg'].url

        faculties = Faculty.objects.filter(university=university)
        context_dict['faculties'] = faculties
        context_dict['faculty_count'] = faculties.count()

        student_list = []

        for f in faculties:
            departments = f.department_set.all()
            for d in departments:
                students = d.student_set.all()
                for student in students:
                    if student not in student_list:
                        student_list.append(student)

        context_dict['student_count'] = len(student_list)
    except University.DoesNotExist:
        pass

    return render_to_response('network/university.html',  context_dict, context_instance=RequestContext(request))


def faculty(request, university_slug, faculty_slug):
    context_dict = {}
    try:
        university = University.objects.get(university_slug=university_slug)
        context_dict['university'] = university

        faculty = Faculty.objects.get(faculty_slug=faculty_slug, university=university)

        student_count = faculty.student_set.count()
        context_dict['student_count'] = student_count

        departments = Department.objects.filter(faculty=faculty)
        context_dict['departments'] = departments
        context_dict['department_count'] = departments.count()

    except university.DoesNotExist:
        pass

    return render_to_response('network/faculty.html',  context_dict, context_instance=RequestContext(request))


def department(request, university_slug, department_slug):
    context_dict = {}
    try:
        university = University.objects.get(university_slug=university_slug)
        context_dict['university'] = university

        department = Department.objects.get(department_slug=department_slug, university=university)

        student_count = department.student_set.count()
        context_dict['student_count'] = student_count

        lecturers = department.lecturer_set.all()
        context_dict['lecturers'] = lecturers
        courses = department.course_set.all()
        context_dict['courses'] = courses

    except university.DoesNotExist:
        pass

    return render_to_response('network/department.html.html',  context_dict, context_instance=RequestContext(request))


def course(request, university_slug, course_slug):
    pass


def section(request, university_slug, course_slug):
    pass


def getuser(request, user_id):
    context_dict = {}
    try:
        user = CustomUser.objects.get(user_id=user_id)
        context_dict['user'] = user
        context_dict['p_pic'] = get_thumbnailer(user.profile_picture)['avatar-lg'].url
        context_dict['user_id']= user_id
        if user.is_student:
            student = user.student
            context_dict['is_lecturer'] = False
            context_dict['name'] = student.name
            context_dict['surname'] = student.surname
            context_dict['university'] = student.university.__unicode__()
            context_dict['department'] = student.department.__unicode__()
            context_dict['education'] = student.education
            context_dict['website'] = student.website

        if user.is_lecturer:
            lecturer = user.lecturer
            context_dict['lecturer'] = lecturer
            context_dict['academicform'] = AcademicForm()
            context_dict['publicationform'] = PublicationForm()

            student_list = []
            for section in lecturer.sections.all():
                students = section.student_set.all()
                for student in students:
                    if student not in student_list:
                        student_list.append(student)


            course_list = []
            for section in lecturer.sections.all():
                if section.course not in course_list:
                    course_list.append(section.course)

            context_dict['s_no'] = len(student_list)
            context_dict['c_no'] = len(course_list)
            context_dict['teaching'] = course_list



            context_dict['academic'] = Academic.objects.filter(user=user)
            context_dict['publication'] = Publication.objects.filter(user=user)
            context_dict['pro'] = Professional.objects.filter(user=user)

            if lecturer.admin_rank is not None:
                context_dict['admin'] = lecturer.admin_rank
            else:
                context_dict['admin'] = ""

    except CustomUser.DoesNotExist:
        pass

    return render_to_response('network/user.html', context_dict, context_instance=RequestContext(request))

def login(request):

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(email=request.POST['email'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    return redirect('/network/home/')
            else:
                return HttpResponse("User is none")
        else:
            return HttpResponse("form is not valid")

    else:
        form = AuthenticationForm(auto_id=False)

    return render_to_response('network/login.html', {
        'form': form,
    }, context_instance=RequestContext(request))


@login_required
def logout(request):

    django_logout(request)
    return redirect('/network/home/')


def student_register(request):

    if request.method == 'POST':
        user_form = RegistrationForm(data=request.POST)
        student_form = StudentForm(request.POST, request.FILES)
        if user_form.is_valid() and student_form.is_valid():

            user = user_form.save()
            user.user_id = generate_random()
            user.is_student = True
            user.save()

            student = student_form.save(commit=False)
            student.user = user
            student.save()

            return redirect('/network/home/')
        else:
            print(student_form.errors, user_form.errors)
    else:
        user_form = RegistrationForm()
        student_form = StudentForm()

    return render_to_response('network/studentregister.html', {
        'user_form': user_form, 'student_form': student_form,
    }, context_instance=RequestContext(request))




def university_register(request):
    if request.method == 'POST':
        u_form = UniversityForm(request.POST, request.FILES)
        if u_form.is_valid():
            uni = u_form.save()
            uni.save()
        else:
            print(u_form.errors)
    else:
        u_form = UniversityForm()

    return render_to_response('network/createuniversity.html', {
        'u_form': u_form,
    }, context_instance=RequestContext(request))


def faculty_register(request):
    if request.method == 'POST':
        f_form = FacultyForm(request.POST)
        if f_form.is_valid():
            fac = f_form.save()
            fac.save()
        else:
            print(f_form.errors)
    else:
        f_form = FacultyForm()

    return render_to_response('network/createfaculty.html', {
        'f_form': f_form,
    }, context_instance=RequestContext(request))


def department_register(request):
    if request.method == 'POST':
        d_form = DepartmentForm(request.POST)
        if d_form.is_valid():
            dep = d_form.save()
            dep.save()
        else:
            print(d_form.errors)
    else:
        d_form = DepartmentForm()

    return render_to_response('network/createdepartment.html', {
        'd_form': d_form,
    }, context_instance=RequestContext(request))


def course_register(request):
    if request.method == 'POST':
        c_form = CourseForm(request.POST)
        if c_form.is_valid():
            cor = c_form.save()
            cor.save()
        else:
            print(c_form.errors)
    else:
        c_form = CourseForm()

    return render_to_response('network/createcourse.html', {
        'c_form': c_form,
    }, context_instance=RequestContext(request))


def lecturer_register(request):

    if request.method == 'POST':
        user_form = RegistrationForm(data=request.POST)
        lecturer_form = LecturerForm(request.POST, request.FILES)
        if user_form.is_valid() and lecturer_form.is_valid():
            user = user_form.save()
            user.user_id = generate_random()
            user.is_lecturer = True
            if request.FILES.get('p_pic'):
                user.profile_picture = request.FILES['p_pic']
            user.save()

            lecturer = lecturer_form.save(commit=False)
            lecturer.user = user
            lecturer.save()


            return redirect('/network/home/')
        else:
            print(lecturer_form.errors, user_form.errors)
    else:
        user_form = RegistrationForm()
        lecturer_form = LecturerForm()

    return render_to_response('network/lecturerregister.html', {
        'user_form': user_form, 'lecturer_form': lecturer_form,
    }, context_instance=RequestContext(request))




# --------------------------------- Views for jQuery use ---------------------------------


def get_faculty(request):
    context = RequestContext(request)
    uni = None
    if request.method == 'GET':
        uni = request.GET['university']

    if uni:
        university = University.objects.get(id=uni)
        faculties = Faculty.objects.filter(university=university)
        out = []
        out.append("<option value=none>Faculty</option>")
        for f in faculties:
            out.append("<option value=%s>%s</option>" % (f.id, f.name))

    return HttpResponse(out)


def get_department(request):
    context = RequestContext(request)

    fac = None

    if request.method == 'GET':
        fac = request.GET['faculty']

    if fac:
        fclty = Faculty.objects.get(id=fac)
        print " faculty in get_dep"
        print fclty
        departments = Department.objects.filter(faculty=fclty)

        out = []
        out.append("<option value=none>Department</option>")
        for d in departments:
            print d
            out.append("<option value=%s>%s</option>" % (d.id, d.name))

    return HttpResponse(out)


def get_sections(request):
    context = RequestContext(request)
    course = None
    if request.method == 'GET':
        course = request.GET['course']

    if course:
        lecturer = Lecturer.objects.get(user=request.user)
        sections = lecturer.sections.filter(course=course)

        out = []
        if sections.count() > 1:
            out.append("<option value=All>All</option>")
        for s in sections:
            out.append("<option value=%s>%s</option>" % (s.section_no, s.section_no))
    return HttpResponse(out)


def add_section(request, university_slug, course_slug):

    try:
        u = University.objects.get(university_slug=university_slug)
    except University.DoesNotExist:
        u = None

    try:
        c = Course.objects.get(course_slug=course_slug)
    except Course.DoesNotExist:
        c = None

    if request.method == 'POST':
        if request.user.is_lecturer:
            form = SectionForm(request.POST)
            if form.is_valid():
                if c and u:
                    section = form.save(commit=False)
                    section.course = c
                    section.save()
                    try:
                        request.user.lecturer.courses.add(c)
                        request.user.lecturer.sections.add(section)
                    except ObjectDoesNotExist:
                        pass
            else:
                print(form.errors)
    else:
        form = SectionForm()

    context_dict = {'form': form, 'u_slug': university_slug, 'c_id': c.code}

    return render_to_response('network/add_section.html', context_dict, context_instance=RequestContext(request))


def new_feed(request):
    context = RequestContext(request)
    lec = Lecturer.objects.get(user=request.user)
    if request.method == 'POST':
        feed_form = FeedCreateForm(request.POST, request.FILES)
        if feed_form.is_valid():
            c = Course.objects.get(code=request.POST.get('course-list'))
            s = Section.objects.get(course=c, section_no=request.POST.get('sections-list'))

            feed = feed_form.save()
            feed.creator = Lecturer.objects.get(user=request.user)
            feed.course = c
            feed.section = s
            feed.feed_id = generate_random()

            if request.FILES.get('attachment') is not None:
                feed.attachment = request.FILES['attachment']

            feed.save()
        else:
            print(feed_form.errors)
    return redirect('/network/home/')


def new_coursework(request):
    context = RequestContext(request)

    if request.method == 'POST':
        c_form = CourseWorkForm(request.POST, request.FILES)

        if c_form.is_valid():
            c = Course.objects.get(code=request.POST.get('course-list'))
            s = Section.objects.get(course=c, section_no=request.POST.get('sections-list'))

            cw = c_form.save()
            cw.section = s
            cw.coursework_id = generate_random()

            if request.FILES.get('attachment') is not None:
                cw.attachment = request.FILES['attachment']

            cw.save()
        else:
            print(c_form.errors)
    return redirect('/network/home/')


def add_comment(request, feed_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.creator = request.user
            comment.save()
            f = Feed.objects.get(feed_id=feed_id)
            f.comments.add(comment)
            return redirect('/network/home/')
        else:
            print(form.errors)

    return redirect('/network/home/')