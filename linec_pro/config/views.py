from django.shortcuts import render
from django.views import generic
# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'index.html'


def AnswerView(request):
    if request.GET.get('your_name')=="a":
        return render(request, 'answer.html')
    elif request.GET.get('your_name')=="b":
        return render(request, 'answer1.html')
    else:
        return render(request, 'answer2.html')