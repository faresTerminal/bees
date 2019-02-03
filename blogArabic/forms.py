from django import forms
from django.db import models


from blogArabic.models import articles, author, comment_put, MyltiImage
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm



# add multy fields to register page
class MyRegistrationForm(UserCreationForm):
   
   email = forms.EmailField(required = True)
  
  


   class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

   def save(self, commit = True):
        user = super(MyRegistrationForm, self).save(commit = False)
       
        user.email = self.cleaned_data['email']
       

        if commit:
                user.save()
        return user 

   def clean_email(self):
      email = self.cleaned_data['email']
      qs = User.objects.filter(email = email)
      if qs.exists():
          raise ValidationError ('Email is already registed')
      return email


   def check_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            raise ValidationError("There is no user registered with the specified email address!")

        return email 



class createForm(forms.ModelForm):
    class Meta:
        model = articles
        fields = [
            'category',
            'title',
            'image',
            'body',
            'prix', 
            'prix_colobal', 
            'number', 
            'wilaya', 
            'baladiya'

            
        ]
class createAuthor(forms.ModelForm):
    class Meta:
        model = author
        fields = [
            'profile_picture',
            'pays',
            'firstname',
            'email',
            'relation',
            'pays',
        ]

class CommentForm(forms.ModelForm):

        class Meta:
                model = comment_put
                fields =[
                 'comment',
                 
                ]


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')    
    class Meta:
        model = MyltiImage
        fields = ('image', )