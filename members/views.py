from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Member, Team
from .forms import MemberForm


# Create your views here.
def index(request):
    members = Member.objects.all()
    context = {"members": members}
    return render(request, "members/index.html", context)


def create(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            phone_number = form.cleaned_data["phone_number"]
            role = form.cleaned_data["role"]
            team = Team.objects.first()
            member = Member(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                role=role,
                team=team,
            )
            member.save()

        return HttpResponseRedirect("/members")
    return render(request, "members/create.html")


def detail(request, member_id):
    return HttpResponse("details about one member")
