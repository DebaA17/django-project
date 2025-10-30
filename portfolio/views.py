from django.shortcuts import render, redirect
from .models import Project, Contact, VisitorLog, Profile



import requests

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def home(request):
    ip = get_client_ip(request)
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    system = browser = ''
    if 'Windows' in user_agent:
        system = 'Windows'
    elif 'Macintosh' in user_agent:
        system = 'MacOS'
    elif 'Linux' in user_agent:
        system = 'Linux'
    else:
        system = 'Other'
    if 'Chrome' in user_agent:
        browser = 'Chrome'
    elif 'Firefox' in user_agent:
        browser = 'Firefox'
    elif 'Safari' in user_agent and 'Chrome' not in user_agent:
        browser = 'Safari'
    elif 'Edge' in user_agent:
        browser = 'Edge'
    else:
        browser = 'Other'

    # Fetch ISP info using ipinfo.io
    isp = ''
    try:
        resp = requests.get(f'https://ipinfo.io/{ip}/json', timeout=2)
        if resp.status_code == 200:
            data = resp.json()
            isp = data.get('org', '')
    except Exception:
        isp = ''

    VisitorLog.objects.create(ip_address=ip, isp=isp, system=system, browser=browser)
    projects = Project.objects.all()
    profile = Profile.objects.first()
    return render(request, 'home.html', {'projects': projects, 'profile': profile})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, message=message)
        return redirect('home')
    return render(request, 'contact.html')
