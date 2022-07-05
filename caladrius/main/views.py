from urllib import request, response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Appointments, Doctor, ToDoList, Item
from .forms import CreateNewList, AppointmentForm
# Create your views here.

from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
User = get_user_model()


def index(response, id):
    ls = ToDoList.objects.get(id=id)
    
    if ls in response.user.todolist.all():    
        if response.method == "POST":
            print(response.POST)
            if response.POST.get("save"):    
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()
            elif response.POST.get("newItem"):
                txt = response.POST.get("new")
                
                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("invalid")
                
        return render(response, "main/list.html", {"ls":ls})
    return render(response, "main/home.html", {})


def home(response):
    user = response.user
    print(f'HOMEPAGE USER ----> {user}')
    doc_list = Doctor.objects.all()
    user_list = User.objects.all()
    
    # user_d = {}
    # k = 1    
    # for obj in doc_list:    
    #     usr = f"{User.objects.get(id=obj.user_id).first_name} {User.objects.get(id=obj.user_id).last_name}"
    #     user_d[k] = usr
    #     k+1
    #     print(usr)   
    print(f"Felix's email is ----> {User.objects.get(id=1)}")
    
    
    # "id": id,
    # "specialization": 'specialization',
    context = {
        "doc_list": doc_list,
        "user_list": user_list,
    }
    
    # for i in len(queryset)
    # doc = context["object_list"]
    print(f"THE LENGTH OF SET IS {len(context['doc_list'])}")
    
    # for i in context["object_list"]:
    #     k = context["object_list"][i]
    #     print(k)
    # k = context["object_list"][0]
    # print(k)
     #{"msg": welcome},
    return render(response, "main/home.html", context)



def rqst_appment(request, id):   
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            
            patient = request.user
            pat_id = patient.id 
            print(f"THE DOCTOR'S ID {id}")
            print(f"THE PATIENT ID IS {pat_id}")            
            doc = User.objects.get(id=id)
            doctor = f"Dr. {doc.first_name} {doc.last_name}"
            print(f'REQUESTED DOCTOR IS: {doctor}')    
            
            app_stat = False
            st = form.data['start_time']
            et = form.data['end_time']
            dt = form.data['date']
            ar = form.data['appointment_reason']
            doc_id = id 
            
            apt = Appointments(start_time=st, end_time=et, date=dt, status=app_stat, appointment_reason=ar, doctor_id=doc_id, patient_id = pat_id)
            apt.save()
            
            
            # print(stt)
            print(f"Results: {st} - {et}, {dt} - {ar}")
                     
            
            
            print('APOINTMENT SAVED;) ')
            msg = "Apointment created."
        return HttpResponseRedirect('/')
            
            
    else:
        form = AppointmentForm(request.POST)
    return render(request, "main/appointments.html", {"form": form})


def display_apm(request):
    if request.method == 'POST':
        uid = request.user.id 
        
        print(f'VIEW APPOINTMENTS UID -----> {uid}')
        # return HttpResponseRedirect('/')
    
    else:
        print('THE VIEW APPOINTMENT PAGE IS NOT RENDERING')
        return render(request, "main/view_apm.html")





def create(response):
    form = CreateNewList()
    if response.method == "POST":
        form =  CreateNewList(response.POST)
        
        if form.is_valid():
            t = form.cleaned_data["name"]
            t = ToDoList(name=t)
            t.save()
            response.user.todolist.add(t)
            
        return HttpResponseRedirect(f"/{t.id}")
            
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form":form})

def signout(response):
    return render(response, "main/logout.html")


def signedIn(response):  
    welcome = "Welcome. You are Signed in." 
    return render(response, "main/home.html", {"msg": welcome})

def showtodo(request):
    return render(request, "main/showtodo.html", {})
    
