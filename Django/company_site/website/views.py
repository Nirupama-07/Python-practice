from django.shortcuts import render
from .forms import Contact

# Create your views here.
def home(request):
    cards=[
        {
            "logo":"💻",
            "title":"Web Development",
            "description":"Responsive and scalable websites built with modern technologies."
        },
        {
            "logo":"📱",
            "title":"Mobile Apps",
            "description":"Android and iOS applications designed for excellent user experience."
        },
        {
            "logo":"🎨",
            "title":"UI / UX Design",
            "description":"Beautiful and user-friendly interfaces that customers love."
        },
        
        {
            "logo":"📝",
            "title":"Functional Testing",
            "description":"All projects are tested throughly befor deploying."
        },
        
        {
            "logo":"🤖",
            "title":"Python with AI",
            "description":"Walk with todays trend by learning python with AI."
        },
        
        {
            "logo":"☎",
            "title":"Customer Support",
            "description":"Customer Care are always available 24x7."
        }
    ]
    stats=[
        {
            "stat":"100+",
            "services":"Projects Completed"
        },
        {
            "stat":"60+",
            "services":"Happy Clients"
        },
        {
            "stat":"5+",
            "services":"Years of Experience"
        }
    ]
    return render(request,"home.html",{"name":"Crushaders", "cards":cards, "stats":stats})

def about(request):
    return render(request,"about.html",{"name":"Crushaders"})

def contact(request):
    if request.method == "POST":
        form = Contact(request.POST)

        if form.is_valid():
            print(form.cleaned_data)

    else:
        form = Contact()
    return render(request,"contact.html",{"name":"Crushaders","form":form})