from django.shortcuts import render
from . models import employeeinfo

# Create your views here.

def index(request):
    return render(request, 'index.html')


def empEntry(request):
    return render(request, 'form.html')


def empRecord(request):
    data = employeeinfo.objects.all()[0:]
    return render(request, 'records.html', {'data': data}) 


def empStore(request):
    if request.method == "POST":
        empID = request.POST.get('empID')
        if employeeinfo.objects.filter(emp_id = empID).exists():
            msgbox = f'already added this id {empID}'
            data = employeeinfo.objects.all()[0:]
            return render(request, 'records.html', {'msgbox': msgbox, 'data': data})        

        else:
            empName= request.POST.get('empName')
            empAddress= request.POST.get('empAddress')
            empEmail= request.POST.get('empEmail')
            empPhone= request.POST.get('empPhone')
            employeeinfo.objects.create(emp_id=empID, emp_name=empName, emp_address=empAddress, emp_email=empEmail,emp_phone=empPhone  )
            msgbox = f'emplyee id: {empID} has been added succesfuly'
            data = employeeinfo.objects.all()[0:]
            return render(request, 'records.html', {'msgbox': msgbox, 'data': data})        
    return render(request, 'index.html')