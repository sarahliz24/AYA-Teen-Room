from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import Http404
# from django.views import generic
from django.contrib import messages
from .models import FeedbackPost, FeedbackReply
from .forms import FeedbackSubmission, ReplyForm
from django.views.decorators.http import require_POST
from django.views.generic import ListView


def home_view(request):
    return render(request, "FEEDBACK/home.html", {})


def feedback_submission(request):
    '''
  
    '''
    form = FeedbackSubmission()
    if request.method == 'POST':
        form = FeedbackSubmission(request.POST)
        # feedback_submission = FeedbackSubmission(instance=request.user, data=request.POST)
        if form.is_valid():
            new_form = form.save()
            new_form.author = request.user
            new_form.save()
            # form.save()
            messages.success(request, "Your feedback has been submitted & is awaiting approval")
            ok_feedback = FeedbackPost.approved.all()
            return render (request, 'FEEDBACK/feedback/feedback_list.html',
                    {'ok_feedback': ok_feedback})
        else:
            messages.error(request, 'Oops, something went wrong!')
    else:
        form = FeedbackSubmission(instance=request.user)
    return render(request, 'FEEDBACK/feedback/feedback_submission.html',
                  {'form': form, })

""" def upload_video(request):
    if request.method == "POST":
        form = VideoPostForm(request.POST, request.FILES or None)
        if form.is_valid():
            new_videopost = form.save()
            new_videopost.author = request.user
            new_videopost.save()
            return redirect('home')
    else:
        form = VideoPostForm()
    return render(request, 'upload_video.html', {'form': form}) """


def feedback_list(request):
    ok_feedback = FeedbackPost.approved.all()
    return render (request, 'FEEDBACK/feedback/feedback_list.html',
                    {'ok_feedback': ok_feedback})


def feedback_detail(request, id):
    feedback = get_object_or_404(FeedbackPost, id=id,
                                 feedback_approval=FeedbackPost.FeedbackApproval.OK)
    feedback_reply = feedback.feedback_reply.filter(allowed=True)
    form = ReplyForm()
    return render(request, 'FEEDBACK/feedback/feedback_detail.html',
                    {'feedback': feedback,
                     'feedback_reply': feedback_reply,
                     'form': form
                    })


@require_POST
def post_reply(request, feedback_id):
    feedback = get_object_or_404(FeedbackPost, id=feedback_id, feedback_approval=FeedbackPost.FeedbackApproval.OK)
    reply = None
    form = ReplyForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = request.user.username
            reply = form.save(commit=False)
            reply.feedback = feedback
            reply.save()
            messages.success(request, "Your reply has been submitted & is awaiting approval")
            ok_feedback = FeedbackPost.approved.all()
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
    feedback = get_object_or_404(FeedbackPost, id=feedback_id)

    if request.method == 'POST' and feedback.author == request.user:
        form = FeedbackSubmission(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            messages.success(request, "Your feedback has been submitted & is awaiting approval")
            ok_feedback = FeedbackPost.approved.all()
            return render (request, 'FEEDBACK/feedback/feedback_list.html',
                    {'ok_feedback': ok_feedback})   
        else:
            messages.error(request, 'Oops, something went wrong!')

    form = FeedbackSubmission(instance=feedback)
    context = {
        'form': form
    }
    return render(request, 'FEEDBACK/feedback/feedback_edit.html', context)


def reply_edit(request, reply_id):
    '''
    Allow user to update reply they have previously
    created
    '''
    reply = get_object_or_404(FeedbackReply, id=reply_id)

    if request.method == 'POST' and reply.author == request.user:
        form = ReplyForm(request.POST, instance=reply)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.feedback = feedback
            reply.save()
            messages.success(request, "Your reply has been submitted & is awaiting approval")
            ok_feedback = Feedback.approved.all()
            return render (request, 'FEEDBACK/feedback/feedback_list.html',
                        {'ok_feedback': ok_feedback})
        else:
            messages.error(request, 'Oops, something went wrong!')
    # else:
        # form = FeedbackReply(instance=request.user)

    form = ReplyForm(instance=reply)
    context = {
        'form': form
    }
    return render(request, 'FEEDBACK/feedback/reply_edit.html', context)


def delete_feedback(request, feedback_id):
    '''
    Allow user to delete own feedback
    '''
    feedback = get_object_or_404(FeedbackPost, id=feedback_id)

    if request.method == 'POST':
        feedback.delete()
        return redirect(feedback_list)
    
    return render(request, 'FEEDBACK/feedback/delete_feedback.html')


def delete_reply(request, id):
    '''
    Allow user to delete own feedback reply
    '''

    reply = get_object_or_404(FeedbackReply, id=id)

    if request.method == 'POST':
        reply.delete()
        return redirect(feedback_list)
    
    return render(request, 'FEEDBACK/feedback/delete_reply.html')
