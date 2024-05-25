from tkinter import Tk, Label, Entry, Button, Frame, PhotoImage
from googletrans import Translator
import os

def install_googletrans():
    """Install googletrans if not already installed."""
    try:
        import googletrans
    except ImportError:
        import subprocess
        subprocess.run(["pip", "install", "googletrans==4.0.0-rc1"], check=True)

# Create a Translator object
translator = Translator()

def translate_to_german(event=None):
    """Translate text to German."""
    text = entry.get()
    if text.lower() == 'exit':
        root.quit()
    else:
        translation = translator.translate(text, dest='de')
        show_translation(translation.text)

def show_translation(text):
    """Display translation in a new widget."""
    translation_label.config(text=text)

def select_language(lang_code):
    """Set the translation source language."""
    translator.src = lang_code

def translate_to_language(lang_code):
    """Translate text to the selected language."""
    text = entry.get()
    if text.lower() == 'exit':
        root.quit()
    else:
        translation = translator.translate(text, dest=lang_code)
        show_translation(translation.text)

def load_flag_image(lang_code, size=15):
    """Load flag image."""
    try:
        image = PhotoImage(file=f"C:/Users/hewso/OneDrive/Documents/Progetti/{lang_code}_flag.png")
        image = image.subsample(image.width() // size, image.height() // size)  # Resize the image
        return image
    except Exception as e:
        print(f"Error loading flag image for language {lang_code}: {e}")
        return None

def create_translator_app():
    """Create the translator application."""
    # Install googletrans if not already installed
    install_googletrans()

    # Create the main window
    global root
    root = Tk()
    root.title("In Deutsch sagen")

    # Set the program icon
    icon_path = r"C:\Users\hewso\OneDrive\Documents\Progetti\germany-icon.ico"
    if os.path.exists(icon_path):
        root.iconbitmap(icon_path)

    # Create a label, entry, and button widgets
    label = Label(root, text="Enter text to translate to German (type 'exit' to quit):")
    label.pack()

    global entry
    entry = Entry(root, width=50, font=('Arial', 14))
    entry.pack(side="top", fill="both", expand=True)
    entry.bind("<Return>", translate_to_german)

    button = Button(root, text="Translate", command=translate_to_german, font=('Arial', 14))
    button.pack(side="top", fill="both", expand=True)

    global translation_label
    translation_label = Label(root, text="", width=50, height=10, wraplength=400, font=('Arial', 14))
    translation_label.pack(side="top", fill="both", expand=True)

    # Flags for selecting input language
    lang_buttons_frame = Frame(root)
    lang_buttons_frame.pack(side="top", pady=10)

    lang_codes = ["en", "fr", "es", "it"]  # Language codes for English, French, Spanish, and Italian
    for lang_code in lang_codes:
        flag_icon = load_flag_image(lang_code)
        if flag_icon:
            lang_button = Button(lang_buttons_frame, image=flag_icon, command=lambda code=lang_code: translate_to_language(code))
            lang_button.image = flag_icon
            lang_button.pack(side="left", padx=5)

    # Run the application
    root.mainloop()

# Run the translator application
create_translator_app()
