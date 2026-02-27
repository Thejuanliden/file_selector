import tkinter as tk
from tkinter import filedialog, messagebox


def choose_file():
    # Öppnar en fildialog för att välja en enskild fil
    file_path = filedialog.askopenfilename(title="Välj en fil")
    if file_path:
        listbox.insert(tk.END, f"FIL: {file_path}")


def choose_folder():
    # Öppnar en dialog för att välja en mapp
    folder_path = filedialog.askdirectory(title="Välj en mapp")

    if folder_path:
        listbox.insert(tk.END, f"MAPP: {folder_path}")


def save_to_list():
    # Hämtar allt innehåll från listboxen som en lista av strängar
    items = listbox.get(0, tk.END)
    if not items:
        messagebox.showwarning("Varning", "Listan är tom!")
        return

    # Här kan du göra vad du vill med strängarna, t.ex. printa dem
    print("Valda sökvägar sparade som strängar:")
    for item in items:
        print(item)

    messagebox.showinfo(
        "Klart", "Sökvägarna har sparats som textsträngar (se konsolen)."
    )


# Grundinställningar för fönstret
root = tk.Tk()
root.title("Fil- & Mappväljare")
root.geometry("500x400")

# Knappar
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Välj fil", command=choose_file).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Välj mapp", command=choose_folder).pack(side=tk.LEFT, padx=5)

# Lista för att visa valda objekt
listbox = tk.Listbox(root, width=60, height=15)
listbox.pack(pady=10, padx=10)

# Spara-knapp
tk.Button(
    root, text="Spara valda strängar", command=save_to_list, bg="lightgreen"
).pack(pady=5)

root.mainloop()
