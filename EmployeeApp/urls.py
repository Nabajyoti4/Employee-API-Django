from os import stat
from django.urls import path
from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('department/', views.departmentApi),
    path('department/<str:id>', views.departmentApi),
    path('employee/', views.employeeApi),
    path('employee/<str:id>', views.employeeApi),
    path('employee/SaveFile',views.SaveFile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)