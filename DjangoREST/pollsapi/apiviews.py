from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status

from .models import Poll,Choice,Vote
from.Serializers import PollSerializers,ChoiceSerializers,VoteSerializers

class PollList(APIView):
    def get(self,request):
        polls=Poll.objects.all()[:20]
        data=PollSerializers(polls,many=True).data
        return Response(data)

    def post(self, request):
        serializer = PollSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        poll = Poll.objects.get(pk=pk)
        serializer = PollSerializers(poll, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def update(self, request,pk):
        poll=Poll.objects.get(pk=pk)
        serializer = PollSerializers(data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_)

    def delete(self,request,pk):
        poll=get_object_or_404(Poll,pk=pk)
        poll.delete()
        print(f"Object {poll} deleted")
        return Response(status=status.HTTP_204_NO_CONTENT)

class PollDetail(APIView):
    # http_method_names=['GET', 'POST']
    def get(self,request,pk):
        poll=get_object_or_404(Poll,pk=pk)
        data=PollSerializers(poll).data
        return Response(data)