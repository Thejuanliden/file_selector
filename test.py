import customtkinter as ctk


class MinApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Layout Exempel")
        self.geometry("600x400")

        # Konfigurera grid för huvudfönstret (1 rad, 2 kolumner)
        self.grid_columnconfigure([0, 1, 2], weight=1)  # Kolumn 1 (höger) ska expandera
        self.grid_rowconfigure(0, weight=1)  # Raden ska ta upp hela höjden

        # --- SIDOMENY ---
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")

        self.label = ctk.CTkLabel(self.sidebar_frame, text="Meny", font=("Arial", 20))
        self.label.grid(row=0, column=0, padx=20, pady=20)

        self.btn_1 = ctk.CTkButton(self.sidebar_frame, text="Knapp 1")
        self.btn_1.grid(row=1, column=0, padx=20, pady=10)

        # --- SIDOMENY HÖGER ---
        self.sidebar_frame_r = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame_r.grid(row=0, column=2, sticky="nsew")

        self.label = ctk.CTkLabel(self.sidebar_frame_r, text="Meny", font=("Arial", 20))
        self.label.grid(row=0, column=0, padx=20, pady=20)

        self.btn_1 = ctk.CTkButton(self.sidebar_frame_r, text="Knapp 1")
        self.btn_1.grid(row=1, column=0, padx=20, pady=10)

        # --- HUVUDINNEHÅLL ---
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.main_label = ctk.CTkLabel(self.main_frame, text="Välkommen till huvudvyn!")
        self.main_label.grid(row=0, column=0)


if __name__ == "__main__":
    app = MinApp()
    app.mainloop()
