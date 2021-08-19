from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"add_student",views.StudentView)

urlpatterns = [
    # path('add_student',views.StudentView.as_view({'get':'list','post':'create'}) ,name="add_student"),
    path('', include(router.urls))
]
