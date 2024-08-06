# This file defines the forms used in the application
# Forms are used to collect and validate user input

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import Event, Message , DUBLIN_LOCATIONS

# Get the custom user model
User = get_user_model()

# This form is used for user registration

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')
    bio = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows': 3}), required=False)
    profile_picture = forms.ImageField(required=False)
    contact_phone = forms.CharField(max_length=15, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'profile_picture', 'bio', 'contact_phone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields['profile_picture'].widget.attrs.update({'class': 'form-control-file'})

# This form is used for updating user profiles

class UserUpdateForm(UserChangeForm):
    password = None

    bio = forms.CharField(
        max_length=500, 
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        required=False
    )
    profile_picture = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control'}),
        required=False
    )
    contact_phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'profile_picture', 'bio', 'contact_phone')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password', None)
          
# This form is used for searching events
class EventSearchForm(forms.Form):
    query = forms.CharField(required=False, label='Search', widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.ChoiceField(
        choices=[('', 'All')] + Event.CATEGORY_CHOICES, 
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    start_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    end_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    location = forms.ChoiceField(
        choices=[('', 'All')] + DUBLIN_LOCATIONS,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    
# This form is used for creating and updating events

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'start_time', 'end_time', 'location', 'entrance', 'status', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'start_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'entrance': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'
                
                
# This form is used for composing messages
class ComposeMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        # Specify which fields to include in the form
        fields = ['receiver', 'subject', 'body']