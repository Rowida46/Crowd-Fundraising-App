from django import forms
from ckeditor.widgets import CKEditorWidget


class CommentForm(forms):
    comment_content = forms.CharField(
        label="your comment", widget=CKEditorWidget(), min_length=1, max_length=100, required=False,
        error_messages={'required': "you can'tsubmit an empty comment"})
