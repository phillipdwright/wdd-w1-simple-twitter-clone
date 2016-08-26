from django.shortcuts import render

from .models import Tweet, User

# Create your views here.

def home(request):
    context = {'tweets': user_tweets}
    return render(request, 'twitter/feed.html', context)


def login(request):
    context = {}
    valid_data = validate_form_data(request.form)
    
    if valid_data:
        # Redirect to feed
        return render(request, 'twitter/feed.html', context)
    else:
        # Leave on the login page
        return render(request, 'twitter/login.html', context)

def profile(request):
    return render("Profile view")