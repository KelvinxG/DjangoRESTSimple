from rest_framework import serializers

from .models import Choice,Poll,Vote




class VoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'

class ChoiceSerializers(serializers.ModelSerializer):
    votes=VoteSerializers(many=True,required=False)
    class Meta:
        model = Choice
        fields = '__all__'

class PollSerializers(serializers.ModelSerializer):
    choices= ChoiceSerializers(many=True,read_only=True,required=False)
    class Meta:
        model = Poll
        fields = '__all__'