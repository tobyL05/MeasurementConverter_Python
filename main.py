import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

#global
buttonState = True
switchButtonState = True

#Window Init
window = tk.Tk()
window.title("Measurement Converter")
window.resizable(False, False)
window.geometry("300x200")
window.config(bg="gainsboro")

def chooseUnit(eventObject): #checks which combox is selected
      #CONVERT TO IMPERIAL FROM METRIC
   if switchButtonState: 
      if units.get()==unitsImperial[0]:
          unitSymbol.config(text="cm")
      if units.get()==unitsImperial[1]:
          unitSymbol.config(text="Km")
      if units.get()==unitsImperial[2]:
          unitSymbol.config(text="Kg")
      if units.get()==unitsImperial[3]:
          unitSymbol.config(text="\N{DEGREE SIGN}C")  
           
      #CONVERT TO METRIC FROM IMPERIAL
   else: 
      if units.get()==unitsMetric[0]:
          unitSymbol.config(text="In")
      if units.get()==unitsMetric[1]:
          unitSymbol.config(text="Mi")
      if units.get()==unitsMetric[2]:
          unitSymbol.config(text="Lbs")
      if units.get()==unitsMetric[3]:
          unitSymbol.config(text="\N{DEGREE SIGN}F")

def convert():
    #check for number
   try:
      input = float(textBox.get())
   except ValueError:
      tkinter.messagebox.showwarning(title="Error!", message="Enter a number!") 
      #throw error if input cannot be converted to float

  #CONVERTING TO IMPERIAL UNITS
   if switchButtonState:
      if units.get()==unitsImperial[0]:
          result = float(round(input/2.54,2)) #converts to inches
          symbol = "in"
      if units.get()==unitsImperial[1]:
          result = float(round(input/1.609,2)) #converts to miles
          symbol = "mi"
      if units.get()==unitsImperial[2]:
          result = float(round(input*2.205,2)) #converts to pounds
          symbol = "lbs"
      if units.get()==unitsImperial[3]:
          result = float(round((input*(9/5))+32,2)) #converts to farenheit
          symbol = "\N{DEGREE SIGN}F"
         
   #CONVERTING TO METRIC UNITS
   else:
      if units.get()==unitsMetric[0]:
          result = float(round(input*2.54,2)) #converts to cm
          symbol = "Cm"
      if units.get()==unitsMetric[1]:
          result = float(round(input*1.609,2)) #converts to km
          symbol = "Km"
      if units.get()==unitsMetric[2]:
          result = float(round(input*2.205,2)) #converts to kg
          symbol = "Kg"
      if units.get()==unitsMetric[3]:
          result = float(round((input-32)*(5/9),2)) #converts to celcius
          symbol = "\N{DEGREE SIGN}C"

   #show final result
   result = str(result) + " " + symbol
   finalResult.config(text=result) 
   def copy(): #copy final result
      window.clipboard_clear()
      window.clipboard_append(result)
   copyButton.config(command = copy)
   copyButton.place(x=200, y=140)

def darkmode(): #for dark mode button
   global buttonState
   if buttonState:
         #turn dark
         window.config(bg="#424242")
         convertText.config(fg="white", bg="#424242")
         unitSymbol.config(fg="white", bg="#424242")
         darkModeButton.config(bg="white")
         finalResult.config(fg="white",bg="#424242")
         buttonState = False
   else:
         #turn light
         window.config(bg="gainsboro")
         convertText.config(fg="black", bg="gainsboro")
         unitSymbol.config(fg="black", bg="gainsboro")
         darkModeButton.config(bg="black")
         finalResult.config(bg="gainsboro", fg="black")
         buttonState = True   
               
def switchUnits(): #switches between imperial and metric
     global switchButtonState
     if switchButtonState:
         units.config(values=unitsMetric)
         switchButtonState = False
     else: 
         units.config(values=unitsImperial)
         switchButtonState = True
     #RESET WINDOW
     finalResult.config(text="")
     unitSymbol.config(text="")
     textBox.delete(0,'end')
     units.set("")
     copyButton.place_forget()
    
#Top row
convertText = tk.Label(text="Convert to",bg="gainsboro",font=("Arial", 20))
convertText.grid(row=0, column=0, padx = (5,5),pady=10, sticky="w")
unitsImperial = ("Inches(in)", "Miles(mi)", "Pounds(lbs)", "Farenheit (\N{DEGREE SIGN}F)")
unitsMetric = ("Centimeter(Cm)","Kilometer(Km)","Kilogram(Kg)","Celcius (\N{DEGREE SIGN}C)")
units = ttk.Combobox(values=unitsImperial)
units.grid(row=0, column=1)    
units.bind("<<ComboboxSelected>>", chooseUnit)

#Mid Row
textBox = tk.Entry(window, width=20)
textBox.grid(row=1, column=0,padx = 10, pady=10, sticky="w")
unitSymbol = tk.Label(text=None,bg="gainsboro")
unitSymbol.grid(row=1, column=1, sticky="w")

#Bottom row
convertButton = tk.Button(window, text="Convert", command=convert)
convertButton.grid(row=2,column=0,padx=10,pady=15,ipadx=35,sticky="w")
finalResult = tk.Label(window, font=("Arial", 14),bg="gainsboro",text="")    
finalResult.grid(row=2,column=1)     

#Bottom row buttons
darkModeButton = tk.Button(window,width=2,bg="Black",bd=0,command=darkmode)
darkModeButton.place(x=100, y=170)
switchButton = tk.Button(window, text="Switch",command=switchUnits)
switchButton.place(x=130,y=169)
copyButton = tk.Button(window, text="Copy")
copyButton.place_forget()
window.mainloop()