from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import login

# Create your views here.

def threads_list(request):
    thread = Tweet.objects.all().order_by('-created_at')
    return render(request, 'thread_list.html', {'thread': thread})

@login_required
def threads_create(request):
    if request.method == 'POST':
        thread_form = TweetForm(request.POST, request.FILES)
        if thread_form.is_valid():
            user = thread_form.save(commit=False)
            user.user = request.user
            user.save()
            return redirect('threads_list') 
    else:
        thread_form = TweetForm()
    return render(request, 'thread_form.html', {'thread_form': thread_form})

@login_required
def threads_edit(request, thread_id):
    thread = get_object_or_404(Tweet, pk = thread_id, user = request.user)
    if request.method == 'POST':
        thread_form = TweetForm(request.POST, request.FILES, instance= thread)
        if thread_form.is_valid():
            user = thread_form.save(commit=False)
            user.user = request.user
            user.save()
            return redirect('threads_list') 
    else:
        thread_form = TweetForm(instance=thread)
    return render(request, 'thread_form.html', {'thread_form': thread_form})

@login_required
def threads_delete(request, thread_id):
    thread = get_object_or_404(Tweet, pk = thread_id, user = request.user)
    if request.method == 'POST':
        thread.delete()
        return redirect('threads_list') 
    return render(request, 'thread_delete.html', {'thread': thread})

def register(request):
    if request.method == 'POST':
        thread_form = UserRegistrationForm(request.POST)
        if thread_form.is_valid():
            user = thread_form.save(commit=False)
            user.set_password(thread_form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('threads_list')
    else:
        thread_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'thread_form': thread_form})


def search_thread(request):
    query = request.GET.get('query')
    if query:
        threads = Tweet.objects.filter(text__icontains=query)
    else:
        threads = Tweet.objects.none()  # Empty queryset if no query

    context = {
        'query': query,
        'threads': threads,
    }
    return render(request, 'search_results.html', context)
