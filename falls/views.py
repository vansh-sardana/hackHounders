# falls/views.py
# falls/views.py
# falls/views.py
# falls/views.py
from django.shortcuts import render
import time
import serial
from django.shortcuts import render


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

    return fall_data



def home(request):
    # Read real-time data from Arduino
    serial_data = read_serial_data()
    print(f"Serial Data: {serial_data}")
    # Parse the serial data
    fall_data = parse_serial_data(serial_data)
    print(f"Fall Data: {fall_data}")
    print(3)

    return render(request, 'home.html', {'fall_data': fall_data})



# falls/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, UserLoginForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to your home page after successful signup
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to your home page after successful login
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


