import tkinter as tk
import pandas as pd
from gtts import gTTS
import pygame
import tempfile

class PeriodicTableApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Periodic Table")

        self.element_data = pd.read_csv("periodic_table_data.csv")
        pygame.mixer.init()

        self.current_popup = None 
        self.create_periodic_table()

        for i in range(1, 8):
            self.root.rowconfigure(i, weight=1)
        for i in range(1, 19):
            self.root.columnconfigure(i, weight=1)

    def create_periodic_table(self):
        button_colors = ["mistyrose", "lemonchiffon", "lightgreen", "grey", "coral", "lightpink", "lightblue", "lightsalmon", "lightcoral", "lightgrey"]

        small_button_data = [(1, 4), (1, 6), (1, 8), (1, 10), (2, 4), (2, 6), (2, 8), (3, 4), (3, 6), (3, 8)]  # Button placement data

        button_texts = ["Non-Metals", "Transition-Metal", "Halogens", "Actinides", "Alkali-Metals", "Post-Transition", "Noble-Gas", "Alkaline-Earth", "Metalloids", "Lanthanides"]

        for _, element in self.element_data.iterrows():
            btn = tk.Button(
                self.root,
                text=f"{element['symbol']}\n{element['name']}",
                width=12,
                height=5,
                command=lambda e=element: self.element_clicked(e),
                bg=element['color'],  
            )
            btn.grid(row=element["row"], column=element["col"])

        for i, (row, col) in enumerate(small_button_data):
            if row == 3:
                row = 3  
            small_btn = tk.Button(
                self.root,
                text="",
                width=2,   
                height=1,   
                state=tk.DISABLED,  
                bg=button_colors[i] if i < len(button_colors) else 'white'  
            )
            small_btn.grid(row=row, column=col) 

            if i < len(button_texts):
                text_label = tk.Label(self.root, text=button_texts[i])  
                text_label.grid(row=row, column=col + 1, sticky="w")  

    def element_clicked(self, element):
        element_info = f"Element : {element['name']}\nSymbol : {element['symbol']}\nAtomic Number : {element['atomic_number']}\nChemical Group : {element['chemical_group']}\nMelting Point : {element['melting_point']}\nBoiling Point : {element['boiling_point']}\nPhase at STP : {element['phase_at_stp']}\nElectronegativity : {element['electronegativity']}\nCommon Oxidation States : {element['common_oxidation_states']}\nNumber of Valance Electrons : {element['number_of_valence_electrons']}"
    
        if self.current_popup:
            self.stop_speech_and_close()
        
        self.speak(element_info)
        self.current_popup = self.display_popup(element_info) 

    def speak(self, text):
        tts = gTTS(text=text, lang='en')

        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        temp_file.close()
        tts.save(temp_file.name)

        pygame.mixer.music.load(temp_file.name)
        pygame.mixer.music.play()
        

    def display_popup(self, element_info):
        popup = tk.Toplevel(self.root)
        popup.title("Element Information")

        text = tk.Text(popup, wrap="word", height=12, width=50, font=("Helvetica", 10), padx=10, pady=5)
        text.pack(fill="both", expand=True)
       
        text.insert("1.0", element_info)
        text.configure(state="disabled")

        close_btn = tk.Button(popup, text="Close", command=self.stop_speech_and_close)
        close_btn.pack(pady=5)

        popup.bind("<Destroy>", lambda event: self.stop_speech())
        return popup
    

    def stop_speech_and_close(self):
        pygame.mixer.music.stop()
        
        if self.current_popup:
            self.current_popup.destroy()

    def stop_speech(self, event=None):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    root = tk.Tk()
    app = PeriodicTableApp(root)
    root.mainloop()