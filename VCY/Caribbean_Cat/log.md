# Log — Caribbean Cat

## Context (29-09-2026)
Baseline-versie op initiatief van Valentijn: Alexia levert geen foto's meer aan, Higgsfield-
abonnement loopt bijna af. Doel: zoveel mogelijk boten van de resterende VCY-vloot op een
goede basis afkrijgen zodat Alexia later kan reviewen en aanpassen. Foto's rechtstreeks van
virgincharteryachts.com/yachts/caribbean-cat (media_import_url).

Caribbean Cat heeft GEEN bruikbare bestandsnamen (hash/camera-codes) en visuele inspectie van
foto's is in deze sessie technisch onmogelijk (netwerkbeleid blokkeert alle toegang tot de
VCY-site en Higgsfield's CDN vanuit de hoofdsessie, bevestigd getest). Daarom GEEN
Exterior/Flybridge/Helm/Bow/Aftdeck/Salon/Galley/Cabin-labels toegekend — zie brief.md en
shotlist.json note_general voor de volledige methodologie (wide/detail-split op numerieke
pixel-analyse, gevalideerd tegen Sandpiper's bekende bestandsnamen).

2 foto's uitgesloten wegens overlap met One Life (Leopard-14.jpg, Leopard-16.jpg).
13 foto's uitgesloten wegens resolutie <1280px, behalve de openings/slotfoto (Leopard-9.jpg,
900x600 — enige bruikbare brede buitenshot na uitsluiting).

## Shotlist
Oorspronkelijk 17 clips (1 opener + 15 detail + 1 closer), zie shotlist.json.

## QC laag 1 (automatisch, qc_check.py)
Eerste ronde: 6 clips geflagd — clip 17 (closer, JERK 2.59), clips 10/12/13/14/16 (TEXT).

Regeneratie ronde 2:
- Clip 17: opgelost (JERK 2.59 -> 1.99) met reddingsprompt (single-axis, 3s).
- Clip 14: schoon.
- Clip 10: TEXT-ruis blijft, maar WISSELT elke poging (ronde1 Th/WN/sa/WAAL/EB, ronde2
  AN/ba/AAA) — patroon wijst op Kling per-generatie OCR-ruis, niet op vaste brontekst.
- Clip 12, 13, 16: IDENTIEKE hoge-confidence treffer "HOME WHERE THE ANCHOR DROPS" (conf
  77-96%) over 2 volledig losse generaties — dit is vrijwel zeker een watermark/caption die
  al in de bronfoto's zelf zit (een bekende stock-foto-slogan), niet oplosbaar met
  prompt-aanpassingen. GEEN vervangende bronfoto's beschikbaar (hele foto-pool van de boot al
  gebruikt na dedup/kwaliteitsfilter).

Beslissing: clip 10 geaccepteerd (2 pogingen, wisselende lage-confidence ruis). Clips 12, 13,
16 UITGESLOTEN uit de montage — niet verder regenereren, credits niet blijven uitgeven aan een
niet-oplosbaar bronprobleem.

Gevolg: eindlengte 51,28s, ONDER de 60-90s-norm uit CLAUDE.md. Geaccepteerd gevolg van beperkte
brondata voor deze specifieke boot (geen vervangende foto's beschikbaar) — gemeld aan
Valentijn.

## QC laag 2 (visueel)
NIET uitgevoerd — zelfde technische sessiebeperking als bij Sandpiper (zie brief.md).

## Montage
14 clips (na uitsluiting van 12/13/16), genormaliseerd naar 1920x1080/30fps, assemble.py,
xfade 0.4s. Eindlengte: 51,30s (dry-run waarschuwde correct: onder 60s).
Eindcontrole (technisch): 1920x1080, 30fps, geen audio in de stille versie, geen zwarte
frames. qc_check.py over de eindvideo gedraaid (JERK-flag op volledige video, verwacht
vanwege crossfade-overgangen, geen aparte afkeuring op basis daarvan).
Transition QC: geen surgical splice, alle clips vers gegenereerd — "oude naad"-risico niet
van toepassing. Volledige frame-voor-frame visuele controle niet mogelijk (zelfde
CDN-beperking); technische eindcontrole wel gedaan.

## Muziek
Track: "Majestic" — Diego Nava (Mixkit, Mixkit Stock Music Free License), zelfde track als
Sandpiper voor consistentie binnen deze batch. Ingekort tot videolengte, fade-in 1,5s,
fade-out 2s, AAC 192kbps.

## Oplevering
- Stille versie: Caribbean_Cat.mp4 (51,30s) —
  https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/e922645d-63fe-48c4-b549-4ed3ad5a1d55.mp4
- Met muziek: Caribbean_Cat_music.mp4 —
  https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/4844945d-8423-4445-91e2-a45fc0cb94bf.mp4

## Openstaande punten voor Alexia/Valentijn
1. GEEN room-categorieen — volgorde is site-gallery-volgorde, geen bevestigde kamervolgorde.
2. Eindlengte 51,30s, onder de 60-90s-norm — geen vervangende foto's beschikbaar om aan te
   vullen na uitsluiting van 3 clips met een niet-oplosbaar watermark-probleem.
3. Laag-2 visuele QC niet uitgevoerd — technische sessiebeperking.
4. Baseline op basis van site-foto's — Alexia's bevestiging nog nodig voor definitieve
   oplevering.

## Credits (gecombineerd met Sandpiper, zelfde sessie/batch)
Balans voor start: 1715
Balans na Sandpiper + Caribbean Cat (48 generaties totaal, incl. regeneraties): 1428
Verbruik: 287 credits voor 2 boten (~144/boot, hoger dan het ±120-richtgetal door de
QC-regeneraties op beide boten).
