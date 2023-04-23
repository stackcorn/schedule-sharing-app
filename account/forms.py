from django import forms

class SigninRoomForm(forms.Form):
    room_name = forms.CharField(label='email', required=True)
    password = forms.CharField(label='password', widget=forms.PasswordInput(), min_length=8, required=True)

class SignupRoomForm(SigninRoomForm):
    check_password = forms.CharField(label='password', widget=forms.PasswordInput(), min_length=8, required=True)