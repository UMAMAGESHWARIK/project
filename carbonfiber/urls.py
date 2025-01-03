from django.urls import path
from . import views

urlpatterns = [
           path('carbonhome/',views.carbonpage),
           path('carbonlogin/',views.carbonlogin),
           path('carbonlogout/',views.carbonlogout),
           path('carbonregister/',views.carbonregistration),
           path('viewcltcarbonreq/', views.viewcltcarbonreq),
           path('viewcltcarbondataset/<str:clientid>/', views.viewcltcarbondataset),
           path('carbonupload/', views.carbonuploaddataset),
           path('carbonprocessdata/', views.carbonprocessdataset),
           path('carbonprocessingdata/<str:orderid>/', views.carbonprocessing),
           path('carbonreport/', views.carbonreport),
           path('viewcarbonreport/<str:clientid>/', views.viewcarbonreport),
           path('Sendcarbonreport/<str:clientid>/', views.sendcarbonreport),


]
