from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Article, Comment

class ArticleEditForm(forms.ModelForm):

    class Meta:

        CATEGORY = (
        )
        model = Article
        exclude = (
            'created_at', 
            'modified_at',
            'view_count', 
            # 'comment_count',
        )
        widgets = {
            # 'subject': forms.TextInput(
            #     attrs={'placeholder': _('Enter title here.')}
            # ),
            # 'reference': forms.TextInput(
            #     attrs={'placeholder': _('Add a reference URL.')}
            # ),
            # 'category': forms.Select(choices=CATEGORY),
            'content': SummernoteWidget(),
        }

    # def __init__(self, *args, **kwargs):
    #     """Init"""
    #     self.user = kwargs.pop('user', None)
    #     super(BoardEditForm, self).__init__(*args, **kwargs)

