from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from info.form import InfoBlogForm, InfoBlogAccessDateUpdateForm
from info.models import InfoBlog


# Create your views here.
def read_post(request):
    # if request.method == 'GET':
    #     return render(request, 'index.html')
    # elif request.method == 'POST':
    return render(request, 'index.html')


# class PostsView(View):
#     def get(self, request, id=None):
#         posts = InfoBlog.objects.filter(is_deleted=False)
#
#         if id:
#             post = InfoBlog.objects.filter(id=id, is_deleted=False).first()
#             return render(request, 'post.html', context={'post': post, 'posts': posts})
#
#         return render(request, 'index.html', context={'posts': posts})


class PostListView(generic.ListView):
    # model = InfoBlog
    template_name = 'info_blog/post_list.html'
    context_object_name = 'posts'
    queryset = InfoBlog.objects.filter(is_deleted=False)
    # ordering = 'price'

    # def get_queryset(self):
    #     email = self.request.GET.get('email')
    #     print(email)
    #     return InfoBlog.objects.filter(email=email)


class PostCreateView(generic.CreateView):
    # model = InfoBlog
    template_name = 'info_blog/post_create.html'
    form_class = InfoBlogForm
    # fields = ('name', 'text', 'rating', 'price')
    # success_url = '/blog/posts/'

    def get_success_url(self):
        return reverse('post-list')


class PostDetailView(generic.DetailView):
    model = InfoBlog
    template_name = 'info_blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = InfoBlog.objects.filter(is_deleted=False)

        return context


class PostUpdateView(generic.UpdateView):
    model = InfoBlog
    template_name = 'info_blog/post_update.html'
    form_class = InfoBlogForm

    def get_success_url(self):
        return reverse('post-list')


class PostDeleteView(generic.DeleteView):
    pass


# class PostAccessDateUpdateView(generic.FormView):
#     template_name = 'info_blog/post_update_access_date.html'
#     form_class = InfoBlogAccessDateUpdateForm
#
#     def get_object(self):
#         return get_object_or_404(InfoBlog, pk=self.kwargs['pk'])
#
#     def get_initial(self):
#         post = self.get_object()
#         return {'new_access_date': post.access_date}
#
#     def form_valid(self, form):
#         post = self.get_object()
#         post.access_date = form.cleaned_data['new_access_date']
#         post.save()
#         return HttpResponseRedirect(reverse('post-detail', args=[post.id]))
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['post'] = self.get_object()
#         return context


class PostAccessDateUpdateView(generic.UpdateView):
    template_name = 'info_blog/post_update_access_date.html'
    form_class = InfoBlogAccessDateUpdateForm
    model = InfoBlog

    def get_success_url(self):
        return reverse('post-detail', args=[self.object.id])

    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     return HttpResponseRedirect(reverse('post-detail', args=[self.object.id]))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.get_object()
        return context