from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Địa chỉ email'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tên của bạn '}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs.update({'autofocus': False})
        self.fields['username'].widget.attrs['placeholder'] = 'Tên tài khoản'
        self.fields['username'].label = 'Tên đăng nhập'
        self.fields['username'].help_text = ''
        
        self.fields['email'].help_text = '<span class="form-text text-muted"><small>Thông tin đơn hàng của bạn sẽ được gửi qua email này.</small></span>'
        self.fields['email'].label = 'Email của bạn'
        self.fields['first_name'].label = 'Tên của bạn'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Mật khẩu'
        self.fields['password1'].label = 'Mật khẩu'
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Mật khẩu không được quá giống các thông tin khác. </li><li>Mật khẩu phải có ít nhất 8 ký tự. </li><li>Không được là mật khẩu hay dùng như "password". </li><li>Mật khẩu không được hoàn toàn là số. </li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Nhập lại mật khẩu'
        self.fields['password2'].label = 'Nhập lại mật khẩu'
        self.fields['password2'].help_text = ''
            
