import webbrowser

def whatsapp_chat(number):
    url = f"https://wa.me/{number}"
    print("Opening WhatsApp chat...")
    webbrowser.open(url)

if __name__ == "__main__":
    whatsapp_chat("918329315420")