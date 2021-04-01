from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import link
import random
import string

def home(request):
    return render(request,'first.html')
def shorten(request):
    if(request.method=='POST'):
       new=link()
       new.long=request.POST['link']
       short= ''.join(random.choice(string.ascii_letters) for x in range(6))
       new.short=short
       new.save()
    return render(request,'first.html',{'text':short})
def urlRedirect(request,token):
    lng=link.objects.get(short=token)
    return redirect(lng.long)
