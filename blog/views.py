
# Create your views here.
from django.shortcuts import render,redirect
from .models import Blogpost,BlogComment
from django.shortcuts import get_object_or_404
from .form import BlogCreateForm,BlogCommentForm
from django.http import HttpResponse,HttpResponseRedirect,response
from django.urls import reverse
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

def index(request):
    myposts =Blogpost.objects.order_by('-pub_date')
    print(myposts)
    return render(request, 'blog/index.html',{'myposts':myposts})


def blog_create(request):
    if request.method == 'POST':
        form = BlogCreateForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

    else:
        form = BlogCreateForm()
    return render(request,'blog/blog_create.html',{'form':form})


def blogpost(request,id):
    post = Blogpost.objects.filter(post_id=id)[0]
    comment = BlogComment.objects.filter(post=id)

    context= {
        'post': post,
        'comment':comment,

    }


    return render(request, 'blog/blogpost.html',context)

''' 
def BlogPostLike(request,pk):
    post = get_object_or_404(Blogpost, id=request.POST.get('blogpost_id'))
    if post.likes.filter(id= request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('blogpost-detail', args=[str(pk)]))
'''

@login_required
@require_POST
def like(request,post_id):
    print(post_id)
    if request.method == 'POST' or request.is_ajax():
        user = request.user
        print(user)
        slug = request.POST.get('slug',None)
        print(slug)
        blogpost1 = get_object_or_404(Blogpost,slug=slug)


        if blogpost1.likes.filter(id=user.id).exists():
          blogpost1.likes.remove(user)
          message = 'you dislike this '


        else:
            blogpost1.likes.add(user)
            message = 'you like this'

    cxn = {'likes_count': blogpost1.total_likes, 'message': message}
    return HttpResponse(json.dumps(cxn), content_type='application/json')

def blogComment(request):
  if request.method == 'POST':
    comment = request.POST.get('comment')
    user = request.user
    post_id = request.POST.get('post_id')
    post = Blogpost.objects.get(post_id=post_id)
    comment = BlogComment(comment=comment,user=user,post=post)
    comment.save()

    return redirect('blogHome', id=post_id)


def blogCommentUpdate(request,sno):
    if request.is_ajax():
      c = request.POST.get('comment','')
      t = BlogComment.objects.get(sno=sno)
      t.comment = c
      t.save()
    xn = {'comment_update': t}
    return JsonResponse(json.dumps(xn), content_type='application/json')

def blog_delete(request,post_id):
    blog =Blogpost.objects.filter(post_id=post_id)
    blog.delete()


    return redirect('blogHome')




