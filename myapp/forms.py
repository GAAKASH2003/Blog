
from django import forms
from .models import *
from django import forms


class PostForm(forms.ModelForm):
    content=forms.CharField(widget=forms.Textarea(attrs={'rows':10}))
    
    class Meta:
      model = Post
      fields =('title','content')

class PostUpdateForm(forms.ModelForm):
  class Meta:
    model=Post
    fields=['title','content']
 
class CommentForm(forms.ModelForm):
  content=forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Add a comment here'}))
  class Meta:
    model=  Comment
    fields=('content',)