from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record



class SignUpForm(UserCreationForm):
    email=forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    first_name=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name '}))
    last_name=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Lastname'}))
    
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')

    def __init__(self,*args,**kwargs):
        super(SignUpForm,self).__init__(*args,**kwargs)
        
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='Enter Username'
        self.fields['username'].widget.label=''
        self.fields['username'].help_text='<span class="form-text text-muted small"> Your Username should only have letters </span>'
            
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['placeholder']='Enter password'
        self.fields['password1'].widget.label=''
        self.fields['password1'].help_text='<span class="form-text text-muted small"> <ul> <li> Your password can\'t be too similar </li><li> Password should be nice and contain letters, numbers all mixed</li><li> It should be at least 8 letters long </li></ul></span>'
        
        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['placeholder']='Confirm password again '
        self.fields['password2'].widget.label=''
        self.fields['password2'].help_text='<span class="form-text text-muted small"> Your Password</span>'
            
   
   
class AddRecordForm(forms.ModelForm):
    first_name=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'Enter First name','class':'form-control'}))
    last_name=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'Enter Last name','class':'form-control'}))
    email=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'Enter Email Address','class':'form-control'}))
    phone=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'Enter Phone Number','class':'form-control'}))
    address=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'Enter your Address','class':'form-control'}))
    city=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'Enter your City','class':'form-control'}))
    state=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'Enter your State ','class':'form-control'}))
    zip_code=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'Enter Zip Code ','class':'form-control'}))
   
   
   
    class Meta:
        model=Record
        fields=('__all__')
        #exclude = ("user",)
        