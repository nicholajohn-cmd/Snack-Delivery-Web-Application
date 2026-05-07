"""
URL configuration for Bookproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from snacks import views
from snacks.views import SignUp,FoodsDetailView,FoodCheckoutView,admin_panel_view,search_snacks,ProductDetailView,submit_form,insert
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login,name='listpage'),
    path('home/',views.base),
    path('index/',views.index),
    path('accounts/',include("django.contrib.auth.urls")),
     path('signup/',SignUp.as_view()),
      path('logout/',views.logout),
      path('details/<int:pk>/', FoodsDetailView.as_view()),
       path('<int:pk>/checkout/', FoodCheckoutView.as_view()),
    path('order/',views.order),
    path('register/',views.reg),
    path('contact/',views.contact),
    path('about/',views.about),
    path('card/', views.view_card, name='view_card'),  # View cart without `id`
    path('card/<int:id>/', views.addtocard, name='add_to_card'),  
    path('Adminpage/',views.Adminpg),
    path('adminlogin/',views.Adminlog),
    path('name/',views.agefn),
    path("cusadmin/", admin_panel_view, name="admin_panel_view"),
    path('delete/<int:id>',views.delete),
    path('update/<int:id>',views.update),
    path('viewmenu/',views.menuview),
     path('delete1/<int:id>',views.delete1),
    path('update1/<int:id>',views.update1),
    path('search/', search_snacks, name='search_snacks'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('submit/',submit_form, name="submit_form"),
    path('insert/<int:pk>/',views.insert),
    path('success/', views.success_view, name='success'),
    path('saveor/',views.ordersave),
     path('delete2/<int:id>',views.delete2),
    path('update2/<int:id>',views.update2),
    path('store1/',views.store),
     path('adminorder/',views.adminorder)
     
]



