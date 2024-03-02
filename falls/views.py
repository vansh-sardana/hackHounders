# falls/views.py
# falls/views.py
# falls/views.py
# falls/views.py
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import AuthenticationForm
from django.db import IntegrityError
from django.shortcuts import render
from django.utils.timezone import now
from django.contrib.auth.forms import UserCreationForm
import time
import serial
from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.utils import timezone
from django.contrib import messages
from django.http import HttpResponseNotFound
def handle_undefined_path(request, undefined_path):
    return HttpResponseNotFound("Page not found")
def read_serial_data():
    # Replace 'COMx' with your Arduino's serial port
    ser = serial.Serial('COM5', 9600)
    # Wait for Arduino to initialize
    time.sleep(2)
    # Read data from the serial port
    data = ser.readline().decode('utf-8').strip()
    # Close the serial port
    ser.close()
    return data

def parse_serial_data(serial_data):
    # Parse the serial data and return a dictionary
    # Example: "Time: 01:32, Latitude: 28.247627, Longitude: 76.813499, Heartbeat: 103"
    data_parts = serial_data.split(',')
    fall_data = {}

    for part in data_parts:
        print(part)
        if ': ' in part:
            key, value = part.split(':', 1)
            fall_data[key.lower()] = value
    fall_data['time']= timezone.localtime(timezone.now()).strftime("%H:%M")
    fall_data['date']=timezone.localtime(timezone.now()).date()
    return fall_data



def home(request):
    # Read real-time data from Arduino
    serial_data = read_serial_data()
    print(f"Serial Data: {serial_data}")
    # Parse the serial data
    fall_data = parse_serial_data(serial_data)
    print(f"Fall Data: {fall_data}")


    return render(request, 'home.html', {'fall_data': fall_data})
from django.contrib.auth.decorators import login_required
# @login_required(login_url='login')  # Redirect to login page if not authenticated
# def home(request):
#     # Check if the user is authenticated
#     if request.user.is_authenticated:
#         # Manually providing fall data when the user is logged in
#         fall_data = {
#             'time': '5:30',
#             'location': 'BMN Munjal University',
#             'date': '1 March',
#             'heartbeat': 90,
#         }
#     else:
#         # If the user is not authenticated, set fall_data to an empty dictionary
#         fall_data = {}

#     return render(request, 'home.html', {'fall_data': fall_data})

# falls/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, UserLoginForm
from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    
    # Clear the fall_data when logging out
    request.session['fall_data'] = {}
    
    return redirect('login')

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            # Add this line to display form errors in the template
            messages.error(request, 'Invalid form submission. Please check the form for errors.')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

from django.views import View  # Add this import

class UserLoginView(SuccessMessageMixin, View):
    template_name = 'login.html'
    form_class = AuthenticationForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print("Login successful!")
            messages.success(self.request, 'Login successful!')
            return redirect('home')
        else:
            print("Invalid login credentials!") 
            messages.error(request, 'Invalid login credentials! Please check your username and password.')
            return render(request, self.template_name, {'form': form})


    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})


from django.shortcuts import render, get_object_or_404, redirect
from .models import EmergencyContact
from .forms import EmergencyContactForm

def emergency_contacts(request):
    emergency_contacts = EmergencyContact.objects.all().distinct
    return render(request, 'emergency_contact_list.html', {'contacts': emergency_contacts})

def add_emergency_contact(request):
    from django.db import IntegrityError
from django.shortcuts import render, redirect
from .forms import EmergencyContactForm
from .models import EmergencyContact
def add_emergency_contact(request):
    if request.method == 'POST':
        form = EmergencyContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmergencyContactForm()

    return render(request, 'add_emergency_contact.html', {'form': form})


def update_emergency_contact(request, pk):
    emergency_contact = get_object_or_404(EmergencyContact, pk=pk)
    if request.method == 'POST':
        form = EmergencyContactForm(request.POST, instance=emergency_contact)
        if form.is_valid():
            form.save()
            return redirect('emergency_contact_list')
    else:
        form = EmergencyContactForm(instance=emergency_contact)

    return render(request, 'update_emergency_contact.html', {'form': form, 'emergency_contact': emergency_contact})

def delete_emergency_contact(request, pk):
    emergency_contact = get_object_or_404(EmergencyContact, pk=pk)
    if request.method == 'POST':
        emergency_contact.delete()
        return redirect('emergency_contacts')

    return render(request, 'delete_emergency_contact.html', {'emergency_contact': emergency_contact})
# falls/views.py
from django.shortcuts import render

def nearby_hospitals(request):
    return render(request, 'nearby_hospitals.html')
