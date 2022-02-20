from django.http import HttpResponse
from django.shortcuts import render

users = [
    {
        'name': 'sudhir',
        'course': 'sql'
    },
    {
        'name': 'utkarsh',
        'course': 'python'
    }
]

def index(request):
    context = {'users': users}
    return render(request, 'question/index.html', context)

