# Cosa sa fare Kapa

Puoi chiedere le operazioni con parole tue, a voce o da terminale.
Le risposte sono scritte: il microfono serve a ricevere i tuoi comandi.
Per installazione, requirements e configurazione iniziale segui il
[README](README.md). Questo file si trova nella cartella principale di Kapa
e si apre anche dal pulsante **Guida** dell'app.

## File e cartelle

- **Creare file:** crea un file di testo con il contenuto richiesto.
- **Scrivere nei file:** aggiunge testo a un file esistente.
- **Dettare testo:** scegli un file, poi detta cosa aggiungere. «Annulla dettatura» annulla.
- **Leggere file:** legge il contenuto di un file di testo.
- **Elencare file:** mostra cosa contiene una cartella.
- **Cercare file:** cerca per nome, cartella o estensione.
- **Creare cartelle:** crea una cartella nella posizione richiesta.
- **Copiare file:** crea una copia in un'altra cartella.
- **Spostare file:** trasferisce un file nella cartella scelta.
- **Rinominare file:** cambia il nome di un file.
- **Eliminare file:** cancella un file; disponibile solo in modalità testuale.
- **Svuotare il cestino:** elimina il contenuto del cestino; solo in modalità testuale.

## Multimedia e YouTube

- **Impostare il volume:** porta l'audio alla percentuale richiesta, da 0 a 100.
- **Regolare il volume:** alza, abbassa, silenzia o riattiva l'audio.
- **Controllare musica e video:** riproduce, mette in pausa, ferma o cambia traccia.
- **Cercare su YouTube:** apre i risultati nel browser.
- **Aprire un video YouTube:** apre il video trovato; senza chiave YouTube mostra la ricerca.
- **Ripetizione e riproduzione casuale:** «ripeti la traccia», «ripeti la playlist», «disattiva ripetizione», «attiva riproduzione casuale», «disattiva riproduzione casuale». «Ricomincia il brano» riporta il brano all'inizio. Questi comandi sono locali; il supporto dipende dal player.
- **Scelta automatica del lettore:** Kapa dà priorità alle sessioni multimediali dei browser disponibili tramite MPRIS (Brave, Firefox, Chromium e altri), scegliendo prima quelle in riproduzione, poi quelle in pausa. Se non rileva browser, sceglie tra i lettori disponibili come Spotify o VLC, con lo stesso ordine. A parità usa l'ordine di rilevamento, senza chiedere quale lettore usare. Un lettore che non risponde non blocca gli altri. Puoi comunque indicare un nome: «metti in pausa Spotify», «metti play su Firefox», «prossima traccia su VLC». Il nome esplicito prevale sulla scelta automatica. Un browser aperto senza sessione MPRIS non è rilevabile come lettore; non viene avviato un lettore assente.

## Schermo, registrazioni e replay

- **Fare screenshot:** salva il monitor principale, uno specifico, tutti i monitor o la finestra attiva, se supportato.
- **Avviare una registrazione:** usa GPU Screen Recorder se installato, altrimenti OBS; puoi chiedere esplicitamente OBS. GSR salva in MP4 con video H.264 e audio AAC; OBS usa le proprie impostazioni.
- **Fermare una registrazione:** interrompe la cattura e salva il video.
- **Registrare per un tempo preciso:** registra da 1 a 600 secondi, poi salva automaticamente.
- **Attivare il buffer di replay:** mantiene pronti gli ultimi secondi dello schermo; con GSR puoi scegliere da 1 a 600 secondi, con OBS usa la durata configurata in OBS.
- **Salvare il replay:** salva gli ultimi secondi catturati dal replay attivo.
- **Fermare il buffer di replay:** disattiva la cattura degli ultimi secondi.

## Applicazioni e sistema

- **Aprire applicazioni:** avvia un programma installato.
- **Verificare applicazioni:** controlla se un programma è installato.
- **Chiudere applicazioni:** chiede la chiusura del programma indicato.
- **Cercare pacchetti:** cerca programmi nei repository della distribuzione.
- **Installare programmi:** apre un terminale per conferma ed eventuale password.
- **Aggiornare il sistema:** apre la procedura prevista per la distribuzione, con conferma.

## Ricerca, appunti e notifiche

- **Cercare su Google:** apre i risultati nel browser predefinito, senza chiavi API Google.
- **Mostrare notifiche:** visualizza un messaggio sul desktop.
- **Copiare testo negli appunti:** prepara il testo da incollare altrove.
- **Leggere gli appunti:** mostra il testo attualmente copiato.
- **Impostare promemoria:** mostra una notifica dopo il tempo richiesto; l'assistente deve restare attivo.

## Voce e conversazione

