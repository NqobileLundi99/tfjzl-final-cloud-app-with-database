from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'onlinecourse'

urlpatterns = [
    # Course list page
    path(
        route='',
        view=views.CourseListView.as_view(),
        name='index'
    ),

    # Authentication
    path(
        'registration/',
        views.registration_request,
        name='registration'
    ),
    path(
        'login/',
        views.login_request,
        name='login'
    ),
    path(
        'logout/',
        views.logout_request,
        name='logout'
    ),

    # Course detail page
    # Example: /5/
    path(
        '<int:pk>/',
        views.CourseDetailView.as_view(),
        name='course_details'
    ),

    # Enroll in a course
    # Example: /5/enroll/
    path(
        '<int:course_id>/enroll/',
        views.enroll,
        name='enroll'
    ),

    # Submit exam
    # Example: /5/submit/
    path(
        '<int:course_id>/submit/',
        views.submit,
        name='submit'
    ),

    # Show exam result
    # Example: /5/submission/3/
    path(
        '<int:course_id>/submission/<int:submission_id>/',
        views.show_exam_result,
        name='show_exam_result'
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
