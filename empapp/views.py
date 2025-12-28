from django.shortcuts import render,HttpResponse
from .models import Employee
from datetime import datetime
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, 'index.html')


def allemp(request):
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    print(context)
    return render(request,'allemp.html',context)


def addemp(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        salary = request.POST['salary']
        bonus =int(request.POST['bonus'])
        phone =int(request.POST['phone'])
        dept = request.POST['dept']
        role = request.POST['role']
        location = request.POST['location']
        new_emp= Employee(firstname=firstname,lastname=lastname,salary=salary,bonus=bonus,phone=phone,dept=dept,role=role,location=location,hiredate=datetime.now())
        new_emp.save()
        return HttpResponse('Employee added Successfully')
    elif request.method =='GET':
        return  render(request,'addemp.html')
    else:
        return HttpResponse('An exception occured ! Employee')


def removeemp(request ,emp_id=0):
    if emp_id:
        try:
            emptoberemoved = Employee.objects.get(id=emp_id)
            emptoberemoved.delete()
            return HttpResponse('Employee removed successfully')
        except:
            return HttpResponse("Please Enter a Valid Emoloyee ID")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request,'removeemp.html', context)


def filteremp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        location = request.POST['location']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(firstname__icontains = name))
        if dept:
            emps = emps.filter(dept__icontains= dept)
        if role:
            emps = emps.filter(role__icontains=role)
        if location:
            emps = emps.filter(location__icontains=location)

        context ={
            'emps':emps
        }
        return render(request,'allemp.html',context)

    elif request.method == 'GET':
        return render(request,'filteremp.html')
    else:
        return HttpResponse('An Exception')
