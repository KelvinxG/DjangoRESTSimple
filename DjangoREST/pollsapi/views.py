from django.shortcuts import render,HttpResponse,get_object_or_404
from django.http import JsonResponse
import datetime
from .models import Poll
from .apiviews import PollSerializers
# Create your views here.
from rest_framework.decorators import api_view





def index(request):
    return HttpResponse("<html><body> <h1>Welcome to the poll project <a href='polls/'>See the poll</a></h1></body></html")

@api_view(['POST'])
def polls_list(request):
    MAX_OBJECTS=20
    polls=Poll.objects.all()[:MAX_OBJECTS]
    try:
        data={"results": list(polls.values("question","created_by__username","pub_date"))}
    except Poll.DoesNotExist:
        data={"results": "Poll does not exist"}
        print("No results")
    return JsonResponse(data)

def polls_detail(request,pk):
    poll=get_object_or_404(Poll,pk=pk)
    try:
        data={"results":{
            "question":poll.question,
            "created_by":poll.created_by.username,
            "pub_date":poll.pub_date,
        }}
    except Poll.DoesNotExist:
        data={"results": "Poll does not exist"}
    return JsonResponse(data)