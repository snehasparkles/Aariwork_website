from flask import Flask,render_template,redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/gallery')
def gallery():
    return render_template("product.html")
@app.route('/contact')
def contact():
    return render_template("contact.html")
@app.route('/about')
def about():
    return render_template("about.html")

Modern_works_Blouse =[
{
    'id':'mwb1' ,
    'name' : 'Item 1',
    'price' : 'Rs.2000',
    'img': '/images/m1.jpg'
},
{
    'id':'mwb2' ,
    'name' : 'Item 2',
    'price' : 'Rs.2000',
    'img': '/images/m2.jpg'
},
{
    'id':'mwb3' ,
    'name' : 'Item 3',
    'price' : 'Rs.2000',
    'img': '/images/m3.jpg'
},
{
    'id':'mwb4' ,
    'name' : 'Item 4',
    'price' : 'Rs.2000',
    'img': '/images/m4.jpg'
},
]

@app.route('/Modern_works_Blouse')
def Modern():
    return render_template("items.html",title = "Modern works Blouse",items= Modern_works_Blouse)

Bridal_designer_Blouse =[
{
    'id':'bbb1' ,
    'name' : 'Item 1',
    'price' : 'Rs.2000',
    'img': '/images/b1.jpg'
},
{
    'id':'bbb2' ,
    'name' : 'Item 2',
    'price' : 'Rs.2000',
    'img': '/images/b2.jpg'
},
{
    'id':'bbb3' ,
    'name' : 'Item 3',
    'price' : 'Rs.2000',
    'img': '/images/b3.jpg'
},
{
    'id':'bbb4' ,
    'name' : 'Item 4',
    'price' : 'Rs.2000',
    'img': '/images/b4.jpg'
},
]

@app.route('/Bridal_designer_Blouse')
def Bridal():
    return render_template("items.html",title = "Bridal designer Blouse",items = Bridal_designer_Blouse)

lehengas =[
{
    'id':'l1' ,
    'name' : 'Item 1',
    'price' : 'Rs.2000',
    'img': '/images/l1.jpg'
},
{
    'id':'l2' ,
    'name' : 'Item 2',
    'price' : 'Rs.2000',
    'img': '/images/l2.jpg'
},
{
    'id':'l3' ,
    'name' : 'Item 3',
    'price' : 'Rs.2000',
    'img': '/images/l3.jpg'
},
{
    'id':'l4' ,
    'name' : 'Item 4',
    'price' : 'Rs.2000',
    'img': '/images/l4.jpg'
},
]

@app.route('/lehengas')
def lehenga():
    return render_template("items.html",title = "lehengas and chudi neck designs",items = lehengas)

Cutworks =[
{
    'id':'cw1' ,
    'name' : 'Item 1',
    'price' : 'Rs.2000',
    'img': '/images/cw1.jpeg'
},
{
    'id':'cw2' ,
    'name' : 'Item 2',
    'price' : 'Rs.2000',
    'img': '/images/cw2.jpg'
},
{
    'id':'cw3' ,
    'name' : 'Item 3',
    'price' : 'Rs.2000',
    'img': '/images/cw3.jpg'
},
{
    'id':'cw4' ,
    'name' : 'Item 4',
    'price' : 'Rs.2000',
    'img': '/images/cw4.jpg'
},
]

@app.route('/Cutworks')
def Cut_works():
    return render_template("items.html",title = "Cut works",items = Cutworks)


Mirrorworks =[
{
    'id':'mw1' ,
    'name' : 'Item 1',
    'price' : 'Rs.2000',
    'img': '/images/mir1.jpg'
},
{
    'id':'mw2' ,
    'name' : 'Item 2',
    'price' : 'Rs.2000',
    'img': '/images/mir2.jpg'
},
{
    'id':'mw3' ,
    'name' : 'Item 3',
    'price' : 'Rs.2000',
    'img': '/images/mir3.jpg'
},
{
    'id':'mw4' ,
    'name' : 'Item 4',
    'price' : 'Rs.2000',
    'img': '/images/mir4.jpg'
},
]

@app.route('/Mirrorworks')
def Mirror_works():
    return render_template("items.html",title = "Mirror works",items = Mirrorworks)

ZardosiworkBlouse =[
{
    'id':'zw1' ,
    'name' : 'Item 1',
    'price' : 'Rs.2000',
    'img': '/images/z1.jpg'
},
{
    'id':'zw2' ,
    'name' : 'Item 2',
    'price' : 'Rs.2000',
    'img': '/images/z2.jpg'
},
{
    'id':'zw3' ,
    'name' : 'Item 3',
    'price' : 'Rs.2000',
    'img': '/images/z3.jpg'
},
{
    'id':'zw4' ,
    'name' : 'Item 4',
    'price' : 'Rs.2000',
    'img': '/images/c1.jpg'
},
]

@app.route('/ZardosiworkBlouse')
def Zardosiwork():
    return render_template("items.html",title = "Zardosi work Blouse",items = ZardosiworkBlouse)




SareeWaistBelts =[
{
    'id':'sw1' ,
    'name' : 'Item 1',
    'price' : 'Rs.2000',
    'img': '/images/sw3.jpeg'
},
{
    'id':'sw2' ,
    'name' : 'Item 2',
    'price' : 'Rs.2000',
    'img': '/images/sw1.jpg'
},
{
    'id':'sw3' ,
    'name' : 'Item 3',
    'price' : 'Rs.2000',
    'img': '/images/sw2.jpg'
},
{
    'id':'sw4' ,
    'name' : 'Item 4',
    'price' :'Rs.2000',
    'img': '/images/sw4.jpg'
},
]

@app.route('/SareeWaistBelts')
def SareeBelts():
    return render_template("items.html",title = "Saree Waist Belts",items = SareeWaistBelts)



PattuPavadaiWorks =[
{
    'id':'ppw1' ,
    'name' : 'Item 1',
    'price' : 'Rs.2000',
    'img': '/images/p1.jpg'
},
{
    'id':'ppw2' ,
    'name' : 'Item 2',
    'price' : 'Rs.2000',
    'img': '/images/p2.jpg'
},
{
    'id':'ppw3' ,
    'name' : 'Item 3',
    'price' : 'Rs.2000',
    'img': '/images/p3.jpg'
},
{
    'id':'ppw4' ,
    'name' : 'Item 4',
    'price' : 'Rs.2000',
    'img': '/images/p4.jpg'
},
]

@app.route('/PattuPavadai')
def PattuPavadai():
    return render_template("items.html",title = "Pattu Pavadai Works",items = PattuPavadaiWorks)



threeDBlouseworks =[
{
    'id':'3dw1' ,
    'name' : 'Item 1',
    'price' : 'Rs.2000',
    'img': '/images/3d1.jpg'
},
{
    'id':'3dw2' ,
    'name' : 'Item 2',
    'price' : 'Rs.2000',
    'img': '/images/3d2.jpg'
},
{
    'id':'3dw3' ,
    'name' : 'Item 3',
    'price' : 'Rs.2000',
    'img': '/images/3d3.jpg'
},
{
    'id':'3dw4' ,
    'name' : 'Item 4',
    'price' : 'Rs.2000',
    'img': '/images/3d4.jpg'
},
]

@app.route('/threeDBlouseworks')
def threeDBlouse():
    return render_template("items.html",title = "3D Blouseworks",items = threeDBlouseworks)



if __name__ == "__main__":
  app.run(host = '0.0.0.0', port=8080 ,debug=True )