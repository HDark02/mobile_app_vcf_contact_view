from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.list import TwoLineListItem
from kivymd.toast.kivytoast.kivytoast import toast as toast_up
import re
import webbrowser
import os
from asynckivy import start, sleep 
from kivy.core.window import Window
from kivy.core.clipboard import Clipboard
Window.set_icon("icon.png")
kv = """
Screen:
    name: "welcome"
    MDFloatLayout:
        md_bg_color: "white"
        Image:
            source: "image_phone.png"
            pos_hint: {"center_x": .5,"center_y": .5}
        Button:
            text: "Choose your vcf file"
            background_normal: "vcf.png"
            size_hint: .5, .5
            font_size: "30sp"
            theme_text_color: "Custom"
            color: "black"
            bold: True
            pos_hint: {"center_x": .5, "center_y": .5}
            on_release:
                root.manager.current = "vcf_screen"
                app.choose_file()
        MDTextButton:
            text: "Welcome to vcf view"
            size_hint: .8, .1
            font_size: "20sp"
            theme_text_color: "Custom"
            text_color: "black"
            pos_hint: {"center_x": .5, "y": .05}
"""

load_file = """
Screen:
    name: "vcf_screen"
    contact_view: contact_view
    top_name: top_name
    MDFloatLayout:
        md_bg_color: "white"
        Image:
            source: "vcf.png"
            pos_hint: {"center_x": .5,"center_y": .5}
        MDTopAppBar:
            id: top_name
            pos_hint: {"center_x": .5, "top": 1}
            title: "File name: " + app.file_name
            left_action_items: [["folder", lambda x: app.choose_file()]]
            right_action_items: [["dots-vertical", lambda x: app.about_us()]]
        ScrollView:
            pos_hint: {"top": .9}
            MDList:
                id: contact_view
"""

about_us = """
Screen:
    name: "about_us"
    MDFloatLayout:
        md_bg_color: "black"
        Image:
            source: "logo6_16_21816.png"
            size_hint: 1, 1
            pos_hint: {"center_x": .5, "center_y": .55}
        MDTopAppBar:
            title: "Contacter Nous"
            pos_hint: {"top":1}
            right_action_items: [["close", lambda x: app.go_back()]]
            padding: 10
            md_bg_color: "black"
                        
        MDLabel:
            id: thank_user
            text: "C'est à avec plaisir que nous sachons que vous aimez nos produits."
            theme_text_color: "Custom"
            text_color: "white"
            font_size: "18sp"
            halign: "center"
            pos_hint: {"center_y": .85, "center_x": .5}
        MDLabel:
            id: thank_user_feelback
            text: "Merci d'envoyer vos avis à propos de nos produits,pour que ses derniers soient ameliorer."
            theme_text_color: "Custom"
            text_color: "white"
            font_size: "18sp"
            halign: "center"
            pos_hint: {"center_y": .7, "center_x": .5}
        MDLabel:
            id: thank_user_new
            text: "Merci de nous contacter :"
            theme_text_color: "Custom"
            text_color: "white"
            font_size: "20sp"
            halign: "center"
            pos_hint: {"center_y": .4, "center_x": .5}
        Link:
            title: "Github"
            link: "https://github.com/HDark02"
            pos_hint: {"center_y": .35, "center_x": .5}
        Link:
            title: "Telegram"
            link: "https://t.me/Thekingdynamo"
            pos_hint: {"center_y": .3, "center_x": .5}
        Link:
            title: "Facebook"
            link: "facebook.com/alexdynamo.dynamo/"
            pos_hint: {"center_y": .25, "center_x": .5}
        Link:
            title: "Instagram"
            link: "instagram.com/thekingdynamo/"
            pos_hint: {"center_y": .2, "center_x": .5}
        Link:
            title: "Beacoin"
            link: "beacons.page/thekingdynamo"
            pos_hint: {"center_y": .15, "center_x": .5}
        Link:
            title: "Tiktok"
            link: "https://www.tiktok.com/@codecraft"
            pos_hint: {"center_y": .1, "center_x": .5}

        
            
<Link@MDFloatLayout>:
    size_hint:
    title: ""
    link: ""
    MDTextButton:
        text: root.title+" :"
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "18sp"
        halign: "center"
        pos_hint: {"center_y": .5, "center_x": .15}
        on_release: app.contact_us(root.ids.lin.text)

    MDTextButton:
        id: lin
        text: root.link
        theme_text_color: "Custom"
        text_color: "orange"
        font_size: "18sp"
        halign: "center"
        pos_hint: {"center_y": .5, "center_x": .6}
        on_release: app.contact_us(lin.text)
"""

