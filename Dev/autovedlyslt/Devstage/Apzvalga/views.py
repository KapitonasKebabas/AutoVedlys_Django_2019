from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import infoSustojimai as sustojimasSql
from datetime import date

# Create your views here.
def logInHtml(request):
    return render(request, 'logIn.html')
def registerHtml(request):
    return render(request, 'register.html')


def apzvalgaHtml(request):
    odometras = sustojimasSql.objects.last().odometras
    return render(request, 'apzvalga_vedlys_auto.html', {'odometras': odometras})
def papildymaHtml(request):
    odometras = sustojimasSql.objects.last().odometras
    sustojimai = sustojimasSql.objects.all()
    suma = 0
    sustojimaiPrideta = 0
    nuvaziuotasAtstumas = int(sustojimasSql.objects.last().odometras) - int(sustojimasSql.objects.first().odometras)
    atstumasPerDiena = int(nuvaziuotasAtstumas / int(sustojimasSql.objects.last().data.day - sustojimasSql.objects.first().data.day))
    for sustojimas in sustojimai:
        suma = suma + float(sustojimas.papildyta)
        sustojimaiPrideta = sustojimaiPrideta + 1
    
    
    return render(request, 'vedlys_auto_structure_entry.html', {
        'sustojimai': sustojimai, 
        'odometras': odometras, 
        'suma': round(suma,2), 
        'sustojimaiPrideta': sustojimaiPrideta,
        'nuvaziuotasAtstumas': nuvaziuotasAtstumas,
        'atstumasPerDiena': atstumasPerDiena
        })

def logIn(request):
    if request.user.is_authenticated:
        return render(request, 'apzvalga_vedlys_auto.html')
    else:
        if request.method == 'POST':

            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('apzvalgaHtml')
            else:
                messages.info(request,'wrong inputs')
                return redirect('/')

        else:
            return render(request, 'Login.html')
def register(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'user taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email is taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.info(request,'user created')
                return render(request, 'logIn.html')
                
        else:
            messages.info(request,'password not matched')
            return redirect('register')

    else:
        return render(request, 'register.html')
def logOut(request):
    auth.logout(request)
    return redirect('/')
def sustojimasAddHtml(request):
    today = date.today()
    return render(request, 'sustojimasAdd.html',{'today': today})
def sustojimasAdd(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            data = request.POST['data']
            papildyta = request.POST['papildyta']
            odometras = request.POST['odometras']
            suma = request.POST['suma']

            userId = auth.get_user(request)
            anketa = sustojimasSql(data=data,papildyta=papildyta,odometras=odometras,userID=userId,suma=suma)
            anketa.save()
            return render(request, 'vedlys_auto_structure_entry.html')
    else:
        return redirect('logIn')