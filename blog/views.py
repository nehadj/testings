from webbrowser import get
from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from django.http import HttpResponse
# below line ,we are importing forms in views
from .forms import BlogPostForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def post_list(request):
    # response_Data=Post.objects.all().values()
    # return HttpResponse(response_Data)
    # return render(request,'blog/index.html')
    response_Data=Post.objects.all()
    return render(request,'blog/index.html',{'Posts':response_Data})

def post_detail_page(request,pk):
    post_data=get_object_or_404(Post,pk=pk) 
    # return HttpResponse(post_data)
    return render(request,'blog/blog_detail.html',{'data':post_data})

@login_required
def post_new(request):
    if request.method=='POST':
        form_data=BlogPostForm(request.POST) #capturing the form data
        if form_data.is_valid():
            post_data=form_data.save()
            return redirect('post_list') #redirect to our post_list url
    else:
        form_data=BlogPostForm()
    return render(request,'blog/blog_add_edit.html',{'form_data':form_data})    

def post_edit(request,pk):
    post_data=get_object_or_404(Post,pk=pk)      
    if request.method=='POST':
        form=BlogPostForm(request.POST,instance=post_data)
        if form.is_valid():
            post_data=form.save()
            return redirect('post_list')
    else:
        form=BlogPostForm(instance=post_data) 
    return render(request,'blog/blog_add_edit.html',{'form_data':form})   

def post_delete(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.delete()
    return redirect('post_list')    

def register_user(request):
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account Created Successfully for {username}')
            return redirect('post_list')
    else:
        form=UserRegistrationForm()
    return render(request,'registration/register.html',{'form':form})
    # return  HttpResponse('going well')
    # form=UserRegistrationForm()
    # return render(request,'registration/registration.html',{'form':form})


   

        
 


