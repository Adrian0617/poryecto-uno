from django import forms

class contactForm(forms.Form):
    name= forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder':"escribe tu nombre"}
    ), min_length=3, max_length=100)
    email= forms.EmailField(label="email", required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder':"escribe tu email"}
    ), min_length=3, max_length=100)
    mensaje= forms.CharField(label="mensaje", required=True, widget= forms.Textarea(
        attrs={'class': 'form-control', 'rows':3, 'placeholder':"escribe tu mensaje"}
    ), min_length=10, max_length=1000)