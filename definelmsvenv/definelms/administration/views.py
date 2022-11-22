from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .forms import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
from lmsmainapp.forms import *
from lmsmainapp.models import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login as auth_login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages



#######login############################

# def admin_login(request):
#     forms = loginform()
#     if request.method == 'POST':
#         forms = loginform(request.POST)
#         if forms.is_valid():
#             username = forms.cleaned_data['username']
#             password = forms.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user:
#                 login.objects.values(request, user)
#                 return redirect('home')
#     context = {'forms': forms}
#     return render(request, 'administration/login.html', context)




# def admin_login(request):
#     forms = loginform()
#     un=login.objects.filter(role=0).values()
#     print('----------------',un)
#     for l in un:
#         # print('**************************',v)
#         u=l.get('username')
#         p=l.get('password')
#     if request.method == 'POST':
#         forms = loginform(request.POST)
#         if forms.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             if username == u and password == p:
#                 total_course = course.objects.count()
#                 context={
#                     'course': total_course,
#                 }
#                 return render(request, 'home.html', context)
#             else:
#                 context = {'forms': forms}
#                 return render(request, 'administration/login.html', context)
#     context = {'forms': forms}
#     return render(request, 'administration/login.html', context)

#   <li class="nav-item">
#                 <a class="nav-link" href="{% url 'home' %}"><i class="icon-speedometer"></i> Dashboard</a>
#             </li>
           




def admin_login(request):

   
	msg=''
   
	if request.method=='POST':
        
       
		username=request.POST['username']
		password=request.POST['password']
		user=login.objects.filter(username=username,password=password,role=0).count()
        
		if user > 0:
            
			user=login.objects.filter(username=username,password=password,role=0).first()
			request.session['username'] = user.username
			print(request.session['username'])
            
			return redirect('home')
            # return redirect(request,'home.html',context1)

		else:
			msg='Invalid!!'
            
	form=loginform
	return render(request, 'administration/login.html',{'forms':form,'msg':msg})




# def admin_login(request):
# 	msg=''
# 	if request.method=='POST':
# 		username=request.POST['username']
# 		password=request.POST['password']
# 		userlogin=login.objects.filter(username=username,password=password,role=0).count()
# 		if userlogin > 0:
# 			userlogin=login.objects.filter(username=username,password=password,role=0).first()
# 			request.session['username']=userlogin.username
# 			return redirect('home')
# 		else:
# 			msg='Invalid!!'
            
# 	form=loginform
# 	return render(request, 'administration/login.html',{'forms':form,'msg':msg})
 
# def admin_logout(request):
#     logout(request)
#     return redirect('login')



def admin_logout(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
        logout(request)
        return redirect('login')


############### home ##############################



def home_page(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
            
        total_course   = course.objects.count()
        total_subject  = subject.objects.count()
        total_exam     = exam.objects.count()
        total_question = question_bank.objects.count()
        context={
            'course'  :total_course,
            'subject' :total_subject,
            'exam'    :total_exam,
            'question':total_question
        }
        return render(request, 'home.html',context)




####################designation######################
def home(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
    
        form = designationForm()
        dsn = designation.objects.all()
        
        context = {'form':form, 'dsn':dsn}
        return render(request, 'core/home.html', context)


@csrf_exempt
def save_data(request):
    if request.method == 'POST':
        form = designationForm(request.POST)
        if form.is_valid():
            did = request.POST.get('dsnid')
            designation1 = request.POST['designation']
            print('student id',did)

            if(did == ''):
                d = designation(designation=designation1)
            else:
                d = designation(id=did, designation=designation1)
            d.save()

            dsn = designation.objects.values()
            student_data = list(dsn)
            return JsonResponse({'status':'Data Saved', 'student_data':student_data})
        else:
            return JsonResponse({'status':'Not Saved'})    

@csrf_exempt
def delete_data(request):
    if request.method == 'POST':
        id = request.POST.get('did')
        d = designation.objects.get(pk=id)
        d.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})    


@csrf_exempt
def edit_data(request):
    if request.method == 'POST':
        id = request.POST.get('did')
        print('Student ID',id)
        desgn = designation.objects.get(pk=id)
        student_data = {'id':desgn.id, 'designation':desgn.designation}
        return JsonResponse(student_data)

################################## add exam #################################

def home_exam(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
        form = examForm()
        exm = exam.objects.all()
        context = {'form':form, 'exm':exm}
        return render(request, 'exam/exam.html', context)


@csrf_exempt
def save_data_exam(request):
    if request.method == 'POST':
        form = examForm(request.POST)
        if form.is_valid():
            eid = request.POST.get('exmid')
            exam_name = request.POST['exam_name']
            description = request.POST['description']
            remarks = request.POST['remarks']
            print('student id',eid)

            if(eid == ''):
                s = exam(exam_name=exam_name, description=description, remarks=remarks)
            else:
                s = exam(id=eid, exam_name=exam_name, description=description, remarks=remarks)
            s.save()

            exm = exam.objects.values()
            student_data = list(exm)
            return JsonResponse({'status':'Data Saved', 'student_data':student_data})
        else:
            return JsonResponse({'status':'Not Saved'})    

@csrf_exempt
def delete_data_exam(request):
    if request.method == 'POST':
        id = request.POST.get('eid')
        s = exam.objects.get(pk=id)
        s.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})    


