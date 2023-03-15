from django import forms
from user.models import User
from django.contrib.auth import authenticate




class RegistraionForm():
    class Meta:
        model = User
        fields = ('email','username','first_name','last_name','phone','photo','password1','password2')
        
        
        
#==============================================================================================================

#===================================================================================================




class UpdateUserForm(forms.ModelForm):
    date_birth = forms.DateField(required=False)
    photo = forms.ImageField(required=False,widget=forms.FileInput)
    facebook_link = forms.URLField(required=False)
    country = forms.CharField(required=False)
    class Meta:
        model = User
        fields = ('first_name','last_name','phone','photo','date_birth','facebook_link','country')

    def clean_country(self):
        if self.is_valid():
            country = self.cleaned_data['country']
            if country:
                return country
            else :
                return None


    def clean_facebook_link(self):
        if self.is_valid():
            facebook_link = self.cleaned_data['facebook_link']
            if facebook_link:
                return facebook_link
            else :
                return None


    def clean_date_birth(self):
        if self.is_valid():
            date_birth = self.cleaned_data['date_birth']
            if date_birth:
                return date_birth
            else :
                return None
    
