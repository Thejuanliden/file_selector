import customtkinter as ctk

app_load_list = ["app1", "app2", "app3", "app4"]


class FilRad(ctk.CTkFrame):
    def add_to_load_list(self, name):
        if name not in app_load_list:
            app_load_list.append(name)
            app_load_list.sort()
        else:
            app_load_list.remove(name)
            app_load_list.sort()
        self.fil_label.configure(text=str(app_load_list))
        print(f"Nuvarande lista: {app_load_list}")

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        #        self.valjd_mapp_path = default_path
        #        self.valjd_fil_path = "Ingen vald"

        # Vi konfigurerar kolumnerna så att textfälten (1 och 3) kan expandera
        self.grid_columnconfigure((1, 2, 3, 4, 5), weight=1)

        for sw in app_load_list:
            checkbox_name = "check_" + sw
            self.checkbox_name = ctk.CTkCheckBox(
                self, text=sw, command=lambda: self.add_to_load_list(sw), width=100
            )
            self.checkbox_name.grid(
                row=checkbox_name.index(sw), column=0, padx=10, pady=10
            )

        # 1. Checkbox
        self.check_app1 = ctk.CTkCheckBox(
            self, text="App 1", command=lambda: self.add_to_load_list("app1"), width=100
        )
        self.check_app1.grid(row=0, column=0, padx=10, pady=10)
        self.check_app1.select()

        self.check_app2 = ctk.CTkCheckBox(
            self, text="App 2", command=lambda: self.add_to_load_list("app2"), width=100
        )
        self.check_app2.grid(row=0, column=1, padx=10, pady=10)
        self.check_app2.select()

        self.check_app3 = ctk.CTkCheckBox(
            self, text="App 3", command=lambda: self.add_to_load_list("app3"), width=100
        )
        self.check_app3.grid(row=0, column=2, padx=10, pady=10)
        self.check_app3.select()

        self.check_app4 = ctk.CTkCheckBox(
            self, text="App 4", command=lambda: self.add_to_load_list("app4"), width=100
        )
        self.check_app4.grid(row=0, column=3, padx=10, pady=10)
        self.check_app4.select()

        # 2. Fil-sektion
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


# 2. HUVUDAPPEN
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Rad-test")
        self.geometry("800x400")

        # Gör så att raderna kan fylla ut hela bredden
        self.grid_columnconfigure(0, weight=1)

        rad = FilRad(self)
        rad.grid(row=1, column=0, sticky="ew", padx=10, pady=5)


if __name__ == "__main__":
    app = App()
    app.mainloop()
