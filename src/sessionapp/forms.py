from django import forms

class FriendsPreferenceForm(forms.Form):
    Priority_1 = forms.CharField(label='Priority #1', max_length = 10)
    Priority_2 = forms.CharField(label='Priority #2', max_length = 10)
    Priority_3 = forms.CharField(label='Priority #3', max_length = 10)
    Priority_4 = forms.CharField(label='Priority #4', max_length = 10)
    Priority_5 = forms.CharField(label='Priority #5', max_length = 10)