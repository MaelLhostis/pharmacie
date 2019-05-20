from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.shortcuts import get_object_or_404
import json


class Form(models.Model):

    name = models.CharField(max_length=250)

    @staticmethod
    def save_form(request):

        dict = {}
        dict['questions'] = []
        dict['choices'] = {}
        choice_key = ""

        for key in request.POST:

            if key == 'title':
                dict['title'] = request.POST[key]
            elif key[-1] == 'q':
                dict['questions'].append(request.POST[key])
            elif key[-1] == 'c':
                dict['choices'].setdefault(request.POST[key], [])
                choice_key = request.POST[key]
            elif key[-1] == 'r':
                dict['choices'][choice_key].append(request.POST[key])

        form = Form(name=dict["title"])
        form.save()

        for q in dict["questions"]:
            question = Question(form=form, question=q)
            question.save()

        for key in dict["choices"]:
            choice = Choice(form=form, question=key, choices=dict["choices"][key])
            choice.save()

    @staticmethod
    def get_form(form_id):
        form = get_object_or_404(Form, pk=form_id)
        context = {}
        context["form"] = (form.id, form.name)
        context["questions"] = []
        context["choices"] = []

        for question in Question.objects.filter(form_id=form.id).order_by("id"):
            context["questions"].append(("q" + str(question.id), question.question))

        for choice in Choice.objects.filter(form_id=form.id).order_by("id"):
            array = [("c" + str(choice.id), choice.question)]
            array = array + choice.choices
            context["choices"].append(array)
        return context

    @staticmethod
    def save_result(request, form_id):
        form = get_object_or_404(Form, pk=form_id)
        dict = {}
        dict["questions"] = []
        dict["choices"] = []

        for question in Question.objects.filter(form_id=form.id).order_by("id"):
            dict["questions"].append(
                (question.id, request.POST["q" + str(question.id)])
            )

        for choice in Choice.objects.filter(form_id=form.id).order_by("id"):
            dict["choices"].append((choice.id, request.POST["c" + str(choice.id)]))

        answer = Answer(form=form, json=json.dumps(dict))
        answer.save()

    @staticmethod
    def get_results(form_id):
        form = get_object_or_404(Form, pk=form_id)
        context = {}
        context["form"] = (form.id, form.name)
        context["questions"] = {}
        context["choices"] = {}

        for answers in Answer.objects.filter(form_id=form_id).order_by("id"):
            dict = json.loads(answers.json)
            for question in dict["questions"]:
                context["questions"].setdefault(
                    get_object_or_404(Question, pk=question[0]).question, []
                ).append(question[1])
            for choice in dict["choices"]:
                context["choices"].setdefault(
                    get_object_or_404(Choice, pk=choice[0]).question, []
                ).append(choice[1])
        return


class Question(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    question = models.CharField(max_length=250, default="")


class Choice(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    question = models.CharField(max_length=250)
    choices = ArrayField(models.CharField(max_length=250))


class Answer(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    json = models.CharField(max_length=250)
