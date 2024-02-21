from django.shortcuts import render
from django.http import HttpResponse
from .models import Member


# Create your views here.
def index(request):
    members = Member.objects.all()
    context = {"members": members}
    return render(request, "members/index.html", context)


def create(request):
    return render(request, "members/create.html")


def detail(request, member_id):
    return HttpResponse("details about one member")
