# Maria Estrada SW Development Midterm
import tkinter as tk

# Menu and prices
menu = {"Tea": 2.00, "Cappuccino": 2.00, "Latte": 2.00,"Iced Latte": 2.00, "Cold Brew": 2.00, "Smoothie": 4.00,
        "Muffin": 3.00, "Croissant": 3.00, "Bagel": 3.00, "Cookie": 1.50}

class CSCafe(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("CS Cafe at MSU Denver")
        self.pack()

        #Create title on page
        self.title_label = tk.Label(self, text="Welcome to the CS Cafe", font=("Helvetica", 20, "bold"), pady=15)
        self.title_label.pack()

        #*****Menu*****
        #Create box to list menu items
        menu_frame = tk.LabelFrame(self, text="Menu")
        menu_frame.pack(side="left", padx=10, pady=10)
        #List menu items
        self.menulist = tk.Listbox(menu_frame)
        for item, price in menu.items():
            self.menulist.insert(tk.END, "{item} - ${price:.2f}".format(item=item, price=price))
        self.menulist.pack(side="left", padx=10, pady=10)

        # Create a button to add an item to the order
        middle = tk.LabelFrame(self)
        middle.pack(side="left", padx=10, pady=10)
        self.add_button = tk.Button(middle, text="Add to order", command=self.add_item)
        self.add_button.pack(pady=10)
        # Label for cost
        self.total_label = tk.Label(middle, text="Total cost: $0.00")
        self.total_label.pack()

        #*****Order*****
        # Display customers order in a frame
        menu_order = tk.LabelFrame(self, text="Order")
        menu_order.pack(side="left", padx=10, pady=10)
        self.orderlist = tk.Listbox(menu_order)
        self.orderlist.pack(side="right", padx=10, pady=10)

        #******Checkout******
        #Frame
        checkout = tk.LabelFrame(self, text="Checkout")
        checkout.pack(side="right", padx=10, pady=10)
        #Place order buttom
        self.exit = tk.Button(checkout, text="Exit", command=root.quit)
        self.exit.pack(side="bottom", padx=5, pady=5)
        #Get name and student ID for order
        self.Name = tk.Label(checkout, text="Enter your Name:").pack()
        self.Name1 = tk.Entry(checkout, width=15, borderwidth=3).pack()
        self.ID = tk.Label(checkout, text="Enter your student ID:").pack()
        self.ID1 = tk.Entry(checkout, width=15, borderwidth=3).pack()

        def placeOrder():
            if self.orderlist.size() > 0:
                self.OrderPlace = tk.Label(checkout, text="Thank you for your order!")
                self.OrderPlace.pack()

        self.exit = tk.Button(checkout, text="Place Order", command=placeOrder)
        self.exit.pack(padx=5, pady=5)


    def add_item(self):
        # Get menu item
        selected_item = self.menulist.get(tk.ACTIVE)  # Get the currently selected item
        if not selected_item:
            return
        item = selected_item.split(" - ")[0]  # Extract the item name from the selected item string

        # Add to order listbox and calculate total
        self.orderlist.insert(tk.END, item) # Add item to listbox
        total = sum([menu[item] for item in self.orderlist.get(0, tk.END)]) # Add cost of order - got from Chat GPT
        self.total_label.config(text="Total cost: ${total:.2f}".format(total=total)) # Update cost - got from Chat GPT

if __name__ == "__main__":
    root = tk.Tk()
    app = CSCafe(master=root) #Root objects as master
    app.mainloop()


