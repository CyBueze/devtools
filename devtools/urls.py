from django.urls import path
from .views import DevToolList, DevToolDetail


urlpatterns = [
  path('devtools/', DevToolList.as_view(), name = 'devtool_list'),
  path('devtools/<int:pk>', DevToolDetail.as_view(), name = 'devtool_detail')
]
