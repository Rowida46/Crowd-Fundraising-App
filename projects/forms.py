from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Project
INPUT_CLASSES = 'text-info'
class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title',)
        fields = ('title','details','features','image','end_at','target_budget','slug',)
        labels={
            'title': ' Project Title',
        }
        error_messages={
            'title': {
            'required': 'Please enter a title for your project.',
            'max_length': 'Project title must be less than 50 characters.',
            'invalid': 'Project title must be alphanumeric and contain no spaces.',
            },

        }
        # widgets = {
        #     'category': forms.Select(attrs={
        #         'class': INPUT_CLASSES, 'required':True
        #     }),
        #      'title': forms.CharField(attrs={
        #         'class': INPUT_CLASSES, 'required':True
        #     }),
        #     'name': forms.TextInput(attrs={
        #         'class': INPUT_CLASSES
        #     }),
        #     'description': forms.Textarea(attrs={
        #         'class': INPUT_CLASSES
        #     }),
        #     'price': forms.TextInput(attrs={
        #         'class': INPUT_CLASSES
        #     }),
        #     'image': forms.FileInput(attrs={
        #         'class': INPUT_CLASSES
        #     })
        # }



        # widgets = {
            # 'title': forms.CharField(attrs={'placeholder': 'Your Name'}),
        #     'details': forms.Textarea(attrs={'placeholder': 'Your Description', 'class': 'form-control', 'id': 'exampleInputdescription'}),
        #     'features': forms.Textarea(attrs={'placeholder': 'Your Description', 'class': 'form-control', 'id': 'exampleInputdescription'}),
        #     'image': forms.ImageField(attrs={'class': 'form-control', 'id': 'exampleInputimage'}),
        #     'end_at':forms.DateTimeField(attrs={'class': 'form-control'}),
        #     'start_at':forms.DateTimeField(attrs={'class': 'form-control'}),
        #     'category': forms.Select(attrs={'class': 'form-control', 'id': 'exampleFormControlSelect1'}),
        #     'target_budget':forms.FloatField(attrs={'class': 'form-control'}),
        #     'tags':forms.MultiValueField(attrs={'class': 'form-control'}),
        #     'slug':forms.SlugField(attrs={'class': 'form-control'})
        # }

    #     class ImageForm(forms.Form):
    # image = forms.ImageField(
    #     widget = forms.FileInput(
    #         attrs = {"id" : "image_field" , # you can access your image field with this id for css styling . 
    #                 , style = "height: 100px ; width : 100px ; " # add style from here .
    #                 }
    #         )
