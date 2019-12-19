from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "computer_shop_online_app"

urlpatterns = [
    url(r"^$", views.main_page, name="main_page"),
    url(r"^login_page/$", views.login_page, name="login_page"),
    url(r"^logout_page/$", views.logout_page, name="logout_page"),
    url(r"^promotion_page/$", views.promotion_page, name="promotion_page"),
    url(r"^register_page/$", views.register_page, name="register_page"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
