from django.shortcuts import render, redirect
from .models import Manager
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType


# Create your views here.
def Manager_list(request):
    manager = Manager.objects.all()
    return render(request, 'back/manager_list.html', {'manager': manager})


def Manager_Del(request, pk):
    manager = Manager.objects.get(pk=pk)
    b = User.objects.filter(username=manager.utxt)
    b.delete()
    manager.delete()
    return redirect('manager_list')


def Manager_Group(request):
    # login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser': perm = 1

    if perm == 0:
        error = "Access Denied"
        return render(request, 'back/error.html', {'error': error})
    group = Group.objects.all().exclude(name="masteruser")
    # group = Group.objects.all()

    return render(request, 'back/manager_group.html', {'group': group})


def Manager_Group_Add(request):
    # login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser': perm = 1

    if perm == 0:
        error = "Access Denied"
        return render(request, 'back/error.html', {'error': error})
    if request.method == 'POST':
        name = request.POST.get('name')
        if name != "":
            if len(Group.objects.filter(name=name)) == 0:
                group = Group(name=name)
                group.save()

    return redirect('manager_group')


def Manager_Group_Del(request, name):
    # login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser': perm = 1

    if perm == 0:
        error = "Access Denied"
        return render(request, 'back/error.html', {'error': error})
    b = Group.objects.filter(name=name)
    b.delete()

    return redirect('manager_group')


def Users_Groups(request, pk):
    # login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser': perm = 1

    if perm == 0:
        error = "Access Denied"
        return render(request, 'back/error.html', {'error': error})
    manager = Manager.objects.get(pk=pk)
    user = User.objects.get(username=manager.utxt)
    ugroup = []
    for i in user.groups.all():
        ugroup.append(i.name)

    group = Group.objects.all()
    return render(request, 'back/users_groups.html', {'ugroup': ugroup, 'group': group, 'pk': pk})


def Add_Users_to_Groups(request, pk):
    # login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser': perm = 1

    if perm == 0:
        error = "Access Denied"
        return render(request, 'back/error.html', {'error': error})
    if request.method == 'POST':
        gname = request.POST.get('gname')
        group = Group.objects.get(name=gname)
        manager = Manager.objects.get(pk=pk)
        user = User.objects.get(username=manager.utxt)
        user.groups.add(group)
    return redirect('users_group', pk=pk)


def Del_Users_to_Groups(request, pk, name):
    # login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser': perm = 1

    if perm == 0:
        error = "Access Denied"
        return render(request, 'back/error.html', {'error': error})
    group = Group.objects.get(name=name)
    manager = Manager.objects.get(pk=pk)
    user = User.objects.get(username=manager.utxt)
    user.groups.remove(group)
    return redirect('users_group', pk=pk)


def Manager_Perms(request):
    # login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login check end
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser': perm = 1

    if perm == 0:
        error = "Access Denied"
        return render(request, 'back/error.html', {'error': error})
    perms = Permission.objects.all()

    return render(request, 'back/manager_perms.html', {'perms': perms})


def Manager_Perms_Del(request, name):
    # login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login check end
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser': perm = 1

    if perm == 0:
        error = "Access Denied"
        return render(request, 'back/error.html', {'error': error})
    perms = Permission.objects.filter(name=name)
    perms.delete()

    return redirect('manager_perms')


def Manager_Perms_Add(request):
    # login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser': perm = 1

    if perm == 0:
        error = "Access Denied"
        return render(request, 'back/error.html', {'error': error})

    if request.method == 'POST':
        name = request.POST.get('name')
        cname = request.POST.get('cname')
        if len(Permission.objects.filter(codename=cname)) == 0:
            content_type = ContentType.objects.get(app_label='manager', model='manager')
            permission = Permission.objects.create(codename=cname, name=name, content_type=content_type)
        else:
            error = "This Code name used before"
            return render(request, 'back/error.html', {'error': error})

    return redirect('manager_perms')


def Users_Perms(request, pk):
    # login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser': perm = 1

    if perm == 0:
        error = "Access Denied"
        return render(request, 'back/error.html', {'error': error})
    manager = Manager.objects.get(pk=pk)
    user = User.objects.get(username=manager.utxt)
    permission = Permission.objects.filter(user=user)
    uperms = []
    for i in permission:
        uperms.append(i.name)

    perms = Permission.objects.all()

    return render(request, 'back/users_perms.html', {'uperms': uperms, 'pk': pk, 'perms': perms})


def Users_Perms_Del(request, pk, name):
    # login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login check end
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser': perm = 1

    if perm == 0:
        error = "Access Denied"
        return render(request, 'back/error.html', {'error': error})
    manager = Manager.objects.get(pk=pk)
    user = User.objects.get(username=manager.utxt)
    permission = Permission.objects.get(name=name)
    user.user_permissions.remove(permission)

    return redirect('users_perms', pk=pk)


def Users_Perms_Add(request, pk):
    # login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login check end
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser': perm = 1

    if perm == 0:
        error = "Access Denied"
        return render(request, 'back/error.html', {'error': error})

    if request.method == 'POST':
        pname = request.POST.get('pname')
        manager = Manager.objects.get(pk=pk)
        user = User.objects.get(username=manager.utxt)
        permission = Permission.objects.get(name=pname)
        user.user_permissions.add(permission)

    return redirect('users_perms', pk=pk)


def Groups_Perms(request, name):
    # login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login check end
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser': perm = 1

    if perm == 0:
        error = "Access Denied"
        return render(request, 'back/error.html', {'error': error})

    group = Group.objects.get(name=name)
    perms = group.permissions.all()
    allperms = Permission.objects.all()

    return render(request, 'back/groups_perms.html', {'perms': perms, 'name': name, 'allperms': allperms})


# def Groups_Perms_Del(request, gname, name):
#     print(gname, name)
#     # login check start
#     if not request.user.is_authenticated:
#         return redirect('login')
#     # login check end
#     perm = 0
#     for i in request.user.groups.all():
#         if i.name == 'masteruser': perm = 1
#
#     if perm == 0:
#         error = "Access Denied"
#         return render(request, 'back/error.html', {'error': error})
#
#     group = Group.objects.get(name=gname)
#     perm = Permission.objects.get(name=name)
#     group.permissions.remove(perm)
#
#     return redirect('groups_perms', name=gname)


def Groups_Perms_Add(request, name):
    # login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login check end
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser': perm = 1

    if perm == 0:
        error = "Access Denied"
        return render(request, 'back/error.html', {'error': error})

    if request.method == 'POST':
        pname = request.POST.get('pname')

        group = Group.objects.get(name=name)
        perm = Permission.objects.get(name=pname)
        group.permissions.add(perm)

    return redirect('groups_perms', name=name)
