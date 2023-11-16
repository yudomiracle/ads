from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from objavlenia.forms import CommentForm
from objavlenia.models import Advertisment


class CreateAdsViews(CreateView):
    model = Advertisment
    fields = '__all__'
    template_name = 'form.html'
    success_url ='/ads/{id}'



class DetailAdsViews(DetailView):
    model = Advertisment
    context_object_name = 'ads'
    template_name = 'ads_detail.html'

class ListAdsViews(ListView):
    model = Advertisment
    context_object_name = 'ads'
    paginate_by = 10
    template_name = 'ads_list.html'

class UpdateAdsViews(UserPassesTestMixin, UpdateView):
    model = Advertisment
    fields = '__all__'
    success_url = '/ads/{id}'
    template_name = 'form.html'

    def test_func(self):
        records = get_object_or_404(Advertisment, pk=self.kwargs['pk'])
        return self.request.user == records.created_by

class DeleteAdsViews(UserPassesTestMixin, DeleteView):
    model = Advertisment
    template_name ='form.html'
    success_url = '/ads/'

    def test_func(self):
        records = get_object_or_404(Advertisment, pk=self.kwargs['pk'])
        return self.request.user == records.created_by


def add_coment_ads(request, ads_id):
    ads = get_object_or_404(Advertisment, pk=ads_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.ads = ads
            comment.save()
            return redirect('ads_detail', ads_id = ads.id)

        else:
            form = CommentForm()

        return render(request, 'add_comment_to_announcement.html', {'form': form})