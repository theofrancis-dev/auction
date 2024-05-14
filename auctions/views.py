from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse 
from .models import Category, SubCategory
from .forms import AuctionForm
from django.contrib.auth.decorators import login_required
from .models import Auction, WatchList, Comment, Avatar
from django.views.generic import CreateView, DetailView, ListView
from decimal import Decimal
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

"""
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")
"""

"""def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
"""


"""def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
"""

def initapp(request):        
    if request.method == "POST":
        # delete all previous data
        SubCategory.objects.all().delete()
        Category.objects.all().delete()
        init_categories()
        total_categories = Category.objects.count()
        total_sub = SubCategory.objects.count()
        msg = ["categories initialized"]        
        return render (request,"auctions/initapp.html", { 'messages' : msg, 'total_categories' : total_categories, 'total_sub' : total_sub})
    total_categories = Category.objects.count()
    total_sub = SubCategory.objects.count()
    msg = []
    return render (request,"auctions/initapp.html", { 'messages' : msg, 'total_categories' : total_categories, 'total_sub' : total_sub} )

def set_subcategories ( category, subcategories):
    subcategories.sort()
    #print (f"Category: {category}")
    for s in subcategories:
        #print (s)
        sub = SubCategory (category= category, denomination=s)
        sub.save()

def init_categories ():
    # Categories    
    
    motors_sub = ["UTVs"," ATVs","Scooters & Mopeds"," Dune Buggies & Sand Rails","Snowmobiles","Personal Watercraft",
    "Automotive Hand Tools","Automotive Diagnostic Service Tools","Automotive Shop Equipment & Supplies","Automotive Air Tools",
    "Automotive Battery Testers & Chargers"," Car & Truck Parts","Motorcycle Parts","Vintage and Classic Car & Truck Parts",
    "In-Car Technology","GPS & Security Devices","ATV","Side-by-Side & UTV Parts & Accessories",
    "Vehicle Repair Manuals & Literature","Fishing","Power & Motor","Sail","Aircraft","Buses","Commercial Trucks",
    "RVs & Campers","Vehicle Trailers","Golf Carts","Harley-Davidson Motorcycles","Custom Built Motorcycles",
    "Can-Am Motorcycles","Other Motorcycle Makes","Honda Motorcycles","Suzuki Motorcycles","Motorcycles"]
    motors = Category(title="Motors")
    motors.save()
    set_subcategories (motors, motors_sub)

    fashion = Category(title="Fashion")
    fashion.save()
    fashion_sub = ["Women's Dresses","Women's Tops","Women's Intimates & Sleepwear","Women's Coats","Jackets & Vests","Women's Sweaters","Women's Activewear","Women's Wallets",
    "Women's Scarves & Wraps","Women's Hair Accessories","Women's Sunglasses & Sunglasses Accessories","Women's Hats","Women's Belts","Men's Shirts","Men's Coats & Jackets",
    "Men's Activewear","Men's Jeans","Men's Pants","Men's Underwear"," Men's Hats","Men's Sunglasses & Sunglasses Accessories","Men's Bags"," Men's Wallets","Men's Belts",
    "Men's Ties","Men's Shoes","Women's Shoes","Boys' Shoes","Girls' Shoes","Fashion Jewelry","Fine Jewelry",
    "Vintage & Antique Jewelry","Loose Diamonds & Gemstones","Men's Jewelry","Jewelry Design & Repair Supplies","Jewelry",
    "Wristwatches","Wristwatch Bands","Pocket Watches","Watch Parts","Tools & Guides","Watch Boxes","Cases & Winders","Watch Batteries",
    "Girls' Clothing","Boys' Clothing","Shoes & Accessories","Unisex ","Costume","Reenactment & Theater Apparel","Vintage Clothing",
    "Wedding & Formal Wear","World & Traditional Clothing","Clothing & Shoe Care Products","Uniforms & Work Clothing"]
    set_subcategories (fashion, fashion_sub)

    arts = Category (title="Books, Movies, Music")
    arts.save()
    arts_sub = ["Guitars & Basses"," Pro Audio Equipment","Percussion Instruments"," Wind & Woodwind Instruments","String Instruments","Pianos","Keyboards & Organs",
    "DVDs & Blu-ray Discs","VHS Tapes"," Other Movie Formats"," Movie Film Stock","LaserDisc Movies","DVD & Movie Wholesale Lots","Nonfiction ","Fiction & Literature ",
    "Antiquarian & Collectible ","Text","Educational & Reference ","Magazines","Children & Young Adult ","Music CDs","Vinyl Records","Other Music Formats",
    "Music Cassettes","Music Storage & Media Accessories","Recorded Music Wholesale Lots","Music"]
    set_subcategories (arts, arts_sub)

    electronics = Category (title="Electronics")
    electronics.save()
    electronics_sub = ["Computer Components & Parts","Laptops & Net","Laptop & Desktop Accessories","Computer Printers","Scanners & Supplies","Computer Drives",
    "Storage & Blank Media","Computer Software","Cell Phone Accessories","Cell Phones & Smartphones","Cell Phone & Smartphone Parts","Smart Watches",
    "Cell Phone Cards & SIM Cards","Smart Watch Accessories","Video Games","Video Game Accessories","Video Game Consoles","Video Game Merchandise"," Video Game Replacement Parts & Tools","Prepaid Gaming Cards","Camera Lenses & Filters",
    "Digital Cameras","Film Photography Equipment","Camera","Drone & Photo Accessories"," Camcorders","Camera Drones","TV","Video & Audio Accessories","Home Audio Equipment",
    "Media Streamers","TV & Video Equipment"," TV","Video & Audio Parts","Other TV","Video & Home Audio Equipment"," Headphones","MP3 Players","Audio Player Docks & Mini Speakers",
    "Portable Audio Accessories","Portable AM/FM Radios","Portable Stereos & Boomboxes","Car Audio in Consumer Electronics","Car Video Monitors & Equipment",
    "Car Electronics Accessories","Car Audio & Video Installation Equipment","Car GPS Units","Car GPS Accessories & Tracking",
    "Rechargeable Batteries","Single Use Batteries","Multipurpose Battery Chargers","Multipurpose AC to DC Adapters","Battery Testers",
    "Battery Converters","Home Surveillance Systems","Smart Speakers","Hubs & Accessories","Other Smart Home Electronics","Smart Plugs",
    "Smart Plug Parts & Accessories","Vintage Audio & Video Electronics","Vintage Calculators","Other ",
    "Vintage Home Telephones","Ham & Amateur Radio Electronics","Radio Communication Parts & Accessories",
    "Walkie Talkies & Two-Way Radios","CB Radios","Radio Antennas","Radio Scanners","VR Headsets","Smartphone VR Headsets",
    "VR Controllers & Motion Sensors","VR Cases","Covers & Skins","Other Virtual Reality Accessories","Standalone VR Headsets"]
    set_subcategories (electronics, electronics_sub)

    collectibles = Category (title="Collectibles & Arts")
    collectibles.save()
    collectibles_sub = ["Knives","Swords","Blades","Armors & Accessories","Comics","Militaria","Decorative Collectibles","Animation Art & Characters","Tobacciana",
    "Sports Trading Cards & Accessories","Sports Fan Apparel & Souvenirs","Original Sport Autographed Items","Vintage Sports Memorabilia","Game Used Sports Memorabilia",
    "Sports Stickers","Sets & Albums","US Coins","Bullion","World Coins","US Paper Money","World Paper Money","Virtual Currency","Miners & Mining Contracts","Yarn",
    "Sewing & Needlecraft Supplies","Sewing Tools & Supplies","Beads & Jewelry Making Supplies","Fabric","Art Supplies","Scrapbooking & Paper Craft Supplies","Antiques",
    "Asian Antiques","Silver Antiques"," Antique Decorative Arts","Antique Furniture","Architectural & Garden Antiques","Period & Style Antiques","Dolls",
    "Dollhouse Miniatures","Teddy Bears","Paper Dolls","Dolls & Bears Wholesale Lots","Teddy Bear Making Supplies","Pottery & China","Glass","Art Prints",
    "Art Paintings","Art Posters","Art Sculptures","Art Photographs","Art Drawings","Music Memorabilia","Original Autographed ","Movie Memorabilia",
    "TV Memorabilia","Theater Memorabilia","Video Game Memorabilia","United States Stamps","European Stamps","Asian Stamps","British Colony & Territory Stamps",
    "Worldwide Stamps","Middle Eastern Stamps"]
    set_subcategories (collectibles, collectibles_sub)

    homegarden = Category (title="Home and Garden")
    homegarden.save()
    homegarden_sub = ["Yard","Garden & Outdoor Living Items","Outdoor Power Equipment","Pools & Spas","Lawn Mowers","Plants","Seeds & Bulbs","Outdoor Lighting Equipment","Outdoor Cooking & Eating Equipment",
    "Power Tools","Hand Tools","Power Tool & Air Tool Accessories","Tool Boxes & Storage","Air Tools & Air Compressors","Measuring & Layout Tools",
    "Small Kitchen Appliances"," Kitchen Tools & Gadgets","Flatware","Knives & Cutlery"," Kitchen","Dining & Bar Storage Equipment",
    "Dinnerware & Serveware","Vacuum Flasks & Mugs","Home Improvement","Heating","Cooling & Air",
    "Building & Hardware Supplies","Home Plumbing & Fixtures","Electrical Supplies","Home Security Equipment","Other  Supplies","Household & Cleaning Supplies","Vacuum Cleaners","Home Organization Supplies",
    "Vacuum Parts & Accessories","General Household Supplies","Household Cleaning Tools","Household Laundry Supplies","Lamps","Lighting & Ceiling Fans","Light Bulbs",
    "String & Fairy Lights","Lighting Parts","Chandeliers & Ceiling Fixtures","Night Lights","Home Décor","Décor Decals","Stickers & Vinyl Art","Decorative Clocks",
    "Home Fragrances","Home Décor Posters & Prints","Home Décor Pillows","Home Décor Plaques & Signs",
    "Home & Garden Furniture","Food & Beverages","Major Appliances","Parts & Accessories","Bedding","Greeting Cards & Party Supplies","Bathroom Supplies & Accessories",
    "Rugs & Carpets","Window Treatments & Hardware","Holiday & Seasonal Décor","Wedding Supplies"]
    set_subcategories (homegarden, homegarden_sub)

    sporting = Category (title="Sporting")
    sporting.save()
    sporting_sub = ["Gun Parts","Hunting Scopes","Optics & Lasers","Tactical & Duty Gear","Hunting Gun Holsters","Belts & Pouches",
    "Range & Shooting Accessories","Hunting Gun Reloading Equipment","Hunting Equipment",
    "Camping & Hiking Equipment","Archery Equipment","Equestrian Equipment","Scooters","Skateboarding & Longboarding Equipment",
    "Air Guns & Slingshots","Bike Components & Parts"," Bikes","Bicycle Accessories",
    "Bicycle Tires","Tubes & Wheels"," Vintage ","Electric Bikes","Golf Clubs & Equipment",
    "Golf Club Components","Golf Clothing","Sporting Shoes & Accessories"," Golf Accessories","Golf Training Aids","Vintage ","Fishing Equipment & Supplies",
    "Fitness","Running & Yoga Equipment","Water Sports","Team Sports","Indoor Games","Tennis & Racquet Sports"]
    set_subcategories (sporting, sporting_sub)

    toys = Category (title="Toys and Hobbies")
    toys.save()
    toys_sub = ["Action Figures","RC Model Vehicles","Toys & Control Line","Games","Diecast & Toy Vehicles","Collectible Card Games & Accessories","Building Toys","Model Railroads & Trains","Toy Models & Kits",
    "Preschool Toys & Pretend Play","Vintage & Antique Toys","Outdoor Toys & Structures","Slot Cars","Puzzles","Robot","Monster & Space Toys"]
    set_subcategories (toys, toys_sub)

    industrial = Category (title="Bussines and Industrial")
    industrial.save()
    industrial_sub = ["Healthcare","Lab & Dental","Electrical Equipment & Supplies",    "CNC","Metalworking & Manufacturing","Test","Measurement & Inspection Equipment",
    "Office Equipment & Supplies","Industrial Automation & Motion Controls","Heavy Equipment","Parts & Attachments","Material Handling","Facility Maintenance & Safety",
    "Restaurant & Food Service","Light Industrial Equipment & Tools","Hydraulics","Pneumatics","Pumps & Plumbing","Retail & Services","Printing & Graphic Arts",
    "Industrial Fasteners & Hardware","HVAC & Refrigeration","Building Materials & Supplies","Agriculture & Forestry Equipment"]
    set_subcategories (industrial, industrial_sub)

    health = Category (title="Health and Beauty")
    health.save()
    health_sub=["Vitamins & Dietary Supplements","Skin Care Products","Hair Care & Styling Products","Fragrances","Makeup Products","Health Care Products",
    "Medical & Mobility","Shaving & Hair Removal Products","Manicure","Pedicure & Nail Care Products","Natural & Alternative Remedies",
    "Vision Care Products","Oral Care Products","Bath & Body Products","Massaging Equipment & Supplies"]
    set_subcategories (health, health_sub)
    
    others = Category (title="Others")
    others.save()    
    others_sub = ["Tickets & Travel","Gift Cards & Coupons","Baby Essentials","Real Estate","Specialty Services","Everything Else ","Collectibles","Consumer Electronics",
    "Others - Antiques","Other - Music","Pet Supplies","Pottery & Glass","Art","Stamps","Travel","Tickets & Experiences"," Jewelry & Watches","Clothing","Other Shoes & Accessories"]
    set_subcategories (others, others_sub)

