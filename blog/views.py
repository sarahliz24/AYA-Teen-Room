from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import Http404
from django.contrib import messages
from .models import FeedbackPost, FeedbackReply
from .forms import FeedbackSubmission, ReplyForm
from django.views.decorators.http import require_POST
from django.views.generic import ListView


def home_view(request):
    '''
    send user to home page
    '''
    return render(request, "blog/home.html", {})


def about(request):
    '''
    send user to about page
    '''
    return render(request, "blog/about.html")


def feedback_submission(request):
    '''
    Form for user to submit feedback
    '''
    form = FeedbackSubmission()
    if request.method == 'POST':
        feedback_added = False
        form = FeedbackSubmission(request.POST)
        # feedback_submission = FeedbackSubmission(instance=request.user, data=request.POST)
        if form.is_valid():
            feedback_added = True
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            ok_feedback = FeedbackPost.approved.all()
            messages.success(request, "Your feedback has been submitted")
            return render (request, 'blog/feedback_list.html',
                    {'ok_feedback': ok_feedback})
        else:
            messages.error(request, 'Oops, something went wrong!')
    else:
        form = FeedbackSubmission(instance=request.user)
    return render(request, 'blog/feedback_submission.html',
                  {'form': form, })


def feedback_list(request):
    '''
    Display list of feedback posts, excluding posts that
    have been dis-allowed
    '''
    ok_feedback = FeedbackPost.approved.all()
    return render (request, 'blog/feedback_list.html',
                    {'ok_feedback': ok_feedback})


def feedback_detail(request, slug):
    '''
    Display single feedback post to user
    '''
    feedback_post = get_object_or_404(FeedbackPost, slug=slug,
                                 feedback_approval=FeedbackPost.FeedbackApproval.OK)

    """ feedback_reply = feedback_post.feedback_reply.filter(allowed=True)
    form = ReplyForm() """

    return render(request, 'blog/feedback_detail.html',
                    {'feedback_post': feedback_post })


def feedback_edit(request, slug):
    '''
    Allow user to update feedback they have previously
    created
    '''
    feedback_post = get_object_or_404(FeedbackPost, slug=slug)
    feedback_added = False

    if request.method == 'POST' and feedback_post.author == request.user:
        form = FeedbackSubmission(request.POST, instance=feedback_post)
        if form.is_valid():
            feedback_added = True
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            # form.save()
            ok_feedback = FeedbackPost.approved.all()
            messages.success(request, "Your edit was successful")
            return render (request, 'blog/feedback_list.html',
                    {'ok_feedback': ok_feedback})   
        else:
            messages.error(request, 'Oops, something went wrong!')

    form = FeedbackSubmission(instance=feedback_post)
    context = {
        'form': form
    }
    return render(request, 'blog/feedback_edit.html', context)


def delete_feedback(request, slug):
    '''
    Allow user to delete own feedback post
    '''
    feedback = get_object_or_404(FeedbackPost, slug=slug)

    if request.method == 'POST':
        feedback.delete()
        ok_feedback = FeedbackPost.approved.all()
        messages.success(request, "Your deletion was successful")
        return render (request, 'blog/feedback_list.html',
            {'ok_feedback': ok_feedback})
    
    return render(request, 'blog/delete_feedback.html')
