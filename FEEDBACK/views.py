from django.shortcuts import render, get_object_or_404
from django.http import Http404
# from django.views import generic
from .models import Feedback, FeedbackReply
from .forms import ReplyForm
from django.views.decorators.http import require_POST


def home_view(request):
    return render(request, "FEEDBACK/home.html", {})


def feedback_list(request):
    ok_feedback = Feedback.approved.all()
    return render (request, 'FEEDBACK/feedback/feedback_list.html',
                    {'ok_feedback': ok_feedback})


def feedback_detail(request, id):
    feedback = get_object_or_404(Feedback, id=id,
                                 feedback_approval=Feedback.FeedbackApproval.OK)
    feedback_reply = feedback.feedback_reply.filter(allowed=True)
    form = FeedbackReply()
    return render(request, 'FEEDBACK/feedback/feedback_detail.html',
                    {'feedback': feedback,
                     'feedback_reply': feedback_reply,
                     'form': form
                    })


@require_POST
def post_reply(request, post_id):
    feedback = get_object_or_404(Post, id=post_id, feedback_approval=Post.FeedbackApproval.OK)
    reply = None
    form = reply_form(data=request.POST)
    if form.is_valid():
        reply = form.save(commit=False)
        reply.feedback = feedback
        reply.save()
    return render(request, 'feedback/reply.html',
                  {'feedback': feedback,
                   'form': form,
                   'reply': reply})