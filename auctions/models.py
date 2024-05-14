#from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime, timedelta
from django.conf import settings
from PIL import ImageTk, Image 
from django.urls import reverse
from django.contrib.auth import get_user_model

class Category (models.Model):
    title = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.title

class SubCategory (models.Model):
    category = models.ForeignKey (Category, on_delete=models.CASCADE, related_name='subcategories')
    denomination = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.denomination

    def get_absolute_url(self):
        return reverse('subcategory_details', kwargs={'pk': self.id})

class Auction (models.Model):

    def return_default_auction_end_date ():
        current_datetime = datetime.now()
        #on future date
        one_month_later = current_datetime + timedelta(days=30)
        return one_month_later

    category = models.ForeignKey (Category,on_delete=models.CASCADE, related_name="auctions_category")
    #TODO To be implemented
    #subCategory = models.ForeignKey (SubCategory,on_delete=models.CASCADE, related_name="auctions_subcategory")
    listed_by = models.ForeignKey (get_user_model(),on_delete=models.CASCADE, related_name="auctioneer")
    product = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    ended_on = models.DateTimeField(default=return_default_auction_end_date)
    image = models.ImageField (upload_to='auction_pics', blank=True, null=True, default='default.jpeg')
    ended = models.BooleanField(default=False)
    #is the same as last bidder
    winner = models.ForeignKey (get_user_model(),on_delete=models.CASCADE, related_name="winners",null = True, blank=True)
    #current_bid
    bid = models.DecimalField (max_digits=20, decimal_places=2, default=0)
    start_bid = models.DecimalField (max_digits=20, decimal_places=2, default=0)

    def __str__(self):
        return self.product

    def get_absolute_url(self):
        return reverse ('auction_details', kwargs={'pk': self.id})
   

class Comment (models.Model):
    #TODO user.comments_user.all() returns all comments made by the user?
    user = models.ForeignKey (get_user_model(),on_delete=models.CASCADE, related_name="comments_user")
    comment = models.CharField (max_length=250)
    #TODO user.comments_auction.all() returns all comments made by user in auctions?
    auction = models.ForeignKey (Auction, on_delete=models.CASCADE, related_name = "comments_auction")

    def __str__(self):
        return self.user.username + ": "+ self.comment
    
class WatchList (models.Model):
    watcher = models.ForeignKey (get_user_model(),on_delete=models.CASCADE, related_name="watchers")
    auction = models.ForeignKey (Auction, on_delete=models.CASCADE, related_name = "watch_lists_auction")
    
    def __str__(self):
        return self.auction.product

#auction.comment_set.all() returns all the comment for the auction
#user.comment_set.all() returns all the comments for a user about an auctions
class Avatar (models.Model):    
    url = models.CharField ( max_length = 256)
    tag = models.CharField ( max_length=200, default="avatar")
    user = models.ForeignKey ( get_user_model(),on_delete = models.DO_NOTHING, null = True, related_name="avatars" )    
    
    def __str__(self):
        return  self.url

   


