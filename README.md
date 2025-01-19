# Telegram Forward Bot

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
```

### Installa le dipendenze:
```bash
pip install pyrogram
```

Crea un'app Telegram su my.telegram.org per ottenere API_ID e API_HASH.
Modifica le variabili API_ID, API_HASH, e SESSION_NAME nel file dello script.

### Utilizzo
Esegui lo script:
```bash
python telegram_forward_bot.py
```

All'avvio, lo script mostrerà un elenco delle chat disponibili. Seleziona la chat sorgente e quella di destinazione inserendo il numero corrispondente.
Lo script inoltrerà automaticamente i messaggi dalla sorgente alla destinazione.

### Funzionamento
Monitoraggio: Lo script verifica costantemente il suo stato. In caso di errore, invia una notifica di stato "OFFLINE" alla chat di destinazione.
Errori FloodWait: Lo script attende automaticamente il tempo richiesto in caso di limitazioni di frequenza da parte di Telegram.

### Contribuire
Le richieste di nuove funzionalità e i miglioramenti sono benvenuti! Puoi inviare una pull request o aprire un issue.

 ###Licenza
Questo progetto è distribuito sotto la licenza MIT. Consulta il file LICENSE per maggiori dettagli.
