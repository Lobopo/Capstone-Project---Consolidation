
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.contrib.auth.decorators import login_required

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

def vote(request, question_id):
    """
    Handle voting for a specific question.

    This view processes the user's choice for a question, increments the 
    vote count for the selected choice, and redirects to the results page. 
    If no choice is selected, it re-renders the question detail page with 
    an error message.

    Args:
        request (HttpRequest): The HTTP request object containing POST data.
        question_id (int): The ID of the question being voted on.

    Returns:
        HttpResponseRedirect: Redirect to the results page after a successful vote.
        HttpResponse: Re-renders the question detail page with an error message 
                      if no choice is selected.
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    """
    Display voting results for a specific question.

    This view fetches a question by its ID and renders the voting results 
    in the 'polls/results.html' template.

    Args:
        request (HttpRequest): The HTTP request object.
        question_id (int): The ID of the question for which to display results.

    Returns:
        HttpResponse: Rendered HTML page displaying the question results.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
