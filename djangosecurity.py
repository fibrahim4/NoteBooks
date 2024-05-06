from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

# Example of a view with login functionality
def user_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse('You are logged in')
    else:
        return HttpResponse('Invalid login')

# Example of a protected view
@login_required
def protected_view(request):
    return HttpResponse('This is a protected area')