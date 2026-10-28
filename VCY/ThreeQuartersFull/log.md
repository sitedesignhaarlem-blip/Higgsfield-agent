# Log — ThreeQuartersFull

## Context (29-09-2026)
Baseline-versie, zelfde aanpak/reden als de vorige boten in deze batch (zie Caribbean Cat/log.md
voor de volledige uitleg). GEEN room-categorieen (geen bruikbare bestandsnamen, visuele
inspectie technisch onmogelijk in deze sessie). Geen gedeelde bestanden met andere boten
gevonden. Beste beeldkwaliteit tot nu toe: alle gebruikte bronfoto's >=1280px.

## Shotlist
19 clips: opener (wide, pro) + 3 extra wide + 12 detail (1280x950) + 2 extra detail (toegevoegd
om binnen 60-90s te komen) + closer.

## QC laag 1
Eerste ronde: 4 van 19 clips geflagd — clip 5 (EDGE 0.289), clip 7/15/17 (TEXT, lage-confidence
ruis).
- Clip 5: opgelost met reddingsprompt (single-axis movement).
- Clip 15: opgelost met verzwaarde no-text-guard.
- Clip 7, 17: TEXT-ruis blijft na herkansing maar telkens ANDERE garbled fragmenten (geen
  herhaald patroon) -- geaccepteerd, wijst op Kling-ruis niet op vaste brontekst.

Eindresultaat: 17/19 clips schoon, 2 geaccepteerd na 2 pogingen.

## QC laag 2 — alsnog uitgevoerd (10-10-2026)
Zelfde methode als de vorige boten. **TEXT:** geen leesbare woorden (ruis),
geen bootnaam/logo. **Visueel (26-punts mosaic):** geen mensen, geen
verzonnen meubels/dieren, geen morphing. Andere boten op de achtergrond in
marina-shots zijn legitiem onderdeel van de bronfoto's. Geen afkeuringen.
**Transition QC:** geen surgical splice van toepassing; geen ghosting
waargenomen.

## Montage
19 clips, genormaliseerd naar 1920x1080/30fps, assemble.py, xfade 0.4s.
Eindlengte: 60,47s (net binnen 60-90s doel).

## Muziek
Track: "Majestic" — Diego Nava (Mixkit Stock Music Free License), zelfde track als de
vorige boten in deze batch.

## Oplevering
- Stille versie: ThreeQuartersFull.mp4 (60,47s) —
  https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/ac4fc3a4-240d-4832-a94c-69546a3edd57.mp4
- Met muziek: ThreeQuartersFull_music.mp4 —
  https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/d7354dca-dca7-4f6d-ba8b-f6b086502fbf.mp4

## Openstaande punten voor Alexia/Valentijn
1. GEEN room-categorieen — volgorde is site-gallery-volgorde.
2. Baseline op basis van site-foto's — Alexia's bevestiging nog nodig voor definitieve
   oplevering.

## Revisie Alexia (28-10-2026) - uitgevoerd
0-19,7s behouden, 20-24 geknipt, 26-48 behouden, 3QF-foto 1-9 (9 clips) erna, daarna de exterieur-closer vanaf 56s.

- Nieuwe clips: 9 (3s std, sound off, 16:9, 40.5 credits; zie `_Alexia_revisie_2810/jobs.txt` voor job-id's)
- Bestand: Three_Quarters_Full.mp4 (met muziek), 69,70s — https://d2ol7oe51mr4n9.cloudfront.net/user_3GAnI2MKRZFE3ukZ4ZGqGe45vyC/19c6ce8d-3dc0-4d12-a70c-1756303e95fc.mp4
- QC: laag 1 + laag 2 op alle nieuwe clips, crossfade-check per naad (NCC-blend + stroken rond de splice-naden). Zie `_Alexia_revisie_2810/log.md`.
