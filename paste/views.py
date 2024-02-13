from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from .models import Snippet
from .forms import SnippetForm, SearchForm
# Create your views here.


def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            print('valid')
            search_token = form.cleaned_data['search']
            return redirect('view_paste', token=search_token)
    else:
        form = SearchForm()
    pastes = Snippet.public.all().order_by('-created_at')[:6]
    context = {'pastes': pastes, 'form': form}
    return render(request, 'index.html', context)


def view_paste(request, token):
    if token and len(token) == 15:
        try:
            paste = Snippet.objects.get(token__icontains=token)
            context = {'paste': paste}
        except Snippet.DoesNotExist:
            context = {'error': 'error occured'}
    return render(request, 'view_paste.html', context)


def create_paste(request):
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_paste', form.instance.token)
    else:
        form = SnippetForm()
    previous_url = request.META.get('HTTP_REFERER')
    context = {'form': form, 'previous_url': previous_url}
    return render(request, 'create_paste.html', context)


def edit_paste(request, token):
    try:
        paste = Snippet.objects.get(token=token, editable=True)
    except Snippet.DoesNotExist as e:
        return HttpResponseNotFound()
    if request.method == "POST":
        form = SnippetForm(request.POST, instance=paste)
        if form.is_valid():
            form.save()
            return redirect('view_paste', form.instance.token)
    else:
        form = SnippetForm(instance=paste)
    context = {'form': form, 'edit': True, 'paste': paste}
    return render(request, 'create_paste.html', context)
