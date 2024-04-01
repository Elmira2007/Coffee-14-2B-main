from django.shortcuts import render
from apps.base.models import InfoUser,Secondary,Testim
from apps.secondary.models import News, Portfolio
from apps.contacts.models import  Contacts

# Create your views here.
def index(request):
    infouser = InfoUser.objects.latest("id")
    secondary = Secondary.objects.latest("id")
    testim  = Testim.objects.all()
    news = News.objects.all()
    portfolio = Portfolio.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        result = Contacts.objects.create(name = name,email = email, subject = subject,message = message)
    return render(request, "index.html",locals())

def news_detail(request,id):
    news = News.objects.get(id=id)
    return render(request,"blog-details.html", locals())