from django.shortcuts import render, get_object_or_404
from .models import Feedback

def feedback_list(request):
    ok_feedback = Feedback.approved.all()
    return render (request, 'feedback/feedback_list.html',
                    {'ok_feedback': ok_feedback})

def feedback_detail(request, id):
    feedback = get_object_or_404(Feedback, id=id,
                                 feedback_approval=Feedback.FeedbackApproval.OK)

    return render(request, 'feedback/feedback_detail.html',
                    {'feedback': feedback})