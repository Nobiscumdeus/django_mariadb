from django.shortcuts import render,redirect
from django.views.generic import ListView




# Create your views here.
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

class EnterView(ListView):
    model=Record
    template_name='customersite/index.html'

def login_user(request):
    #Check to see if loggin in 
    #records=Record.objects.all()

    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        #Authenticate 
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been logged in ")
            return redirect('customersite:enter')
            #return render(request,'customersite/index.html',{'records':records})
            
        else:
            messages.success(request,"Sorry, there was an error, try again !!!")
            return redirect('customersite:home')
    else:
        return render(request,'customersite/index.html',{
       # 'records':records # We show the records, since the user must be in already 
        })
        
        


def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out")
    return redirect("customersite:home")

def register_user(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)  #Send the post details to our signup form
        if form.is_valid():
            form.save()
            #Authenticate and log then in 
            username=form.cleaned_data['username']  #Th form.cleaned_data essentially allows to pull the username entry
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"You have been sucessfully registered")
            return redirect('customersite:home')
            
    else:
        form=SignUpForm() #Here we are not passing the request, since they are not filled yet 
        return render(request,'customersite/register.html',{'form':form})
    return render(request,'customersite/register.html',{'form':form}) #In case there is an error, this returns 
        


def customer_record(request,pk):
    if request.user.is_authenticated:
        customer_records=Record.objects.get(id=pk)
        return render(request,'customersite/detail.html',{'detail':customer_records})
    
    else:
        messages.success(request,"You must be logged in")
        return redirect('customersite:home')
    
def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_it=Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"Deleted Successfully")
        return redirect('customersite:enter')
        
    else:
        messages.success(request,"You must be logged in")
        return redirect('customersite:home')
        
        
def update_record(request,pk):
    if request.user.is_authenticated:
        current_record=Record.objects.get(id=pk)
        form=AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,'Records updated succesfully...')
            return redirect('customersite:enter')

        return render(request,'customersite/updaterecord.html',{'form':form})      
    else:
        messages.success(request,'You must be logged in ...')
        return redirect('customersite:home')  
        





def add_record(request):
    form=AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method=="POST":
            if form.is_valid():
                add_record=form.save()  #We don't need to call the model h=again sunce, its been inherited by the form itself in forms.py
                messages.success(request,"Record added successfully ...")
                return redirect('customersite:enter')
        return render(request,'customersite/addrecord.html',{'form':form})
    else:
        messages.success(request,'You must be logged in')
        return redirect('customersite:home')

   
        