#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Navigation Moderne - NiTriTe V17 Beta
Barre de navigation latérale
"""

import customtkinter as ctk
import tkinter as tk
from pathlib import Path
from PIL import Image, ImageTk
from v14_mvp.design_system import DesignTokens, ModernColors


class ModernNavigation(ctk.CTkFrame):
    """Barre de navigation latérale moderne"""
    
    def __init__(self, parent, on_page_change):
        super().__init__(
            parent,
            fg_color=DesignTokens.BG_SECONDARY,
            width=280,
            corner_radius=0
        )
        
        self.on_page_change = on_page_change
        self.current_page = "applications"
        self.nav_buttons = {}
        
        self._create_header()
        self._create_nav_buttons()
        self._create_footer()
    
    def _create_header(self):
        """Header avec logo"""
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill=tk.X, padx=DesignTokens.SPACING_MD, pady=0)

        # Logo - compact
        logo_frame = ctk.CTkFrame(
            header,
            fg_color=DesignTokens.BG_SECONDARY,
            width=150,
            height=150,
            corner_radius=DesignTokens.RADIUS_MD
        )
        logo_frame.pack(pady=0)  # Aucune marge
        logo_frame.pack_propagate(False)

        # Charger l'icône Nitrite
        try:
            import sys
            if getattr(sys, 'frozen', False):
                # Mode PyInstaller
                icon_path = Path(sys.executable).parent / 'assets' / 'Nitrite_icon1.ico'
            else:
                # Mode développement
                icon_path = Path(__file__).parent.parent.parent / 'assets' / 'Nitrite_icon1.ico'

            if icon_path.exists():
                icon_image = Image.open(icon_path)
                # Icône compact pour gagner de l'espace
                icon_image = icon_image.resize((150, 150), Image.Resampling.LANCZOS)
                icon_photo = ctk.CTkImage(light_image=icon_image, dark_image=icon_image, size=(150, 150))

                logo_label = ctk.CTkLabel(
                    logo_frame,
                    image=icon_photo,
                    text=""
                )
                logo_label.image = icon_photo  # Garder référence
            else:
                # Fallback au "N" si icône pas trouvée
                logo_label = ctk.CTkLabel(
                    logo_frame,
                    text="N",
                    font=(DesignTokens.FONT_FAMILY, 48, "bold"),
                    text_color="white"
                )
        except Exception as e:
            # Fallback en cas d'erreur
            print(f"Erreur chargement icône: {e}")
            logo_label = ctk.CTkLabel(
                logo_frame,
                text="N",
                font=(DesignTokens.FONT_FAMILY, 48, "bold"),
                text_color="white"
            )

        logo_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Info - en dessous du logo, centré - remonté au maximum
        info_frame = ctk.CTkFrame(header, fg_color="transparent")
        info_frame.pack(fill=tk.X, pady=(0, 0))

        title = ctk.CTkLabel(
            info_frame,
            text="NiTriTe",
            font=(DesignTokens.FONT_FAMILY, 16, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor='center'
        )
        title.pack(pady=0)

        version = ctk.CTkLabel(
            info_frame,
            text="Version 20.0",
            font=(DesignTokens.FONT_FAMILY, 11),
            text_color=DesignTokens.TEXT_SECONDARY,
            anchor='center'
        )
        version.pack(pady=0)
        
        # Séparateur
        sep = ctk.CTkFrame(self, fg_color=DesignTokens.BORDER_DEFAULT, height=1)
        sep.pack(fill=tk.X, padx=DesignTokens.SPACING_MD, pady=(DesignTokens.SPACING_XS, DesignTokens.SPACING_MD))
    
    def _create_nav_buttons(self):
        """Créer boutons navigation"""
        pages = [
            ("applications", "📱", "Applications"),
            ("tools", "🔧", "Outils"),
            ("master_install", "📦", "Master Install"),
            ("portables", "💾", "Apps Portables"),
            ("os_downloads", "💿", "OS & USB Tools"),
            ("terminal", "⌨️", "Terminal"),
            ("updates", "🔄", "Mises à jour"),
            ("backup", "💾", "Sauvegarde"),
            ("optimizations", "⚡", "Optimisations"),
            ("diagnostic", "🔍", "Diagnostic"),
            ("logs", "📋", "Logs"),
            ("scripts", "📜", "Scripts Windows"),
            ("ai_agents", "🤖", "Agents IA"),
            ("settings", "⚙️", "Paramètres"),
        ]
        
        for page_id, icon, title in pages:
            btn = self._create_nav_button(page_id, icon, title)
            self.nav_buttons[page_id] = btn
        
        # Sélectionner première page
        self._select_page("applications")
    
    def _create_nav_button(self, page_id, icon, title):
        """Créer un bouton de navigation"""
        btn_frame = ctk.CTkFrame(
            self,
            fg_color="transparent",
            corner_radius=DesignTokens.RADIUS_MD,
            cursor="hand2"
        )
        btn_frame.pack(fill=tk.X, padx=DesignTokens.SPACING_MD, pady=DesignTokens.SPACING_XS)
        
        # Content
        content = ctk.CTkFrame(btn_frame, fg_color="transparent")
        content.pack(fill=tk.BOTH, expand=True, padx=DesignTokens.SPACING_SM, pady=DesignTokens.SPACING_SM)
        
        # Icône
        icon_label = ctk.CTkLabel(
            content,
            text=icon,
            font=(DesignTokens.FONT_FAMILY, 18),
            text_color=DesignTokens.TEXT_SECONDARY
        )
        icon_label.pack(side=tk.LEFT, padx=DesignTokens.SPACING_SM)
        
        # Titre
        title_label = ctk.CTkLabel(
            content,
            text=title,
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
            text_color=DesignTokens.TEXT_SECONDARY,
            anchor='w'
        )
        title_label.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Store references
        btn_frame.icon_label = icon_label
        btn_frame.title_label = title_label
        
        # Bind events
        for widget in [btn_frame, content, icon_label, title_label]:
            widget.bind('<Button-1>', lambda e, pid=page_id: self._on_click(pid))
            widget.bind('<Enter>', lambda e, b=btn_frame: self._on_hover(b, True))
            widget.bind('<Leave>', lambda e, b=btn_frame: self._on_hover(b, False))
        
        return btn_frame
    
    def _on_click(self, page_id):
        """Gérer clic navigation"""
        self._select_page(page_id)
        self.on_page_change(page_id)
    
    def _on_hover(self, btn, is_enter):
        """Gérer hover"""
        is_active = btn.cget('fg_color') == DesignTokens.ACCENT_PRIMARY
        
        if not is_active:
            if is_enter:
                btn.configure(fg_color=DesignTokens.BG_HOVER)
            else:
                btn.configure(fg_color="transparent")
    
    def _select_page(self, page_id):
        """Sélectionner une page"""
        # Désélectionner tout
        for pid, btn in self.nav_buttons.items():
            if pid != page_id:
                btn.configure(fg_color="transparent")
                btn.icon_label.configure(text_color=DesignTokens.TEXT_SECONDARY)
                btn.title_label.configure(text_color=DesignTokens.TEXT_SECONDARY)
        
        # Sélectionner nouveau
        if page_id in self.nav_buttons:
            btn = self.nav_buttons[page_id]
            btn.configure(fg_color=DesignTokens.ACCENT_PRIMARY)
            btn.icon_label.configure(text_color="white")
            btn.title_label.configure(text_color="white")
            self.current_page = page_id
    
    def _create_footer(self):
        """Footer"""
        spacer = ctk.CTkFrame(self, fg_color="transparent")
        spacer.pack(fill=tk.BOTH, expand=True)

        # Séparateur au-dessus du footer
        sep = ctk.CTkFrame(self, fg_color=DesignTokens.BORDER_DEFAULT, height=1)
        sep.pack(fill=tk.X, padx=DesignTokens.SPACING_MD, pady=DesignTokens.SPACING_XS)

        footer = ctk.CTkFrame(
            self,
            fg_color=DesignTokens.BG_ELEVATED,
            corner_radius=0
        )
        footer.pack(fill=tk.X, side=tk.BOTTOM)

        # Lien site web
        website_btn = ctk.CTkButton(
            footer,
            text="🌐 Site Web NiTriTe",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            fg_color="transparent",
            hover_color=DesignTokens.BG_HOVER,
            text_color=DesignTokens.ACCENT_PRIMARY,
            cursor="hand2",
            command=self._open_website,
            height=32
        )
        website_btn.pack(pady=(DesignTokens.SPACING_SM, DesignTokens.SPACING_XS), padx=DesignTokens.SPACING_MD)

        # Copyright
        footer_text = ctk.CTkLabel(
            footer,
            text="© 2024 OrdiPlus",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_XS),
            text_color=DesignTokens.TEXT_TERTIARY
        )
        footer_text.pack(pady=(0, DesignTokens.SPACING_SM))

    def _open_website(self):
        """Ouvrir le site web dans le navigateur"""
        import webbrowser
        webbrowser.open("https://heiphaistos44-crypto.github.io/Site-Web-NiTriTe/")