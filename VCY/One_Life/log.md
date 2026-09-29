# Log — One Life

## Context (29-09-2026)
Baseline-versie, zelfde aanpak/reden als de vorige boten in deze batch (zie Caribbean Cat/log.md
voor de volledige uitleg). GEEN room-categorieen (geen bruikbare bestandsnamen, visuele
inspectie technisch onmogelijk in deze sessie). 2 foto's gedeeld met Caribbean Cat uitgesloten.

## Bijzonderheid: dunne fotokwaliteit
Deze boot se gallery bestaat grotendeels uit oude Facebook-uploads op 756x567 (onder de
1280px-norm uit CLAUDE.md sectie 7). Slechts 6 van de 28 bruikbare foto's zijn >=1280px.
Om een video van voldoende lengte te halen zijn 8 foto's onder de norm toch gebruikt --
bewuste uitzondering, verwacht iets zachter beeld. 2 zeer lage-resolutie site-thumbnails
(wildcat-too-main.png, wildcat-too-bow.png) volledig uitgesloten.

## Shotlist
17 clips: opener (wide, pro) + 1 extra wide + 6 detail (hi-res, 5s) + 8 detail (756px, 3s) +
closer.

## QC laag 1
Eerste ronde: 7 van 17 clips geflagd.
- Clip 2 (wide extra): JERK 4.74 + TEXT groeiend fragment "LION/LIONE/LIONEC" conf75-95 over
  meerdere frames -- vermoedelijk een bootnaam/merk zichtbaar in de bronfoto (zelfde patroon
  als Sandpiper's "Sand"-geval). Opgelost met reddingsprompt + verzwaarde no-text-guard.
- Clip 8, 13: JERK (2.51, 2.90) -- opgelost met reddingsprompt (single-axis movement).
- Clip 1, 5, 7, 12: TEXT lage-confidence ruis -- clip 1, 5, 12 opgelost met verzwaarde
  no-text-guard. Clip 7 blijft ruis vertonen na 2 pogingen (telkens ANDERE garbled
  fragmenten, geen herhaald patroon) -- geaccepteerd, wijst op Kling-ruis.

Eindresultaat: 16/17 clips schoon, 1 geaccepteerd na 2 pogingen.

## QC laag 2
Niet uitgevoerd — zelfde technische sessiebeperking als bij de vorige boten.

## Montage
17 clips, genormaliseerd naar 1920x1080/30fps, assemble.py, xfade 0.4s.
Eindlengte: 59,18s — net ONDER de 60-90s-norm (dry-run gaf waarschuwing). Geaccepteerd:
dichtbij de ondergrens en geen extra bruikbare foto's meer over binnen de kwaliteitsgrens.

## Muziek
Track: "Majestic" — Diego Nava (Mixkit Stock Music Free License), zelfde track als de
vorige boten in deze batch.

## Oplevering
- Stille versie: One_Life.mp4 (59,18s) —
  https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/d8f3fb07-34b0-4bb0-a13c-2715bd8fc788.mp4
- Met muziek: One_Life_music.mp4 —
  https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/aafabc25-82d9-4660-af5d-e02d996dc489.mp4

## Openstaande punten voor Alexia/Valentijn
1. GEEN room-categorieen — volgorde is site-gallery-volgorde.
2. Beeldkwaliteit wisselend (8 van 17 clips op bronfoto's onder de resolutienorm).
3. Eindlengte 59,18s, net onder de norm.
4. Laag-2 visuele QC niet uitgevoerd — technische sessiebeperking.
5. Baseline op basis van site-foto's — Alexia's bevestiging nog nodig voor definitieve
   oplevering.
