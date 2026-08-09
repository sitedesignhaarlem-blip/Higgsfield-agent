# Villa Walkthrough Video Agent

Dit is het draaiboek voor het automatisch genereren van cinematische walkthrough-video's
voor villa's/yachts, op basis van bestaande listing-foto's. Volg dit proces exact voor
elke villa in `villas.csv`, zonder tussentijds naar bevestiging te vragen tenzij expliciet
aangegeven in dit document.

## Vereisten (eenmalig, door Valentijn te checken)
- MCP-connector **Higgsfield** actief in deze Claude Code sessie
- MCP-connector **Google Drive** actief in deze Claude Code sessie
- `ffmpeg` geïnstalleerd en beschikbaar in PATH
- `villas.csv` ingevuld met kolommen: `villa_naam,drive_folder_link,status`

## Workflow per villa (status = "todo" in villas.csv)

### Stap 1 — Foto's ophalen
1. Open de Google Drive folder via de link in `drive_folder_link`.
2. Download alle foto's naar een lokale werkmap: `./work/<villa_naam>/source/`
3. Sorteer de foto's op een logische route door het huis (bijv. entree → woonkamer →
   keuken → slaapkamers → buitenruimte/zwembad → view). Gebruik bestandsnamen/EXIF als hint,
   maar gebruik je eigen beoordeling van de foto-inhoud als de volgorde niet duidelijk is.

### Stap 2 — Clip-planning
1. Bepaal het aantal clips: richtlijn is **1 clip per 1-2 opeenvolgende foto's** in de route,
   met een minimum van 8 en maximum van 15 clips per villa (tenzij er te weinig foto's zijn).
2. Voor elke clip: wijs een `start_image` en `end_image` toe uit twee opeenvolgende foto's
   in de route, zodat er echte camera-travel ontstaat tussen twee echte standpunten
   (nooit dezelfde foto als start én eind — geen statische drift).
3. Schrijf dit plan weg naar `./work/<villa_naam>/clip_plan.json` vóórdat je gaat genereren,
   zodat het traceerbaar is.

### Stap 3 — Genereren via Higgsfield
Voor elke clip in het plan:
- Model: Kling 3.0
- Duur: 5s
- Mode: std
- Aspect ratio: 16:9
- Kosten: 7,5 credits per clip
- Gebruik de batch-generation functionaliteit (max 12 parallelle jobs tegelijk) om clips
  in groepjes te genereren i.p.v. één voor één.
- Wacht tot een batch klaar is voordat je de volgende start.
- Download de resulterende clips naar `./work/<villa_naam>/clips/`

**Credit-check:** tel vooraf het totale aantal clips × 7,5 en meld dit bij het opstarten
van een villa als het boven de 100 credits uitkomt, zodat Valentijn dit kan zien in de output
(gewoon melden in je antwoord, niet blokkeren — hij bepaalt zelf het budget).

### Stap 4 — Samenvoegen
1. Voeg alle clips in de juiste (geplande) volgorde samen tot één MP4 met ffmpeg:
   `ffmpeg -f concat -safe 0 -i filelist.txt -c copy output.mp4`
   (gebruik re-encode i.p.v. `-c copy` als de clips niet exact dezelfde codec/resolutie hebben)
2. Sla het eindresultaat op als: `./output/<villa_naam>_walkthrough.mp4`

### Stap 5 — Afronden
1. Zet status van deze villa in `villas.csv` op `done`.
2. Geef een korte samenvatting: villanaam, aantal clips, credits verbruikt, output-pad.
3. Ga door naar de volgende villa met status `todo`.

## Belangrijke regels
- Verwerk villa's **één voor één**, niet gelijktijdig — dit voorkomt verwarring in de
  werkmappen en maakt fouten makkelijker te traceren.
- Als een Drive-link niet werkt of leeg is: zet status op `error` in villas.csv met een
  korte reden in een extra kolom `notes`, en ga door naar de volgende villa. Niet blokkeren.
- Als er minder dan 4 bruikbare foto's zijn voor een villa: sla over, status `skipped`,
  reden noteren — te weinig materiaal voor een goede walkthrough.
- Test-modus: als Valentijn vraagt om "eerst 2-3 villa's te testen", verwerk dan alleen
  de eerste 2-3 rijen met status `todo` en stop daarna, ongeacht hoeveel er nog open staan.

## Wat NIET automatisch te doen
- Geen video's automatisch versturen naar klanten — dat blijft een aparte, bewuste stap.
- Geen prijsafspraken of facturen aanraken — dit script gaat alleen over videoproductie.
