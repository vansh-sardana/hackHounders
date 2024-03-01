# falls/views.py
# falls/views.py
# falls/views.py
# falls/views.py
from django.shortcuts import render

def home(request):
    # Sample data, replace this with the actual data from your fall detection system
    fall_data = {
        'time': '5:30',
        'location': 'BMN Munjal University',
        'date': '1 March',
        'heartbeat': 90,
    }

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


