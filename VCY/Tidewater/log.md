# Log — Tidewater

## Context (29-09-2026)
Baseline-versie, zelfde aanpak/reden als de vorige boten in deze batch (zie Caribbean Cat/log.md
voor de volledige uitleg). GEEN room-categorieen (geen bruikbare bestandsnamen, visuele
inspectie technisch onmogelijk in deze sessie). Numerieke wide/detail-classificatie
(blue_ratio/top_blue heuristiek) gebruikt voor volgorde/prompt-keuze.

4 bestanden uit de bekende gedeelde cluster met Elysium/Southern Mist/Wild Blue (19A8645,
19A8647-2, 19A8872_1, wildblue-4/11/12/13) zijn uitgesloten. Daarnaast zijn 4 afbeeldingen
die in de ruwe HTML-crawl naar boven kwamen bij nader onderzoek herkend als thumbnails uit
het "Browse Similar Yachts"-blok (van Thumper, Freedom, Tropically Impaired, Don't Blink,
Southern Cross) -- geen Tidewater-materiaal, dus niet in de shotlist opgenomen.

## Shotlist
Oorspronkelijk 19 clips: opener (wide, pro, 5s) + 3 extra wide (3s) + 13 detail (3-5s,
ongecategoriseerd) + 1 extra wide (3s) + closer (dezelfde bronfoto als opener, pull-back, 5s).

## QC laag 1 (qc_check.py: JERK/EDGE/TEXT — DRIFT niet actief, geen lokale bronfoto's)
Eerste ronde: 6 van 19 clips geflagd op TEXT (01, 03, 07, 10, 14, 18); clip 07 ook op EDGE.

- **Clip 18** (TEXT, hoge confidence): "Tidewater" conf91, "Beaufort," conf95, "SC" conf96 --
  een coherente, leesbare naam+locatie-caption, geen garbled ruis. Getest met een herkansing
  met verzwaarde prompt ("no caption, no watermark, no location tag, no overlay text of any
  kind"): resultaat bleef nagenoeg identiek ("Tidewater" conf84, "Beaufort," conf96, "SC"
  conf96). Dit bevestigt dat de tekst in de bronfoto zelf gebrand staat (vermoedelijk een
  fotografie-watermark/caption uit de originele bron) en niet via prompting weg te krijgen is.
  **Besluit: clip uitgesloten uit de eindmontage** (zelfde afweging als bij Caribbean Cat --
  geen credits blijven besteden aan een onoplosbare bron, liever een iets kortere eindvideo).
- Clips 01, 03, 07, 10, 14: lage-confidence garbled fragmenten (bv. "sc"/"st" conf56/65,
  "whe" conf53, "AA"/"NE" conf47-58, "IN"/"ali," conf46-62, "MMM" conf47) -- geen coherent of
  herhaald patroon, geen van deze overlapt met de "Tidewater/Beaufort, SC"-tekst uit clip 18.
  Geaccepteerd als gewone Kling-OCR-ruis.
- Clip 07 (EDGE 0.238): geaccepteerd, geen zichtbaar geometrie-defect gerapporteerd door de
  overige scores en geen consistente vervorm-indicator.

Eindresultaat: 17/19 clips schoon of geaccepteerd, 1 clip (18) definitief uitgesloten na
bevestiging dat het bronmateriaal-tekst betreft.

## QC laag 2
Niet uitgevoerd — zelfde technische sessiebeperking als bij de vorige boten.

## Transition QC
Niet visueel uitgevoerd — zelfde technische sessiebeperking. Geen surgical splice (alle
gebruikte clips zijn vers gegenereerd), dus het oude-naad-risico uit sectie 12 van CLAUDE.md
is hier niet van toepassing. Crossfade-duur standaard 0,4s.

## Montage
18 clips (19 gepland, clip 18 uitgesloten na QC), genormaliseerd naar 1920x1080/30fps,
assemble.py, xfade 0,4s.
Eindlengte: 61,83s (binnen 60-90s doel, ondanks het uitsluiten van 1 clip).
Technische eindcontrole: 1920x1080, 30fps, geen audiospoor (stille versie), geen zwarte
frames aan begin/eind.

## Muziek
Track: "Majestic" — Diego Nava (Mixkit Stock Music Free License), zelfde track als de
vorige boten in deze batch.

## Oplevering
- Stille versie: Tidewater.mp4 (61,83s) —
  https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/b4b45afa-8c1e-48b2-90c2-f516310b9041.mp4
- Met muziek: Tidewater_music.mp4 —
  https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/456c64ee-c175-44fd-a817-f9b92518aa14.mp4

## Credits
Balance tijdens productie: 691,75 (gecheckt na de eerste batch-inzending, ruim boven de
300-credit-meldgrens).

## Openstaande punten voor Alexia/Valentijn
1. **Clip 18 (opnieuw exterieur-wide) is uit de video gehaald** omdat de bronfoto een gebrande
   naam+locatie-caption bevatte die niet te verwijderen was. Als Alexia een schone versie van
   deze bronfoto (zonder caption) kan aanleveren, kan dit shot alsnog worden toegevoegd.
2. GEEN room-categorieen — volgorde is site-gallery-volgorde.
3. Laag-2 visuele QC en transition-QC niet uitgevoerd — technische sessiebeperking.
4. Baseline op basis van site-foto's — Alexia's bevestiging nog nodig voor definitieve
   oplevering.
