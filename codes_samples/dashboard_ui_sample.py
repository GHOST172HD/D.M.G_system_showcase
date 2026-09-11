from tkinter import messagebox, filedialog
from tkinter.scrolledtext import ScrolledText

import ttkbootstrap as tb
from ttkbootstrap.constants import *

class DashboardUI:
    """Écran principal après connexion."""

    def __init__(self, window, api, user, on_logout=None):
        # ================= WINDOW =================
        self.window = window
        self.api = api
        self.user = user
        self.on_logout = on_logout

        # ================= STATE =================
        self.selected_patient_id = None
        self.patient_photo_image = None
        self.current_patient = {}
        self.current_consultations = []
        self.current_notes = []
        self.current_ordonnances = []

        # ================= STYLE =================
        apply_styles()

        # ================= BUILD =================
        self.build_ui()
        self.refresh_patients(show_errors=False)

    # ================= MAIN UI =================
    def build_ui(self):
        clear_window(self.window)

        # ================= MAIN FRAME =================
        main_frame = tb.Frame(self.window)
        main_frame.pack(fill=BOTH, expand=True)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(0, weight=1)

        # ================= CARD =================

        card = tb.Frame(main_frame, padding=20, bootstyle=LIGHT)
        card.grid(row=0, column=0, sticky=NSEW, padx=32, pady=28)
        card.columnconfigure(1, weight=1)
        card.rowconfigure(1, weight=1)