import customtkinter as ctk

app_load_list = ["app1", "app2", "app3", "app4"]


class CheckRad(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # Vi konfigurerar kolumnerna så att textfälten (1 och 3) kan expandera
        self.grid_columnconfigure((1, 2, 3, 4, 5), weight=1)
        # skapa lista för att spara referenser till checkboxar som det behövs senare
        self.checkboxes = []

        for i, sw in enumerate(app_load_list):
            cb = ctk.CTkCheckBox(
                self, text=sw, command=lambda n=sw: self.add_to_load_list(n), width=100
            )
            cb.grid(row=0, column=i, padx=10, pady=10)
            cb.select()

        self.fil_label = ctk.CTkLabel(
            self,
            text=app_load_list,
            fg_color="gray20",
            corner_radius=6,
            width=200,
            anchor="w",
            wraplength=200,
        )
        self.fil_label.grid(row=0, column=4, padx=5, sticky="e")

    def add_to_load_list(self, name):
        if name not in app_load_list:
            app_load_list.append(name)
            app_load_list.sort()
        else:
            app_load_list.remove(name)

        self.fil_label.configure(text=str(app_load_list))
        print(f"Nuvarande lista: {app_load_list}")


# 2. HUVUDAPPEN
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Rad-test")
        self.geometry("800x400")

        # Gör så att raderna kan fylla ut hela bredden
        self.grid_columnconfigure(0, weight=1)

        rad = CheckRad(self)
        rad.grid(row=1, column=0, sticky="ew", padx=10, pady=5)


if __name__ == "__main__":
    app = App()
    app.mainloop()
