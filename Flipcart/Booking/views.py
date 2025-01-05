from calendar import error
from itertools import count

from django.db.models.expressions import result
from django.http import HttpResponse
from django.shortcuts import render

from .models import emp


# Create your views here.
def show(request):
    return HttpResponse("<h2 > Welcome To Django </h2>")

def home(req):
    return render(req,'home.html')

def display(req):
    student_marks={'sid':101,'sname':'Vasanth','marks':[91,88,89]}
    return render(req,'display.html',student_marks)

def stdinfo(req):
    student_info={'sid':589,'sname':'Vasanth','gender':'M','course':'Python Full Stack'}
    return render(req,'studentinfo.html',student_info)

def sathyahome(req):
    return render(req,'sathyahome.html')

def register(req):
    return render(req,'register.html')

def login(req):
    return render(req,'login.html')

def welcome(req):
    a=req.GET.get('uname')
    return render(req,'welcome.html',{'uname':a})

def login2(req):
    return render(req,'login2.html')

def home2(req):
    return render(req,'home2.html')

def register2(req):
    return render(req,'register2.html')

def welcome2(req):
    a = req.POST.get('uname')
    b = req.POST.get('pwd')
    if (a=='vasanth' and b=='sathya'):
        return render(req,'welcome2.html',{'uname':a})

    else:
        return render(req,'invalid.html')

def invalid(req):
    return render(req,'invalid.html')

def registration(req):
    return render(req,'registration.html')

def details(req):
    a=req.POST.get('pid')
    b=req.POST.get('name')
    c = req.POST.get('dob')
    d = req.POST.get('age')
    e = req.POST.get('gender')
    f = req.POST.get('email')
    g = req.POST.get('city')
    h = req.POST.get('state')
    i = req.POST.getlist('hobbies')
    d1={'pid':a,'name':b,'dob':c,'age':d,'gender':e,'email':f,'city':g,'state':h,'hobbies':i}
    return render(req,'details.html',d1)

def salary(req, method=None):
    if method=='POST':
        a=int(req.POST.get('annualsalary'))
        b=a/12
        return render(req,'salary.html',)
    else:
        return render(req,'salary.html')

def big(req):
    d={'a':10,'b':187,'c':589}
    return render(req,'bignumber.html',d)

def checkticket(req):
    d1={'age':40}
    return render(req,'ticket.html',d1)

def studentmarks(req):
    d2={'sid':589,'sname':'Vasanth','marks':[88,89,35],'result':''}
    res='PASS'
    for i in d2['marks']:
        if i<35:
            res='FAIL'
            break
    d2['result']=res
    return render(req,'studentmarks.html',d2)

def employee(req):
    d3={'empdetails':[{'eid':589,'ename':'Vasanth','sal':40000},
                    {'eid':550,'ename':'Rohith','sal':35000}]}
    return render(req,'employee.html',d3)


def cal(req):
    if req.method=='POST':
        a=int(req.POST.get('num1'))
        b=int(req.POST.get('num2'))
        c= req.POST.get('cal')
        add = sub = mul = div = None
        err=''
        if c == 'ADD':
            result = a + b
            add = result
        elif c == 'SUB':
            result = a - b
            sub = result
        elif c == 'MUL':
            result = a * b
            mul = result
        elif c == 'DIV' and b != 0:
            result = a // b
            div = result
        else:
            result = ' Division by Zero is Possible'
            err=result
        return render(req, 'task.html', {'a':a,'b':b,'add': add,'sub': sub,'mul': mul,'div': div,'error':err})
    else:
        return render(req,'task.html')


def money(req):
    if req.method=='POST':
        a=req.POST.get('indmoney')
        b=req.POST.get('usamoney')
        result=''
        error=''
        if a and not b:
            a=int(a)
            result = a / 83
            return render(req, 'money.html', {'indmoney': a, 'usamoney': result, 'error': error})
        elif b and not a:
            b=int(b)
            result = b * 83
            return render(req, 'money.html', {'indmoney': result, 'usamoney': b, 'error': error})
        elif a and b:
            error = 'Please provide a value in either INR or USD'
        return render(req, 'money.html', {'indmoney': a, 'usamoney': result,'error': error})
    else:
        return render(req,'money.html')


def password(req):
    if req.method=='POST':
        a=req.POST.get('pwd')
        b=req.POST.get('cpwd')
        res=''
        if a == b :
            c='Thankyou..!'
            res=c
        else:
            error='Password and Confirm Password, Should be Same..!'
            res=error
        return render(req,'password.html',{'c':res})

    else:
        return render(req,'password.html')



def marks(req):
    if req.method=='POST':
        a=int(req.POST.get('sciencemarks'))
        result= ''
        if a < 35 :
            b='FAIL'
            result=b
        elif a > 35 and a <= 100:
            c='PASS'
            result=c
        else:
            d='Marks should be between 0 to 100 only..!0'
            result=d
        return render(req,'marks.html',{'result':result,'a':a})
    else:
        return render(req,'marks.html')



def register3(req):
    if req.method=='POST':
        a=req.POST.get('eid')
        b=req.POST.get('ename')
        c=req.POST.get('salary')
        d=req.POST.get('dno')
        e=emp(employee_id=a,employee_name=b,salary=c,dno=d)
        e.save()
        return render(req,'register3.html',{'msg':'Registered Successfully...!'})
    else:
        return render(req,'register3.html')

