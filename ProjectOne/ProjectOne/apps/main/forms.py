from django import forms

class ReviewFilter(forms.Form):
    min_rating = forms.IntegerField(label="от", required=False)
    max_rating = forms.IntegerField(label="до", required=False)
    author_name = forms.CharField(label="Автор", required=False)
    review_text = forms.CharField(label="Текст", required=False)