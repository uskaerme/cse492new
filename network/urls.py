from django.conf.urls import patterns, url
from network import views

urlpatterns = patterns('',

                       url(r'^login/$', views.login, name='login'),
                       url(r'^logout/$', views.logout, name='logout'),

                       url(r'^home/$', views.index, name='index'),

                       url(r'^test2/$', views.test2, name='index'),

                       url(r'^user/(?P<user_id>[\w\-]+)/$', views.getuser, name='getuser'),
                       url(r'^user/(?P<user_id>[\w\-]+)/newacademic/$', views.user_academic, name='getuser'),
                       url(r'^university/(?P<university_slug>[-\w]+)/$', views.university, name='university'),
                       url(r'^university/(?P<university_slug>[\w\-]+)/faculty/(?P<faculty_slug>[\w\-]+)/$',
                           views.faculty, name='faculty'),
                       url(r'^university/(?P<university_slug>[\w\-]+)/department/(?P<department_slug>[\w\-]+)/$',
                           views.department, name='department'),
                       url(r'^university/(?P<university_slug>[\w\-]+)/course/(?P<course_slug>[\w\-]+)/$',
                           views.course, name='course'),

                       url(r'^university/(?P<university_slug>[\w\-]+)/course/(?P<course_slug>[\w\-]+)/section/(?P<section_no>[\w\-]+)/$',
                           views.section, name='section'),

                       url(r'^test/$', views.test, name='index'),
                       url(r'^submit/$', views.new_feed, name='submit'),
                       url(r'^addcoursework/$', views.new_coursework, name='new cw'),
                       url(r'^getsections/$', views.get_sections, name='get_sections'),
                       url(r'^getfaculties/$', views.get_faculty, name='get_faculty'),
                       url(r'^getdepartments/$', views.get_department, name='get_department'),



                       url(r'^register/lecturer/$', views.lecturer_register, name='lecturer_register'),
                       url(r'^register/student/$', views.student_register, name='student_register'),
                       url(r'^register/university/$', views.university_register, name='university_register'),
                       url(r'^register/faculty/$', views.faculty_register, name='faculty_register'),
                       url(r'^register/department/$', views.department_register, name='department_register'),
                       url(r'^register/course/$', views.course_register, name='course_register'),

                       url(r'^university/(?P<university_slug>[\w\-]+)/course/(?P<course_slug>[\w\-]+)/addsection/$',
                           views.add_section, name='addsection'),
                       url(r'^feed/(?P<feed_id>[\w\-]+)/addcomment/$', views.add_comment, name='addcomment'),
                       )