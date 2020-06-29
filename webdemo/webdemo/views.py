from django.http import HttpResponse


# Function View
def welcome(request):
    return HttpResponse("<h1 style='color:blue'>Welcome to Django</h1>")
