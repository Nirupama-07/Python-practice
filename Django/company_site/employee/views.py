from django.shortcuts import render, redirect
from .models import Employee

# Create your views here.
def employee_list(request):
    employees=Employee.objects.order_by("salary")
    active=Employee.objects.filter(status=True)
    inactive=Employee.objects.filter(status=False)
    

    context={
        "name":"Crushaders",
        "employees": employees,
        "count": employees.count(),
        "active":active.count(),
        "inactive":inactive.count()
        
    }
    return render(request,"employee.html",context)

def add_employee(request):
    if request.method=="POST":
        name=request.POST.get("name")
        department=request.POST.get("department")
        salary=request.POST.get("salary")
        status = "status" in request.POST
    
        Employee.objects.create(
            name=name,
            department=department,
            salary=salary,
            status=status
        )
        return redirect("employee:employee")
    
    return render(request, "add_Employee.html")

def view_employee(request,id):
    employee=Employee.objects.get(id=id)

    return render(request,"view_employee.html",{"employee":employee})

def delete_employee(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()

    return redirect("employee:employee")

def edit_employee(request,id):
    employee=Employee.objects.get(id=id)

    if request.method=="POST":
        employee.name=request.POST.get("name")
        employee.department=request.POST.get("department")
        employee.salary=request.POST.get("salary")
        employee.status="status" in request.POST

       
        employee.save()
        return redirect("employee:employee")


    return render(request,"edit_employee.html",{"employee":employee})