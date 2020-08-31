from django.urls import path, include
from . import views

urlpatterns = [
    path('manager/list/', views.Manager_list, name="manager_list"),
    path('manager/group/', views.Manager_Group, name="manager_group"),
    path('manager/group/add/', views.Manager_Group_Add, name="manager_group_add"),
    path('manager/del/<int:pk>', views.Manager_Del, name="manager_del"),
    path('manager/group/show/<int:pk>', views.Users_Groups, name="users_group"),
    path('manager/add/group/<int:pk>', views.Add_Users_to_Groups, name="add_users_to_groups"),
    path('manager/del/group/<int:pk>/<str:name>', views.Del_Users_to_Groups, name="del_users_to_groups"),
    path('manager/group/del/<str:name>', views.Manager_Group_Del, name="manager_group_del"),
    path('manager/perms/', views.Manager_Perms, name="manager_perms"),
    path('manager/perms/add/', views.Manager_Perms_Add, name="manager_perms_add"),
    path('manager/perms/del/<str:name>', views.Manager_Perms_Del, name="manager_perms_del"),
    path('manager/perms/user/<int:pk>', views.Users_Perms, name="users_perms"),
    path('manager/del/user/perms/<int:pk>/<str:name>', views.Users_Perms_Del, name="users_perms_del"),
    path('manager/add/user/perms/<int:pk>', views.Users_Perms_Add, name="users_perms_add"),
    path('manager/perms/group/<str:name>', views.Groups_Perms, name="groups_perms"),
    path('manager/perms/group/add/<str:name>', views.Groups_Perms_Add, name="groups_perms_add"),
    # path('manager/del/group/perms/<str:name>/<str:name>', views.Groups_Perms_Del, name="groups_perms_del"),

]
