from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import Form


def index(request):
    template = loader.get_template("form/index.html")
    context = {}
    return HttpResponse(template.render(context, request))


def create_form(request):
    template = loader.get_template("form/create.html")
    #Form.create_form(request)
    context = {}
    return HttpResponse(template.render(context, request))

def save_form(request):

    Form.save_form(request)
    return HttpResponseRedirect("/form")

def show_form(request, form_id):

    context = Form.get_form(form_id)
    template = loader.get_template("form/form.html")
    return HttpResponse(template.render(context, request))


def save_result(request, form_id):

    Form.save_result(request, form_id)

    return HttpResponseRedirect("/form")


def show_result(request, form_id):

    context = Form.get_results(form_id)

    return HttpResponseRedirect("/form")
