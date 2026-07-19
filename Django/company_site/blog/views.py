from django.shortcuts import render
from datetime import datetime

# Create your views here.
def blog(request):
    cards=[
        {
            "img":"https://onlinetyping.in/images/hand-keyboard.jpg",
            "title":"Keyboard Research and Optimization",
            "description":"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ipsum, laboriosam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Aut, iusto.",
            "date": datetime(2026, 8, 19)
        },
        {
            "img":"https://i.pinimg.com/originals/9e/dd/33/9edd33e79dd9c618bfd9c931a1376c6b.jpg",
            "title":"Search Engine Optimization",
            "description":"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ipsum, laboriosam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Aut, iusto.",
            "date": datetime(2026, 5, 9),
            
        },
        {
            "img":"https://img.freepik.com/premium-photo/interconnected-icons-visual-representation-social-media-marketing-strategy_1320055-12134.jpg?w=1060",
            "title":"Social Media Marketing",
            "description":"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ipsum, laboriosam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Aut, iusto.",
            "date": datetime(2026, 6, 27),
        },
        {
            "img":"https://www.redlineminds.com/wp-content/uploads/2017/07/conversion-optimization-insta.jpg",
            "title":"Conversion Rare Optimization",
            "description":"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ipsum, laboriosam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Aut, iusto.",
            "date": datetime(2026, 9, 15),
        }
    ]
    return render(request,"blog.html",{"name":"Crushaders",
                                       "cards":cards})