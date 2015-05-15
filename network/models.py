import os
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.template.defaultfilters import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import RegexValidator
import datetime
from django.utils.timezone import utc
import watson

year_regex = RegexValidator(regex=r'^\d{4}$')


class CustomUser(AbstractBaseUser, PermissionsMixin):
    # Custom user class
    email = models.EmailField(
        verbose_name='email address',
        unique=True,
        max_length=255
    )
    user_id = models.CharField(unique=True, max_length=10, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to='profile_pics', null=True, blank=True)

    is_lecturer = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Academic(models.Model):
    user = models.ForeignKey(CustomUser, null=True, blank=True)
    degree = models.CharField(max_length=10)
    field = models.CharField(max_length=50)
    institution = models.CharField(max_length=50)
    year = models.CharField(validators=[year_regex], max_length=4)


class Publication(models.Model):
    user = models.ForeignKey(CustomUser, null=True, blank=True)
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    year = models.CharField(validators=[year_regex], max_length=4)
    reference = models.CharField(max_length=250)
    link = models.URLField(max_length=100, null=True, blank=True)


class Professional(models.Model):
    user = models.ForeignKey(CustomUser, null=True, blank=True)
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    start = models.CharField(max_length=50)
    end = models.CharField(max_length=50)


class University(models.Model):

    name = models.CharField(max_length=80, unique=True)
    shortname = models.CharField(max_length=15, unique=True, null=True, blank=True)
    university_slug = models.SlugField(unique=True, null=True, blank=True)

    profile_picture = models.ImageField(upload_to='profile_pics', null=True, blank=True)

    website = models.URLField(max_length=50, null=True, blank=True)
    general_info = models.CharField(max_length=1000, null=True, blank=True)
    contact_info = models.CharField(max_length=400, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    established = models.CharField(validators=[year_regex], max_length=4, null=True, blank=True)

    def save(self, *args, **kwargs):

        if self.shortname is None:
            self.university_slug = slugify(self.name)
        else:
            self.university_slug = slugify(self.shortname)
        super(University, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

watson.register(University.objects.all(), fields=("name", "shortname","location"))

class Faculty(models.Model):

    name = models.CharField(max_length=80)
    shortname = models.CharField(max_length=15, null=True, blank=True)
    faculty_slug = models.SlugField(null=True, blank=True)
    website = models.URLField(max_length=50, null=True, blank=True)
    information = models.CharField(max_length=1000, null=True, blank=True)

    university = models.ForeignKey(University)

    class Meta:
        unique_together = (("university", "name"),)

    def save(self, *args, **kwargs):
        if self.shortname is None:
            self.faculty_slug = slugify(self.name.lower())
        else:
            self.faculty_slug = slugify(self.shortname.lower())
        super(Faculty, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Department(models.Model):

    name = models.CharField(max_length=50)
    shortname = models.CharField(max_length=15, null=True, blank=True)
    department_slug = models.SlugField(null=True, blank=True)
    information = models.CharField(max_length=1000, null=True, blank=True)
    website = models.URLField(max_length=50, null=True, blank=True)

    faculty = models.ForeignKey(Faculty)

    class Meta:
        unique_together = (("faculty", "name"),)

    def save(self, *args, **kwargs):
        if self.shortname is None:
            self.department_slug = slugify(self.name.lower())
        else:
            self.department_slug = slugify(self.shortname.lower())
        super(Department, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Course(models.Model):

    code = models.CharField(primary_key=True, max_length=10)
    course_slug = models.SlugField(null=True, blank=True)
    description = models.CharField(max_length=75, null=True, blank=True)
    info = models.CharField(max_length=1000, null=True, blank=True)
    grading = models.CharField(max_length=300, null=True, blank=True)
    semester = models.CharField(max_length=25)
    credits = models.IntegerField(null=True, blank=True)

    department = models.ForeignKey(Department)

    prerequisites = models.ManyToManyField("self", null=True, blank=True)

    def save(self, *args, **kwargs):
        self.course_slug = slugify(self.code.lower())
        super(Course, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.code


class Section(models.Model):

    course = models.ForeignKey(Course)
    section_no = models.CharField(max_length=10)

    class Meta:
        unique_together = (("course", "section_no"),)

    def __unicode__(self):
        return "%s %s" % (self.course, self.section_no)


class LocationTime(models.Model):
    section = models.ForeignKey(Section, null=True, blank=True)
    location = models.CharField(max_length=300)
    time = models.TimeField(blank=True)


class Lecturer(models.Model):

    user = models.OneToOneField(CustomUser, related_name='lecturer')

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    website = models.URLField(max_length=50, null=True, blank=True)

    academic_rank = models.CharField(max_length=50,)
    admin_rank = models.CharField(max_length=50, null=True, blank=True)

    sections = models.ManyToManyField(Section, related_name="lecturer")
    department = models.ForeignKey(Department, null=True, blank=True)

    def __unicode__(self):
        return "%s %s" % (self.name, self.surname)


class Assistant(models.Model):

    user = models.OneToOneField(CustomUser, related_name='assistant')

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    website = models.URLField(max_length=50, null=True, blank=True)

    lecturing_sections = models.ManyToManyField(Section, related_name="assistants")
    attending_sections = models.ManyToManyField(Section, related_name="assistant_students")

    def __unicode__(self):
        return "%s %s" % (self.name, self.surname)


class Student(models.Model):

    EDU_TYPE = (
        ('Yüksek Lisans', 'Yüksek Lisans'),
        ('Lisans', 'Lisans'),
    )

    user = models.OneToOneField(CustomUser, related_name='student')

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    website = models.URLField(max_length=50, null=True, blank=True)

    education = models.CharField(max_length=50, choices=EDU_TYPE, default='Graduate')

    sections = models.ManyToManyField(Section, related_name="students")
    departments = models.ManyToManyField(Department)

    def __unicode__(self):
        return "%s %s" % (self.name, self.surname)


class CommentContainer(models.Model):
    cont_id = models.CharField(unique=True, max_length=10, null=True)


class Comment(models.Model):

    container = models.ForeignKey(CommentContainer, null=True, blank=True)
    content = models.CharField(max_length=280)
    creator = models.ForeignKey(CustomUser, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now=True, blank=True)


class Feed(models.Model):

    creator = models.ForeignKey(Lecturer, null=True, blank=True)
    section = models.ForeignKey(Section, null=True, blank=True)

    container = models.ForeignKey(CommentContainer, null=True, blank=True)

    content = models.CharField(max_length=280)
    creation_date = models.DateTimeField(auto_now=True)
    feed_id = models.CharField(unique=True, max_length=10, null=True)
    attachment = models.FileField(upload_to='attachments', blank=True, null=True)

    def filename(self):
        return os.path.basename(self.attachment.name)

    def __unicode__(self):
        return "%s %s" % (self.section, self.content)





class CourseWork(models.Model):

    SUBMISSION_OPTIONS = (
        ('In class', 'In class'),
        ('Online', 'Online'),
    )

    section = models.ForeignKey(Section, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now=True, null=True)
    coursework_id = models.CharField(unique=True, max_length=10, null=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=75)
    submission_type = models.CharField(max_length=30, choices=SUBMISSION_OPTIONS,
                                       default='Online')
    deadline = models.DateTimeField()
    attachment = models.FileField(upload_to='attachments', blank=True, null=True)

    container = models.ForeignKey(CommentContainer, null=True, blank=True)

    def filename(self):
        return os.path.basename(self.attachment.name)

    def remaining(self):
        default = "şimdi"
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        diff = self.deadline - now

        periods = (
            (diff.days / 365, "yıl", "yıl"),
            (diff.days / 30, "ay", "ay"),
            (diff.days / 7, "hafta", "hafta"),
            (diff.days, "gün", "gün"),
            (diff.seconds / 3600, "saat", "saat"),
            (diff.seconds / 60, "dakika", "dakika"),
            (diff.seconds, "saniye", "saniye"),
        )

        for period, singular, plural in periods:

            if period:
                return "%d %s kaldı" % (period, singular if period == 1 else plural)

        return default


class Submission(models.Model):

    course_work = models.ForeignKey(CourseWork)
    submitted_by = models.ForeignKey(CustomUser)
    sub_id = models.CharField(unique=True, max_length=10, null=True)
    submission_date = models.DateTimeField(auto_now=True, null=True)
    notes = models.CharField(max_length=150, null=True)
    attachment = models.FileField(blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True, validators=[
        MaxValueValidator(100),
        MinValueValidator(0)
    ])