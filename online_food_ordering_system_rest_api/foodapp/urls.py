from django.urls import path,include
from foodapp import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('item',views.ItemManager)



app_name="foodapp"

urlpatterns = [
    path('create/user/',views.UserCreate.as_view(),name="user_create"),
    path('user/manage/',views.UserProfileManager.as_view(),name="usermanager"),
    path('user/token/',views.UserTokenGeneration.as_view(),name="usertoken"),
    path('',include(router.urls)),
    
    
    
]