'''
nav_listings
nav_closed
nav_sell
nav_my_items
nav_watch_list
nav_listings
'''



def index(request):
    auctions = Auction.objects.filter (ended=False)
    categories = Category.objects.all()
    avatar = get_user_avatar(request)
    print (f"index -> user avatar: {avatar}")
    context = {"auctions" : auctions,"avatar": avatar,"nav_listings":"active","categories":categories }
    return render(request, "auctions/index.html", context)

#closed listings page
@login_required(login_url='/accounts/login/')
def closed(request):
    print ()
    print ("++++++++++ closed ***************")
    all_ended_auctions = Auction.objects.filter (ended=True)
    auctions = all_ended_auctions.filter (winner = request.user)
    categories = Category.objects.all()

    avatar = get_user_avatar(request)
    print (f"user avatar: {avatar} avatar: {avatar}")
    context = {"auctions" : auctions,"avatar": avatar,"nav_closed":"active","categories":categories }
    return render(request, "auctions/closed.html", context)

#view for the Auction Form
@login_required(login_url='/accounts/login/')
def create_auction (request):
    categories = Category.objects.all()

    if request.method == 'POST':        
        image = request.FILES["image"]        
        auction = Auction (listed_by=request.user, image=image)
        form = AuctionForm ( instance = auction, data=request.POST )
        if form.is_valid():
            form.save()
            return redirect ('my_items')
    else:      
        form = AuctionForm()       
    context = {'form':form, 'nav_sell':"active", "avatar":get_user_avatar (request),"categories":categories }
    return render (request, "auctions/auction_create.html", context)
   
