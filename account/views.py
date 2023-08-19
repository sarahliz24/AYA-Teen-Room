from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import FormLoggingIn, UserSignUp, EditUser, EditTeenUserProfile
from django.contrib.auth.decorators import login_required
from .models import TeenUserProfile


def user_login(request):
    if request.method == "POST":
        form = FormLoggingIn(request.POST)  # create form instance
        if form.is_valid():  # validate form
            cd = form.cleaned_data  # converts data to clean form
            # check if user is in database
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('User verified')
                else:
                    #  check if valid user is active
                    return HttpResponse('User not active')
            else:
                #  user not in database
                return HttpResponse('User not valid')
    else:
        form = FormLoggingIn()
    return render(request, 'account/login.html', {'form': form})


""" @login_required # check is user is authenticated
def dashboard(request):
    return render(request,
                    'account/dashboard.html',
                    {'section': 'dashboard'}) """


@login_required  # check is user is authenticated
def feedback(request):
    return render(request,
                  'pages/feedback.html',
                  {'section': 'feedback'})


def logout(request):
    logout(request)
    return redirect('home')


def signup(request):
    if request.method == 'POST':
        signup_form = UserSignUp(request.POST)  # create form instance
        if signup_form.is_valid():
            teen_user = signup_form.save(commit=False)
            teen_user.set_password(
                signup_form.cleaned_data['password'])
            teen_user.save()
            messages.success(request, "Signup was successful")
            TeenUserProfile.objects.create(user=teen_user)
            login(request, teen_user)  # log in user automatically
            return render(request, 'registration/successful_reg.html',
                          {'teen_user': teen_user})
    else:
        # messages.error(request, 'Oops, something went wrong! Try again')
        signup_form = UserSignUp()
    return render(request, 'registration/signup.html',
                  {'signup_form': signup_form})


@login_required
def ProfileEdit(request):
    if request.method == 'POST':
        signup_form = EditUser(instance=request.user, data=request.POST)
        teen_user_profile = EditTeenUserProfile(
                                        instance=request.user.profile,
                                        data=request.POST,
                                        files=request.FILES)
        if signup_form.is_valid() and teen_user_profile.is_valid():
            signup_form.save()
            teen_user_profile.save()
            messages.success(request, "Update of your details successful")
            return render(request, 'pages/feedback.html')
        else:
            messages.error(request, 'Oops, something went wrong!')
    else:
        signup_form = EditUser(instance=request.user)
        teen_user_profile = EditTeenUserProfile(
                                        instance=request.user.profile)
    return render(request, 'registration/edit.html',
                  {'signup_form': signup_form,
                   'teen_user_profile': teen_user_profile})
