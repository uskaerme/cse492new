from django import forms

from network.models import CustomUser, Student, Lecturer, University, \
    Faculty, Department, Course, Feed, Section, Comment, Academic, Publication, CourseWork

from bootstrap3_datetime.widgets import DateTimePicker


class RegistrationForm(forms.ModelForm):
    # New user registration form

    email = forms.EmailField(widget=forms.widgets.TextInput())
    password1 = forms.CharField(widget=forms.widgets.PasswordInput())
    password2 = forms.CharField(widget=forms.widgets.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match")
        return self.cleaned_data

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class AuthenticationForm(forms.Form):
    # User login form
    email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))

class StudentForm(forms.ModelForm):
    '''
    def __init__(self, *args, **kwargs):
        self.base_fields['university'] = forms.ModelChoiceField()
        self.base_fields['faculty'] = forms.ModelChoiceField()
        self.base_fields['department'] = forms.ModelChoiceField()

        self.base_fields['university'].empty_label = 'Select University'
        self.base_fields['university'].widget.attrs['id'] = 'university-dropdown'

        self.base_fields['faculty'].empty_label = 'Select Faculty'
        self.base_fields['faculty'].widget.attrs['id'] = 'faculty-dropdown'
        self.base_fields['faculty'].widget.attrs['disabled'] = 'true'

        self.base_fields['department'].empty_label = 'Select Department'
        self.base_fields['department'].widget.attrs['id'] = 'department-dropdown'
        self.base_fields['department'].widget.attrs['disabled'] = 'true'

        super(StudentForm(), self).__init__(*args, **kwargs)
    '''
    class Meta:
        model = Student
        fields = ('name', 'surname', 'education')




class UniversityForm(forms.ModelForm):

    class Meta:
        model = University
        exclude = {}


class FacultyForm(forms.ModelForm):

    class Meta:
        model = Faculty
        exclude = {'faculty_slug'}


class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        exclude = {'department_slug'}


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        exclude = {}


class AcademicForm(forms.ModelForm):

    class Meta:
        model = Academic
        exclude = {'user'}

    def __init__(self, *args, **kwargs):
        self.base_fields['degree'].widget.attrs['id'] = 'ac-degree'
        self.base_fields['field'].widget.attrs['id'] = 'ac-field'
        self.base_fields['institution'].widget.attrs['id'] = 'ac-institution'
        self.base_fields['year'].widget.attrs['id'] = 'ac-year'
        super(AcademicForm, self).__init__(*args, **kwargs)


class PublicationForm(forms.ModelForm):

    class Meta:
        model = Publication
        exclude = {}

    def __init__(self, *args, **kwargs):

        self.base_fields['title'].widget.attrs['id'] = 'pb-title'
        self.base_fields['authors'].widget.attrs['id'] = 'pb-authors'
        self.base_fields['year'].widget.attrs['id'] = 'pb-year'
        self.base_fields['reference'].widget.attrs['id'] = 'pb-reference'
        self.base_fields['link'].widget.attrs['id'] = 'pb-link'
        super(PublicationForm, self).__init__(*args, **kwargs)


class LecturerForm(forms.ModelForm):
    '''
    university = forms.ModelChoiceField(University.objects.all(), widget=forms.Select(
        attrs={'id': 'university-dropdown'}), empty_label='Select University')
    faculty = forms.ModelChoiceField(Faculty.objects.all(), widget=forms.Select(
        attrs={'id': 'faculty-dropdown', 'disabled': True}), empty_label='Select Faculty')
    department = forms.ModelChoiceField(University.objects.all(), widget=forms.Select(
        attrs={'id': 'department-dropdown', 'disabled': True}), empty_label='Select Department')
    '''
    class Meta:
        model = Lecturer
        fields = ('name', 'surname', 'academic_rank', 'admin_rank', 'department','website')


class FeedCreateForm(forms.ModelForm):

    class Meta:
        model = Feed
        fields = ['content']
        widgets = {
          'content': forms.Textarea(attrs={'rows': 3, 'cols': 15, 'label':'' ,'placeholder':"Create feed"}),
        }


class SectionForm(forms.ModelForm):

    class Meta:
        model = Section
        fields = ('section_no',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
          'content': forms.Textarea(attrs={'rows': 1, 'cols': 52, 'id': "comment-text", 'placeholder':"Add a comment"}),
        }


class CourseWorkForm(forms.ModelForm):

    deadline = forms.DateTimeField(
        required=False,
        widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm",
                                       "pickSeconds": False}))

    class Meta:
        model = CourseWork
        exclude = ['section', 'coursework_id', 'attachment','comments']
