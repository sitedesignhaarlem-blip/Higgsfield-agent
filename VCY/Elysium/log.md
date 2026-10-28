# Log — Elysium

## Context (29-09-2026)
Baseline-versie, zelfde aanpak/reden als Caribbean Cat (zie dat log.md voor de volledige
uitleg: Alexia levert geen foto's aan, Higgsfield-abonnement loopt bijna af, doel is zoveel
mogelijk boten op een goede basis afkrijgen). Foto's rechtstreeks van
virgincharteryachts.com/yachts/elysium. GEEN room-categorieen (geen bruikbare bestandsnamen,
visuele inspectie technisch onmogelijk in deze sessie). 9 gedeelde bestanden met Southern
Mist/Tidewater/Wild Blue uitgesloten.

## Shotlist
19 clips: 1 opener (wide, pro) + 3 extra wide/exterior-achtige shots + 14 detail-clips +
1 closer (dezelfde bronfoto als opener). Alle 30 hires foto's van deze boot waren technisch
bruikbaar; 18 gebruikt (rest niet, om binnen het 60-90s-doel te blijven).

## QC laag 1
Eerste ronde: 3 clips geflagd op TEXT (index 6, 8, 9 — allemaal lage-confidence garbled
fragmenten, geen herhaald/identiek patroon zoals bij Caribbean Cat's watermark-geval).
Regeneratie met verzwaarde no-text-guard: index 8 en 9 schoon, index 6 kreeg een nieuw
(ander) 2-teken fragment ('yy' conf85) — geaccepteerd na 1 herkansing, patroon wijst op
Kling-ruis.

## QC laag 2 — alsnog uitgevoerd (10-10-2026)
Zelfde methode als Sandpiper/Caribbean Cat (`sandbox_exec` image_paths).
**TEXT:** geen leesbare woorden — "Seen"/"Thad"/"WARE" zijn losse OCR-ruis-
fragmenten (teak/water), geen bootnaam of logo gevonden.
**Visueel (27-punts mosaic + close-ups op 2 verdachte tiles):** geen mensen,
geen verzonnen meubels/dieren/vaartuigen, geen morphing. De 2 tiles die in
de mosaic wazig oogden (flybridge sunpad/helm-overgang, ~24-29s) bleken bij
close-up gewoon scherpe, correcte frames — artefact van de kleine tile-
compressie, geen echt defect.
**Transition QC:** geen surgical splice van toepassing; geen ghosting
waargenomen.

## Montage
19 clips, genormaliseerd naar 1920x1080/30fps, assemble.py, xfade 0.4s.
Eindlengte: 62,47s (binnen 60-90s doel).

## Muziek
Track: "Majestic" — Diego Nava (Mixkit Stock Music Free License), zelfde track als de
vorige boten in deze batch.

## Oplevering
- Stille versie: Elysium.mp4 (62,47s) —
  https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/0f58d194-bba4-47f5-9a09-f0472b669b3f.mp4
- Met muziek: Elysium_music.mp4 —
  https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/1f758200-3143-445a-8293-b184787bee13.mp4

## Openstaande punten voor Alexia/Valentijn
1. GEEN room-categorieen — volgorde is site-gallery-volgorde.
2. Baseline op basis van site-foto's — Alexia's bevestiging nog nodig voor definitieve
   oplevering.

## Revisie Alexia (28-10-2026) - deurclip testclip

Alexia wil dat het schuifdeurtje bij Elysium foto 9 opengaat naar het kleine hutje (foto 10),
en hetzelfde voor Wild Blue en Southern Mist (voor SM foto 17).

Foto 9 (deur dicht) en foto 10 (close-up bed van binnen) hebben heel verschillende standpunten,
dus geen start+end-paar (morphing-risico, sectie 8). Gekozen: single-image clip vanaf foto 9
met prompt "deur schuift naar links open", daarna foto 10 als aparte clip.

- Foto: Elysium_9.jpg, media_id `eb230e1d-93f0-4d00-998e-08cc3685e2ce`
- Clip: job `33be792d-693c-4955-b911-67750f861574`, 3s std, sound off, 16:9, 4,5 credits
- Resultaat: deur schuift soepel naar links, bed wordt zichtbaar, kussen en ruit stabiel,
  geen mensen of verzonnen objecten. Wacht op akkoord Valentijn.

## Revisie Alexia (28-10-2026) - uitgevoerd
Bestaande video tot 57,3s, daarna Elysium-foto 1-8, dan foto 9 (deurclip: deur schuift open) en foto 10, daarna de bestaande exterieur-closer. Let op: Alexia schreef 'aan het einde'; de foto's staan vóór de exterieur-closer zodat de video op een exterieur eindigt (zoals bij de andere boten).

- Nieuwe clips: 9 (3s std, sound off, 16:9, 40.5 credits; zie `_Alexia_revisie_2810/jobs.txt` voor job-id's)
- Bestand: Elysium_music.mp4, 87,83s — https://d2ol7oe51mr4n9.cloudfront.net/user_3GAnI2MKRZFE3ukZ4ZGqGe45vyC/89f7dfde-2819-4a94-ada1-3c88c179decd.mp4
- QC: laag 1 + laag 2 op alle nieuwe clips, crossfade-check per naad (NCC-blend + stroken rond de splice-naden). Zie `_Alexia_revisie_2810/log.md`.