#https://docs.djangoproject.com/en/3.1/topics/auth/default/
@login_required(login_url='/accounts/login/')
def auction_details (request, pk):
    auction = Auction.objects.get (id = pk)
    categories = Category.objects.all()
    #get al lthe comments for the auction
    all_comments = auction.comments_auction.all()
    context = {"auction":auction, "avatar":get_user_avatar (request), "nav_listings": "active","categories":categories,"all_comments":all_comments} 

    if request.method=="POST":              
        bid_as_text = request.POST.get("newbid") 
        if len(bid_as_text) > 0: 
            bid = Decimal (bid_as_text)            
            if bid > auction.bid:
                auction.bid = bid
                w = request.user
                auction.winner = w
                auction.save()
                messages.success(request, 'bid accepted!')           
            else:
                messages.error (request, "The bid should be higher than the current bid")  
        else:
            #print ("bid_as_text empty ")            
            messages.error (request, "Input Error. Did you enter a new bid?")  
    return render (request,"auctions/auction_detail.html", context)

#class AuctionView (DetailView):    
#    model = Auction
    
@login_required(login_url='/accounts/login/')
def watchlist (request):
    categories = Category.objects.all()
    user = request.user
    watchlist = user.watchers.all()
    context = {"avatar":get_user_avatar (request), "nav_watch_list":"active","categories":categories,"watchlist":watchlist}    
    return render (request,"auctions/watchlist.html", context)

