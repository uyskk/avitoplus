from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, CreateView, DetailView

from .models import Advert, Like, Comment
from .forms import AdvertForm, CommentForm


class AdvtListView(ListView):

    model = Advert
    template_name = "adverts_list.html"
    context_object_name = "adverts"
    paginate_by = 8

    def get_queryset(self):

        query = self.request.GET.get("q")

        if query:
            adverts = Advert.objects.filter(Q(title__icontains=query))
        else:
            adverts = super().get_queryset()

        for advt in adverts:

            likes = Like.objects.filter(advt=advt).filter(user=self.request.user)

            if likes.exists():
                advt.is_liked = True

        return adverts


class AdvtCreateView(CreateView):

    model = Advert
    template_name = "advert_create.html"
    form_class = AdvertForm

    def get_success_url(self):
        return reverse("advt-list")


class AdvtDetailView(DetailView):

    model = Advert
    template_name = "advert.html"
    context_object_name = "advert"


@method_decorator(login_required, name="dispatch")
class LikeView(View):

    def get_success_url(self):
        return reverse("advt-list")

    def get(self, request, *args, **kwargs):
        like = Like()
        like.advt = get_object_or_404(Advert, pk=self.kwargs.get("pk"))
        like.user = self.request.user
        like.save()
        return redirect(self.get_success_url())


@method_decorator(login_required, name="dispatch")
class DislikeView(View):

    def get_success_url(self):
        return reverse("advt-list")

    def get(self, request, *args, **kwargs):
        Like.objects.get(advt_id=self.kwargs.get("pk"), user=self.request.user).delete()
        return redirect(self.get_success_url())


class CommentCreateView(View):

    def post(self, request, *args, **kwargs):

        form = CommentForm(data=request.POST)

        if form.is_valid():

            comment = form.save(commit=False)

            comment.advt = get_object_or_404(Advert, pk=self.kwargs.get("pk"))
            comment.user = self.request.user

            comment.save()

        return redirect("advt-detail", pk=self.kwargs.get("pk"))
