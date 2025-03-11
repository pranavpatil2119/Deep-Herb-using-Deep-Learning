import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image , ImageTk 
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
import time
import CNNModel 
from keras import optimizers
import sqlite3
from tensorflow.keras.optimizers import SGD
global fn
fn=""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Medicinal Plant Classification and Plant Prescription")



bg = Image.open("m.jpg")

# bg.resize((1366,500),Image.ANTIALIAS)
# print(w,h)
bg_img = ImageTk.PhotoImage(bg)
bg_lbl = tk.Label(root, image=bg_img)
bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

frame_alpr = tk.LabelFrame(root, text=" --Process-- ", width=280, height=900, font=('times', 14, ' bold '),bg="grey")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=0, y=0)

# calling the function
def shift():
    x1,y1,x2,y2 = canvas.bbox("marquee")
    if(x2<0 or y1<0): #reset the coordinates
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height()//2
        canvas.coords("marquee",x1,y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(1000//fps,shift)

canvas=tk.Canvas(root,bg="black")
canvas.pack()
canvas.place(x=0, y=0)
text_var="Medicinal Plant and Disease Prediction"
text=canvas.create_text(0,-2000,text=text_var,font=('Raleway',25,'bold'),fill='white',tags=("marquee",),anchor='w')
x1,y1,x2,y2 = canvas.bbox("marquee")
width = 1600
height = 50
canvas['width']=width
canvas['height']=height
fps=40    #Change the fps to make the animation faster/slower
shift()   #Function Calling







  
               
               
       

# Create a function to retrieve the selected item from the drop-down list
def get_selected_item():
    selected_item = combobox.get()  # Get the selected item from the Combobox
    print(selected_item)
    #label.config(text=f"Selected Item: {selected_item}")  # Update the label text with the selected item
    if (selected_item=='Minor burns')or(selected_item=='wounds')or(selected_item=='skin irritations'):
        label=tk.Label(root,text='''  Aloe Vera (Aloe barbadensis miller)  ''',width=40,font=('times',20,'bold'),bg="white",fg="black")
        label.place(x=700,y=100)
        label=tk.Label(root,text='''                       
        Conditions: Minor burns, wounds, skin irritations \n
        Potential Uses: Aloe vera gel is applied topically for soothing and \n 
        promoting healing in minor burns, cuts, and skin irritations. \n 
        It might help in relieving sunburn as well.''',width=90,bg="black",fg="white",height=33)
        label.place(x=700,y=200)
        image2 =Image.open('alo.webp')
        image2 =image2.resize((250,250), Image.ANTIALIAS)

        background_image=ImageTk.PhotoImage(image2)

        background_label = tk.Label(root, image=background_image)

        background_label.image = background_image

        background_label.place(x=350, y=250)
    elif (selected_item=='Heart Disease')or(selected_item=='Diabetes')or(selected_item=='lowering blood pressure'or (selected_item=='cardiovascular diseases')):
        label=tk.Label(root,text='''Amla (Emblica officinalis)''',width=40,font=('times',20,'bold'),bg="white",fg="black")
        label.place(x=700,y=100)
        label=tk.Label(root,text='''
        Conditions: 1. Heart Disease, 2. Diabetes , 3. lowering blood pressure , 4.cardiovascular diseases \n
        Potential Uses: Amla is rich in vitamin C and antioxidants.It is used to support the immune system, 
        promote digestive health, and improve overall well-being.
        \n
        Heart Health:\n
        Amla is believed to have cardio-protective properties due to its high antioxidant content, 
        which may help in reducing the risk of heart diseases. 
        It may contribute to lowering cholesterol levels and improving heart health.\n
        
        Diabetes Management:\n
        Some studies suggest that Amla may help in managing diabetes by regulating blood sugar levels. 
        Its anti-diabetic properties might assist in improving insulin sensitivity and glucose metabolism.\n
        
        Anti-Cancer Potential:\n
        Amla contains antioxidants and phytochemicals that have shown potential anti-cancer properties in some research. 
        Its compounds might help in inhibiting the growth of cancer cells and reducing oxidative stress.\n
        
        Blood Pressure Regulation:\n
        The presence of certain bioactive compounds in Amla may contribute to lowering blood 
        pressure and maintaining cardiovascular health.''',bg="black",fg="white",width=90,height=33)
        label.place(x=700,y=200)
        image2 =Image.open('amla.png')
        image2 =image2.resize((250,250), Image.ANTIALIAS)

        background_image=ImageTk.PhotoImage(image2)

        background_label = tk.Label(root, image=background_image)

        background_label.image = background_image

        background_label.place(x=350, y=250)
        
    elif (selected_item=='Schizophrenia')or(selected_item=='Eye Disorders'):
         label=tk.Label(root,text=''' Betel (Piper betle)''',width=40,font=('times',20,'bold'),bg="white",fg="black")
         label.place(x=700,y=100)
         label=tk.Label(root,text='''
         Conditions: Schizophrenia,Oral health, digestion,Eye Disorders
         \n
         Potential Uses: Betel leaves are used traditionally for improving oral health and aiding digestion. 
         They are commonly chewed along with other ingredients for their potential medicinal properties.
         \n
         Schizophrenia :\n
         Schizophrenia is a mental disorder characterized by a range of symptoms like hallucinations, 
         delusions, disorganized thinking, and impaired cognitive function. It primarily affects perception 
         and thoughts, and its treatment typically involves antipsychotic medications, therapy, and support services. 
         Schizophrenia is not directly related to eye disorders like glaucoma or poor digestion.\n

        Eye Disorders :\n
        such as glaucoma involve damage to the optic nerve due to increased intraocular pressure. 
        Glaucoma can lead to vision loss if left untreated. Poor digestion, on the other hand, 
        is a gastrointestinal issue and is not directly associated with eye disorders like glaucoma or schizophrenia.''',bg="black",fg="white",width=90,height=33)
         label.place(x=700,y=200)
         image2 =Image.open('betel.jpg')
         image2 =image2.resize((250,250), Image.ANTIALIAS)

         background_image=ImageTk.PhotoImage(image2)

         background_label = tk.Label(root, image=background_image)

         background_label.image = background_image

         background_label.place(x=350, y=250)
         
    elif (selected_item=='Hair Problems,Depression')or(selected_item=='Diabetes,Eye Health'):
         label=tk.Label(root,text=''' Curry Leaf (Murraya koenigii) ''',width=40,font=('times',20,'bold'),bg="white",fg="black")
         label.place(x=700,y=100)
         label=tk.Label(root,text='''
         Conditions: Digestive issues,Eye health,hair problems,Depression,Diabetes,Heart Disease\n
         Potential Uses: Curry leaves are used in traditional medicine for aiding digestion and promoting 
         gastrointestinal health. They are also believed to have benefits for hair health.
         \n
         Hair Problems:\n
         Curry leaves are traditionally used for hair care. They contain antioxidants, vitamins, and minerals that 
         might help in maintaining healthy hair, preventing premature graying, and promoting hair growth.\n
         Depression:\n
        There is limited scientific evidence directly linking curry leaves to the treatment of depression. 
        However, their nutritional content, including antioxidants, could potentially contribute to overall well-being.\n
        Diabetes:\n
        Some studies suggest that curry leaves may help in managing blood sugar levels due to their potential 
        anti-diabetic properties. They might assist in regulating insulin levels and improving glucose metabolism.\n
        Eye Health:\n
        Curry leaves contain nutrients like vitamin A and antioxidants that are beneficial for eye health. 
        However, specific evidence regarding their direct impact on eye health is limited.\n
        Heart Disease:\n
        There is limited scientific evidence directly supporting curry leaves' role in preventing or treating 
        heart disease. Their potential cardiovascular benefits might be related to their antioxidant content.''',bg="black",fg="white",width=90,height=33)
         label.place(x=700,y=200)
         image2 =Image.open('curry.jpeg')
         image2 =image2.resize((250,250), Image.ANTIALIAS)

         background_image=ImageTk.PhotoImage(image2)

         background_label = tk.Label(root, image=background_image)

         background_label.image = background_image

         background_label.place(x=350, y=250)
         
    elif (selected_item=='Cronic Inflammation, coughs, flatulence')or(selected_item=='Fever, respiratory issues'):
         label=tk.Label(root,text=''' Nagadali (Sida rhombifolia) ''',width=40,font=('times',20,'bold'),bg="white",fg="black")
         label.place(x=700,y=100)
         label=tk.Label(root,text='''
         Conditions: Fever, respiratory issues,Cronic Inflammation, coughs, flatulence \n
         Potential Uses: Nagadali is traditionally used for treating fever and respiratory ailments. 
         It's believed to possess antipyretic properties.
         \n
         Chronic Inflammation: \n
         Nagadali is believed to have anti-inflammatory properties. Some traditional practices suggest 
         its use for managing chronic inflammation, although scientific evidence validating its effectiveness 
         for this purpose is not extensive.\n
         Coughs:\n
         In traditional medicine, Nagadali has been used as an expectorant to help with coughs. 
         It might have properties that can assist in reducing cough symptoms, but robust scientific evidence is lacking.\n
         Flatulence:\n
         Nagadali is sometimes used to alleviate flatulence or gas-related issues. It may have properties that help in
         reducing gas formation or relieving digestive discomfort, but its efficacy for this purpose requires 
         more research.''',bg="black",fg="white",width=90,height=33)
         label.place(x=700,y=200)
         image2 =Image.open('nagadali.jpg')
         image2 =image2.resize((250,250), Image.ANTIALIAS)

         background_image=ImageTk.PhotoImage(image2)

         background_label = tk.Label(root, image=background_image)

         background_label.image = background_image

         background_label.place(x=350, y=250)
         
    elif (selected_item=='Crohns Disease, Swelling of the tissues')or(selected_item=='Blood Plates,wounds')or(selected_item==' Skin disorders'):
         label=tk.Label(root,text=''' Raktachandani (Cordia dichotoma) ''',width=40,font=('times',20,'bold'),bg="white",fg="black")
         label.place(x=700,y=100)
         label=tk.Label(root,text='''
         Conditions: Skin disorders, wounds,Blood Plates, Crohn's Disease--Swelling of the tissues  \n
         Potential Uses: Raktachandani leaves and extracts are used in traditional medicine for skin-related issues 
         such as wounds, sores, and certain skin disorders.
         \n
         Blood Platelets:\n
         Raktachandani is sometimes believed to have properties that can help in maintaining healthy blood platelet levels.
         However, scientific evidence supporting its efficacy specifically for regulating blood platelets might be limited
         or inconclusive.\n
         Crohn's Disease:\n
         Crohn's disease is a chronic inflammatory condition affecting the digestive tract. 
         Raktachandani's traditional use might be attributed to its potential anti-inflammatory properties, which could 
         theoretically aid in managing inflammation associated with Crohn's disease. 
         However, specific scientific evidence supporting its effectiveness for this condition is lacking.\n
         Swelling of Tissues:\n
         In Ayurvedic practices, Raktachandani is sometimes used for its purported anti-inflammatory effects,
         which might help in reducing swelling or inflammation of tissues. However, scientific validation regarding 
         its use for this purpose is limited.''',bg="black",fg="white",width=90,height=33)
         label.place(x=700,y=200)
         image2 =Image.open('rakt.png')
         image2 =image2.resize((250,250), Image.ANTIALIAS)

         background_image=ImageTk.PhotoImage(image2)

         background_label = tk.Label(root, image=background_image)

         background_label.image = background_image

         background_label.place(x=350, y=250)
         
    elif (selected_item=='Liver and Digestive Disorders')or(selected_item=='Digestive issues, antioxidant'):
         label=tk.Label(root,text=''' Wood Sorrel (Oxalis corniculata) ''',width=40,font=('times',20,'bold'),bg="white",fg="black")
         label.place(x=700,y=100)
         label=tk.Label(root,text='''
         Conditions: Digestive issues, antioxidant,Liver and Digestive Disorders\n
         Potential Uses: Wood Sorrel is used for its potential benefits in aiding digestion and as an antioxidant. 
         It's believed to have medicinal properties helpful for various ailments.
         \n
         Liver Disorders:\n
         Wood Sorrel has been used in some traditional practices for its potential hepatoprotective properties, 
         suggesting it might be beneficial for liver health. However, scientific evidence specifically supporting 
         its effectiveness for treating liver disorders is limited.\n
         Digestive Disorders:\n
         Some traditional herbal practices utilize Wood Sorrel for digestive issues. It is believed to have properties 
         that might aid in easing digestive discomfort. However, scientific validation regarding its use for 
         this purpose may be lacking.''',bg="black",fg="white",width=90,height=33)
         label.place(x=700,y=200)
         image2 =Image.open('wood.jpg')
         image2 =image2.resize((250,250), Image.ANTIALIAS)

         background_image=ImageTk.PhotoImage(image2)

         background_label = tk.Label(root, image=background_image)

         background_label.image = background_image

         background_label.place(x=350, y=250)
    
    
    
        



# Create a Label
label = tk.Label(frame_alpr, text='''       Select an Item:         ''',font=('times',15, ' bold '),bg="white",fg="black",height=2,bd=5)
label.place(x=30,y=150)

# Create a Combobox (Drop-down list)
options = ['Minor burns', 'wounds', 'skin irritations', 'Heart Disease', 'Diabetes','lowering blood pressure',
           'cardiovascular diseases','Schizophrenia','Eye Disorders','Hair Problems,Depression','Diabetes,Eye Health',
           'Fever, respiratory issues','Digestive issues, antioxidant','Cronic Inflammation, coughs, flatulence',' Skin disorders',
           'Crohns Disease, Swelling of the tissues','Liver and Digestive Disorders'
           ,'Blood Plates,wounds']  # List of options
selected_option = tk.StringVar()  # Variable to hold selected item
combobox = ttk.Combobox(frame_alpr, textvariable=selected_option, values=options, state="readonly",font=('times',15, ' bold '))
combobox.place(x=30,y=250)

# Create a Button to get the selected item
button = tk.Button(root, text=" Get Selected Item ", command=get_selected_item,width=15, height=2, font=('times', 15, ' bold '),bg="white",fg="black")
button.place(x=30,y=500)




#################################################################################################################
def window():
    root.destroy()



# button2 = tk.Button(frame_alpr, text="Amla", command=Amla, width=20, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
# button2.place(x=10, y=70)




exit = tk.Button(frame_alpr, text="Exit", command=window, width=15, height=1, font=('times', 15, ' bold '),bg="black",fg="white")
exit.place(x=30, y=700)



root.mainloop()

