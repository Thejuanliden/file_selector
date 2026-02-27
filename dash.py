import customtkinter as ctk


class DashboardApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Enkel Dashboard")
        self.geometry("400x400")

        # 1. Konfigurera huvudfönstrets grid
        # Vi vill ha 2 kolumner som delar lika på utrymmet
        self.grid_columnconfigure((0, 1), weight=1)
        # Vi vill att rad 1 (där boxarna är) ska växa, men inte rad 0 (topbar)
        self.grid_rowconfigure(1, weight=1)

        # --- RAD 0: TOP BAR ---
        # columnspan=2 gör att denna frame sträcker sig över båda kolumnerna
        self.top_bar = ctk.CTkFrame(self, height=60, corner_radius=0)
        self.top_bar.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=5)

        self.title_label = ctk.CTkLabel(
            self.top_bar, text="MIN DASHBOARD", font=("Arial", 18, "bold")
        )
        self.title_label.pack(
            pady=10
        )  # Här använder vi pack() inuti framen för enkelhet

        # --- RAD 1, KOLUMN 0: VÄNSTER BOX ---
        self.left_box = ctk.CTkFrame(self)
        self.left_box.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.l_label = ctk.CTkLabel(self.left_box, text="Statistik")
        self.l_label.pack(pady=20)

        # --- RAD 1, KOLUMN 1: HÖGER BOX ---
        self.right_box = ctk.CTkFrame(self)
        self.right_box.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        self.r_label = ctk.CTkLabel(self.right_box, text="Användare")
        self.r_label.pack(pady=20)


if __name__ == "__main__":
    app = DashboardApp()
    app.mainloop()
