from django.shortcuts import render
from app.models import *
# Create your views here.

def dept(request):
    LOA=DEPT.objects.all()
    d={'data':LOA}
    return render(request,'dept.html',d)
def emp(request):
    LOM=EMP.objects.all()
    d={'enm':LOM}
    return render(request,'emp.html',d)