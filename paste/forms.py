from django import forms
from .models import Snippet


class SnippetForm(forms.ModelForm):
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


class SearchForm(forms.Form):
    search = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={
                             'class': 'input input-bordered w-full max-w-xs join-item', 'Placeholder': 'search your token'}))

    def clean_search(self):
        search_token = self.cleaned_data['search']
        if len(search_token) < 15:
            raise forms.ValidationError("Invalid token")
        try:
            Snippet.objects.get(token__icontains=search_token)
        except Snippet.DoesNotExist:
            raise forms.ValidationError(
                "Paste with this token does not exist.")
        return search_token
