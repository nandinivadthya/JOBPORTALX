from django.urls import path
from .views import (
    home,
    register_view,
    login_view,
    logout_view,
    employee_dashboard,
    recruiter_dashboard,
    upload_job,
    edit_job,
    delete_job,
    apply_job,
    view_applicants,
    update_application_status,
    view_application_details,
    serve_resume,
)

urlpatterns = [
    path('', home, name="home"),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('employee/dashboard/', employee_dashboard, name='employee_dashboard'),
    path('recruiter/dashboard/', recruiter_dashboard, name='recruiter_dashboard'),
    path('upload/job/', upload_job, name='upload_job'),
    path('edit/job/<int:job_id>/', edit_job, name='edit_job'),
    path('delete/job/<int:job_id>/', delete_job, name='delete_job'),
    path('apply/job/<int:job_id>/', apply_job, name='apply_job'),
    path('view/applicants/<int:job_id>/', view_applicants, name='view_applicants'),
    path('update/application/<int:application_id>/<str:status>/', update_application_status, name='update_application_status'),
    path('view/application/<int:application_id>/', view_application_details, name='view_application_details'),
    path('application/<int:application_id>/resume/', serve_resume, name='serve_resume'),
]