@csrf_exempt
def edit_data_exam(request):
    if request.method == 'POST':
        id = request.POST.get('eid')
        print('Student ID',id)
        student = exam.objects.get(pk=id)
        student_data = {'id':student.id, 'exam_name':student.exam_name, 'description':student.description, 'remarks':student.remarks}
        return JsonResponse(student_data)


        
################################## add course #################################


def add_course(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
            if request.method == 'POST':
                # y =(0,1,{request.session['username']})
                form = courseform1(request.POST, request.FILES)
                # un=login.objects.filter(role=0).values()
                # print('----------------',un)
               
                if form.is_valid():
                    form.save()
                    designation = course.objects.all()
                    context = {'form': form, 'st': designation}
                    return render(request, 'course/course.html',context)
                    
            else:
                form = courseform1()
            designation = course.objects.all()
            context = {'form': form, 'st': designation}
            return render(request, 'course/course.html', context)




# def home_course(request):
#     form = courseform1()
#     exm = course.objects.all()
#     context = {'form':form, 'exm':exm}
#     return render(request, 'course/course.html', context)


# @csrf_exempt
# def save_data_course(request):
#     if request.method == 'POST':
#         form = courseform1(request.POST)
#         if form.is_valid():
#             eid = request.POST.get('exmid')
#             course_name = request.POST['course_name']
#             description = request.POST['description']
#             amount = request.POST['amount']
#             duration = request.POST.POST('duration')
#             exam = request.POST['exam']
#             image = request.POST['image']
#             user = request.POST['user']
#             print('student id',eid)

#             if(eid == ''):
#                 s = course(course_name=course_name, description=description, amount=amount,duration=duration,exam=exam,image=image,user=user)
#             else:
#                 s = course(id=eid, course_name=course_name, description=description, amount=amount,duration=duration,exam=exam,image=image,user=user)
#             s.save()

#             exm = course.objects.values()
#             student_data = list(exm)
#             return JsonResponse({'status':'Data Saved', 'student_data':student_data})
#         else:
#             return JsonResponse({'status':'Not Saved'})    

@csrf_exempt
def delete_data_course(request):
    if request.method == 'POST':
        id = request.POST.get('cid')
        s = course.objects.get(pk=id)
        s.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})    


# @csrf_exempt
# def edit_data_course(request):
#     if request.method == 'POST':
#         id = request.POST.get('eid')
#         print('Student ID',id)
#         student = course.objects.get(pk=id)
#         student_data = {'id':student.id, 'course_name':student.course_name, 'amount':student.amount, 'duration':student.duration,'exam':student.exam, 'image':student.image, 'user':student.user}
#         return JsonResponse(student_data)


########################## add subject ########################



