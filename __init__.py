import customtkinter as ctk
from tkinter import filedialog, messagebox
import os

def search_c00kies(servicio):
    filepath = filedialog.askopenfilename(title=f"Select a file for {servicio}")
    if not filepath:
        return
    

    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
        

    if servicio.lower() in content.lower():
        respuesta = messagebox.askyesno("Cookies saved", f"Founded cookies for {servicio}. Do you want to save them?")
        if respuesta:
            save_c00kies(filepath, servicio)
    else:
        messagebox.showinfo("Without cookies", f"No cookies for {servicio} in the selected file.")

def save_c00kies(filepath, servicio):

    with open(filepath, 'r', encoding='utf-8') as file:
        cookies = [line for line in file if servicio.lower() in line.lower()]
    

    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    save_path = os.path.join(desktop_path, 'cookies.txt')
    

    with open(save_path, 'w', encoding='utf-8') as file:
        file.writelines(cookies)
    
    messagebox.showinfo("Saved Successfully", f"Cookies of {servicio} saved in {save_path}")

def other_service():

    other_service_window = ctk.CTkToplevel(root)
    other_service_window.title("Other service")
    other_service_window.geometry("300x100")
    other_service_window.iconbitmap("descarga.ico")
    ctk.CTkLabel(other_service_window, text="Name:").pack(pady=5)
    
    servicio_entry = ctk.CTkEntry(other_service_window)
    servicio_entry.pack(pady=5)
    
    def on_enter(event):
        servicio = servicio_entry.get()
        other_service_window.destroy() 
        search_c00kies(servicio)
    
    servicio_entry.bind("<Return>", on_enter)

ctk.set_appearance_mode("System") 
ctk.set_default_color_theme("blue") 

root = ctk.CTk()
root.title("Cookies Filter - Value - V.1")
root.geometry("400x250")
root.iconbitmap("descarga.ico")

servicios = ["Netflix", "Disney", "HBO", "Epic Games"]
for servicio in servicios:
    button = ctk.CTkButton(root,     
    border_width=2,
    corner_radius=3,
    border_color= "black", 
    bg_color="#262626",
    fg_color= "#262626",hover=True, hover_color='#4000ff', text=servicio, command=lambda s=servicio: search_c00kies(s))
    button.pack(pady=10)


otro_button = ctk.CTkButton(root,    
    border_width=2,
    corner_radius=3,
    border_color= "black", 
    bg_color="#262626",
    fg_color= "#262626",
    hover=True, hover_color='#4000ff', text="Other", command=other_service)
otro_button.pack(pady=10)

root.mainloop()