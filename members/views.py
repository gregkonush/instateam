from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Member
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
            member = Member(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                role=role,
            )
            member.save()

        return HttpResponseRedirect("/members")
    return render(request, "members/create.html")


def edit(request, member_id):
    if request.method == "POST":

        if "delete" in request.POST:
            member = Member.objects.get(pk=member_id)
            member.delete()
            return HttpResponseRedirect("/members")

        form = MemberForm(request.POST)
        if form.is_valid():
            member = Member.objects.get(pk=member_id)
            member.first_name = form.cleaned_data["first_name"]
            member.last_name = form.cleaned_data["last_name"]
            member.email = form.cleaned_data["email"]
            member.phone_number = form.cleaned_data["phone_number"]
            member.role = form.cleaned_data["role"]
            member.save()

        return HttpResponseRedirect("/members")
    member = Member.objects.get(pk=member_id)
    context = {"member": member}
    return render(request, "members/edit.html", context)
