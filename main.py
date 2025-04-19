from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.list import TwoLineListItem
from kivymd.toast.kivytoast.kivytoast import toast as toast_up
from plyer import filechooser
import re
import webbrowser
import os
from kivy.core.window import Window
Window.size = (398, 804)
kv="""
Screen:
    name: "welcome"
    MDFloatLayout:
        md_bg_color: "white"
        Image:
            source: "image_phone.jpg"
            pos_hint: {"center_x": .5,"center_y": .5}
        Button:
            text: "Choose your vcf file"
            background_normal: "vcf_image.ico"
            size_hint: .6, .2
            font_size: "24sp"
            theme_text_color: "Custom"
            text_color: "black"
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
    contact_view:contact_view
    top_name:top_name
    MDFloatLayout:
        md_bg_color: "white"
        Image:
            source: "image_phone.jpg"
            pos_hint: {"center_x": .5,"center_y": .5}
        MDTopAppBar:
            id: top_name
            pos_hint: {"center_x": .5, "top": 1}
            title: "File name: " + app.file_name
            left_action_items: [["folder", lambda x : app.choose_file()]]
            right_action_items: [["dots-vertical", lambda x : app.about_us()]]
        ScrollView:
            pos_hint: {"top": .9}
            MDList:
                id: contact_view
"""
about_us="""
Screen:
	name: "about_us"
	MDFloatLayout:
		md_bg_color: "black"
		Image:
			source: "logo6_16_21816.png"
			size_hint: 1, 1
			pos_hint: {"center_x": .5, "center_x": .5}
		MDTopAppBar:
			title: "Contacter Nous"
			pos_hint: {"top":1}
            right_action_items: [["close", lambda x: app.back_home()]]
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
			font_size: "18sp"
			halign: "center"
			pos_hint: {"center_y": .3, "center_x": .5}
		
		MDTextButton:
			text: "Telegram:"
			theme_text_color: "Custom"
			text_color: "white"
			font_size: "18sp"
			halign: "center"
			pos_hint: {"center_y": .2, "center_x": .15}
			on_release:app.contacter_nous(index=1)
		MDTextButton:
			text: "https://t.me/Thekingdynamo"
			theme_text_color: "Custom"
			text_color: "orange"
			font_size: "18sp"
			halign: "center"
			pos_hint: {"center_y": .2, "center_x": .6}
			on_release: app.contacter_nous(index=2)
			
"""
class contact(MDApp):
    file_name =""
    def about_us(self):
        screenmanager.transition.direction = "left"
        screenmanager.current = "about_us"
    def contacter_nous(self, index):
        if (index== 1) or (index == 2):
            webbrowser.open("https://t.me/Thekingdynamo")
    def choose_file(self):
        screenmanager.get_screen("vcf_screen").contact_view.clear_widgets()
        filechooser.open_file(on_selection= self.file_vcf)
    def file_vcf(self, selected):
        if selected:
            all_selected = (selected[0]).split("\\")
            
            selected_out = all_selected.pop(-1)
            
            os.chdir("//".join(all_selected))
            if os.path.isfile(selected[0]):
                vcf = selected_out
                screenmanager.get_screen("vcf_screen").top_name.title= vcf
                self.load_vcf_file(selected[0])
    def load_vcf_file(self, file_name):
        screenmanager.get_screen("vcf_screen").contact_view.clear_widgets()
        def discontin(nom, numero, id_contact):
            line =TwoLineListItem(text=nom[0], secondary_text=numero[0],id=str(id_contact), on_release=lambda x: print(f""))
            screenmanager.get_screen("vcf_screen").contact_view.add_widget(line)
        def continu(nom, numero):
            nume=[]
            numero1=(numero)
            for numero in numero1:
                nume.append(numero.replace(" ",""))
            numero =(nume)
            list_ = list(zip(nom, numero))
            id_contact=0
            for il in list_:
                id_contact+=1
                line =TwoLineListItem(text=il[0], secondary_text=il[1],id=str(id_contact), on_release=lambda x: print(f"{il[0]},\n{il[1]}"))
                
                screenmanager.get_screen("vcf_screen").contact_view.add_widget(line)
        with open(file_name, "r") as file:
            texte = file.read()
            toast_up(f"{file_name} load succesfully ...")
            num = "TEL;CELL:([0-9+*#]{8,})"; name = "N:;([ a-zA-Z]+);;;"
            numero = re.findall(num, texte)
            nom= re.findall(name, texte)
            if len(numero) == len(nom):
                continu(nom, numero)
            else:
                need= texte.split("END:VCARD")
                id_contact=0
                for i in need:
                    cont=[]
                    numero = re.findall(num, i)
                    nom= re.findall(name, i)
                    id_contact+=1
                    if len(numero)==0 and len(nom)==0:
                        numero = ["none_defini"]
                        nom = ["none_defini"]
                    elif len(numero)==0 and len(nom)!=0:
                        numero = ["none_defini"]
                        discontin(nom, numero, id_contact)
                    elif len(numero)!=0 and len(nom)==0:
                        nom = ["none_defini"]
                        discontin(nom, numero, id_contact)
                    else:
                        discontin(nom, numero, id_contact)
                        

    def back_home(self):
        screenmanager.transition.direction="right"
        screenmanager.current = "vcf_screen"
    def build(self):
        global screenmanager
        screenmanager = ScreenManager()
        screenmanager.add_widget(Builder.load_string(kv))
        screenmanager.add_widget(Builder.load_string(load_file))
        screenmanager.add_widget(Builder.load_string(about_us))
        
        return screenmanager

if __name__ == "__main__":
    contact().run()
