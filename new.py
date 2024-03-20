import customtkinter as ctk

from PIL import Image, ImageTk


# Create the main application window
app = ctk.CTk()
app.title("Background Image Resizing Example")

# Load the background image

fam = ctk.CTkFrame(app,background_image="download.png")
fam.pack()
app.mainloop()
