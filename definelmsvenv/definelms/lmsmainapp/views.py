from copy import Error
from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse, response,JsonResponse
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from collections import namedtuple
from PIL import Image
from rest_framework.parsers import MultiPartParser, FormParser
from .forms import *
from django.views.decorators.csrf import csrf_exempt


class WebLogin(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        data = login.objects.filter(username = username, password = password, role='Admin')
        if not data.exists():
            return Response(Error)
        login_data = login.objects.filter(username = username).first()
        serializer = loginSerializer(login_data, many=False)
        return Response(serializer.data)

class loginView(APIView):
 
    def get(self,request,username=None):
        if username is not None:
            user = login.objects.filter(username = username).first()
            serializer = loginSerializer(user, many=False)
            return Response(serializer.data)

        user = login.objects.all()
        serializer = loginSerializer(user,many=True)
        return Response(serializer.data)

    def post(self,req):
        serializer = loginSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
       
    def delete(self,req,id):
        login.objects.filter(id=id).delete()
        return Response({"msg":1})

    def put(self,req,id): 
        user   = login.objects.filter(id=id).first()
        
        serializer = loginSerializer(user,data=req.data,partial=True)
        
        if serializer.is_valid():
            
            serializer.save()
            print(serializer.data)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


# SERIALIZER FOR REGISTRATION OPERATIONS:

class registrationView(APIView):

    def get(self,request,username=None):
        if username is not None:
            register   = registration.objects.get(username=username)
            serializer = registrationSerializer(register)
            return Response(serializer.data)

        register       = registration.objects.all()
        serializer     = registrationSerializer(register,many=True)
        return Response(serializer.data)

    def post(self,req):
        Login={'username':req.data['mobile'],'password':req.data['mobile'],'role':0}
        serializer = registrationSerializer(data=req.data)
        logserial=loginSerializer(data=Login)
        if serializer.is_valid():
            serializer.save()

            if logserial.is_valid():
                logserial.save()

            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self,req,username):
        registration.objects.filter(username=username).delete()
        return Response({"msg":1})

    def put(self,req,username): 
        register   = registration.objects.filter(username=username).first()
        
        serializer = registrationSerializer(register,data=req.data,partial=True)
        
        if serializer.is_valid():
            
            serializer.save()
            print(serializer.data)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class examView(APIView):

    def get(self,request,id=None):
        if id is not None:
            exam1      = exam.objects.get(id=id)
            serializer = examSerializer(exam1)
            return Response(serializer.data) 
        exam1      = exam.objects.all()       
        serializer = examSerializer(exam1,many=True)
        return Response(serializer.data)


    def post(self,req):
        serializer = examSerializer(data=req.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


    def delete(self,req,id):
        exam.objects.get(id=id).delete()
        return Response({"msg":1}) 


    def put(self,req,id):
        exam1      = exam.objects.filter(id=id).first()
        serializer = examSerializer(exam1,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)  


#course

def addcourse(request):
        """Process images uploaded by users"""
        if request.method == 'POST':
            form = courseform1(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return render(request, 'course.html', {'form': form})
                
        else:
            form = courseform1()
        return render(request, 'course.html', {'form': form})

# def add_course(request):
#         if request.method == 'POST':
#             form = courseform1(request.POST, request.FILES)
#             if form.is_valid():
#                 form.save()
#                 designation = course.objects.all()
#                 context = {'form': form, 'st': designation}
#                 return render(request, 'course/course.html',context)
                
#         else:
#             form = courseform1()
#         designation = course.objects.all()
#         context = {'form': form, 'st': designation}
#         return render(request, 'course/course.html', context)

class courseView(APIView):

    def get(self,request,id=None):
        if id is not None:
            courses = course.objects.get(id=id)
            serializer = courseSerializer(courses)
            return Response(serializer.data) 
        courses = course.objects.all()       
        serializer = courseSerializer(courses,many=True)
        return Response(serializer.data)

    #parser_classes = (MultiPartParser, FormParser, )
    def post(self,req, *args, **kwarg):
        print(req.data)
        serializer = courseSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


    def delete(self,req,id):
        course.objects.get(id=id).delete()
        return Response({"msg":1}) 


    def put(self,req,id):
        courses = course.objects.filter(id=id).first()
        serializer = courseSerializer(courses,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)  


#subject adding
def addsubject(request):
        """Process images uploaded by users"""
        if request.method == 'POST':
            form = subjectForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                # Get the current instance object to display in the template
                img_obj = form.instance
                return render(request, 'subject.html', {'form': form})
        else:
            form = subjectForm()
        return render(request, 'subject.html', {'form': form})


#SERIALIZERS FOR SUBJECT OPERATION

class subjectView(APIView):


    def get(self,request,id=None):
        if id is not None:
            subjects = subject.objects.get(id=id)
            serializer = subjectSerializer(subjects)
            return Response(serializer.data) 
        subjects = subject.objects.all()       
        serializer = subjectSerializer(subjects,many=True)
        return Response(serializer.data)


    def post(self,req):
        serializer = subjectSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)  


    def delete(self,req,id):
        subject.objects.get(id=id).delete()
        return Response({"msg":1}) 


    def put(self,req,id):
        subjects = subject.objects.filter(id=id).first()
        serializer = subjectSerializer(subjects,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)  


#SERIALIZERS FOR TOPIC OPERATION

# get particular topic assosiated with particular subjects
class ParticularTopic(APIView):
    def get(self, request,id):
        topics = topic.objects.filter(subject = id)
        serializer = topicSerializer(topics, many=True)
        return Response(serializer.data)

class topicView(APIView):

    def get(self,request,id=None):
        if id is not None:
            topics     = topic.objects.get(id=id)
            serializer = topicSerializer(topics)
            return Response(serializer.data) 
        topics     = topic.objects.all()       
        serializer = topicSerializer(topics,many=True)
        return Response(serializer.data)


    def post(self,req):
        serializer = topicSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)  


    def delete(self,req,id):
        topic.objects.get(id=id).delete()
        return Response({"msg":1})   


    def put(self,req,id):
        topics = topic.objects.filter(id=id).first()
        serializer = topicSerializer(topics,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


#subtopic

class subtopicView(APIView):

    def get(self,request,id=None):
        if id is not None:
            subtopics     = Subtopics.objects.get(id=id)
            serializer = subtopicSerializer(subtopics)
            return Response(serializer.data) 
        subtopics     = Subtopics.objects.all()       
        serializer = subtopicSerializer(subtopics,many=True)
        return Response(serializer.data)


    def post(self,req):
        serializer = subtopicSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)  


    def delete(self,req,id):
        Subtopics.objects.get(id=id).delete()
        return Response({"msg":1})   


    def put(self,req,id):
        subtopics = Subtopics.objects.filter(id=id).first()
        serializer = subtopicSerializer(subtopics,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

#SERIALIZER FOR QUESTION BANK

class question_bankView(APIView):

    def get(self,request,id=None):
        if id is not None:
            question1      = question_bank.objects.get(id=id)
            serializer     = question_bankSerializer(question1)
            return Response(serializer.data) 
        question1      = question_bank.objects.all()       
        serializer     = question_bankSerializer(question1,many=True)
        return Response(serializer.data)


    def post(self,req):
        serializer = question_bankSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


    def delete(self,req,id):
        question_bank.objects.get(id=id).delete()
        return Response({"msg":1}) 


    def put(self,req,id):
        question1      = question_bank.objects.filter(id=id).first()
        serializer     = question_bankSerializer(question1,data=req.data)
        # print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)  


class questionView(APIView):  #TO GET QUESTION BY CERTAIN TOPIC ID

    def get(self,request,id=None):
        if id is not None:
            question1      = question_bank.objects.filter(topic=id)
            serializer     = question_bankSerializer(question1,many=True)
            return Response(serializer.data) 


#FOR EXAM MASTER

class exammasterView(APIView):

    def get(self,request,id=None):
        if id is not None:
            master1      = exam_master.objects.get(id=id)
            serializer     = exam_masterSerializer(master1)
            return Response(serializer.data) 
        master1        = exam_master.objects.all()       
        serializer     = exam_masterSerializer(master1,many=True)
        return Response(serializer.data)

    def post(self,req):
        serializer  = exam_masterSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)  

    def put(self,request,id):
        exammaster1 =  exam_master.objects.get(id=id)
        serializer  =  exam_master(exammaster1,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
            
    def delete(self,request,id):
        exam_master.objects.get(id=id).delete()
        return Response("successfully deleted")

# API to list the available tests...

class masterView(APIView):

    def post(self,request):
        sub_id=request.data['subject']
        tpc_id=request.data['topic']
        date  =request.data['date']

        print(request)
        master1      = exam_master.objects.filter(exam_criteria__subject=sub_id,exam_criteria__topic=tpc_id , exam_start_date__lte=date, exam_end_date__gte=date)
        serializer   = exam_masterSerializer(master1,many=True)
        return Response(serializer.data)  

class examQuestionAllocationView(APIView):

    def get(self,request,id=None):
        if id is not None:
            exam1      = exam_question_allocation.objects.get(id=id)
            serializer = examQuestionallocationSerializer(exam1)
            return Response(serializer.data) 
        exam1      = exam_question_allocation.objects.all()       
        serializer = examQuestionallocationSerializer(exam1,many=True)
        return Response(serializer.data)


    def post(self,req):
        serializer = examQuestionallocationSerializer(data=req.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


    def delete(self,req,id):
        exam_question_allocation.objects.get(id=id).delete()
        return Response({"msg":1}) 


    def put(self,req,id):
        exam1      = exam_question_allocation.objects.filter(id=id).first()
        serializer = examQuestionallocationSerializer(exam1,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors) 


class questionbankoptionsview(APIView):
    
    def get(self,request,id=None):
        if id is not None:
            question1      = question_bank_options.objects.get(id=id)
            serializer     = question_bank_optionsSerializer(question1)
            return Response(serializer.data) 
        question1      = question_bank_options.objects.all()       
        serializer     = question_bank_optionsSerializer(question1,many=True)
        return Response(serializer.data)


    def post(self,req):
        serializer = question_bank_optionsSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


    def delete(self,req,id):
        question_bank_options.objects.get(id=id).delete()
        return Response({"msg":1}) 


    def put(self,req,id):
        question1      = question_bank_options.objects.filter(id=id).first()
        serializer     = question_bank_optionsSerializer(question1,data=req.data)
        # print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class mcqView(APIView):

    def get(self,request,id=None):
        if id is not None:
            mcq        = question_bank.objects.get(id=id)
            serializer = qustnSerializer(mcq)
            return Response(serializer.data) 
        mcq        = question_bank.objects.all()       
        serializer = qustnSerializer(mcq,many=True)
        return Response(serializer.data)

class Particularmcq(APIView):

    def get(self, request,id):
        mcq        = exam_question_allocation.objects.filter(id=id)
        serializer = examQuestionallocationSerializer(mcq, many=True)
        return Response(serializer.data)

class GetQuestions(APIView):
    def get(self, request,id):
        data = exam_question_allocation.objects.filter(exam_master = id)
        serializer = examdetailsSerializer(data, many=True)
        return Response(serializer.data)




from django.contrib.auth.decorators import login_required

# # @login_required(login_url='login')
# def home_page(request):
#     total_course   = course.objects.count()
#     total_subject  = subject.objects.count()
#     total_exam     = exam.objects.count()
#     total_question = question_bank.objects.count()
#     context={
#         'course'  :total_course,
#         'subject' :total_subject,
#         'exam'    :total_exam,
#         'question':total_question
#     }
#     return render(request, 'home.html',context)

# def add_designation(request):
#     forms = AddDesignationForm()
#     if request.method == 'POST':
#         forms = AddDesignationForm(request.POST)
#         if forms.is_valid():
#             forms.save()
#             return redirect('designation')
#     designation = Designation.objects.all()
#     context = {'forms': forms, 'designation': designation}
#     return render(request, 'administration/designation.html', context)




###############################################
#     forms = Addexam()
#     if request.method == 'POST':
#         forms = Addexam(request.POST)
#         if forms.is_valid():
#             forms.save()
#             return redirect('add-exam')
#     exam1 = exam.objects.all()
#     context = {'form': forms, 'exam': exam1}
#     return render(request, 'exam/exam.html', context)



