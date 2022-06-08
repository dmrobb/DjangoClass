from django import forms
from .models import Review
from django.forms import ModelForm



# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label='First Name',max_length = 30)
#     last_name = forms.CharField(label='Last Name',max_length=30)
#     email = forms.EmailField(label='Email')
#     review = forms.CharField(label='Please write your review here.',
#                             widget=forms.Textarea(attrs={'class':"myform",
#                             'rows':'2','cols':'30'}))

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        #pass only certain fields
        # fields = ['first_name','last_name','stars'] #pass only certain fields
        #pass all fields
        fields = '__all__'
        labels = {
            'first_name': 'Your First Name ',
            'last_name': 'Your Last Name ',
            'stars':'Rating '
            }
        error_messages = {
            'stars':{
                'min_value': 'Your min value is 1',
                'max_value' : 'Your max value is 5'
            }
        }