- **Ricordare la conversazione:** mantiene il contesto durante la sessione; al riavvio riparte da zero.
- **Mostrare i comandi:** scrivi «aiuto» nel terminale per vedere l'elenco disponibile.
- **Parlare su richiesta:** premi «Parla ora» o la scorciatoia; il microfono resta chiuso quando non ascolta.
- **Configurare la scorciatoia:** il pulsante «Scorciatoie» aiuta a scegliere il tasto nel desktop.
- **Capire l'ultima richiesta:** la finestra mostra la frase trascritta, l'azione richiesta, il risultato e se è stata usata l'elaborazione locale o Groq. Il registro strutturato resta sul computer, senza audio.
- **Comandi locali:** play, pausa, traccia successiva/precedente, stop, volume, screenshot, replay, apertura delle app più comuni, lettura degli appunti e registrazione dello schermo (anche a tempo) funzionano senza chiamate a Groq quando la frase è riconosciuta. Richieste complesse o con più azioni passano a Groq.

## Finestra e avvio

- **Aprire la GUI:** doppio clic su «Kapa.desktop».
- **Evitare doppie aperture:** altri clic sull'avviatore richiamano la finestra già aperta.
- **Modalità compatta:** rimpicciolendo la finestra resta solo il microfono; riallargandola tornano tutti i comandi.
- **Avvio automatico:** aprendo la GUI parte anche l'assistente, con il microfono chiuso.
- **Restare in background:** chiudendo la finestra, rimane nel tray se il desktop lo supporta.
- **Uscire completamente:** clic destro sull'icona nel tray → «Chiudi».

## Miniguida: ricerca Google

Di' o scrivi «cerca su Google ricette per la pizza»: Kapa apre la pagina dei
risultati nel browser predefinito. Scegli tu quale risultato visitare.
Non serve una chiave API Google; Kapa non legge né riassume le pagine.
L'interpretazione di questa richiesta passa tramite Groq e richiede la
relativa chiave. Il browser deve poter accedere a Internet.

## Miniguida: registrazioni e replay con GSR e OBS

### Quale programma viene usato

- Se `gpu-screen-recorder` è installato, Kapa usa GSR come predefinito.
- Se GSR manca, prova OBS.
- Con entrambi installati, chiedi «registra lo schermo con OBS» per scegliere OBS.
- Se GSR è installato ma dà un errore, Kapa segnala il problema senza passare automaticamente a OBS.

«Ferma la registrazione», «salva il replay» e «ferma il buffer replay» seguono
la cattura avviata da Kapa. Kapa non prende in carico catture OBS già avviate
manualmente. Alla chiusura prova a fermare le proprie catture, lasciando aperto OBS.

### Comandi di esempio

- «Registra lo schermo»: avvia con il programma predefinito.
- «Registra lo schermo con OBS»: sceglie OBS esplicitamente.
- «Fai un video di dieci secondi con OBS»: avvia OBS e lo ferma dopo dieci secondi.
- «Ferma la registrazione»: ferma e salva la registrazione avviata da Kapa.
- «Avvia il buffer replay»: avvia con il programma predefinito.
- «Avvia il buffer replay da sessanta secondi con GPU Screen Recorder»: sceglie GSR e la durata.
- «Avvia il buffer replay con OBS»: usa la durata configurata in OBS.
- «Salva il replay»: salva con GSR oppure richiede il salvataggio a OBS.
- «Ferma il buffer replay»: interrompe il buffer avviato da Kapa.

### Preparare OBS una volta

1. Installa OBS 28 o successivo, nativo oppure Flatpak (`com.obsproject.Studio`).
2. Apri OBS e completa la configurazione iniziale: scegli le sorgenti video e audio, la cartella e il formato di registrazione. Kapa registra la scena attuale di OBS.
3. In **Strumenti → Impostazioni server WebSocket**, abilita il server e annota la password e la porta.
4. Nel file `.env` nella cartella principale di Kapa aggiungi `OBS_PASSWORD=la_tua_password`. Se la porta è diversa da quella predefinita, aggiungi anche `OBS_PORT=la_tua_porta` (default `4455`).
5. Dalla cartella principale aggiorna le dipendenze con `.venv/bin/python -m pip install -r requirements.txt`, poi riavvia Kapa. Se usi un ambiente diverso da quello creato dall'installer, usa il suo interprete Python.
6. Prova «registra lo schermo con OBS», poi «ferma la registrazione».

Per usare il replay, abilita e configura anche il buffer nelle impostazioni
di output di OBS. Chiedi poi di avviarlo senza indicare una durata: Kapa usa
quella già impostata. Con OBS un nome file personalizzato o una durata replay
esplicita vengono segnalati come non supportati, senza modificarne le impostazioni.

Se OBS è chiuso, Kapa prova ad aprirlo e collegarsi al server locale. Se compare
un errore, verifica server WebSocket, porta e password. Se il collegamento si
interrompe durante una cattura, controlla direttamente in OBS se è ancora attiva.

## Dipendenze e disponibilità

Le registrazioni richiedono GPU Screen Recorder oppure OBS configurato come sopra.
Le altre funzioni richiedono
le relative dipendenze e il supporto del desktop. L'interpretazione tramite
Groq richiede Internet e una chiave API; la trascrizione vocale avviene sul PC.
Le prove pratiche documentate sono su Nobara KDE: le altre distro sono da verificare.
