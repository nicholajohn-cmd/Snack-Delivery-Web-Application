from django import forms
from snacks.models import Regis1,Food1,payments
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Regis1
        fields = ['sName', 'eEmail', 'sphone', 'sAddress', 'sCode', 'sAgree']
class menuform(forms.ModelForm):
    class Meta:
        model= Food1
        fields=['ssnacks','veg_or_nonveg','description','price']
        


    # Optionally, you can add custom validation if needed.
    def clean_sPhone(self):
        phone = self.cleaned_data.get('sPhone')
        if len(phone) < 10:
            raise forms.ValidationError("Phone number should be at least 10 digits.")
        return phone
class paymentpg(forms.ModelForm):
    class Meta:
        model=payments
        fields='__all__'
