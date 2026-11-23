# Sito ufficiale di Kapa

## Anteprima locale su Nobara

Apri `dist/index.html` con un doppio clic in Dolphin. Dal terminale, nella cartella principale del progetto, puoi usare:

```bash
xdg-open sito/dist/index.html
```

Il selettore IT / EN apre l’altra pagina anche da un file locale. Il menu usa ancore native. Per vedere una modifica salva il file e ricarica la pagina. HTML e CSS sono sufficienti per visitare il sito sia in locale sia su un host statico.

## Cambiare il tema

Apri `dist/tema.css` con Kate o un altro editor di testo.

| Impostazione | Effetto |
| --- | --- |
| `--sfondo`, `--accento` | Colore di base e turchese usato per il pulsante, le icone e il focus |
| `--testo`, `--testo-secondario`, `--testo-pulsante` | Colori dei testi principali, secondari e del pulsante primario |
| `--pannello`, `--bordo` | Colore e trasparenza delle schede e dei loro bordi |
| `--immagine-sfondo` | File mostrato dietro al titolo e alla schermata |
| `--visibilita-sfondo`, `--intensita-fasci` | Valori da `0` a `1` |
| `--visibilita-particelle` | Valore da `0` a `1`, con `0` per nasconderle |
| `--passo-particelle` | Abbassa il valore, per esempio da `108px` a `80px`, per aumentare la densità |

Per sostituire lo sfondo, copia l’immagine in `dist/assets/` e modifica la riga, per esempio `--immagine-sfondo: url("assets/nuovo-sfondo.webp");`. Le animazioni rispettano la preferenza di movimento ridotto del browser.

## Cambiare testi, sezioni, screenshot e link

Modifica `contenuti.json`. I blocchi `it` ed `en` contengono i testi e le descrizioni SEO di ciascuna lingua. `schede` contiene gli otto titoli e le descrizioni delle funzioni, `passi` i tre passaggi, `distribuzioni` i desktop testati. L’elenco espandibile viene da `COSA_SA_FARE.md` nella radice del progetto. `esempi_vocali` contiene i tre esempi italiani mostrati su entrambe le pagine.

- Aggiorna `link.release_attuale` con l’URL della pagina del nuovo tag GitHub. `link.release` resta l’indice delle release nel footer.
- Inserisci in `link.video` l’URL HTTPS di un video dimostrativo accessibile ai visitatori. Lascia il campo vuoto per nascondere il pulsante.
- Per l’anteprima della GUI, acquisisci il pannello di Kapa pronto e con **Ultima richiesta** e **Risposta** compilate dopo un’azione reale. Fornisci un PNG originale chiamato `pannello-attivo.png`, ritagliato alla finestra e privo di dati personali. Copialo in `dist/assets/`, poi aggiorna `schermate[0]` con il percorso, le dimensioni originali e le descrizioni IT/EN.
- Per gli schermi ad alta densità puoi aggiungere `"file_2x": "assets/pannello@2x.webp"` a `schermate[0]`. Usa una cattura con lo stesso ritaglio e il doppio dei pixel per lato (980 × 1440 per l’anteprima attuale). Mantieni `misure` riferito al file base.
- La condivisione usa `social`. L’immagine `dist/assets/social.jpg` è larga 1200 × 630 e usa il logo e lo sfondo originali. Puoi sostituirla aggiornando anche dimensioni e descrizioni nel JSON.

Dopo aver modificato il JSON, rigenera le pagine con Python 3.10 o successivo. Dalla cartella principale:

```bash
python3 sito/genera.py
```

La rigenerazione riscrive i due `index.html`. I CSS e gli asset sono sorgenti statici conservati direttamente in `dist/` e inclusi nella pubblicazione. Per cambiare la struttura delle sezioni usa `genera.py`. Per cambiare spaziature, dimensioni e colonne usa `dist/stile.css`.

## File del sito

- `contenuti.json` e `genera.py` sono i sorgenti per personalizzare e rigenerare le pagine.
- `dist/index.html` e `dist/en/index.html` sono le pagine pubblicabili.
- `dist/tema.css`, `dist/stile.css` e `dist/assets/` contengono l’aspetto e le immagini.
- `dist/.nojekyll` indica a GitHub Pages di servire il sito statico direttamente.

## Pubblicare con GitHub Actions

Nel repository destinato a GitHub, apri **Settings → Pages** e seleziona **GitHub Actions** in **Build and deployment → Source**. Dopo il push su `main`, il workflow `.github/workflows/pages.yml` rigenera il sito e pubblica il solo contenuto di `sito/dist/`. Si avvia per modifiche al sito, a `COSA_SA_FARE.md` o al workflow stesso. Puoi anche avviarlo da **Actions → GitHub Pages → Run workflow**, scegliendo `main`.

Per gli aggiornamenti, modifica i sorgenti, rigenera per controllare l’anteprima locale e includi nel commit i file del sito aggiornati. L’indirizzo pubblico è definito da `url` in `contenuti.json`. [Istruzioni di GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