class contact(MDApp):
    file_name = ""

    def about_us(self):
        screenmanager.transition.direction = "left"
        screenmanager.current = "about_us"
    def go_back(self):
        screenmanager.transition.direction = "right"
        screenmanager.current = "vcf_screen"

    def contact_us(self, index):
        webbrowser.open(index)

    def choose_file(self):
        from tkinter import Tk
        from tkinter.filedialog import askopenfilename
        root = Tk()
        root.withdraw()
        file_path = askopenfilename(
            title="Choisir un fichier VCF",
            filetypes=[("Fichier VCF", "*.vcf"), ("Tous les fichiers", "*.*")]
        )
        if file_path:
            file_path = file_path.replace("/", "\\")
            self.file_vcf([file_path])

    def file_vcf(self, selected):
        if selected:
            all_selected = selected[0].split("\\")
            selected_out = all_selected.pop(-1)
            os.chdir("//".join(all_selected))
            if os.path.isfile(selected[0]):
                vcf = selected_out
                screenmanager.get_screen("vcf_screen").top_name.title = vcf
                #Chargement fluide du fichier
                start(self.load_vcf_file(selected[0]))

    async def load_vcf_file(self, file_name):
        """Chargement fluide (non bloquant) du fichier .vcf"""
        screen = screenmanager.get_screen("vcf_screen")
        screen.contact_view.clear_widgets()

        try:
            with open(file_name, "r", encoding="utf-8", errors="ignore") as file:
                texte = file.read()
            toast_up(f"{file_name} chargé avec succès.")
        except Exception as e:
            toast_up(f"Erreur de lecture : {e}")
            return

        num = r"TEL;CELL:([0-9+*#]{8,})"
        name = r"N:;([ a-zA-Z]+);;;"

        cards = texte.split("END:VCARD")
        total = len(cards)
        added = 0

        for card in cards:
            nom = re.findall(name, card)
            numero = re.findall(num, card)
            if not nom and not numero:
                continue

            if not nom:
                nom = ["Nom non défini"]
            if not numero:
                numero = ["Numéro non défini"]

            line = TwoLineListItem(
                text=nom[0],
                secondary_text=numero[0],
                on_release=lambda x, n=nom[0], p=numero[0]: self.copier_contact(n, p)
            )
            screen.contact_view.add_widget(line)
            added += 1

            # ⚡ On laisse l'UI respirer tous les 30 contacts
            if added % 30 == 0:
                await sleep(0)

        toast_up(f"{added} contacts chargés")
    def copier_contact(self, nom, numero):
        """Copie le nom et le numéro dans le presse-papier"""
        texte = f"{nom} - {numero}"
        Clipboard.copy(texte)
        toast_up(f"📋 {texte} copié !")
    def back_home(self):
        screenmanager.transition.direction = "right"
        screenmanager.current = "vcf_screen"

    def build(self):
        global screenmanager
        self.icon= "vcf.png"
        self.title = "Vcf Contacts"
        screenmanager = ScreenManager()
        screenmanager.add_widget(Builder.load_string(kv))
        screenmanager.add_widget(Builder.load_string(load_file))
        screenmanager.add_widget(Builder.load_string(about_us))
        return screenmanager


if __name__ == "__main__":
    contact().run()
