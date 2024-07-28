# Author: Regina Anne Vergara
# Date Submitted: 7/27/24
# Activity: M08 Final Project
# Description: RideIT is a transportation app that helps you book rides wherever you are by entering your location 
# where drivers near you can pick you up!


import tkinter as tk
from tkinter import messagebox

# Global counter for generating booking numbers
booking_counter = 1

def open_name_screen():
    # Hide the start screen and show the name entry screen
    start_screen.pack_forget()
    name_screen.pack(pady=20)

def open_booking_screen():
    # Hide the name screen and show the booking screen
    name_screen.pack_forget()
    booking_screen.pack(pady=20)

def return_to_booking_screen():
    # Hide the confirmation screen and show the booking screen
    confirmation_screen.pack_forget()
    booking_screen.pack(pady=20)

def return_to_name_screen():
    # Hide the booking screen and show the name entry screen
    booking_screen.pack_forget()
    name_screen.pack(pady=20)

def book_transport():
    global booking_counter  # Use the global counter variable
    
    vehicle_type = vehicle_var.get()
    pickup_location = pickup_entry.get()
    destination = destination_entry.get()
    rider_name = name_entry.get()

    if not rider_name:
        messagebox.showwarning("Input Error", "Please enter your name.")
    elif not vehicle_type:
        messagebox.showwarning("No Selection", "Please select a vehicle type.")
    elif not pickup_location:
        messagebox.showwarning("Input Error", "Please enter your pickup location.")
    elif not destination:
        messagebox.showwarning("Input Error", "Please enter your destination.")
    else:
        # Generate the booking number
        booking_number = booking_counter
        booking_counter += 1  # Increment the counter for the next booking
        
        # Display confirmation screen
        confirmation_message = (
            f"Booking Confirmation:\n"
            f"Booking Number: {booking_number}\n"
            f"Rider Name: {rider_name}\n"
            f"Vehicle Type: {vehicle_type}\n"
            f"Pickup Location: {pickup_location}\n"
            f"Destination: {destination}\n\n"
            "Your driver is on the way!"
        )
        
        # Show confirmation screen with return button
        confirmation_label.config(text=confirmation_message)
        booking_screen.pack_forget()
        confirmation_screen.pack(pady=20)

# Main window
root = tk.Tk()
root.title("RideIT")

# Start Screen
start_screen = tk.Frame(root)
start_screen.pack(pady=20)

start_label = tk.Label(start_screen, text="Welcome to RideIT", font=("Arial", 20))
start_label.pack(pady=10)

book_button = tk.Button(start_screen, text="Book", command=open_name_screen)
book_button.pack(pady=20)

# Name Entry Screen
name_screen = tk.Frame(root)

tk.Label(name_screen, text="Enter Your Name:", font=("Arial", 14)).pack(pady=10)
name_entry = tk.Entry(name_screen, width=40)
name_entry.pack(pady=10)

proceed_button = tk.Button(name_screen, text="Proceed", command=open_booking_screen)
proceed_button.pack(pady=20)

# Booking Screen
booking_screen = tk.Frame(root)

# Vehicle Selection
vehicle_var = tk.StringVar()

vehicle_options = ["7-Seater Car", "5-Seater Car", "2-Seater Car"]
tk.Label(booking_screen, text="Choose Vehicle Type:", font=("Arial", 14)).pack(pady=10)

for vehicle in vehicle_options:
    rb = tk.Radiobutton(booking_screen, text=vehicle, variable=vehicle_var, value=vehicle)
    rb.pack(anchor=tk.W)

# Pickup
tk.Label(booking_screen, text="Pickup Location:", font=("Arial", 12)).pack(pady=5)
pickup_entry = tk.Entry(booking_screen, width=40)
pickup_entry.pack(pady=5)

# Destination
tk.Label(booking_screen, text="Destination:", font=("Arial", 12)).pack(pady=5)
destination_entry = tk.Entry(booking_screen, width=40)
destination_entry.pack(pady=5)

# Book Button
book_button = tk.Button(booking_screen, text="Book Now", command=book_transport)
book_button.pack(pady=10)

# Confirmation Screen
confirmation_screen = tk.Frame(root)

confirmation_label = tk.Label(confirmation_screen, text="", font=("Arial", 14))
confirmation_label.pack(pady=20)

# Return Button (in Confirmation Screen)
return_button_confirmation = tk.Button(confirmation_screen, text="Edit Booking", command=return_to_booking_screen)
return_button_confirmation.pack(pady=10)

# Start the GUI event loop
root.mainloop()
