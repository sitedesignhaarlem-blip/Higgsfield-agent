# Alexia-revisie 28-10-2026 — alle zes boten (Elysium, Wild Blue, Southern Mist, One Life, Sandpiper, Three Quarters Full)

Bronmateriaal: 70 foto's van Alexia (zie `photos/` voor de 16:9-bijsneden bronnen, `media_ids.txt`
voor de upload-id's, `jobs.txt` voor alle job-id's). Alle nieuwe clips: Kling 3.0, 3s, std, sound off,
16:9, 4,5 credits per clip. Montage: bestaande opgeleverde video's (v2 + muziek) tweede-nauwkeurig
gesplitst op Alexia's tijdstippen, nieuwe clips ertussen, crossfade 0,4s, muziek "Majestic" opnieuw
over de nieuwe lengte (fade-in 1,5s / fade-out 2s, 90%).

## Fotocontrole (full-size, niet op thumbnails)
Alle 70 foto's op volledig formaat bekeken op mensen. Foto's mét mensen (NIET gegenereerd, zie
openstaande punten): Wild Blue 1 (kapitein + 2 personen flybridge), Wild Blue 4 (2 zonnebaders),
Southern Mist 1, 2, 3, 4, 19 (drone-opnames, bemanning/gasten op flybridge en achterdek).
Wild Blue 5 had een man op het zwemplatform: bijgesneden naar het mensvrije deel (stuk romp+plateau).
Portret-foto's (Elysium 5-8, Southern Mist 13 en 16) vooraf naar 16:9 bijgesneden (aspect-ratio-bug).
Kleine bronfoto's (One Life 1,2,5-8; Southern Mist 5-9,12,14,17,18: 756x567) zijn zichtbaar zachter.

## Clips (62 + 2 herkansingen)
- 3QF 1-9 -> clips 101-109 | Elysium 1-8,10 -> 201-208,210 | One Life 1-8 -> 301-308, leopard head -> 309
- Southern Mist 5-18 -> 405-418 (Elysium-deur vóór 17) | Sandpiper 1-16 -> 501-516 | Wild Blue 2,3,5,6,7 -> 602,603,605,606,607
- Deurclip (Elysium foto 9, schuifdeur opent): job 33be792d..., 4,5 cr, hergebruikt in Elysium, Wild Blue, Southern Mist.
- 303 (One Life 3): eerste job mislukt (geen kosten), opnieuw ingediend met aangepaste prompt.
- 605 (Wild Blue 5): eerste versie had een verzonnen witte fender op het zwemplatform -> afgekeurd,
  opnieuw met `no fenders, no buoys` in de prompt. +4,5 cr.
- Preset-deflectie ("IN THE DARK") bij exterieur-prompts: opgelost met declined_preset_id.
- Kosten: 63 clips x 4,5 = 283,5 cr (+ deurclip 4,5 eerder). Saldo voor: 313,5 -> nu 25,5.

## QC
Laag 1 (qc_check.py met RapidOCR-vervanger voor tesseract, geen root in de sandbox): JERK/EDGE rustig;
TEXT-treffers alleen op ruis in patronen (strepenkussens, vloermat) en echte tekst op de boot zelf
(WILD BLUE op de romp in foto 5, LEOPARD 51 bij Sandpiper). Geen verzonnen tekst.
Laag 2: alle contactsheets van alle nieuwe clips visueel bekeken. Geen mensen, geen verzonnen meubels
of boten. Enige afkeur: 605 (fender), zie boven. Kanttekening: One Life 303 (voordek): in het begin
van de clip een lichte lensvervorming van de railing, acceptabel.

## Transition QC
Elke crossfade per video: middenframe vs. blend van de twee buren (NCC) + visuele controle van de
splice-naden (nieuwe naad direct na een bestaand fragment) met 10fps-stroken. Snijpunten staan
minstens 0,1-0,3s buiten de oude crossfade-zones (CLAUDE.md §12).
