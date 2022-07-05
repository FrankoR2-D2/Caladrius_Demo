from urllib import request, response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Appointments, Doctor, ToDoList, Patient
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
    
    pat_list = Patient.objects.all()

    print(f"Felix's email is ----> {User.objects.get(id=1)}")
    

    context = {
        "doc_list": doc_list,
        "user_list": user_list,
        "pat_list": pat_list
    }
    

    print(f"THE LENGTH OF SET IS {len(context['doc_list'])}")
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


    uid = request.user.id 
    
    # apm = Appointments.objects.filter(pk=uid).exists()
    print(f'VIEW APPOINTMENTS UID -----> {uid}')
    
    apt = Appointments.objects.filter(patient_id=uid)
    print(apt)
    if Appointments.objects.filter(patient_id=uid).exists():
        apm = Appointments.objects.filter(patient_id=uid).values('start_time', 'end_time', 'status', 'doctor_id', 'patient_id')
         
        # st = apm.
        # print(apm.start_time)
        # print(f"THE START TIME IS {st} for USER ID {uid} ")
        
        apm_obj = apm.first()
        #apm._meta.get_field('start_time')
        
        s_time = apm_obj.get('start_time')
        e_time = apm_obj.get('end_time')
        status = apm_obj.get('status')
        doc_id = apm_obj.get('doctor_id')
        pat_id = apm_obj.get('patient_id')
        
        
        doc = User.objects.filter(pk=doc_id).values('first_name', 'last_name') #.values('first_name', 'last_name')
        
        doc_obj = doc.first()
        
        doc_f =  doc_obj.get('first_name')
        doc_l = doc_obj.get('last_name')
        
        pat = User.objects.filter(pk=pat_id).values('first_name', 'last_name')
        pat_f =  doc_obj.get('first_name')
        pat_l = doc_obj.get('last_name')

        
        doctor = f"Dr. {doc_f} {doc_l}"
        patient = f"{pat_f} {pat_l}"
        
        print(f"DOCTOR ---------------> {doctor}")
        

        print(f'APPOINTMENT DETAILS: {s_time}, {e_time}, {status}, {doc_id}')
        
        hp = True
        
        doc_list = Doctor.objects.all()
        user_list = User.objects.all()
        apm_list = Appointments.objects.all()
        pat_list = Patient.objects.all()
        
        
        context = {
            "s_time": s_time,
            "e_time": e_time,
            "status": status,
            "doctor": doctor,
            "patient": patient,
            "hp": hp,
            
            
        }
        print("APPOINTMENT EXISTS")
        return render(request, "main/view_apm.html", context)

    else:
        
        d_list = Doctor.objects.all()
        u_list = User.objects.all()
        a_list = Appointments.objects.all()
        p_list = Patient.objects.all()
        
        
        msg =  "You have not yet created an appointment."
        hp = False
        context = {
            "msg": msg,
            "hp": hp,
            "d_list": d_list,
            "u_list": u_list,
            "a_list": a_list,
            "p_list": p_list
        }
        return render(request, "main/view_apm.html", context)





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
    
