from django import forms

from apps.main.models import Post




    
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=["title", "short_description", "full_description", "preview", "author" ,"category"]
        
        widgets={
            "title": forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"write title..."
            }),
            "short_description": forms.Textarea(attrs={
                "class":"form-control",
                "placeholder":"write short description..."
            }),
            "full_description": forms.Textarea(attrs={
                "class":"form-control",
                "placeholder":" full description..."
            }),
            "preview": forms.FileInput(attrs={
                "class":"form-control"
            }),
            "category":forms.Select(attrs={
                "class":"form-select"
            }),
            "author":forms.Select(attrs={
                "class":"form-select"
            })  
        }
