import customtkinter as ctk
from deep_translator import GoogleTranslator
from PIL import Image
import os


def translate_language():
    text_to_trans = user_text.get()
    lang = lang_to_var.get()

    output = GoogleTranslator(source="auto", target=lang).translate(text_to_trans)

    translated_text.configure(state="normal")
    translated_text.delete(0, "end")
    translated_text.insert(0, output)


root = ctk.CTk()
root.title("Language Translator")
root.minsize(500, 600)
root.maxsize(500, 600)

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

image_path = os.path.join(os.path.dirname(__file__), 'design.jpg')
image = ctk.CTkImage(light_image=Image.open(image_path), size=(750, 700))
image_label = ctk.CTkLabel(root, image=image, text=" ")
image_label.place(x=0, y=0)

title = ctk.CTkLabel(root, text="Language translator", font=('COMIC SANS MS', 40), fg_color="#C850C0", corner_radius=10)
title.pack(anchor=ctk.CENTER, pady=40)

app_frame = ctk.CTkFrame(root, width=500, height=500, fg_color="transparent", border_color="#FFCC70", border_width=4,
                         corner_radius=10)
app_frame.pack(fill=ctk.X, padx=20, pady=10)

ctk.CTkLabel(app_frame, text="Enter text to translate here ").pack(expand=True, fill=ctk.X)
user_text = ctk.CTkEntry(app_frame, height=100)
user_text.pack(fill=ctk.X)

ctk.CTkLabel(app_frame, text="Choose language to translate to: ").pack()

lang_to_var = ctk.StringVar()
lang_list = GoogleTranslator().get_supported_languages()
lang_to = ctk.CTkOptionMenu(app_frame, values=lang_list, variable=lang_to_var)
lang_to.set("english")
lang_to.pack(fill=ctk.X, ipady=5)

ctk.CTkLabel(app_frame, text="Translated Text").pack()
translated_text = ctk.CTkEntry(app_frame, height=100, placeholder_text="Translated text will show here",
                               placeholder_text_color="grey", state=ctk.DISABLED)
translated_text.pack(fill=ctk.X)

translated_btn = ctk.CTkButton(app_frame, text="Translate", command=translate_language, corner_radius=50, width=80,
                               height=40, fg_color="#C850C0", hover_color="#4158D0")
translated_btn.pack(pady=20)

root.mainloop()
