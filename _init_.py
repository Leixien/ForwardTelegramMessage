import time
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import threading

# Configurazione API Telegram
API_ID = 'API_ID'  # Inserisci il tuo API ID
API_HASH = 'API_HASH'  # Inserisci il tuo API Hash
SESSION_NAME = 'forward_bot'  # Nome della sessione

# Variabili globali per sorgente e destinazione
SOURCE_CHANNEL = None  # Sarà impostato dall'utente
DESTINATION_CHAT = None  # Sarà impostato dall'utente

# Avvia l'app cliente
app = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH)

# Variabile per monitorare lo stato dello script
is_running = True

@app.on_message(filters.chat(SOURCE_CHANNEL))  # Filtra i messaggi dal canale sorgente
def forward_message(client, message):
    try:
        # Inoltra il messaggio alla chat di destinazione
        message.forward(DESTINATION_CHAT)
        print(f"Messaggio inoltrato: {message.text}")
    except FloodWait as e:
        print(f"Attesa necessaria: {e.x} secondi")
        time.sleep(e.x)  # Gestisce l'errore FloodWait aspettando il tempo richiesto
    except Exception as e:
        print(f"Errore durante l'inoltro: {e}")

# Funzione per monitorare lo stato del bot
def monitor_bot():
    global is_running
    while True:
        try:
            # Controlla ogni 30 secondi se lo script è ancora in esecuzione
            time.sleep(30)
        except Exception as e:
            print(f"Errore nel monitoraggio: {e}")
            is_running = False
            break

# Funzione per notificare la chat se lo script si arresta
def notify_on_failure():
    global is_running
    while True:
        if not is_running:
            try:
                app.send_message(DESTINATION_CHAT, "OFFLINE")
                print("Notifica di offline inviata.")
            except Exception as e:
                print(f"Errore nell'invio della notifica: {e}")
            break
        time.sleep(10)

if __name__ == '__main__':
    print("STARTING SCRIPT")

    # Recupera le chat disponibili
    with app:
        print("Recupero delle chat disponibili...")
        dialogs = app.get_dialogs()
        chat_options = []
        for i, dialog in enumerate(dialogs):
            print(f"{i + 1}. Nome: {dialog.chat.title} | ID: {dialog.chat.id}")
            chat_options.append(dialog.chat)

    # Permetti all'utente di scegliere la chat sorgente
    source_index = int(input("Seleziona il numero della chat sorgente dalla lista: ")) - 1
    SOURCE_CHANNEL = chat_options[source_index].id

    # Permetti all'utente di scegliere la chat di destinazione
    dest_index = int(input("Seleziona il numero della chat di destinazione dalla lista: ")) - 1
    DESTINATION_CHAT = chat_options[dest_index].id

    print(f"Sorgente: {chat_options[source_index].title} (ID: {SOURCE_CHANNEL})")
    print(f"Destinazione: {chat_options[dest_index].title} (ID: {DESTINATION_CHAT})")

    # Avvia il monitoraggio in un thread separato
    monitor_thread = threading.Thread(target=monitor_bot, daemon=True)
    monitor_thread.start()

    # Avvia il bot in un blocco try per catturare errori generali
    try:
        app.run()
    except KeyboardInterrupt:
        print("Bot arrestato manualmente.")
    except Exception as e:
        print(f"Errore critico: {e}")
        is_running = False

    # Avvia il thread per notificare lo stato offline
    notify_thread = threading.Thread(target=notify_on_failure, daemon=True)
    notify_thread.start()
