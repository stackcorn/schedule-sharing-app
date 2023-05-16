from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login

from .forms import *
from .models import *


# Create your views here.
def signup(request):
    template_name = 'account/signup.html'
    form = SignupRoomForm(request.POST or None)
    params = {'form': form}
    if form.is_valid():
        # cleaned_data[フィールド名]で値をそれぞれ変数へ入れていく
        room_name = form.cleaned_data['room_name']
        password = form.cleaned_data['password']
        check_password = form.cleaned_data['check_password']
        # 設定したいpasswordと確認用passwordが一致しているか確認する
        if password == check_password:
            try:
                # User.objects.create_user()を実行した時点で、userは作成される
                # 変数名としてuserを使っているが、今回はusernameを部屋名（room_name）として使う
                # 部屋は部屋名とパスワードを持つ
                user = User.objects.create_user(
                    username=room_name, password=password)
                return redirect('account:signin')
            except IntegrityError:
                params['context'] = 'この部屋名はすでに登録されています'
                return render(request, template_name, params)
        else:
            params['context'] = 'パスワードが異なっています'
            return render(request, template_name, params)
    else:
        return render(request, template_name, params)


def signin(request):
    template_name = 'account/signin.html'
    form = SigninRoomForm(request.POST or None)
    params = {'form': form}
    if form.is_valid():
        room_name = form.cleaned_data['room_name']
        password = form.cleaned_data['password']
        user = authenticate(request, username=room_name, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success pag
            return redirect('schedule:schedule_list')
        else:
            # Return an 'invalid login' error message.
            params['context'] = '入室に失敗しました'
            return render(request, template_name, params)
    else:
        return render(request, template_name, params)
