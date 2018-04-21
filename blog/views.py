from django.shortcuts import render

def post_list(request):
    print('hello')
    return render(request, 'blog/post_list.html', {})

# Create your views here.
