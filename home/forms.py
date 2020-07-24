from django import forms
from .models import User
import bcrypt

class RegisterForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    confirm_pass = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Confirm Password'
    )
    class Meta:
        model = User
        fields = ('__all__')

    def save(self, commit=True):
        
        print(self.instance)
        m = super(RegisterForm, self).save(commit=False)
        m.password = bcrypt.hashpw(m.password.encode(), bcrypt.gensalt()).decode()
        m.save()
        return m