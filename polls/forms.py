from django import forms


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


def handle_uploaded_file(f):
    count = 0
    with open('name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            print("count", ++count)
            destination.write(chunk)
