from django import forms
from . models import Auction

class AuctionForm (forms.ModelForm):
    class Meta:
        model = Auction
        fields = ('category', 'product','description', 'image','start_bid' )
        