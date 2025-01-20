# Telegram Message Forwarder Script

Script Telegram scritto in Python per inoltrare automaticamente messaggi da una chat a un'altra, con funzionalità avanzate di filtro basate su parole chiave.

## Caratteristiche
- **Inoltro dinamico dei messaggi**: Inoltra i messaggi da una chat sorgente a una destinazione, con opzione per filtrare messaggi contenenti parole chiave specifiche.
- **Elenco delle chat**: Recupera e salva la lista di tutte le chat/dialoghi disponibili, facilitando la selezione di sorgente e destinazione.
- **Supporto per credenziali**: Consente di salvare e riutilizzare le credenziali per evitare ripetuti login.
- **Interfaccia interattiva**: Menu per scegliere tra elencare le chat o avviare l'inoltro.

## Requisiti
- Python 3.7 o superiore
- Libreria **Telethon**

## Installazione

Clona il repository:
   ```bash
   git clone https://github.com/tuo-username/telegram-forward-script.git
   cd telegram-forward-script
   ```
Installa le dipendenze:
  ```bash
  pip install telethon
  ```

Crea un'app Telegram su my.telegram.org per ottenere:
  1. API ID
  2. API Hash 

## Utilizzo
Avvio dello script:
```bash
python _init_.py
```

Elenco delle chat:
  Seleziona l'opzione 1 per recuperare e salvare la lista delle chat in un file chiamato chats_of_<phone_number>.txt.
  Usa questo file per trovare gli ID delle chat desiderate.

Inoltro messaggi:
  Seleziona l'opzione 2 per avviare l'inoltro dei messaggi.
  Inserisci l'ID della chat sorgente e della chat di destinazione.
  Specifica delle parole chiave per filtrare i messaggi (opzionale).
  
## Funzionamento

  **Inoltro basato su parole chiave**: Se fornisci parole chiave, verranno inoltrati solo i messaggi che le contengono. Se lasci vuoto, inoltrerà tutti i messaggi.
  
  **Controllo continuo**: Lo script verifica costantemente i nuovi messaggi nella chat sorgente e li inoltra alla destinazione.

Esempio di Output:
```yaml
1. Nome: Chat Personale | ID: 12345678
2. Nome: Canale Privato | ID: -1009876543210
3. Nome: Gruppo Test | ID: -1001234567890
```

Esempio di forwarding:

```arduino
Controllo nuovi messaggi e inoltro...
Messaggio ricevuto da -1001234567890: "Offerta speciale oggi!"
Messaggio inoltrato a -1009876543210.
```

## Licenza
Questo progetto è distribuito sotto la licenza MIT. Consulta il file LICENSE per maggiori dettagli.
