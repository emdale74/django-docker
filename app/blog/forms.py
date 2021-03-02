from django import forms


class CommentForm(forms.Form):
    description = forms.CharField(widget=forms.Textarea)
    article_fk = forms.IntegerField(widget=forms.HiddenInput())


class EditArticle(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
