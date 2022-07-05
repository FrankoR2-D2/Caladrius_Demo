
from urllib import request
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from register.form import UserCreationForm
from main.forms import PatientForm
from main.models import Patient

from django.contrib import messages

from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.
def register(request):
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
    
        if form.is_valid():
            form.save()
            
            
            
            eml = form.cleaned_data.get('email')
            
            print(f'THE USERNAME: {eml}')
            messages.success(request, 'Successfully created new user: ' + eml)
            
            usr  = get_user_model()
            print(f'THE USER ID IS : {usr}')
            
            
        return redirect("/home")
    else:
        form = UserCreationForm()
    
    form = UserCreationForm()
    return render(request, "register/register.html", {"form": form})


def user_login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.  
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        #attempt to see if the username/password
        # combination is valid -
        user = authenticate(email=email, password=password)
        if user:
            
            if user.is_active:
                # Login if user is active and valid 
                # Redirecting user back to home page 
                login(request, user)
                
                
                
                
                print(f'THE USER ID IS ------> {user}')
                
                return redirect('addPatient/', user)
            else:
                # An inactive account indication !!!
                return HttpResponse("Your Rango account is disabled.")
        else:
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, "registration/login.html", {})


def addPatient(request):
    if request.method == 'POST':
        form =  PatientForm(request.POST)
        if form.is_valid():
            p = form.cleaned_data["patientNotes"]
            pat = Patient(patientNotes=p, user=request.user)
            pat.save()
            request.user.addPatient.add(pat)
            
        return HttpResponseRedirect("/home") 
    else:
        form = PatientForm()
    return render(request, "main/addpatient.html", {"form":form})
        


# def login_view(request):
#     # next = request.GET.get('next')
#     form = AuthenticationForm(request.POST)
#     if form.is_valid():
#         email = form.cleaned_data.get('email')
#         password = form.cleaned_data.get('password')
#         user = authenticate(email=email, password=password)
#         # if next:
#         #     return redirect(next)
#         # return redirect('home/')
#         if user is not None:
#             welcome = "Welcome. You are Signed in." 
            
#             login(request, user)
#             return redirect('home/', {"msg": welcome})
#     context = {
#     'form': form,
#     }
#     return render(request, "registration/login.html", context )
    


# user = get_user_model()

# def loginPage(request):
#     print('login login login')
#     form = AuthenticationForm(request.POST)
#     context = {'form':form}
#     print(context)
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         print(f'The USERNAME IS: {email}')
#         print(f'The PASSWORD IS: {password}')
        
        
#         user = authenticate(request, username=email, password=password)
        
    #     if user is not None:
    #         welcome = "Welcome. You are Signed in." 
            
    #         login(request, user)
    #         return redirect('home/', {"msg": welcome})
    # return render(request, "registration/login.html", context )

  