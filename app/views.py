from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
# Create your views here.
from django.db.models import Q

def dept(request):
    LOA=DEPT.objects.all() #It will fetch all the data
    LOA=DEPT.objects.order_by('loc')  #it will arrange the data  in assecding order according to location based on asci values 
    LOA=DEPT.objects.order_by('-loc') #it will arrange the data  in descending order according to location based on asci values
    LOA=DEPT.objects.order_by(Length('loc')) #it will arrange the data  in assecding order according to location based on its length
    LOA=DEPT.objects.order_by(Length('loc').desc()) #it will arrange the data  in descending order according to location based on its length
    LOA=DEPT.objects.filter(deptno=10) # it will fetch only deptno 20 data
    LOA=DEPT.objects.exclude(deptno=10)  # it will fetch except deptno 20 data
    LOA=DEPT.objects.filter(deptno__gt=20) #it will fetch grater then deptno 20 values
    LOA=DEPT.objects.filter(deptno__lt=30) #it will fetch  less then deptno 30 values
    LOA=DEPT.objects.filter(deptno__gte=20) #it will fetch deptno 20 and its grater then deptno 20 values
    LOA=DEPT.objects.filter(deptno__lte=20) #it will fetch deptno 20 and  less then deptno 20 values
    LOA=DEPT.objects.all()
    d={'data':LOA}
    return render(request,'dept.html',d)
def emp(request):
    LOM=EMP.objects.all()
    LOM=EMP.objects.filter(hiredate='1981-2-20') # it will fetch who are joined in that specific date
    LOM=EMP.objects.exclude(hiredate='1981-2-20') # it will fetch whon not joined in that specific date
    LOM=EMP.objects.filter(hiredate__year='1982') # it will fetch who joined in 1982 only
    LOM=EMP.objects.filter(hiredate__month='5')  # it will fetch who are joined in specified month(5=MAY) ,it cannot care about day or year
    LOM=EMP.objects.filter(hiredate__day='17') # it will fect who are joined in sepecified day(17),it cannot care about year or month
    LOM=EMP.objects.filter(job__startswith='s') #it will fetch who's job starts with 's' 
    LOM=EMP.objects.filter(job__startswith='S') # it will fetch who's job starts with 's'
        #above two statments will give same answere because django is case sensitive only but your sql records are case-insensitive for only starts,ends,contains
    LOM=EMP.objects.filter(job__endswith='k') # it will fetch who's job end with 'k'
    LOM=EMP.objects.filter(job__contains='r') # it will fetch who's job having the character k
    LOM=EMP.objects.filter(ename__in=('SMITH','ALLEN','KING')) #it will fetch only smith,allen,king data
    LOM=EMP.objects.filter(Q(sal__gt=800) & Q(sal__lt=2000)) #it will fetch the data whose salary is grater then 800 and less then 2000
    LOM=EMP.objects.filter(Q(sal__gt=800) & Q(sal__lt=2000) & Q(job='CLERK')) #it will fetch the data whose salary is grater then 800 and less then 2000 and job = clerk
    LOM=EMP.objects.filter(sal__regex='3[0-9]{3}')   #it will fetch whose salary is starts with 3 and after 3 which have 3 charachters 
    LOM=EMP.objects.filter(job__regex='S[A-Z]{6}N')   #it will fetch whose job is starts with S and ends with N and which contains 6 characters between
    LOM=EMP.objects.all()[0:6] # it will give first 6 records 
    LOM=EMP.objects.all()[0:6:2] # it will fetch 3 reconda starts with 0 and step value is 2 i.e i will give 0th and 3rd and 5th row 
    LOM=EMP.objects.all()
    d={'enm':LOM}
    return render(request,'emp.html',d)




    '''LOW=Webpage.objects.filter(name__regex='[a-zA-Z]{7}')
    LOW=Webpage.objects.filter(Q(topic_name='Cricket') & Q(name='dhoni'))
'''