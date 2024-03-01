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


