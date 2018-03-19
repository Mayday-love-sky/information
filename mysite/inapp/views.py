from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import render


# Create your views here.
information_list=[{"inquiry":"111"},]

def index(request):
    if request.method=="POST":
        inquiry = request.POST.get("inquiry",None)
        temp = {"inquiry":inquiry}
        information_list.append(temp)
    return render(request,"index.html",{"data":information_list})
