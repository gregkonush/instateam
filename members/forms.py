from django import forms


class MemberForm(forms.Form):
    CHOICES = [("ADM", "Administrator"), ("REG", "Regular")]
    first_name = forms.CharField(label="First name", max_length=30)
    last_name = forms.CharField(label="Last name", max_length=30)
    email = forms.EmailField(max_length=256)
    phone_number = forms.CharField(max_length=50)
    role = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES,
    )
