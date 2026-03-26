from django.urls import path
from .views import *

urlpatterns = [
    path('',home_page, name='home_page'),
    path('login_page/',login_page, name='login_page'),
    path('logout_page/',logout_page, name='logout_page'),
    # path('signup/', SignUpView.as_view(), name='signup'),

    path('faculty/create/',faculty_create, name='faculty_create'),
    path('faculty/<int:pk>/edit/',faculty_edit, name='faculty_edit'),
    path('faculty/<int:pk>/delete/',faculty_delete, name='faculty_delete'),
    path('faculty/list/',faculty_list, name='faculty_list'),


    path('kafedra/create/',kafedra_create, name='kafedra_create'),
    path('kafedra/<int:pk>/edit/',kafedra_edit, name='kafedra_edit'),
    path('kafedra/<int:pk>/delete/',kafedra_delete, name='kafedra_delete'),
    path('kafedra/list/',kafedra_list, name='kafedra_list'),


    path('groups/create/',groups_create, name='groups_create'),
    path('groups/<int:pk>/edit/',groups_edit, name='groups_edit'),
    path('groups/<int:pk>/delete/',groups_delete, name='groups_delete'),
    path('groups/list/',groups_list, name='groups_list'),

    path('students/create/', students_create, name='students_create'),
    path('students/<int:pk>/edit/', students_edit, name='students_edit'),
    path('students/<int:pk>/delete/', students_delete, name='students_delete'),
    path('students/list/', students_list, name='students_list'),

    path('subject/create/', subject_create, name='subject_create'),
    path('subject/<int:pk>/edit/', subject_edit, name='subject_edit'),
    path('subject/<int:pk>/delete/', subject_delete, name='subject_delete'),
    path('subject/list/', subject_list, name='subject_list'),

    path('teachers/create/', teachers_create, name='teachers_create'),
    path('teachers/<int:pk>/edit/', teachers_edit, name='teachers_edit'),
    path('teachers/<int:pk>/delete/',teachers_delete, name='teachers_delete'),
    path('teachers/list/', teachers_list, name='teachers_list'),
]