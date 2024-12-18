from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Question, Choice


@login_required
def index(request):
    """
    Display the latest 5 questions in the polls app.

    This view retrieves the 5 most recent questions based on the 'pub_date' field 
    and renders them in the 'polls/index.html' template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML page displaying the latest questions.
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    """
    Display details of a specific question.

    This view fetches a question by its ID and displays its details in 
    the 'polls/detail.html' template.

    Args:
        request (HttpRequest): The HTTP request object.
        question_id (int): The ID of the question to display.

    Returns:
        HttpResponse: Rendered HTML page displaying the question details.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
