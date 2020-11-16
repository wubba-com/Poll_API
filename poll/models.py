from django.db import models


class Questions(models.Model):
    text_question = models.TextField('Вопрос')
    QUESTION_TYPE = [
        (1, 'Ответ текстом'),
        (2, 'Ответ с выбором одного варианта'),
        (3, 'Ответ с выбором нескольких вариантов'),
    ]
    question_type = models.IntegerField('Тип вопроса', choices=QUESTION_TYPE)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.text_question


class Polls(models.Model):
    name_poll = models.CharField('Название опроса', max_length=128, db_index=True)
    date_start = models.DateTimeField('Начало опроса')
    date_finish = models.DateTimeField('Конец опроса')
    description = models.TextField('Описание', default='')
    question = models.ManyToManyField(Questions, verbose_name='Вопросы', related_name='question_from_poll',
                                      blank=True)

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'
        ordering = ['-date_start']

    def __str__(self):
        return self.name_poll


class Choice(models.Model):
    question = models.ForeignKey(Questions, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'


class Answer(models.Model):
    user_id = models.IntegerField()
    poll = models.ForeignKey(Polls, on_delete=models.CASCADE, related_name='poll')
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='question_from_answer')
    choice = models.ForeignKey(Choice, related_name='choice', on_delete=models.CASCADE, null=True)
    choice_text = models.CharField('Ответ', max_length=256, default='')

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return self.choice_text
