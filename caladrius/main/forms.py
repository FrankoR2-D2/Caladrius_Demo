from django import forms 
from django.forms import Textarea
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime, AdminTextInputWidget

from .models import Appointments

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)

class PatientForm(forms.Form):
    patientNotes = forms.CharField(max_length=300)


# class DTForm(forms.Form):
#     start_time = forms.TimeField(widget=AdminTimeWidget())
#     end_time = forms.TimeField(widget=AdminTimeWidget())
#     date = forms.DateField(widget=AdminDateWidget())
#     appointment_reason = forms.CharField(required=False, widget=AdminTextInputWidget())


    

# class DateInput(forms.Form):
#     input_type = 'date'
    
# class TimeInput(forms.Form):
#     input_type = 'forms.TimeField(, required=False)'


class DatePickerInput(forms.DateInput):
        input_type = 'date'

class TimePickerInput(forms.TimeInput):
        input_type = 'time'

class DateTimePickerInput(forms.DateTimeInput):
        input_type = 'datetime'
        
        


class AppointmentForm(forms.Form):
    start_time = forms.TimeField(widget=TimePickerInput)
    end_time = forms.TimeField(widget=TimePickerInput)
    date = forms.DateField(widget=DatePickerInput)
    appointment_reason = forms.CharField(required=False, widget=Textarea)
    
    
    # model = Appointments
    # fields = ('start_time', 'end_time', 'date', 'appointment_reason' )
    # class Meta:
    #     widgets = {
    #         "start_time": forms.TimeInput(attrs={'type': 'time'}),
    #         "end_time": AdminTimeWidget(),
    #         "date": AdminDateWidget(),
    #         "appointment_reason": AdminTextInputWidget()
    #     }













# class AppointmentForm(forms.ModelForm):
#     start_time = forms.TimeField(widget=AdminTimeWidget())
#     end_time = forms.TimeField(widget=AdminTimeWidget())
#     date = forms.DateField(widget=AdminDateWidget())
#     appointment_reason = forms.CharField(required=False, widget=AdminTextInputWidget())
    
#     class Meta:
#         model = Appointments
#         fields = ('start_time', 'end_time', 'date', 'appointment_reason' )
#         widgets = {
#             "start_time": AdminTimeWidget(),
#             "end_time": AdminTimeWidget(),
#             "date": AdminDateWidget(),
#             "appointment_reason": AdminTextInputWidget()
#         }
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['start_time'].widget.attrs['placeholder'] = 'start_time'
    #     self.fields['end_time'].widget.attrs['placeholder'] = 'end_time'
    #     self.fields['date'].widget.attrs['placeholder'] = 'date'
    #     self.fields['appointment_reason'].widget.attrs['placeholder'] = 'appointment_reason'