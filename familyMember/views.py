from django.shortcuts import get_object_or_404, render
from .models import FamilyMember
from .forms import FamilyMemberForm
# Create your views here.


def createMemberView(request):
    myForm = FamilyMemberForm()
    if request.method == "POST":
        myForm = FamilyMemberForm(request.POST)
        if myForm.is_valid():
            FamilyMember.objects.create(**myForm.cleaned_data)
            print("good stuff")
        else: 
            print("Bad stuff")
            print(myForm.errors)
    context = {
        "form" : myForm
    }
    return render(request, "familyMembers/createMember.html", context)

def specificMemberView(request, id):
    obj = get_object_or_404(FamilyMember, id = id)
    context = {
        "object" : obj
    }
    return render(request, "familyMembers/specificMember.html", context)

def memberListView(request):
    queryset = FamilyMember.objects.all()
    print(queryset)
    context = {
        "objectList" : queryset
    }
    return render(request, "familyMembers/memberList.html", context)