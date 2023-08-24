from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import Http404
# from django.views import generic
from django.contrib import messages
from .models import Feedback, FeedbackReply
from .forms import FeedbackSubmission, ReplyForm
from django.views.decorators.http import require_POST
from django.views.generic import ListView


def home_view(request):
    return render(request, "FEEDBACK/home.html", {})


def feedback_submission(request):
    '''
    form = FeedbackSubmission(data=request.POST)
    if form.is_valid():
        feedback_form.instance.author = request.user.username
        feedback = feedback_form.save(commit=False)
        # feedback.post = post
        feedback.save()
    else:
       form = FeedbackSubmission() 
    return render(request, 'FEEDBACK/feedback/feedback_submission.html',)
    '''
    form = FeedbackSubmission()
    if request.method == 'POST':
        form = FeedbackSubmission(request.POST)
        # feedback_submission = FeedbackSubmission(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your feedback has been submitted & is awaiting approval")
            ok_feedback = Feedback.approved.all()
            return render (request, 'FEEDBACK/feedback/feedback_list.html',
                    {'ok_feedback': ok_feedback})
        else:
            messages.error(request, 'Oops, something went wrong!')
    else:
        form = FeedbackSubmission(instance=request.user)
    return render(request, 'FEEDBACK/feedback/feedback_submission.html',
                  {'form': form, })


'''
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
            return render(request, 'feedback/feedback_list.html')
        else:
            messages.error(request, 'Oops, something went wrong!')
    else:
        signup_form = EditUser(instance=request.user)
        teen_user_profile = EditTeenUserProfile(
                                        instance=request.user.profile)
    return render(request, 'registration/edit.html',
                  {'signup_form': signup_form,
                   'teen_user_profile': teen_user_profile})
'''


def feedback_list(request):
    ok_feedback = Feedback.approved.all()
    return render (request, 'FEEDBACK/feedback/feedback_list.html',
                    {'ok_feedback': ok_feedback})


def feedback_detail(request, id):
    feedback = get_object_or_404(Feedback, id=id,
                                 feedback_approval=Feedback.FeedbackApproval.OK)
    feedback_reply = feedback.feedback_reply.filter(allowed=True)
    form = ReplyForm()
    return render(request, 'FEEDBACK/feedback/feedback_detail.html',
                    {'feedback': feedback,
                     'feedback_reply': feedback_reply,
                     'form': form
                    })


@require_POST
def post_reply(request, feedback_id):
    feedback = get_object_or_404(Feedback, id=feedback_id, feedback_approval=Feedback.FeedbackApproval.OK)
    reply = None
    form = ReplyForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = request.user.username
            reply = form.save(commit=False)
            reply.feedback = feedback
            reply.save()
            messages.success(request, "Your reply has been submitted & is awaiting approval")
            ok_feedback = Feedback.approved.all()
            return render (request, 'FEEDBACK/feedback/feedback_list.html',
                        {'ok_feedback': ok_feedback})
        else:
            messages.error(request, 'Oops, something went wrong!')
    else:
        form = ReplyForm(instance=request.user)
    return render(request, 'FEEDBACK/feedback/reply_form.html',
                  {'form': form,
                   'feedback': feedback,
                   'reply': reply })


def feedback_edit(request, feedback_id):
    '''
    Allow user to update feedback they have previously
    created
    '''
    feedback = get_object_or_404(Feedback, id=feedback_id)

    if request.method == 'POST' and feedback.author == request.user:
        form = FeedbackSubmission(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            messages.success(request, "Your feedback has been submitted & is awaiting approval")
            ok_feedback = Feedback.approved.all()
            return render (request, 'FEEDBACK/feedback/feedback_list.html',
                    {'ok_feedback': ok_feedback})   
        else:
            messages.error(request, 'Oops, something went wrong!')
    else:
        messages.error(request, "You cannot edit another users feedback")
        # return render (request, 'FEEDBACK/feedback/feedback_list.html',)

    form = FeedbackSubmission(instance=feedback)
    context = {
        'form': form
    }
    return render(request, 'FEEDBACK/feedback/feedback_edit.html', context)
