from django.shortcuts import render, redirect
from news_content.models import News
import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from manager.models import Manager
from django.contrib.auth.models import User, Group, Permission


def Panel(request):
    if not request.user.is_authenticated:
        return redirect('login')

    perm = 0
    parms = Permission.objects.filter(user=request.user)
    for i in parms:
        if i.codename == 'master_user': perm = 1

    if perm == 0:
        error = "Access Denied"
        return render(request, 'back/error.html', {'error': error})

    return render(request, 'back/home.html')


def News_List(request):
    if request.user.is_authenticated:
        news = News.objects.all()
    else:
        return redirect('login')

    return render(request, 'back/news_list.html', {'news': news})


def Add_News(request):
    if request.user.is_authenticated:
        now = datetime.datetime.now()

        year = now.year
        month = now.month
        day = now.day

        if len(str(day)) == 1:
            day = "0" + str(day)
        if len(str(month)) == 1:
            month = "0" + str(month)

        today = str(year) + "/" + str(month) + "/" + str(day)
        time = str(now.hour) + ":" + str(now.minute)
        if request.method == 'POST':
            newstitle = request.POST.get('newstitle')
            newstxtshort = request.POST.get('newstxtshort')
            newstxt = request.POST.get('newstxt')

            if newstitle == "" or newstxtshort == "" or newstxt == "":
                error = "All Fields Required"
                return render(request, 'back/error.html', {'error': error})

            b = News(name=newstitle, short_txt=newstxtshort, body_txt=newstxt, date=today, time=time,
                     writer=request.user, picname='-')
            b.save()
            return redirect('news_list')
    else:
        return redirect('login')

    return render(request, 'back/add_news.html')


def News_Publish(request, pk):
    news = News.objects.get(pk=pk)
    news.act = 1
    news.save()
    return redirect('news_list')


def Login(request):
    utxt = request.POST.get('username')
    ptxt = request.POST.get('password')
    if utxt != '' and ptxt != '':
        user = authenticate(username=utxt, password=ptxt)
        if user != None:
            login(request, user)
            return redirect('panel')

    return render(request, 'back/login.html')


def Logout(request):
    logout(request)
    return redirect('login')


def Register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if name == "":
            msg = "Please Input Your Name"
            return render(request, 'back/msgbox.html', {'msg': msg})
        if password1 != password2:
            msg = "Your Password Didn't Match"
            return render(request, 'back/msgbox.html', {'msg': msg})

        count1 = 0
        count2 = 0
        count3 = 0
        for i in password1:
            if "0" < i < "9":
                count1 = 1
            if "A" < i < "Z":
                count2 = 1
            if "a" < i < "z":
                count3 = 1

        if count1 == 0 or count2 == 0 or count3 == 0:
            msg = "Your Password Didn't Strong Enough"
            return render(request, 'back/msgbox.html', {'msg': msg})

        if len(password1) < 8:
            msg = "Your Password Must be Greater Than 8 Characters"
            return render(request, 'back/msgbox.html', {'msg': msg})

        if len(User.objects.filter(username=uname)) == 0 and len(User.objects.filter(email=email)) == 0:
            user = User.objects.create_user(username=uname, email=email, password=password1)
            b = Manager(name=name, utxt=uname, email=email)
            b.save()
        else:
            msg = "User already exists"
            return render(request, 'back/msgbox.html', {'msg': msg})

    return render(request, 'back/login.html')