@login_required(login_url='/accounts/login/')
def add_to_watchlist (request, id):
    auction = Auction.objects.get (id = id)
    #Check if the auction is not int the watch list already
    if (WatchList.objects.filter(watcher = request.user.id, auction = auction).count())==0:        
        watch = WatchList ( auction = auction, watcher = request.user )
        watch.save()
    return redirect (watchlist)

# +++++++++++++++++++++++++++++++++++++++++ Remove from watch list
@login_required(login_url='/accounts/login/')
def remove_watch (request, id):    
    WatchList.objects.filter(id=id).delete()
    return redirect (watchlist)

# +++++++++++++++++++++++++++++++++++++++++ Items sell by the user
@login_required(login_url='/accounts/login/')
def my_items (request):
    print ()
    print ("++++++++++ my items ***************")
    categories = Category.objects.all()
    items = Auction.objects.filter (listed_by = request.user )
    avatar = get_user_avatar(request)
    print (f"user avatar: {request.user} avatar: {avatar}")
    context = {"items": items, "avatar": avatar,"nav_my_items":"active", "categories":categories}
    return render (request,"auctions/my_items.html", context)

def subcategory_details (request, pk):
    cat = Category.objects.get (pk)
    cat_title = cat.title
    sub_list = cat.categories
    context = {"categorie":cat_title, "subcat" : sub_list}
    return render (request, "auctions/subcategorie_details.html",context)

