from django import forms
from .models import Snippet


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ['author', 'text', 'private', 'editable', 'language']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Author Field
        self.fields['author'].widget.attrs.update({
            'class': 'input input-bordered input-sm w-full max-w-xs bg-[#0d1117] text-[#c9d1d9] placeholder-[#8b949e] border border-[#30363d] rounded-md',
            'placeholder': 'Author',
        })
        
        # Text Field
        self.fields['text'].widget.attrs.update({
            'class': 'textarea textarea-bordered textarea-sm w-full p-2 bg-[#0d1117] text-[#c9d1d9] placeholder-[#8b949e] border border-[#30363d] rounded-md font-mono',
            'placeholder': 'Write your code or text',
        })
        
        # Private Checkbox
        self.fields['private'].widget.attrs.update({
            'class': 'checkbox checkbox-sm rounded-md border border-[#30363d] bg-[#0d1117] text-[#238636]',
        })
        
        # Editable Checkbox
        self.fields['editable'].widget.attrs.update({
            'class': 'checkbox checkbox-sm rounded-md border border-[#30363d] bg-[#0d1117] text-[#a371f7]',
        })


class SearchForm(forms.Form):
    search = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={
                             'class': 'input input-bordered w-full max-w-xs join-item',
                             'Placeholder': 'search eg. a14477ce-8t7b-4', 'pattern': '[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-4'}))

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
