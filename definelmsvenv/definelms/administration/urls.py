from django.urls import path, include
from . import views
from lmsmainapp.views import*


urlpatterns = [

path('login/', views.admin_login, name='login'),
path('logout', views.admin_logout, name='logout'),

path('home/', views.home_page,name="home"),

path('administartion/', views.home, name='administration'),
path('save/', views.save_data, name='save'),
path('delete/', views.delete_data, name='delete'),
path('edit/', views.edit_data, name='edit'),

##############exam#########################
path('exam/', views.home_exam, name='add-examex'),
path('saveex/', views.save_data_exam, name='saveex'),
path('deleteex/', views.delete_data_exam, name='deleteex'),
path('editex/', views.edit_data_exam, name='editex'),

##############course#########################

path('course1/', views.add_course,name='cr'),
# path('savecr/', views.add_course),
path('deletec/', views.delete_data_course, name='deletecr'),
# path('editc/', views.edit_data_course, name='editcr'),


##############subject#########################

path('subjects/', views.add_subject,name='sub'),
# path('savecr/', views.add_course),
path('deletes/', views.delete_data_subject, name='deletesb'),
# path('editc/', views.edit_data_course, name='editcr'),



##############topic#########################
path('topic/', views.add_topic, name='topicc'),
# path('savet/', views.save_data_topic, name='savetp'),
path('deletet/', views.delete_data_topic, name='deletetp'),
# path('editt/', views.edit_data_topic, name='edittp'),



##############subtopic#########################
path('topicsb/', views.add_subtopic, name='topicsub'),
# path('savet/', views.save_data_topic, name='savetp'),
path('deletesb/', views.delete_data_subtopic, name='deletesub'),
# path('editt/', views.edit_data_topic, name='edittp'),



##############questionbank#########################
path('questionbankadd/', views.add_question, name='qbadd'),
# path('savet/', views.save_data_topic, name='savetp'),
path('questionbankdelete/', views.delete_data_question, name='deleteqb'),
# path('editt/', views.edit_data_topic, name='edittp'),

##############exammaster########################
path('em/', views.addexmaster, name='homeem'),
path('deleteem/', views.delete_data_exmaster, name='deleteem'),
path('editst/', views.edit_data_exmaster,name='editst'),

############opations#################
path('op/', views.addoptions, name='op'),
path('deleteop/', views.delete_data_addoptions, name='deleteop'),
path('editop/', views.edit_data_addoptions,name='editop'),

]