
README (IT & EN)
markdown
Copia
Modifica
# Telegram Forward Bot

## Italiano

Un bot Telegram scritto in Python per inoltrare automaticamente i messaggi da una chat sorgente a una chat di destinazione.

### Caratteristiche
- **Selezione dinamica delle chat**: Scegli la chat sorgente e quella di destinazione tra le chat disponibili all'avvio dello script.
- **Gestione degli errori**: Supporta `FloodWait` e notifiche in caso di arresto del bot.
- **Monitoraggio dello stato**: Avvisa la chat di destinazione con un messaggio "OFFLINE" in caso di crash.

### Requisiti
- Python 3.7 o superiore
- Libreria Pyrogram

### Installazione
1. Clona il repository:
   ```bash
   git clone https://github.com/tuo-username/telegram-forward-bot.git
   cd telegram-forward-bot
Installa le dipendenze:
bash
Copia
Modifica
pip install pyrogram
Crea un'app Telegram su my.telegram.org per ottenere API_ID e API_HASH.
Modifica le variabili API_ID, API_HASH, e SESSION_NAME nel file dello script.
Utilizzo
Esegui lo script:
bash
Copia
Modifica
python telegram_forward_bot.py
All'avvio, lo script mostrerà un elenco delle chat disponibili. Seleziona la chat sorgente e quella di destinazione inserendo il numero corrispondente.
Lo script inoltrerà automaticamente i messaggi dalla sorgente alla destinazione.
Funzionamento
Monitoraggio: Lo script verifica costantemente il suo stato. In caso di errore, invia una notifica di stato "OFFLINE" alla chat di destinazione.
Errori FloodWait: Lo script attende automaticamente il tempo richiesto in caso di limitazioni di frequenza da parte di Telegram.
Contribuire
Le richieste di nuove funzionalità e i miglioramenti sono benvenuti! Puoi inviare una pull request o aprire un issue.

Licenza
Questo progetto è distribuito sotto la licenza MIT. Consulta il file LICENSE per maggiori dettagli.

English
A Telegram bot written in Python to automatically forward messages from a source chat to a destination chat.

Features
Dynamic chat selection: Choose the source and destination chats from available chats at script startup.
Error handling: Supports FloodWait and notifications in case of bot shutdown.
State monitoring: Notifies the destination chat with an "OFFLINE" message in case of a crash.
Requirements
Python 3.7 or higher
Pyrogram library
Installation
Clone the repository:
bash
Copia
Modifica
git clone https://github.com/your-username/telegram-forward-bot.git
cd telegram-forward-bot
Install dependencies:
bash
Copia
Modifica
pip install pyrogram
Create a Telegram app on my.telegram.org to get your API_ID and API_HASH.
Update the API_ID, API_HASH, and SESSION_NAME variables in the script file.
Usage
Run the script:
bash
Copia
Modifica
python telegram_forward_bot.py
At startup, the script will display a list of available chats. Select the source and destination chats by entering their corresponding numbers.
The script will automatically forward messages from the source to the destination.
How it Works
Monitoring: The script constantly checks its state. If an error occurs, it sends an "OFFLINE" notification to the destination chat.
FloodWait errors: The script automatically waits for the required time when Telegram enforces rate limits.
Contribute
Feature requests and improvements are welcome! Feel free to submit a pull request or open an issue.
