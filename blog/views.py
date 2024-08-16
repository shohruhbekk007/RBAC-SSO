# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    is_admin = request.user.groups.filter(name='Admin').exists()
    return render(request, 'home.html', {'is_admin': is_admin})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')
