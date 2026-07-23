from django.shortcuts import render, redirect,get_object_or_404
from .models import Employee
from .forms import EmployeeForm

# Create your views here.
def employee_list(request):
    employees=Employee.objects.order_by("name","status")
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
    if(request.method=="POST"):
        form=EmployeeForm(request.POST)

        if form.is_valid():
            employee = form.save(commit=False)

            employee.status = False

            employee.save()
            return redirect("employee:employee")
    else:
        form=EmployeeForm()
    
    return render(request, "add_Employee.html",{"form":form})

def view_employee(request,id):
    employee=Employee.objects.get(id=id)

    return render(request,"view_employee.html",{"employee":employee})

def delete_employee(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()

    return redirect("employee:employee")

def edit_employee(request,id):
    employee = get_object_or_404(Employee, id=id)

    if request.method=="POST":
        form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            
            form.save()
            return redirect("employee:employee")

       
    else:
        form = EmployeeForm(instance=employee)


    return render(request,"edit_employee.html",{"employee":employee,"form":form})