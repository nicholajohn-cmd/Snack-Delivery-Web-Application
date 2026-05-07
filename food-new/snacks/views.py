from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from snacks.models import Food1,Order1,Regis1,payments
from django.contrib.auth.forms import UserCreationForm,User
from django.views import generic
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from snacks.forms import RegistrationForm,menuform,paymentpg
from django.contrib.auth import authenticate, login
from django.apps import apps
def login(request):
    return render(request,'master.html')

def base(request):
    data=Food1.objects.all()
    return render(request,'base.html',{'b':data})
def index(request):
    return render(request,'index.html')
class SignUp(generic.CreateView):
    form_class    = UserCreationForm
    success_url   = reverse_lazy('login')
    template_name = 'signup.html'
def logout(request):
    return render(request,'logout.html')
class FoodsDetailView(DetailView):
    model = Food1
    template_name = 'details.html'
class FoodCheckoutView(LoginRequiredMixin, DetailView):
    model = Food1
    template_name = 'checkout.html'
    login_url     = 'login'
def order(req):
    return render(req,'order.html')
def reg(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('/details/<int:pk>/')  # Redirect to a success page after successful submission
    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})

def success(request):
    return render(request, 'success.html')  
def contact(request):
    return render(request, 'contact.html') 

def about(request):
    return render(request, 'about-us.html') 
a=[]
def addtocard(request,id):
    s=Food1.objects.get(id=id)
    f=[s.id,s.ssnacks,s.veg_or_nonveg,s.description,s.price]
    a.append(f)

    return render(request,'addcard.html',{'s': a}) 
def view_card(request):
    return render(request, 'addcard.html', {'s': a}) 
@login_required
def Adminpg(request):
    return render(request,'adminpg.html')

def Adminlog(request):
    response= render(request,'adminlog.html')
    return response
def agefn(request):
        username = request.GET["name"]
        password = request.GET["password"]
        # Authenticate user against Django's admin system
        user = authenticate(request, username=username, password=password)
        if user:
            response= render(request,'data.html')
        else:
            response= render(request,'adminlog.html')
        return response
def final(request):

    response= render(request,'data.html')
    return response
def admin_panel_view(request):
    acc=Regis1.objects.all()

    return render(request, "adminpanal.html", {"data": acc})
def delete(request,id):
    s=Regis1.objects.get(id=id)
    s.delete()
    return redirect('/cusadmin')
def update(request,id):
    admin=Regis1.objects.get(id=id)
    if request.method=="POST":
        form=RegistrationForm(request.POST, instance=admin)
        if form.is_valid():
            form.save()
        return redirect('/cusadmin')
    return render(request,'update.html',{'s':admin})

def menuview(request):
    acc1=Food1.objects.all()

    return render(request, "viewmenu1.html", {"data1": acc1})
def delete1(request,id):
    s=Food1.objects.get(id=id)
    s.delete()
    return redirect('/viewmenu')
def update1(request,id):
    ad=Food1.objects.get(id=id)
    if request.method=="POST":
        form=menuform(request.POST, instance=ad)
        if form.is_valid():
            form.save()
        return redirect('/viewmenu')
    return render(request,'update1.html',{'s':ad})
def search_snacks(request):
    query = request.GET.get('q', '')
    snacks = Food1.objects.filter(ssnacks__icontains=query) if query else Food1.objects.all()
    
    return render(request, 'search_results.html', {'snacks': snacks, 'query': query})
class ProductDetailView(DetailView):
    model = Food1
    template_name = 'details.html'  # Ensure this matches your template filename
    context_object_name = 'object'
def submit_form(request):
    success = False
    if request.method == "POST":
        # Fetch form data
        Ccard = request.POST.get("ccardno1")  # Make sure this matches the form field name
        Eexpires = request.POST.get("Expires")
        Ccsc = request.POST.get("CSC")
        Ffname = request.POST.get("F_name")
        Aaddress = request.POST.get("Address1")
        Ccity = request.POST.get("City")
        Sstate = request.POST.get("State1")
        Ccode = request.POST.get("Post_code")
        Mmobileno = request.POST.get("Mobile_no")
      

        # Save to database
        payments.objects.create(
            ccardno1=Ccard, Expires=Eexpires, CSC=Ccsc,
            F_name=Ffname, L_name=Llname, Address1=Aaddress,
            Building_no=Bbuilding, City=Ccity, State1=Sstate,
            Post_code=Ccode, Mobile_no=Mmobileno, Email_id=Eemail
        )

        success = True  # Indicate successful save


    return render(request, "checkout.html", {"success": success})
def insert(request, pk):
    # Get the 'Food1' object using the primary key (pk)
    snacks = Food1.objects.get(id=pk)

    # Initialize the form for 'Payment'
    return render(request, 'forms.html', { 'c': snacks})
def success_view(request):
    return render(request, 'success.html')
def ordersave(request):
    acc=payments.objects.all()
    return render(request, "saveorder.html", {"data": acc})
def delete2(request,id):
    s=payments.objects.get(id=id)
    s.delete()
    return redirect('/saveor')
def update2(request,id):
    a=payments.objects.get(id=id)
    if request.method=="POST":
        f=menuform(request.POST,instance=f)
        if f.is_valid():
            f.save()
        return redirect('/saveor')
    return render(request,'update2.html',{'s':f})
def store(request):
   
    print("hello")
    snackname=request.GET['s_snacks1']
    price=request.GET['s_price1']
    image=request.GET['s_image_url']
    cardno=request.GET['ccardno1']
    Expires=request.GET['Expires']
    CSV=request.GET['CSC']
    Name=request.GET['F_name']
    Address=request.GET['Address1']
    City=request.GET['City']
    State=request.GET['State1']
    Post_code=request.GET['Post_code']
    Mobile_no=request.GET['Mobile_no']
    print(type(price))
    s=payments.objects.create(s_snacks1=snackname,s_price1=price,s_image_url=image,ccardno1=cardno,Expires=Expires,CSC=CSV,F_name=Name,Address1=Address,City=City,State1=State,Post_code=Post_code,Mobile_no=Mobile_no)
    s.save()

    return render(request,'success.html')
def adminorder(request):
    return render(request,'adminorder.html')




