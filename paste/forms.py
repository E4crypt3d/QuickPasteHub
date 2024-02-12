from django.forms import ModelForm, forms
from .models import Snippet


class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        fields = ['author', 'text', 'private', 'editable', 'language']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].widget.attrs['class'] = 'input input-bordered input-sm w-full max-w-xs'
        self.fields['author'].widget.attrs['Placeholder'] = 'Author'
        self.fields['text'].widget.attrs['class'] = 'textarea textarea-bordered textarea-sm w-full'
        self.fields['text'].widget.attrs['Placeholder'] = 'Write your code or text'
        # self.fields['language'].widget.attrs['class'] = 'select select-bordered w-full max-w-xs'
        self.fields['private'].widget.attrs['class'] = 'checkbox'
        self.fields['editable'].widget.attrs['class'] = 'checkbox'
