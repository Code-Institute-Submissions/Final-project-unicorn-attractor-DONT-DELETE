from django import forms
from .models import Bug, BugComment, BugStatus

class New_posts(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('title', 'description')

class Bug_status(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('title','description', 'status')

class Comment_form(forms.ModelForm):
    class Meta:
        model = BugComment
        fields = ('comment',)


