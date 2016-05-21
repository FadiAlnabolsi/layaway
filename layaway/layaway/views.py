from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.models import User

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/')
    else:
        return render_to_response("invalid.html")

def loggedin(request):
    return render_to_response('loggedin.html',
                             {'full_name': request.user.username })

def invalid_login(request):
    return render_to_response("invalid.html")

def logout(request):
    auth.logout(request)
    return render_to_response("homepage.html")

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.data['username']
            initializeUserInfo = UserInfo()
            initializeUserInfo.user = User.objects.get(username=username)
            initializeUserInfo.save()

            return HttpResponseRedirect('/accounts/register_success')

        else:
            args.update(form.errors)
            args.update(csrf(request))
            return render_to_response('register.html', args) 

    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()

    return render_to_response('register.html', args)

def register_success(request):
    return render_to_response('register_success.html')
