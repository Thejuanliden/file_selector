import customtkinter as ctk


class SpanApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x600")

        # Konfigurera 3 rader och 3 kolumner med lika vikt
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # DEN STORA RUTAN (2x2)
        # Den börjar i 0,0 men "mutar" in grannarna
        self.big_box = ctk.CTkFrame(self, fg_color="royalblue")
        self.big_box.grid(
            row=0, column=0, rowspan=2, columnspan=2, sticky="nsew", padx=5, pady=5
        )

        self.label1 = ctk.CTkLabel(self.big_box, text="Jag täcker 2x2 rutor!")
        self.label1.pack(expand=True)

        # FYLLNADSRUTOR (för att visa resten av griddet)
        # Rad 0, Kolumn 2 (uppe till höger)
        self.box_top_right = ctk.CTkFrame(self, fg_color="gray25")
        self.box_top_right.grid(
            row=0, column=2, rowspan=3, sticky="nsew", padx=5, pady=5
        )
        self.label1 = ctk.CTkLabel(self.box_top_right, text="Jag täcker 1x3 rutor!")
        self.label1.pack(expand=True)
        # Rad 2, Kolumn 0 (nere till vänster)
        self.box_bottom_left = ctk.CTkFrame(self, fg_color="gray25")
        self.box_bottom_left.grid(
            row=2, column=0, columnspan=2, sticky="nsew", padx=5, pady=5
        )
        self.label1 = ctk.CTkLabel(self.box_bottom_left, text="Jag täcker 2x1 rutor!")
        self.label1.pack(expand=True)


if __name__ == "__main__":
    app = SpanApp()
    app.mainloop()
