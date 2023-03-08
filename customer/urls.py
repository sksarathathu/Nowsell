from django.urls import path
from customer import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
   
    path("register",views.SignUpView.as_view(),name="signup"),
    path("",views.SignInView.as_view(),name="signin"),
    path("home",views.HomeIndexView.as_view(),name="home"),
    path("profile",views.ProfileView.as_view(),name="profile"),
    path("editprofile",views.EditProfileView.as_view(),name="editprofile"),
    path("logout",views.SignOutView,name="signout"),
    path("addproducts",views.ProductView.as_view(),name="addproduct"),
    path("productadded",views.ProductAddedView.as_view(),name="addedproduct"),
    path("productdetail/<int:id>",views.ProductDetailView.as_view(),name="productdetail"),
    path("checkout/<int:id>",views.OrderView.as_view(),name="checkout"),
    path("deleteproduct/<int:id>",views.ProductDeleteView.as_view(),name="deleteprod"),
    path("myproductdetail/<int:id>",views.MyProductDetailView.as_view(),name="myproductdetail"),
    path("addwishlist/<int:id>",views.addto_wishlist,name="addtowishlist"),
    path("wishlist",views.WishlistView.as_view(),name="wishlist"),
    path("wishlistdelete/<int:id>",views.delete_wishlist,name="deletewish"),
    path("mobiles",views.MobileView.as_view(),name="mobiles"),
    path("cars",views.CarView.as_view(),name="cars"),
    path("profileediting",views.edit_profile,name="edit_profile")
   
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)