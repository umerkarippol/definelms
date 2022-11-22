from django.urls import path
from lmsmainapp import views as api_views
from rest_framework.authtoken import views
from lmsmainapp import views

urlpatterns = [

    path('login1/', api_views.loginView.as_view(), name="login1"),
    path('login1/<id>', api_views.topicView.as_view(), name="login_put_dlt"),

    path('registration/', api_views.registrationView.as_view(), name="registration"),
    path('registration/<id>', api_views.registrationView.as_view(), name="registration_put_dlt"),

    path('exam/', api_views.examView.as_view(), name="exam"),
    path('exam/<id>', api_views.examView.as_view(), name="exam_put_dlt"),

    path('course/', api_views.courseView.as_view(), name="course"),
    path('course/<id>', api_views.courseView.as_view(), name="course_put_dlt"),
    path('addcourse/', views.addcourse),
 
    path('subject/', api_views.subjectView.as_view(), name="subject"),
    path('subject/<id>', api_views.subjectView.as_view(), name="subject_put_dlt"),
    path('addsubject/', views.addsubject),

    path('topic/', api_views.topicView.as_view(), name="topic"),
    path('topic/<id>', api_views.topicView.as_view(), name="topic_put_dlt"),
    path('topicfilter/<id>', api_views.ParticularTopic.as_view(), name="particular_topic"),

    path('subtopic/', api_views.subtopicView.as_view(), name="subtopic"),
    path('subtopic/<id>', api_views.subtopicView.as_view(), name="subtopic_put_dlt"),
    
    path('exammaster/', api_views.exammasterView.as_view(), name="exam_master"),
    path('exammaster/<id>', api_views.exammasterView.as_view(), name="exam_master_put_dlt"),

    path('masterview/', api_views.masterView.as_view(), name="master_view"),

    path('eqallocation/', api_views.examQuestionAllocationView.as_view(), name="exam_question_allocation"),
    path('eqallocation/<id>', api_views.examQuestionAllocationView.as_view(), name="exam_question_allocation_put_dlt"),

    path('questionbank/', api_views.question_bankView.as_view(), name="question_bank"),
    path('questionbank/<id>', api_views.question_bankView.as_view(), name="question_bank_put_dlt"),
    path('questionview/', api_views.questionView.as_view(), name="question_bank"),

    path('questionoption/', api_views.questionbankoptionsview.as_view(), name="question"),
    path('questionoption/<id>', api_views.questionbankoptionsview.as_view(), name="exam_put_dlt"),
    
    
    path('mcq/', api_views.mcqView.as_view(), name="subtopic"),
    path('mcq/<id>', api_views.GetQuestions.as_view(), name="subtopic"),


  
    
    # path('home/', views.home_page,name="home"),

   
    ######course#############

   
    
]