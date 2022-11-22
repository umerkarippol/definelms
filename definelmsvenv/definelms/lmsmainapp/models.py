from email.policy import default
from logging.config import IDENTIFIER
from secrets import choice
from unittest.util import _MAX_LENGTH
from django.db import models
from django.db.models.fields import CharField, TextField

class login(models.Model):
    id       = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role     = models.IntegerField(null=True)

    class Meta:
        db_table = 'login'

class registration(models.Model):
    
    name       = models.CharField(max_length=50,default="",null=True)
    address    = models.CharField(max_length=500,default="",null=True)
    mobile     = models.CharField(max_length=10,default="",null=True)
    email      = models.EmailField(max_length=254,default="",null=True)
    username   = models.CharField(max_length=50,primary_key=True)
    token      = models.CharField( max_length=50,null=True,default="")
    image      = models.ImageField(upload_to='register',null=True,default="")

    class Meta:
        db_table='registration'

class exam(models.Model):
    id          = models.AutoField(primary_key=True)
    exam_name   = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    remarks     = models.CharField(max_length=500)

    class Meta:
        db_table = 'exam'

class course(models.Model):
    id          = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=20,default="")
    description = models.CharField(max_length=100,default="")
    amount      = models.IntegerField(default=0)
    duration    = models.CharField(max_length=10,default="")
    exam        = models.ForeignKey(exam,on_delete=models.CASCADE)
    image       = models.ImageField(upload_to='course')
    user        = models.ForeignKey(login,on_delete=models.CASCADE)

    class Meta:
        db_table='course'

class subject(models.Model):
    id           = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=50,default="")
    description  = models.CharField(max_length=2000,default="")
    image        = models.ImageField(max_length=150,default="")
    user         = models.ForeignKey(login,on_delete=models.CASCADE)

    class Meta:
        db_table='subject'

class course_subject_allocation(models.Model):
    id           = models.AutoField(primary_key=True)
    course    = models.ForeignKey(course,on_delete=models.CASCADE)
    subject   = models.ForeignKey(subject,on_delete=models.CASCADE)

    class Meta:
        db_table='course_subject_allocation'


class topic(models.Model):
    id           = models.AutoField(primary_key=True)
    topic_name   = models.CharField(max_length=100,default="")
    description  = models.CharField(max_length=2000,default="")
    subject      = models.ForeignKey(subject,on_delete=models.CASCADE)
    user         = models.ForeignKey(login,on_delete=models.CASCADE)

    class Meta:
        db_table='topic'

class topic_course_allocation(models.Model):
    id          = models.AutoField(primary_key=True)
    course      = models.ForeignKey(course,on_delete=models.CASCADE)
    subject     = models.ForeignKey(subject,on_delete=models.CASCADE)
    topic       = models.ForeignKey(topic,on_delete=models.CASCADE)
    class Meta:
        db_table='topic_course_allocation'


# subtopic details
class Subtopics(models.Model):
    id          = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    topic       = models.ForeignKey(topic, on_delete=models.CASCADE)
    

    class Meta:
        db_table = 'Subtopics'


# class course_info(models.Model):
#     id          = models.AutoField(primary_key=True)
#     course      = models.CharField(max_length=100)
#     subject     = models.CharField(max_length=100)
#     topic       = models.CharField(max_length=100)
#     course_type = models.BooleanField(default=True)
#     description = models.CharField(max_length=2000,default="")
#     image       = models.ImageField(upload_to='course_info',null=True)
#     user        = models.ForeignKey(login,on_delete=models.CASCADE)

#     class Meta:
#         db_table='course_info'


class course_registration(models.Model):
    id            = models.AutoField(primary_key=True)
    course        = models.ForeignKey(course,on_delete=models.CASCADE)
    register      = models.ForeignKey(registration,on_delete=models.CASCADE)
    date          = models.DateField(auto_now_add=True)
    membership    = models.BooleanField(default=True)
    paid_reg_date = models.DateField(auto_now_add=True) 
    end_reg_date  = models.DateField()
    user          = models.ForeignKey(login,on_delete=models.CASCADE)
    is_paid       = models.BooleanField(default=False)

    class Meta:
        db_table='course_registration'



class notification(models.Model):
    id          = models.AutoField(primary_key=True)
    course      = models.ForeignKey(course,on_delete=models.CASCADE)
    message     = models.CharField(max_length=1000,default="")
    expiry_date = models.DateField()
    date        = models.DateField(auto_now_add=True)
    remarks     = models.CharField(max_length=50,default="")

    class Meta:
        db_table='notification'


