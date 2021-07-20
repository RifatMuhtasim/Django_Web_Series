from story.models import StoryPost
from django.shortcuts import get_object_or_404, render
from .models import StoryPost
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User


context = {
        'title': 'Story- Pray 4 Refugees',
        'StoryPosts': StoryPost.objects.all()
}

class StoryPostList(ListView):
    model = StoryPost
    template_name = 'story/story.html'
    context_object_name = 'StoryPosts'
    ordering = [ "-StoryPostTime" ]
    paginate_by = 5

class StoryPostDetail(DetailView):
    model = StoryPost
    template_name = 'story/storydetail.html'

class StoryPostAuthor(ListView):
    model = StoryPost
    template_name = 'story/storyauthor.html'
    context_object_name = 'StoryPosts'
    paginated_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return StoryPost.objects.filter(StoryPostAuthor = user).order_by('-StoryPostTime')
