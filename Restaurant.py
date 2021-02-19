from tkinter import *
from tkinter import messagebox

def process(pizza_type,pizza_size,beverage_type,beverage_size):
	message1 = messagebox.askyesno("Confirm" , "Is this your final order?")
	# the calculation
	if message1 == 1:
		Price = LabelFrame(window, text = "Bill" , padx = 30 , pady = 25 )
		Price.grid(row = 2 , column = 0)
		price = {"Peporoni Pizza" : 100 , "Cheese Pizza" : 125 , "Veg-Pizza" : 75 , "Coke" : 25 , "Limca" : 35 , "Pepsi" : 40}
		size = {"Large " : 3 , "Medium " : 2 , "Small " : 1 , "Large" : 3 , "Medium" : 2 , "Small" : 1}
		price_1 = Label(Price , text = (pizza_size + pizza_type + " and " + beverage_size + beverage_type), bg = "Yellow")
		price_1.grid(row = 0 , column = 0 )
		price_2 = Label(Price , text = ("Pizza : " + str(price[pizza_type] * size[pizza_size]) + " and " + "Beverage : " + str(price[beverage_type] * size[beverage_size])), bg = "Yellow")
		price_2.grid(row = 1 , column = 0 )
		final_price = Label(Price , text = ("Total : " + str( price[pizza_type] * size[pizza_size] + price[beverage_type] * size[beverage_size])), bg = "Yellow")
		final_price.grid(row = 2 , column = 0 )

window = Tk()
window.title("Bill maker")


# Defining The Radio Buttons
pizza_type = StringVar()
pizza_type.set(0)
a = LabelFrame(window, text = "Pizza Type" , padx = 30 , pady = 25 )
a.grid(row = 0 , column = 0, padx = 35 , pady = 30)
Radiobutton(a, text = "Peporoni Pizza" , variable = pizza_type , value = "Peporoni Pizza",bg = "#22AA22", fg = "Black").grid(row = 0 , column = 0)
Radiobutton(a, text = "Cheese Pizza" , variable = pizza_type , value = "Cheese Pizza",bg = "#22AA22", fg = "Black").grid(row = 1 , column = 0)
Radiobutton(a, text = "Veg-Pizza" , variable = pizza_type , value = "Veg-Pizza",bg = "#22AA22", fg = "Black").grid(row = 2 , column = 0)

pizza_size = StringVar()
pizza_size.set(0)
b = LabelFrame(window, text = "Pizza Size" , padx = 30 , pady = 25 )
b.grid(row = 0 , column = 1, padx = 35 , pady = 30)
Radiobutton(b, text = "Large" , variable = pizza_size , value = "Large " ,bg = "#AA2222", fg = "Black").grid(row = 0 , column = 0)
Radiobutton(b, text = "Medium" , variable = pizza_size , value = "Medium ",bg = "#AA2222", fg = "Black").grid(row = 1 , column = 0)
Radiobutton(b, text = "Small" , variable = pizza_size , value = "Small ",bg = "#AA2222", fg = "Black").grid(row = 2 , column = 0)

beverage_type = StringVar()
beverage_type.set(0)
c = LabelFrame(window, text = "Beverage Type" , padx = 30 , pady = 25 )
c.grid(row = 0 , column = 2, padx = 35 , pady = 30)
Radiobutton(c, text = "Coke" , variable = beverage_type , value = "Coke",bg = "#2222AA", fg = "Black").grid(row = 0 , column = 0)
Radiobutton(c, text = "Limca" , variable = beverage_type , value = "Limca",bg = "#2222AA", fg = "Black").grid(row = 1 , column = 0)
Radiobutton(c, text = "Pepsi" , variable = beverage_type , value = "Pepsi",bg = "#2222AA", fg = "Black").grid(row = 2 , column = 0)

beverage_size = StringVar()
beverage_size.set(0)
d = LabelFrame(window, text = "Beverage Size" , padx = 30 , pady = 25 )
d.grid(row = 0 , column = 3, padx = 35 , pady = 30)
Radiobutton(d, text = "Large" , variable = beverage_size , value = "Large",bg = "#856ff8", fg = "Black").grid(row = 0 , column = 0)
Radiobutton(d, text = "Medium" , variable = beverage_size , value = "Medium",bg = "#856ff8", fg = "Black").grid(row = 1 , column = 0)
Radiobutton(d, text = "Small" , variable = beverage_size , value = "Small",bg = "#856ff8", fg = "Black").grid(row = 2 , column = 0)


#Making the submit button
button = Button(window, text = "Submit" ,bg = "Black" , fg = "White", command = lambda : process(pizza_type.get(),pizza_size.get(),beverage_type.get(),beverage_size.get()))
button.grid(row = 1 , column = 0 )
window.mainloop()