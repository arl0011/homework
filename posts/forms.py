from django import forms

class PostForm(forms.Form):
    image = forms.ImageField(required=False)
    title = forms.CharField(required=True,max_length=256)
    content = forms.CharField(required=True,max_length=456)

    def clean_title(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        if title and title.lower() == "python":
            raise forms.ValidationError("title cannot be python")
        return title 
    def clean(seld):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        if title and content and title.lower()== content.lower():
            raise forms.ValidationError("title and content cannot be the same")
        if content and content.isdigit():
            raise forms.ValidationError("content cannot be a number")
        return cleaned_data
