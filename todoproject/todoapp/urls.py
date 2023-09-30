from . import views
from django.urls import path,include

urlpatterns = [

    path('',views.home,name='home'),
    #path('details',views.details,name='details')
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('edit/<int:taskid>/',views.update,name='update'),
    path('cltask/',views.Taklistview.as_view(),name='cltask'),
    path('cldetail/<int:pk>/',views.Taskdetailview.as_view(),name='cldetail'),
    path('clupdate/<int:pk>/',views.Taskupdateview.as_view(),name='clupdate'),
    path('cldelete/<int:pk>/',views.Taskdeleteview.as_view(),name='cldelete'),
]
