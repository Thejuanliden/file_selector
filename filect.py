import customtkinter as ctk
from tkinter import filedialog, messagebox

# Grundinställningar för temat
ctk.set_appearance_mode("System")  # "System", "Dark" eller "Light"
ctk.set_default_color_theme("blue")  # "blue", "green" eller "dark-blue"
ctk.set_widget_scaling(1.2)  # Skalar upp allt med 20%


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Modern Filväljare")
        self.geometry("600x450")

        # Layout med grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Rubrik
        self.label = ctk.CTkLabel(
            self, text="Hantera sökvägar", font=ctk.CTkFont(size=20, weight="bold")
        )
        self.label.grid(row=0, column=0, padx=20, pady=20)

        # Knapp-panel
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        self.btn_file = ctk.CTkButton(
            self.button_frame, text="Lägg till fil", command=self.choose_file
        )
        self.btn_file.pack(side="left", padx=10, pady=10, expand=True)

        self.btn_folder = ctk.CTkButton(
            self.button_frame, text="Lägg till mapp", command=self.choose_folder
        )
        self.btn_folder.pack(side="left", padx=10, pady=10, expand=True)

        # Textområde (Textbox istället för Listbox för bättre styling)
        self.textbox = ctk.CTkTextbox(self, width=560, height=200)
        self.textbox.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        # Spara-knapp
        self.btn_save = ctk.CTkButton(
            self,
            text="Skriv ut valda till konsol",
            fg_color="transparent",
            border_width=2,
            command=self.save_to_list,
        )
        self.btn_save.grid(row=3, column=0, padx=20, pady=20)

    def choose_file(self):
        path = filedialog.askopenfilename(
            title="Välj en fil", initialdir="/home/jlid/code"
        )
        if path:
            self.textbox.insert("end", f"FIL: {path}\n")

    def choose_folder(self):
        path = filedialog.askdirectory(title="Välj en mapp")
        if path:
            self.textbox.insert("end", f"MAPP: {path}\n")

    def save_to_list(self):
        content = self.textbox.get("1.0", "end-1c")
        if not content.strip():
            messagebox.showwarning("Varning", "Listan är tom!")
            return

        # Splitta texten till en lista av strängar
        paths_list = content.splitlines()
        print("Sparade strängar:")
        for p in paths_list:
            print(p)

        messagebox.showinfo(
            "Klart", f"{len(paths_list)} sökvägar har loggats i terminalen."
        )


if __name__ == "__main__":
    app = App()
    app.mainloop()
