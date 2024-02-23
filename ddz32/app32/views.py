from django.contrib import messages
from django.core.signing import Signer
from django.shortcuts import render, redirect

from app32.models import Post


# Create your views here.
def index(request):
    return render(request, 'index.html')

def create_post(request):
    if request.method == 'POST':
        post = Post(title=request.POST['title'])
        if post != '' and post != None:
            message = messages.add_message(request, 100, f'" {post} " successfully created')
            signer = Signer()
            sing_post = signer.sign(post)
            print(sing_post)
            post.save()
            return redirect('home')
        else:
            messages.add_message(request, 100,  f'" {post} " not created')
            return redirect('home')

    return render(request, 'create.html')