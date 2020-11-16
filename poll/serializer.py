from rest_framework import serializers
from .models import Polls, Questions, Answer, Choice


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'


class PollListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polls
        fields = ('id', 'name_poll')


class PollDetailSerializer(serializers.ModelSerializer):
    question = serializers.SlugRelatedField(slug_field='text_question', read_only=True, many=True)

    class Meta:
        model = Polls
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polls
        fields = '__all__'

    def update(self, instance, validated_data):
        if validated_data['question']:
            raise serializers.ValidationError({'Error': 'Вы не можете изменить вопросы после создания'})
        instance.name_poll = validated_data.get('name_poll', instance.name_poll)
        instance.date_start = validated_data.get('date_start', instance.date_start)
        instance.date_finish = validated_data.get('date_finish', instance.date_finish)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class CurrentUserDefault(object):
    def set_context(self, serializer_field):
        self.user_id = serializer_field.context['request'].user.id

    def __call__(self):
        return self.user_id


class AnswerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(default=CurrentUserDefault())
    poll = serializers.SlugRelatedField(slug_field='id', queryset=Polls.objects.all())
    question = serializers.SlugRelatedField(slug_field='id', queryset=Questions.objects.all())
    choice = serializers.SlugRelatedField(queryset=Choice.objects.all(), slug_field='id', allow_null=True)
    choice_text = serializers.CharField(max_length=200, required=False, allow_null=True)

    class Meta:
        model = Answer
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    question = serializers.SlugRelatedField(slug_field='text_question', read_only=True)

    class Meta:
        model = Choice
        fields = '__all__'
