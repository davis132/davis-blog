from django.contrib import admin
from django.urls import path
from blogs import views
from django.conf.urls.static import static
from davis_blog import settings

admin.site.site_header = "Davis Blog"
admin.site.site_title =  "Davis Blog"
admin.site.index_title = "Davis Blog"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("blog/", views.blog, name="blog"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("see-contacts/", views.display_contact, name="display_contact"),
    path("create-blog/", views.create_blog, name="create_blog"),
    path("view-blog/", views.view_blog, name="view_blog"),
    path("logout/", views.logout, name="logout"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
