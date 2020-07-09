from django.urls import path
from blog import views as blog_views
app_name = 'blog_site'

urlpatterns = [
    path('home/', blog_views.PostListView.as_view(), name='blog-home'),
    path('about/', blog_views.about, name='blog-about'),
    path('post/<int:pk>/', blog_views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', blog_views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', blog_views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', blog_views.PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>/', blog_views.UserPostListView.as_view(), name='user-posts'),
    # the username is taken as key args

]

# <app>/<model>_<viewtype>.html
# so PostListView.as_view() was looking for blog/post_list.html
# but the template can be changed

# the create new post will search for post_form.html by convention
