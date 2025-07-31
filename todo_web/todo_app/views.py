from django.shortcuts import render,redirect
from todo_app.models import test

def todo(request):
    data = test.objects.all()
    
    if request.method == 'POST':
        var1 = request.POST.get('startdete')
        var2 = request.POST.get('enddete')
        var3 = request.POST.get('taskname')
        
        test_instance = test(startdete = var1,enddete = var2,taskname  = var3)
        test_instance.save()
        return redirect('todo')
    return render (request,'todo.html',{'data':data})
    # return HttpResponse('This is to do!')
# Create your views here.

def edit(request,id):
    data = test.objects.get(id = id)
    data = test.objects.all()
    
    if request.method == 'POST':
        var1 = request.POST.get('startdete')
        var2 = request.POST.get('enddete')
        var3 = request.POST.get('taskname')
        
        # test_instance = test(startdete = var1,enddete = var2,taskname  = var3)
        # test_instance.save()
        data.startdete = var1
        data.enddete = var2
        data.taskname = var3
        data.save()
        
        return redirect('todo')
    return render (request,'edit.html',{'data':data})

def delete(request,id):
    data= test.objects.get(id = id)
    data.delete()
    return redirect('todo')
    