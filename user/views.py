from django.shortcuts import render,redirect,reverse,get_object_or_404
# Create your views here.
from django.contrib.auth.models import User
from user.models import User
from django.shortcuts import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.views.generic.edit import UpdateView

from user.forms import RegistraionForm
from projects.models import Project


from user.forms import UpdaeData,OptionalData

    
    
# def showprofile(request,id):
#         user=get_object_or_404(User,id=id)
#         if user:
#             if request.method=='GET':
#                 # user=RegistraionForm(instance=request.user)
#                 return render(request,"profile.html",context={'user':user})
        
def showprofile(request, id):
    user = get_object_or_404(User,id=id)

    return render(request, "profile.html", context={'user': user})
             
 
 

 
 
        
        
        
def user_project(request,id):
    user=User.objects.get(id=id)
    project=Project.objects.filter(user=user)
    context={
        "user":user,
        "project":project
    }
    return render(request,'viewProject.html',context)
    
     



def delete_profile(request,id):
    user=User.objects.get(id=id)
    if request.method=='POST':
        user.delete()
        return redirect('donation')
    elif request.method=='GET':
        user.delete()
        return redirect('donation')
    
    



     
     
     
     
        
# def user_donation(request,id):
#     user=User.objects.get(id=id)
#     project=Donation.objects.filter(user=user)
#     context={
#         "user":user,
#         "project":project
#     }
#     return render(request,'viewProject.html',context)

        
                




# class Optional(UpdateView):
#     model=User
#     template_name="optional.html"
#     form_class=OptionalData
#     success_url="/profile"
    

    
    
    
    
    
    
    
    
    

def update(request, id ):
    post = User.objects.get(id=id)
    if request.method=='GET':
        postform = UpdaeData(instance=post)
        return render(request, 'editprofile.html', context={'form': postform})
    if request.method=='POST':
        postform = UpdaeData( request.POST, request.FILES, instance=post)
        if postform.is_valid():
            postform.save()
            return render(request,'profile.html',context={'user':post})
        return render(request,'profile.html',context={'user':post})
    
    
    
    

def optional(request, id ):
    post = User.objects.get(id=id)
    if request.method=='GET':
        postform = OptionalData(instance=post)
        return render(request, 'optional.html', context={'form': postform})
    if request.method=='POST':
        postform = OptionalData( request.POST, request.FILES, instance=post)
        if postform.is_valid():
            postform.save()
            return render(request,'profile.html',context={'user':post})
        return render(request,'profile.html',context={'user':post})