def categories(request, pk):
    categories = Category.objects.all()
    sub = SubCategory.objects.filter (category = pk)   
    context = {"categories" : categories, "selected":pk,"subs": sub, "avatar":get_user_avatar (request),"nav_category":"active"}
    return render (request, "auctions/categories.html", context)

def by_category (request, id):    
    categories = Category.objects.all()
    category = Category.objects.get (id = id)
    auctions = category.auctions_category.all()   
    context = {"categories" : categories, "nav_category":"active","category":category, "auctions": auctions, "avatar":get_user_avatar (request)}
    return render (request, "auctions/by_category.html", context)

@login_required(login_url='/accounts/login/')
@require_http_methods(["POST"])
def new_comment (request, auction_id ):
    # get the user class
    user = request.user
    auction = Auction.objects.get (pk = auction_id)    
    new_comment = request.POST.get("comment")
    c = Comment (user = user, auction = auction, comment = new_comment )
    c.save()
    #shows the comments
    all_comments = auction.comments_auction.all()
    categories = Category.objects.all()
    context = {"auction":auction, "avatar":get_user_avatar (request), "nav_listings": "active","categories":categories, "all_comments":all_comments} 
    return render (request, "auctions/auction_detail.html", context )


 # +++++++++++++++++++++++++++++++++++++++++ End Auction   
@login_required(login_url='/acounts/login/')
def closed_auctions(request):
    auctions = Auction.objects.filter ( ended=True, winner = request.user)
    categories = Category.objects.all()
    context = {"auctions":auctions, "avatar":get_user_avatar (request), "nav_closed": "active","categories":categories} 
    return render (request, "auctions/closed.html", context )

   
@login_required(login_url='/accounts/login/')
def end_auction (request, id):     
    #mark auction as ended  
    auction = Auction.objects.get(pk=id)
    auction.ended = True
    auction.save()
    return redirect (my_items)


def registerPage (request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm (request.POST)
        if form.is_valid():
            new_user = form.save() #save the user
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            #assign an avatar to the user
            assign_avatar_to_new_user (new_user)
                                                
            login(request, new_user)
            return HttpResponseRedirect(reverse("index"))
    context = {'form': form}
    return render (request, 'auctions/signup.html', context)

def show_avatars(request):
    avatars = Avatar.objects.filter(user__isnull=True)
    context ={"avatars":avatars,"avatar":get_user_avatar (request)}
    return render (request,"auctions/avatars.html", context)

def change_avatar(request, pk):    
    #get the old avatar for the user, and set to null
    avatar = Avatar.objects.get (user = request.user )
    print ("+++++change avatar++++++++++++")
    print (f"old avatar: {avatar}")
    if avatar:
        avatar.user = None
        avatar.save()
        avatar = Avatar.objects.get (pk = pk)
        print (f"new avatar: {avatar}")
        avatar.user = request.user
        avatar.save()    
    return redirect('index')

def init_avatars(start_file, end_file):    
    Avatar.objects.all().delete()
    for i in range (start_file, end_file):
        number_str = str (i)
        zero_filled_number = number_str.zfill(4)
        img_file = "../../static/auctions/avatars/"+zero_filled_number+".jpeg"
        avatar = Avatar (url=img_file, tag="avatar")
        avatar.save()

def set_avatars(request):
    init_avatars(0,128)
    avatars = Avatar.objects.all()
    context ={"avatars":avatars}
    return render (request,"auctions/avatars.html", context)

def get_user_avatar (request):
    if request.user.is_authenticated: 
        print (f"get_user_avatar: ${request.user}")  
        avatar =  Avatar.objects.filter (user = request.user ).first()
        print (avatar)   
        print (f"avatar url {avatar.url}")
        if avatar:
            return avatar.url
    return ""

def assign_avatar_to_new_user (new_user):
    #get the first unused avatar
    print ("assign_avatar_to_new_user")
    print (new_user)
    avatar = Avatar.objects.filter (user__isnull=True).first()
    print(avatar)
    if avatar is not None:
        avatar.user = new_user
        avatar.save()
        return True
    return False

