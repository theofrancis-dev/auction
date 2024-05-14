from django.urls import path
from . import views, models

urlpatterns = [
    path("", views.index, name="index"),
    path("auctions", views.index, name="index"),    
    path("auctions/sell/", views.create_auction, name="sell"),
    path("initapp", views.initapp, name="initapp"),    
    path("auctions/watchlist/", views.watchlist, name="watch_list"), 
    path("auctions/add_to_watchlist/<int:id>", views.add_to_watchlist, name="add_to_watch_list"),
    path("auctions/myitems/", views.my_items, name="my_items"),
    path("auctions/categories/<int:pk>", views.categories, name="categories"),
    path("auctions/subcategory_details/<int:pk>", views.subcategory_details, name="my_items"),
    path("auction_details/<int:pk>",  views.auction_details , name="auction_details"),
    path("auctions/remove_watch/<int:id>",  views.remove_watch , name="remove_watch"),
    path("auctions/by_category/<int:id>", views.by_category, name="by_category"),
    path("auctions/end_now/<int:id>", views.end_auction, name="end_auction"),   
    path("auctions/new_comment/<int:auction_id>", views.new_comment, name="new_comment"),   
    path("auctions/closed/", views.closed_auctions, name="closed_auctions"),
    path('avatars/', views.show_avatars, name="avatars"),
    path('initapp/avatars/', views.set_avatars, name="set_avatars"),
    path('avatars/change/<int:pk>', views.change_avatar, name ="change_avatar"),
    path('register', views.registerPage, name ="register"),
    path('signup', views.registerPage, name = "signup"),

]
