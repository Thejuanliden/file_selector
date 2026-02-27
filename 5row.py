import customtkinter as ctk
from tkinter import filedialog


class FilRad(ctk.CTkFrame):
    def __init__(self, master, label_text, default_path, button_name, **kwargs):
        super().__init__(master, **kwargs)

        self.valjd_mapp_path = default_path
        self.valjd_fil_path = "Ingen vald"

        # Vi konfigurerar kolumnerna så att textfälten (1 och 3) kan expandera
        self.grid_columnconfigure((1, 3), weight=1)

        # 1. Checkbox
        self.check = ctk.CTkCheckBox(self, text=label_text, width=100)
        self.check.grid(row=0, column=0, padx=10, pady=10)

        # 2. Fil-sektion
        self.fil_label = ctk.CTkLabel(
            self,
            text=self.valjd_fil_path,
            fg_color="gray20",
            corner_radius=6,
            width=200,
            anchor="w",
            wraplength=200,
        )
        self.fil_label.grid(row=0, column=1, padx=5, sticky="ew")

        self.file_btn = ctk.CTkButton(
            self, text="Välj Fil", width=80, command=self.valj_fil
        )
        self.file_btn.grid(row=0, column=2, padx=5)

        # 3. Mapp-sektion
        self.mapp_label = ctk.CTkLabel(
            self,
            text=self.valjd_mapp_path,
            fg_color="gray20",
            corner_radius=6,
            width=200,
            anchor="w",
            wraplength=200,
        )
        self.mapp_label.grid(row=0, column=3, padx=5, sticky="ew")

        self.folder_btn = ctk.CTkButton(
            self, text="Välj Mapp", width=80, fg_color="gray30", command=self.valj_mapp
        )
        self.folder_btn.grid(row=0, column=4, padx=5)

        # 4. Funktionsknapp
        self.action_btn = ctk.CTkButton(
            self, text=button_name, width=80, fg_color="green"
        )
        self.action_btn.grid(row=0, column=5, padx=10)

    def valj_fil(self):
        fil = filedialog.askopenfilename()
        if fil:
            self.valjd_fil_path = fil
            # Här uppdaterar vi texten i labeln direkt!
            self.fil_label.configure(text=fil)

    #                text=fil.split("/")[-1]
    #           )  # split för att bara visa filnamnet

    def valj_mapp(self):
        mapp = filedialog.askdirectory(initialdir=self.valjd_mapp_path)
        if mapp:
            self.valjd_mapp_path = mapp
            # Uppdaterar mappen
            self.mapp_label.configure(text=mapp)


# 2. HUVUDAPPEN
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Rad-test")
        self.geometry("800x400")

        # Gör så att raderna kan fylla ut hela bredden
        self.grid_columnconfigure(0, weight=1)

        # Data för våra 5 rader
        installningar = [
            ("Backup", "/home/user", "Kör"),
            ("Bilder", "/home/user/pics", "Importera"),
            ("Loggar", "/var/log", "Rensa"),
            ("Musik", "/home/user/music", "Spara"),
            ("Projekt", "/home/user/dev", "Bygg"),
        ]

        # Skapa raderna med en loop
        for i, (namn, path, btn) in enumerate(installningar):
            rad = FilRad(self, label_text=namn, default_path=path, button_name=btn)
            rad.grid(row=i, column=0, sticky="ew", padx=10, pady=5)


if __name__ == "__main__":
    app = App()
    app.mainloop()
