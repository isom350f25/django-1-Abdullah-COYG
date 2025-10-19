from django.shortcuts import render

def myname_view(request):
    return render(request, "myname.html")

def myclasses_view(request):
    return render(request, "myclasses.html")

def link_view(request):
    return render(request, "link_view.html")
