from django.urls import path
from . import views

app_name="employee"

urlpatterns=[
    path("employee/",views.employee_list,name="employee"),
    path("employee/add/",views.add_employee,name="add_employee"),
    path("employee/<int:id>/",views.view_employee,name="view_employee"),
    path("delete/<int:id>/",views.delete_employee,name="delete_employee"),
    path("edit/<int:id>/",views.edit_employee,name="edit_employee")
]