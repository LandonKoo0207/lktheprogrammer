from django.conf.urls import url, include
from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^$', views.PostListView.as_view(), name='post-list'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^post/(?P<slug>[-\w]+)/$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^create/$', views.PostCreateView.as_view(success_url="/blog"), name='post_create'),
    url(r'^update/(?P<pk>\d+)/$', views.PostUpdateView.as_view(), name='post_update'),
    url(r'^delete/(?P<id>\d+)/$', views.PostDeleteView, name="post_delete"),
]
