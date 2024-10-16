#DangoDBApp.urls

from django.urls import path
from .views import (
    ProgramAPIView,
    DepartmentAPIView, 
    StdntInfoAPIView,
    StudentPersonalDataAPIView,
    StudentFamilyAPIView,
    StudentAcademicBackgroundAPIView,
    StudentAcademicHistoryAPIView,
    StudentAddPersonalDataAPIView,
    StudentBasicInfoAPIView,
    EmailVerificationAPIView,
    BugReportAPIView,
    StudentOfficialInfoAPIView,
    
    )
from .Views_V2.StudentFullDataView import StudentDataAPIView

urlpatterns = [
    #Full Student Data
    path('full-student-data/', StudentDataAPIView.as_view(), name='full-student-data'),
    path('full-student-data', StudentDataAPIView.as_view(), name='full-student-data'),

    #Official student Data
    path('official-student-data/', StudentOfficialInfoAPIView.as_view(), name='official-student-data'),
    path('official-student-data', StudentOfficialInfoAPIView.as_view(), name='official-student-data'),
    
    
    
    #path('apimymodel/', TblProgramAPIView.as_view(), name='mymodel-list'),
    path('program/', ProgramAPIView.as_view(), name = 'program-list'),
    path('department/',DepartmentAPIView.as_view(), name = 'department-list'),
    path('student/', StdntInfoAPIView.as_view(), name = 'student-list'),

    path('emailapi', EmailVerificationAPIView.as_view(), name = 'email-verification'),


    path('personal-student-data/',StudentPersonalDataAPIView.as_view(),name = 'student-personal-list'),
    path('add-personal-data/',StudentAddPersonalDataAPIView.as_view(),name = 'add-personal-data'),
    path('stdntfamily/',StudentFamilyAPIView.as_view(),name = 'student-family-list'),
    path('stdntacademicbackground/',StudentAcademicBackgroundAPIView.as_view(),name = 'student-academicbackground-list'),
    path('stdntacademichistory/',StudentAcademicHistoryAPIView.as_view(),name = 'student-academichistory-list'),


    path('stdntbasicinfo',StudentBasicInfoAPIView.as_view(),name = 'student-basic-list'),
    path('stdntbasicinfo/',StudentBasicInfoAPIView.as_view(),name = 'student-basic-list'),

    path('bugs/', BugReportAPIView.as_view(), name= 'bug-report'),
    path('stdntofficialmod/<str:id_or_offercode>/<str:deactivate>',StudentBasicInfoAPIView.as_view(),name = 'student-official-info-mod'),
    path('deactivate_or_modify_program/<str:id_or_offercode>/<str:deactivate>', ProgramAPIView.as_view(), name='deactivate_modify_program-active'),
    path('deactivate_or_modify_department/<str:id_or_offercode>/<str:deactivate>', DepartmentAPIView.as_view(), name = 'deactivate_modify_department-active'),
    path('deactivate_or_modify_addstdntinfo/<str:id_or_offercode>/<str:deactivate>', StdntInfoAPIView.as_view(), name='deactivate_modify_addstdntinfo'),    
    
    path('deactivate_or_modify_personal-student-data/<str:id_or_offercode>/<str:deactivate>',StudentPersonalDataAPIView.as_view(),name = 'deactivate_or_modify_personal-student-data'),
    path('deactivate_or_modify_stdntfamily/<str:id_or_offercode>/str:deactivate',StudentFamilyAPIView.as_view(),name = 'dm-student-family'),
    path('deactivate_or_modify_stdntacademicbackground/<str:id_or_offercode>/str:deactivate',StudentAcademicBackgroundAPIView.as_view(),name = 'dm-student-academic-background'),
    path('deactivate_or_modify_stdntacademichistory/<str:id_or_offercode>/str:deactivate',StudentAcademicHistoryAPIView.as_view(),name = 'dm-student-academic-history'),
    
]   