class payment(models.Model):
    id              = models.AutoField(primary_key=True)
    invoice         = models.IntegerField()
    course          = models.CharField(max_length=50)
    date            = models.DateField()
    registration    = models.ForeignKey(registration,on_delete=models.CASCADE)
    amount          = models.IntegerField(default=0)
    tax             = models.IntegerField()
    payment_details = models.CharField(max_length=500)
    user            = models.ForeignKey(login,on_delete=models.CASCADE)

    class Meta:
        db_table='payment'


class question_bank(models.Model):
    id              = models.AutoField(primary_key=True)
    question        = models.CharField(max_length=5000,default="",null=False)
    subject         = models.ForeignKey(subject,on_delete=models.CASCADE)
    topic           = models.ForeignKey(topic,on_delete=models.CASCADE)
    subtopic        = models.ForeignKey(Subtopics, on_delete=models.CASCADE)
    no_of_options   = models.IntegerField(default=0,null=False)
    tags            = models.CharField(max_length=1000)
    is_explanation  = models.BooleanField(default=False)
    is_image        = models.BooleanField(default=False)
    explanation     = models.CharField(max_length=1000,default="")
    difficulty_level= models.CharField(max_length=50,default="")
    created_date    = models.DateField(auto_now_add=True)
    last_updated_date= models.DateField(auto_now=True)
    user            = models.ForeignKey(login,on_delete=models.CASCADE)
    status          = models.CharField(max_length=50,default="")
    remark          = models.CharField(max_length=50,default="")
    is_reported     = models.BooleanField(default=False)
    report_reason   = models.CharField(max_length=1000,default="")
    correct_answer  = models.CharField(max_length=1,null=False)
    option          = models.CharField(max_length=5000,default="")

    class Meta:
        db_table='question_bank'

class question_bank_options(models.Model):
    id               = models.AutoField(primary_key=True)
    question         = models.ForeignKey(question_bank,related_name='options',on_delete=models.CASCADE)
    choice           = models.CharField(max_length=1500,null=False)
    identifier       = models.CharField(max_length=1,null=False)

    class Meta:
        db_table='question_bank_options'

class exam_master(models.Model):
    id               = models.AutoField(primary_key=True)
    name             = models.CharField(max_length=250,default="")
    exam             = models.ForeignKey(exam,on_delete=models.CASCADE)
    course           = models.ForeignKey(course,on_delete=models.CASCADE)
    no_of_questions  = models.IntegerField(default=0)
    total_time       = models.TimeField()
    no_of_attempt    = models.IntegerField(default=0)
    datetime         = models.DateTimeField(auto_now_add=True)
    exam_start_date  = models.DateField()
    exam_end_date    = models.DateField()
    exam_description = models.CharField(max_length=500,default="")
    is_draft         = models.BooleanField(default=False)
    user             = models.ForeignKey(login,on_delete=models.CASCADE)

    class Meta:
        db_table = 'exam_master'

class exam_question_allocation(models.Model):
    id               = models.AutoField(primary_key=True)
    exam_master      = models.ForeignKey(exam_master,on_delete=models.CASCADE)
    question         = models.ForeignKey(question_bank,related_name='qid',on_delete=models.CASCADE)

    class Meta:
        db_table = 'exam_question_allocation'

class contribution(models.Model):
    id               = models.AutoField(primary_key=True)
    question         = models.ForeignKey(question_bank,on_delete=models.CASCADE)
    subject          = models.ForeignKey(subject,on_delete=models.CASCADE)
    topic            = models.ForeignKey(topic,on_delete=models.CASCADE)
    explanation      = models.CharField(max_length=500,default="",null=False)
    is_approved      = models.BooleanField(default=False,null=False)
    user             = models.ForeignKey(login,on_delete=models.CASCADE)

    class Meta:
        db_table='contribution'


class question_reporting(models.Model):
    id               = models.AutoField(primary_key=True)
    question         = models.ForeignKey(question_bank,on_delete=models.CASCADE)
    user             = models.ForeignKey(login,on_delete=models.CASCADE)
    reported_date    = models.DateField(auto_now_add=True)
    reporting_reason = models.CharField(max_length=500,default="")
    remarks          = models.CharField(max_length=250,default="")
    is_solved        = models.BooleanField(default=True)

    class Meta:
        db_table = 'question_reporting'



