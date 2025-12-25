#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gestionnaire de Drag & Drop - NiTriTe V17
Permet de réorganiser les éléments par glisser-déposer
"""

import tkinter as tk
from typing import Callable, Optional


class DragDropHandler:
    """Gestionnaire de drag & drop pour les widgets CustomTkinter"""

    def __init__(self, parent_container, on_reorder: Optional[Callable] = None):
        """
        Initialiser le gestionnaire de drag & drop

        Args:
            parent_container: Le conteneur parent des widgets
            on_reorder: Callback appelé lors de la réorganisation (optionnel)
        """
        self.parent_container = parent_container
        self.on_reorder = on_reorder

        self.dragged_widget = None
        self.drag_data = {
            "widget": None,
            "start_x": 0,
            "start_y": 0,
            "original_bg": None
        }

    def make_draggable(self, widget, drag_handle=None):
        """
        Rendre un widget draggable

        Args:
            widget: Le widget à rendre draggable
            drag_handle: Widget spécifique à utiliser comme poignée (optionnel)
        """
        handle = drag_handle if drag_handle else widget

        # Bind les événements de drag
        handle.bind("<Button-1>", lambda e: self._on_drag_start(e, widget))
        handle.bind("<B1-Motion>", lambda e: self._on_drag_motion(e, widget))
        handle.bind("<ButtonRelease-1>", lambda e: self._on_drag_release(e, widget))

        # Changer le curseur pour indiquer que c'est draggable
        handle.configure(cursor="hand2")

    def _on_drag_start(self, event, widget):
        """Début du drag"""
        self.drag_data["widget"] = widget
        self.drag_data["start_x"] = event.x_root
        self.drag_data["start_y"] = event.y_root

        # Sauvegarder la couleur de fond originale
        try:
            self.drag_data["original_bg"] = widget.cget("fg_color")
        except:
            self.drag_data["original_bg"] = None

        # Effet visuel pendant le drag
        try:
            widget.configure(fg_color=("gray70", "gray30"))
        except:
            pass

    def _on_drag_motion(self, event, widget):
        """Pendant le drag"""
        # Optionnel: Faire bouger le widget visuellement (peut causer des problèmes avec pack/grid)
        # Pour l'instant, juste un effet visuel
        pass

    def _on_drag_release(self, event, widget):
        """Fin du drag"""
        # Restaurer l'apparence
        try:
            if self.drag_data["original_bg"]:
                widget.configure(fg_color=self.drag_data["original_bg"])
        except:
            pass

        # Calculer la position de drop
        drop_x = event.x_root
        drop_y = event.y_root

        # Trouver le widget cible sous la souris
        target_widget = self._find_widget_at_position(drop_x, drop_y)

        if target_widget and target_widget != widget:
            # Réorganiser les widgets
            self._reorder_widgets(widget, target_widget)

        # Réinitialiser les données de drag
        self.drag_data = {
            "widget": None,
            "start_x": 0,
            "start_y": 0,
            "original_bg": None
        }

    def _find_widget_at_position(self, x, y):
        """Trouver le widget à une position donnée"""
        # Obtenir tous les widgets enfants du conteneur
        for child in self.parent_container.winfo_children():
            # Vérifier si les coordonnées sont dans ce widget
            widget_x = child.winfo_rootx()
            widget_y = child.winfo_rooty()
            widget_w = child.winfo_width()
            widget_h = child.winfo_height()

            if (widget_x <= x <= widget_x + widget_w and
                widget_y <= y <= widget_y + widget_h):
                return child

        return None

    def _reorder_widgets(self, dragged, target):
        """Réorganiser les widgets en fonction du drag & drop"""
        # Obtenir les positions actuelles dans le pack order
        children = list(self.parent_container.winfo_children())

        try:
            dragged_index = children.index(dragged)
            target_index = children.index(target)
        except ValueError:
            return

        # Retirer le widget dragué
        dragged.pack_forget()

        # Le réinsérer à la nouvelle position
        if dragged_index < target_index:
            # Déplacement vers le bas
            dragged.pack(before=target, **self._get_pack_info(dragged))
        else:
            # Déplacement vers le haut
            dragged.pack(after=target, **self._get_pack_info(dragged))

        # Appeler le callback si défini
        if self.on_reorder:
            new_order = [child for child in self.parent_container.winfo_children()]
            self.on_reorder(new_order)

    def _get_pack_info(self, widget):
        """Obtenir les informations de pack d'un widget"""
        try:
            info = widget.pack_info()
            return {
                "fill": info.get("fill", tk.NONE),
                "expand": info.get("expand", False),
                "side": info.get("side", tk.TOP),
                "padx": info.get("padx", 0),
                "pady": info.get("pady", 0),
                "anchor": info.get("anchor", tk.CENTER)
            }
        except:
            # Valeurs par défaut si le widget n'est pas packé
            return {
                "fill": tk.X,
                "expand": False,
                "side": tk.TOP,
                "padx": 0,
                "pady": 5
            }


class DraggableCard:
    """
    Carte draggable réutilisable
    Fournit un indicateur visuel de drag et une poignée de déplacement
    """

    def __init__(self, parent, drag_handler: DragDropHandler):
        """
        Créer une carte draggable

        Args:
            parent: Widget parent
            drag_handler: Instance de DragDropHandler
        """
        self.parent = parent
        self.drag_handler = drag_handler

    def add_drag_handle(self, card_widget):
        """
        Ajouter une poignée de drag visible à une carte

        Args:
            card_widget: Le widget carte CustomTkinter
        """
        import customtkinter as ctk
        from v14_mvp.design_system import DesignTokens

        # Créer une zone de drag handle
        drag_handle = ctk.CTkFrame(
            card_widget,
            fg_color="transparent",
            width=30,
            height=30,
            cursor="hand2"
        )

        # Icône de drag (trois lignes)
        drag_icon = ctk.CTkLabel(
            drag_handle,
            text="⋮⋮",
            font=(DesignTokens.FONT_FAMILY, 16),
            text_color=DesignTokens.TEXT_TERTIARY
        )
        drag_icon.pack(expand=True)

        # Tooltip
        self._create_tooltip(drag_handle, "Glisser pour réorganiser")

        # Rendre draggable
        self.drag_handler.make_draggable(card_widget, drag_handle=drag_handle)

        return drag_handle

    def _create_tooltip(self, widget, text):
        """Créer un tooltip simple"""
        tooltip = None

        def show_tooltip(event):
            nonlocal tooltip
            import customtkinter as ctk
            from v14_mvp.design_system import DesignTokens

            tooltip = tk.Toplevel()
            tooltip.wm_overrideredirect(True)
            tooltip.wm_geometry(f"+{event.x_root+10}+{event.y_root+10}")

            label = ctk.CTkLabel(
                tooltip,
                text=text,
                fg_color=DesignTokens.BG_ELEVATED,
                corner_radius=4,
                padx=8,
                pady=4
            )
            label.pack()

        def hide_tooltip(event):
            nonlocal tooltip
            if tooltip:
                tooltip.destroy()
                tooltip = None

        widget.bind("<Enter>", show_tooltip)
        widget.bind("<Leave>", hide_tooltip)
