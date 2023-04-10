from django import forms

class RegisterRoomForm(forms.Form):
    room_name = forms.CharField(label='email', required=True)
    password = forms.CharField(label='password', widget=forms.PasswordInput(), min_length=8, required=True)