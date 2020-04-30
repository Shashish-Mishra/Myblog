from django.shortcuts import render
from .models import Blogpost
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'blog/home.html')

def index(request):
    myposts=Blogpost.objects.all()
    return render(request,'blog/blog.html',{'mypost':myposts})

def blogpost(request,id):
    p = Blogpost.objects.filter(post_id=id)[0]
    print(p)
    return render(request,'blog/blogpost.html',{'post':p})


'''def blog(request):
    if request.method=='POST':
        ftitle=request.POST.get('title','')
        fhead0=request.POST.get('head0','')
        fchead0=request.POST.get('chead0','')
        fhead1=request.POST.get('head1','')
        fchead1=request.POST.get('chead1','')
        fhead2=request.POST.get('head2','')
        fchead2=request.POST.get('chead2','')
        fauthor=request.POST.get('author','')
        dbpost=Blogpost(title=ftitle,head0=fhead0,chead0=fchead0,head1=fhead1,chead1=fchead1,head2=fhead2,chead2=fchead2,author=fauthor)
        print(ftitle)
        dbpost.save()


    return render(request,'blog/form.html')'''