def add_subject(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
        if request.method == 'POST':
            form = subjectform(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                designation = subject.objects.all()
                context = {'form': form, 'st': designation}
                return render(request, 'subject/subject.html',context)
                
        else:
            form = subjectform()
        designation = subject.objects.all()
        context = {'form': form, 'st': designation}
        return render(request, 'subject/subject.html', context)


@csrf_exempt
def delete_data_subject(request):
    if request.method == 'POST':
        id = request.POST.get('cid')
        s = subject.objects.get(pk=id)
        s.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0}) 


######################add topic ###########################




def add_topic(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
        if request.method == 'POST':
            form = topicform(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                designation = topic.objects.all()
                context = {'form': form, 'st': designation}
                return render(request, 'topic/topic.html',context)
                
        else:
            form = topicform()
        designation = topic.objects.all()
        context = {'form': form, 'st': designation}
        return render(request, 'topic/topic.html', context)  

@csrf_exempt
def delete_data_topic(request):
    if request.method == 'POST':
        id = request.POST.get('eid')
        s = topic.objects.get(pk=id)
        s.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})    



######################add subtopic ###########################




def add_subtopic(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
        if request.method == 'POST':
            form = subtopicform(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                designation = Subtopics.objects.all()
                context = {'form': form, 'st': designation}
                return render(request, 'subtopic/subtopic.html',context)
                
        else:
            form = subtopicform()
        designation = Subtopics.objects.all()
        context = {'form': form, 'st': designation}
        return render(request, 'subtopic/subtopic.html', context)  

@csrf_exempt
def delete_data_subtopic(request):
    if request.method == 'POST':
        id = request.POST.get('cid')
        s = Subtopics.objects.get(pk=id)
        s.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})    


        
######################add question ###########################




def add_question(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
        if request.method == 'POST':
            form = question_bankform(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                designation = question_bank.objects.all()
                context = {'form': form, 'st': designation}
                return render(request, 'questionbank/questionbank.html',context)
                
        else:
            form = question_bankform()
        designation = question_bank.objects.all()
        context = {'form': form, 'st': designation}
        return render(request, 'questionbank/questionbank.html', context)  

@csrf_exempt
def delete_data_question(request):
    if request.method == 'POST':
        id = request.POST.get('cid')
        s = question_bank.objects.get(pk=id)
        s.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})    



################# add exam master ###########################

def addexmaster(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
        if request.method == 'POST':
            form = exammasterForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                designation = exam_master.objects.all()
                context = {'form': form, 'st': designation}
                return render(request, 'exam_master/exammaster.html',context)
        else:
            form = exammasterForm()
        designation=exam_master.objects.all()
        context = {'form': form, 'st': designation}
        return render(request, 'exam_master/exammaster.html', context)


@csrf_exempt
def delete_data_exmaster(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        s  = exam_master.objects.get(pk=id)
        s.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})    


@csrf_exempt
def edit_data_exmaster(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        examo = exam_master.objects.get(pk=id)
        exam_data = {'id':examo.id, 'topic_name':examo.topic_name, 'description':examo.description, 'subject':examo.subject, 'user':examo.user}
        return JsonResponse(exam_data)


##################### QUESTIONBANK OPTIONS ##################



def addoptions(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
        if request.method == 'POST':
            form = optionsForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                designation = question_bank_options.objects.all()
                context = {'form': form, 'st': designation}
                return render(request, 'qsoptions/options.html',context)
                
        else:
            form = optionsForm()
        designation = question_bank_options.objects.all()
        context = {'form': form, 'st': designation}
        return render(request, 'qsoptions/options.html',context)





@csrf_exempt
def delete_data_addoptions(request):
    if request.method == 'POST':
        id = request.POST.get('oid')
        d = question_bank_options.objects.get(pk=id)
        d.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0}) 


@csrf_exempt
def edit_data_addoptions(request):
    if request.method == 'POST':
        id = request.POST.get('eid')
        #print('Exam ID',id)
        examo = topic.objects.get(pk=id)
        exam_data = {'id':examo.id, 'exam_name':examo.exam_name,'description':examo.description,'remarks':examo.remarks}
        return JsonResponse(exam_data)
