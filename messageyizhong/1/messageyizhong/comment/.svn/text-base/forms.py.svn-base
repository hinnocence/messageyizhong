from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(label='name', max_length=32)
    content = forms.CharField(widget=forms.Textarea)
    subject = forms.CharField(label='subject',max_length=50)
#    datetime = form.DateTimeField()    
