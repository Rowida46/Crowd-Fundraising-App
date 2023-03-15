from django import forms
from ckeditor.widgets import CKEditorWidget


class CommentForm(forms.Form):
    comment_content = forms.CharField(
        label="add your comment", widget=CKEditorWidget(), min_length=1, max_length=100,
        error_messages={'required': "you can'tsubmit an empty comment"})
