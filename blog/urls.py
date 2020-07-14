
from django.contrib import admin
from django.urls import path
from page.views import home
#media
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
#마지막에 urlpatterns + static~하고 추가하는 이유 
#   : static 파일(누구에게나 보여야하는 이미지)말고, 유저가 올리는 파일에 대한, 파일마다 url을 주기 위함. 
