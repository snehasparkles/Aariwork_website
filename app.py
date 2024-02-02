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
    'name' : 'item 1',
    'price' : 2000,
    'img': '/images/c1.jpg'
},
{
    'id':'mwb2' ,
    'name' : 'item 2',
    'price' : 2000,
    'img': '/images/c1.jpg'
},
{
    'id':'mwb3' ,
    'name' : 'item 3',
    'price' : 2000,
    'img': '/images/c1.jpg'
},
{
    'id':'mwb4' ,
    'name' : 'item 4',
    'price' : 2000,
    'img': '/images/c1.jpg'
},
]

@app.route('/Modern_works_Blouse')
def Modern():
    return render_template("items.html",title = "Modern works Blouse",items= Modern_works_Blouse)

Bridal_designer_Blouse =[
{
    'id':'bbb1' ,
    'name' : 'item 1',
    'price' : 2500,
    'img': '/images/c1.jpg'
},
{
    'id':'bbb2' ,
    'name' : 'item 2',
    'price' : 3000,
    'img': '/images/c1.jpg'
},
{
    'id':'bbb3' ,
    'name' : 'item 3',
    'price' : 3000,
    'img': '/images/c1.jpg'
},
{
    'id':'bbb4' ,
    'name' : 'item 4',
    'price' : 2400,
    'img': '/images/c1.jpg'
},
]

@app.route('/Bridal_designer_Blouse')
def Bridal():
    return render_template("items.html",title = "Bridal designer Blouse",items = Bridal_designer_Blouse)

lehengas =[
{
    'id':'l1' ,
    'name' : 'item 1',
    'price' : 2500,
    'img': '/images/c1.jpg'
},
{
    'id':'l2' ,
    'name' : 'item 2',
    'price' : 3000,
    'img': '/images/c1.jpg'
},
{
    'id':'l3' ,
    'name' : 'item 3',
    'price' : 3000,
    'img': '/images/c1.jpg'
},
{
    'id':'l4' ,
    'name' : 'item 4',
    'price' : 2400,
    'img': '/images/c1.jpg'
},
]

@app.route('/lehengas')
def lehenga():
    return render_template("items.html",title = "lehengas",items = lehengas)

Cutworks =[
{
    'id':'cw1' ,
    'name' : 'item 1',
    'price' : 2500,
    'img': '/images/c1.jpg'
},
{
    'id':'cw2' ,
    'name' : 'item 2',
    'price' : 3000,
    'img': '/images/c1.jpg'
},
{
    'id':'cw3' ,
    'name' : 'item 3',
    'price' : 3000,
    'img': '/images/c1.jpg'
},
{
    'id':'cw4' ,
    'name' : 'item 4',
    'price' : 2400,
    'img': '/images/c1.jpg'
},
]

@app.route('/Cutworks')
def Cut_works():
    return render_template("items.html",title = "Cut works",items = Cutworks)


Mirrorworks =[
{
    'id':'mw1' ,
    'name' : 'item 1',
    'price' : 2500,
    'img': '/images/c1.jpg'
},
{
    'id':'mw2' ,
    'name' : 'item 2',
    'price' : 3000,
    'img': '/images/c1.jpg'
},
{
    'id':'mw3' ,
    'name' : 'item 3',
    'price' : 3000,
    'img': '/images/c1.jpg'
},
{
    'id':'mw4' ,
    'name' : 'item 4',
    'price' : 2400,
    'img': '/images/c1.jpg'
},
]

@app.route('/Mirrorworks')
def Mirror_works():
    return render_template("items.html",title = "Mirror works",items = Mirrorworks)

ZardosiworkBlouse =[
{
    'id':'zw1' ,
    'name' : 'item 1',
    'price' : 2500,
    'img': '/images/c1.jpg'
},
{
    'id':'zw2' ,
    'name' : 'item 2',
    'price' : 3000,
    'img': '/images/c1.jpg'
},
{
    'id':'zw3' ,
    'name' : 'item 3',
    'price' : 3000,
    'img': '/images/c1.jpg'
},
{
    'id':'zw4' ,
    'name' : 'item 4',
    'price' : 2400,
    'img': '/images/c1.jpg'
},
]

@app.route('/ZardosiworkBlouse')
def Zardosiwork():
    return render_template("items.html",title = "Zardosi work Blouse",items = ZardosiworkBlouse)




SareeWaistBelts =[
{
    'id':'sw1' ,
    'name' : 'item 1',
    'price' : 2500,
    'img': '/images/c1.jpg'
},
{
    'id':'sw2' ,
    'name' : 'item 2',
    'price' : 3000,
    'img': '/images/c1.jpg'
},
{
    'id':'sw3' ,
    'name' : 'item 3',
    'price' : 3000,
    'img': '/images/c1.jpg'
},
{
    'id':'sw4' ,
    'name' : 'item 4',
    'price' : 2400,
    'img': '/images/c1.jpg'
},
]

@app.route('/SareeWaistBelts')
def SareeBelts():
    return render_template("items.html",title = "Saree Waist Belts",items = SareeWaistBelts)



PattuPavadaiWorks =[
{
    'id':'ppw1' ,
    'name' : 'item 1',
    'price' : 2500,
    'img': '/images/c1.jpg'
},
{
    'id':'ppw2' ,
    'name' : 'item 2',
    'price' : 3000,
    'img': '/images/c1.jpg'
},
{
    'id':'ppw3' ,
    'name' : 'item 3',
    'price' : 3000,
    'img': '/images/c1.jpg'
},
{
    'id':'ppw4' ,
    'name' : 'item 4',
    'price' : 2400,
    'img': '/images/c1.jpg'
},
]

@app.route('/PattuPavadai')
def PattuPavadai():
    return render_template("items.html",title = "Pattu Pavadai Works",items = PattuPavadaiWorks)



threeDBlouseworks =[
{
    'id':'3dw1' ,
    'name' : 'item 1',
    'price' : 2500,
    'img': '/images/c1.jpg'
},
{
    'id':'3dw2' ,
    'name' : 'item 2',
    'price' : 3000,
    'img': '/images/c1.jpg'
},
{
    'id':'3dw3' ,
    'name' : 'item 3',
    'price' : 3000,
    'img': '/images/c1.jpg'
},
{
    'id':'3dw4' ,
    'name' : 'item 4',
    'price' : 2400,
    'img': '/images/c1.jpg'
},
]

@app.route('/threeDBlouseworks')
def threeDBlouse():
    return render_template("items.html",title = "3D Blouseworks",items = threeDBlouseworks)



# if __name__ == "__main__":
app.run(host = '0.0.0.0', port=8080 )