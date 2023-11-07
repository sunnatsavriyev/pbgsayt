from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',index, name='index'),
    path('reseler_account/',reseler_account, name='reseler_account'),
    path('addacount/<int:profilid>',addaccountview, name='addacount'),
    path('login/',Userlogin, name='login'),
    path('logout/',UserLogout, name='logout'),
    # path('sign/',sign, name='sign_up'),
    path('editprofil/<int:editid>',EditProfilView, name='editprofil'),
    path('account_page/',account_page, name='account_page'),
    path('edit_account/<int:edit_id>/',EditProjectView, name='edit_account'),
    path('delete_account/<int:delete_id>/',DeleteProjectView, name='delete_account'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
