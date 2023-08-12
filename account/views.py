from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import FormLoggingIn

def user_login(request):
    if request.method == "POST":
        form = FormLoggingIn(request.POST) # create form instance
        if form.is_valid(): # validate form
            cd = form.cleaned_data # 
            # check if user is in database
            user = authenticate(request,
                                username=cd['username'],
                                password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('User verified')
                else:
                    # check if valid user is active
                    return HttpResponse('User not active') 
            else:
                # user not in database
                return HttpResponse('User not valid')
    else:
        form = FormLoggingIn()
    return render(request, 'account/user_login.html', {'form': form})


