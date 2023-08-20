from django.shortcuts import render, get_object_or_404
from .models import Feedback, FeedbackReply
from .forms import ReplyForm
from django.views.decorators.http import require_POST

def feedback_list(request):
    ok_feedback = Feedback.approved.all()
    return render (request, 'feedback/feedback_list.html',
                    {'ok_feedback': ok_feedback})

def feedback_detail(request, id):
    feedback = get_object_or_404(Feedback, id=id,
                                 feedback_approval=Feedback.FeedbackApproval.OK)

    return render(request, 'feedback/feedback_detail.html',
                    {'feedback': feedback})

@require_POST
def post_reply(request, post_id):
    feedback = get_object_or_404(Post, id=post_id, feedback_approval=Post.FeedbackApproval.OK)
    reply = None
    form = reply_form(data=request.POST)
    if form.is_valid():
        reply = form.save(commit=False)
        reply.feedback = feedback
        reply.save()
    return render(request, 'FEEDBACK/feedback/reply.html',
                  {'feedback': feedback,
                   'form': form,
                   'reply': reply})