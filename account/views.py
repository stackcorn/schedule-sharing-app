from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login

from .forms import *
from .models import *

# Create your views here.
def signup_view(request):
    template_name = 'account/signup.html'
    form = SignInAndSignUpForm(request.POST or None)
    params = {'form': form}
    if form.is_valid():
        # cleaned_data[フィールド名]で値をそれぞれ変数へ入れていく
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        try:
            # User.objects.create_user()を実行した時点で、userは作成される
            # ここではemailをusernameに入れている
            user = User.objects.create_user(username=email, password=password)
            return redirect('account:signin')
        except IntegrityError:
            params['context'] = 'このユーザーはすでに登録されています'
            return render(request, template_name, params)
    else:
        return render(request, template_name, params)
    

def signin_view(request):
    template_name = 'account/signin.html'
    form = SignInAndSignUpForm(request.POST or None)
    params = {'form': form}
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success pag
            return redirect('plan:list')
        else:
            # Return an 'invalid login' error message.
            params['context'] = 'メールアドレス、またはパスワードが違います'
            return render(request, template_name, params)
        
    return render(request, template_name, params)