import customtkinter as ctk
from checkbox import CheckRad
from file_selector import FilRad
from tkinter import filedialog

app_load_list = ["app1", "app2", "app3", "app4"]


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Rad-test")
        self.geometry("800x400")

        # Gör så att raderna kan fylla ut hela bredden
        self.grid_columnconfigure(0, weight=1)

        # Data för våra 5 rader
        installningar = [
            (app_load_list[0], "/home/user", "Kör"),
            (app_load_list[1], "/home/user/pics", "Importera"),
            (app_load_list[2], "/var/log", "Rensa"),
            (app_load_list[3], "/home/user/music", "Spara"),
        ]

        check_rad = CheckRad(self, app_load_list)
        check_rad.grid(row=0, column=0, sticky="ew", padx=10, pady=5)

        # Skapa raderna med en loop
        for i, (namn, path, btn) in enumerate(installningar):
            rad = FilRad(self, label_text=namn, default_path=path, button_name=btn)
            rad.grid(row=(i + 1), column=0, sticky="ew", padx=10, pady=5)


if __name__ == "__main__":
    app = App()
    app.mainloop()
