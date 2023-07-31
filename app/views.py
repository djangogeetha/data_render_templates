from django.shortcuts import render

# Create your views here.

def  data_render(request):
    d={'name':'GEETHA','age':12,'hobbies':['dancing','signing']}
    return render(request,'data_render.html',context=d)
def conditions(request):
    d={'a':'500','b':700,'c':100}
    return render(request,'conditions.html',context=d)
