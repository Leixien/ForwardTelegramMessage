# Configurazione API Telegram
API_ID = 'API_ID'  # Inserisci il tuo API ID
API_HASH = 'API_HASH'  # Inserisci il tuo API Hash
SESSION_NAME = 'forward_bot'  # Nome della sessione

import time
import asyncio
from telethon.sync import TelegramClient
from telethon import errors

class TelegramForwarder:
    def __init__(self, api_id, api_hash, phone_number):
        # Inizializza il client Telegram
        self.api_id = api_id
        self.api_hash = api_hash
        self.phone_number = phone_number
        self.client = TelegramClient('session_' + phone_number, api_id, api_hash)

    async def list_chats(self):
        """
        Recupera e salva la lista delle chat/dialoghi disponibili.
        """
        await self.client.connect()

        # Controlla se l'utente è autorizzato
        if not await self.client.is_user_authorized():
            await self.client.send_code_request(self.phone_number)
            try:
                await self.client.sign_in(self.phone_number, input('Enter the code: '))
            except errors.rpcerrorlist.SessionPasswordNeededError:
                password = input('Two-step verification is enabled. Enter your password: ')
                await self.client.sign_in(password=password)

        # Ottieni la lista dei dialoghi
        dialogs = await self.client.get_dialogs()
        chats_file = open(f"chats_of_{self.phone_number}.txt", "w", encoding="utf-8")
        for dialog in dialogs:
            print(f"Chat ID: {dialog.id}, Title: {dialog.title}")
            chats_file.write(f"Chat ID: {dialog.id}, Title: {dialog.title} \n")
          
        chats_file.close()
        print("Lista delle chat salvata con successo!")

    async def forward_messages_to_channel(self, source_chat_id, destination_channel_id, keywords):
        """
        Forward dei messaggi da una chat sorgente a una destinazione, filtrando eventualmente con keywords.
        """
        await self.client.connect()

        # Controlla se l'utente è autorizzato
        if not await self.client.is_user_authorized():
            await self.client.send_code_request(self.phone_number)
            await self.client.sign_in(self.phone_number, input('Enter the code: '))

        # Recupera l'ultimo messaggio per iniziare a tracciare
        last_message_id = (await self.client.get_messages(source_chat_id, limit=1))[0].id

        while True:
            print("Controllo nuovi messaggi e inoltro...")
            # Recupera nuovi messaggi
            messages = await self.client.get_messages(source_chat_id, min_id=last_message_id, limit=None)

            for message in reversed(messages):
                # Controlla se ci sono keywords da applicare
                if keywords:
                    if message.text and any(keyword in message.text.lower() for keyword in keywords):
                        print(f"Messaggio contiene keyword: {message.text}")
                        await self.client.send_message(destination_channel_id, message.text)
                        print("Messaggio inoltrato.")
                else:
                    # Inoltra direttamente se non ci sono keyword
                    await self.client.send_message(destination_channel_id, message.text)
                    print("Messaggio inoltrato.")

                # Aggiorna l'ultimo ID del messaggio
                last_message_id = max(last_message_id, message.id)

            # Aspetta prima di controllare nuovi messaggi
            await asyncio.sleep(5)


# Funzione per leggere le credenziali da file
def read_credentials():
    try:
        with open("credentials.txt", "r") as file:
            lines = file.readlines()
            api_id = lines[0].strip()
            api_hash = lines[1].strip()
            phone_number = lines[2].strip()
            return api_id, api_hash, phone_number
    except FileNotFoundError:
        print("File credenziali non trovato.")
        return None, None, None

# Funzione per scrivere le credenziali in un file
def write_credentials(api_id, api_hash, phone_number):
    with open("credentials.txt", "w") as file:
        file.write(api_id + "\n")
        file.write(api_hash + "\n")
        file.write(phone_number + "\n")

async def main():
    # Leggi credenziali da file o chiedi all'utente di inserirle
    api_id, api_hash, phone_number = read_credentials()
    if api_id is None or api_hash is None or phone_number is None:
        api_id = input("Enter your API ID: ")
        api_hash = input("Enter your API Hash: ")
        phone_number = input("Enter your phone number: ")
        write_credentials(api_id, api_hash, phone_number)

    forwarder = TelegramForwarder(api_id, api_hash, phone_number)
    
    print("Scegli un'opzione:")
    print("1. Lista delle chat")
    print("2. Inoltro messaggi")
    
    choice = input("Inserisci la tua scelta: ")
    
    if choice == "1":
        # Elenco delle chat
        await forwarder.list_chats()
    elif choice == "2":
        # Inoltro messaggi
        source_chat_id = int(input("Inserisci l'ID della chat sorgente: "))
        destination_channel_id = int(input("Inserisci l'ID della chat di destinazione: "))
        print("Inserisci keywords (separate da virgola) o lascia vuoto per inoltrare tutti i messaggi:")
        keywords = input("Keywords: ").split(",")
        await forwarder.forward_messages_to_channel(source_chat_id, destination_channel_id, keywords)
    else:
        print("Scelta non valida.")

# Avvia l'event loop e la funzione principale
if __name__ == "__main__":
    asyncio.run(main())
