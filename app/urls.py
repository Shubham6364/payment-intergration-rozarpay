from django.urls import path,include
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('success',views.success,name="success"),
]
