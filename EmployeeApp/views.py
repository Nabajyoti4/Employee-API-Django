from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.response import Response

from EmployeeApp.models import Employees, Departments
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def employeeApi(request,id=0):
    if request.method == 'GET':
        try:
            employees = Employees.objects.all()
            Employees_serializer = EmployeeSerializer(employees, many=True)
            return JsonResponse(Employees_serializer.data, safe=False)
        except Exception as e:
            return JsonResponse("Failed to Fetch Employees", safe=False)

    elif request.method == 'POST':
        Employee_data = JSONParser().parse(request)
        Employees_serializer = EmployeeSerializer(data=Employee_data)
        if Employees_serializer.is_valid():
            Employees_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    
    elif request.method == 'PUT':
        Employee_data = JSONParser().parse(request)
        Employee = Employees.objects.get(EmployeeId=Employee_data['EmployeeId'])
        Employee_serializer=EmployeeSerializer(Employee, data=Employee_data)
        if Employee_serializer.is_valid():
            Employee_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)

    elif request.method == 'DELETE':
        Employee= Employees.objects.get(EmployeeId=id)
        Employee.delete()
        return JsonResponse("Deleted Succesfully", safe=False)



@csrf_exempt
def departmentApi(request,id=0):
    if request.method == 'GET':
        try:
            departments = Departments.objects.all()
            departments_serializer = DepartmentSerializer(departments, many=True)
            return JsonResponse(departments_serializer.data, safe=False)
        except Exception as e:
            return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department=Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        department_serializer=DepartmentSerializer(department, data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)

    elif request.method == 'DELETE':
        department=Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Succesfully", safe=False)



@csrf_exempt
def SaveFile(request):
    file = request.FILES['myFile']
    file_name = default_storage.save(file.name, file)

        
    


