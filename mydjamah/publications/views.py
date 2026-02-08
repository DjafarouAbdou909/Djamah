from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostsForms
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Posts, Comment  


def home(request):
    """
    Vue principale affichant la liste des publications publiées.
    """
    posts = Posts.objects.filter(published=True)
    return render(request, "index.html", {'posts': posts})


@login_required
def create_posts(request):
    """
    Crée une publication pour l'utilisateur authentifié.
    Gère le formulaire de création et le traitement POST.
    """
    if request.method == 'POST':
        form = PostsForms(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Ton post a été publié !")
            return redirect('home')
    else:
        form = PostsForms()
    
    return render(request, 'create_post.html', {'form': form})


@login_required
def create_likes(request, post_id):
    """
    Gère le like ou le retrait de like sur un post pour l'utilisateur authentifié.
    
    - Si l'utilisateur a déjà liké le post, le like est supprimé.
    - Sinon, un nouveau like est créé.
    """
    post = get_object_or_404(Posts, id=post_id)
    like = post.likes.filter(user=request.user).first()

    if like:
        like.delete()
    else:
        post.likes.create(user=request.user)

    return redirect('home')


@login_required
def create_comments(request, post_id):
    """
    Crée un commentaire sur un post pour l'utilisateur authentifié.
    Le commentaire est créé uniquement si un contenu est fourni.
    """
    post = get_object_or_404(Posts, id=post_id)

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            post.comments.create(user=request.user, content=content)
    
    return redirect('home')


@login_required
def replies_comments(request, comment_id):
    """
    Permet de répondre à un commentaire existant.
    Le nouveau commentaire est lié au post d'origine et au commentaire parent.
    """
    parent_comment = get_object_or_404(Comment, id=comment_id)
    post = parent_comment.post

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(
                user=request.user,
                post=post,
                content=content,
                parent=parent_comment
            )
    
    return redirect('home')


