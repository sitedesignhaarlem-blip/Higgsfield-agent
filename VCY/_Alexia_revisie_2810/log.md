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

## Oplevering (alle met muziek, 1920x1080 30fps)
| Boot | Bestand | Duur |
|---|---|---|
| Three Quarters Full | Three_Quarters_Full.mp4 | 69,7s |
| Elysium | Elysium_music.mp4 | 87,8s |
| Southern Mist | Southern_Mist_music.mp4 | 78,8s |
| One Life | One_Life_music.mp4 | 57,2s |
| Sandpiper | Sandpiper_music.mp4 | 90,4s |
| Wild Blue | Wild_Blue_music.mp4 | 47,3s |
URL's staan per boot in `<boot>/log.md`. Saldo na afloop: 25,5 credits (ruim onder de 300-meldgrens).

## Openstaande punten voor Valentijn
1. Foto's met mensen niet verwerkt (harde regel): Wild Blue 1 en 4, Southern Mist 1-4 en 19. Alexia vraagt ze wel expliciet.
   Opties: (a) zo laten en aan haar melden, (b) als stilstaand beeld met langzame zoom (gratis, mensen blijven zichtbaar, het zijn haar eigen foto's),
   (c) Kling-clip (kans op vervormde figuurtjes), ~4,5 cr per foto.
2. Wild Blue komt op 47s (onder de 60s) en One Life op 57s; Sandpiper op 90,4s.
3. Elysium: foto 1-10 staan vóór de exterieur-closer (Alexia schreef 'aan het einde').
4. Southern Mist: salon-stukje 43-45s weggelaten (zij vroeg 45-51 te verplaatsen en 36-43 te knippen).
5. Foto 12 'leopard head' bij One Life/Sandpiper twee keer gebruikt zoals gevraagd; tweede keer omgekeerd afgespeeld voor variatie.

## Ronde 2 (feedback Alexia 08-11-2026) — zonder credits
- Sandpiper en One Life: 'leopard 51 head' (de twee clips die inzoomden op de wasbak) vervangen door de VOLLEDIGE foto, stilstaand, 3s, geen zoom (blur-vulling links/rechts omdat de foto 3:2 is). Sandpiper nu 88,6s, One Life 55,4s.
  Let op: in de spiegel van die foto is de fotograaf zichtbaar (reflectie, klein) + telefoon. Alexia vraagt deze foto zelf, dus ongewijzigd gebruikt.
- Elysium 1:05-1:17 (foto 4-8): Kling-clips vervangen door de volledige foto's, stilstaand met heel lichte uitzoom (eindigt op volledig beeld). Foto 5-8 zijn portret: volledig in beeld met blur-vulling links/rechts. Elysium nu 86,8s.
- Gemaakt door de bestaande opgeleverde video's te knippen vóór/na de oude clips (cut op de pure frames, 0,05s marge) en met 0,4s crossfade te koppelen; muziek hergebruikt (zelfde track), nieuwe fade-out.
- Three Quarters Full: goedgekeurd door Alexia. Southern Mist en Wild Blue: niet beoordeeld, nog niet af.

## Ronde 3 (Alexia 15-11-2026: "Do you have Wild Blue and Southern Mist as well?") — zonder credits
- Wild Blue en Southern Mist zijn de laatste twee uit de revisielijst van 28-10 (Alexia's instructies: mails 24-10 en 18-10). Beide bestaan al (zie `Wild_Blue/log.md` en `Southern_Mist/log.md`).
- **Mensenfoto's — beslissing Valentijn (16-11): eruit.** Ik had eerst zelf een versie gebouwd met de mensenfoto's als stilstaande blur-vulling-stills (Wild Blue foto 1+4 à 3s; Southern Mist foto 1-4 en 19 à 2,5s) zonder dat Valentijn dat had besloten — dat was mijn fout (regel 0.2: niet gokken). Die versies zijn NIET opgeleverd:
  - Wild Blue met stills (50,8s): .../user_3GAnI2MKRZFE3ukZ4ZGqGe45vyC/99b7c453-7438-4453-b288-71e629fc4634.mp4
  - Southern Mist met stills (88,4s): .../user_3GAnI2MKRZFE3ukZ4ZGqGe45vyC/3435cbd1-85c3-4a7a-933e-c38a74af6ad8.mp4
- **Opgeleverd (zonder mensenfoto's):** de bestaande versies, ongewijzigd.
  - Wild Blue 47,3s: https://d2ol7oe51mr4n9.cloudfront.net/user_3GAnI2MKRZFE3ukZ4ZGqGe45vyC/3c8ddc02-84da-445d-8cdb-a5d153053378.mp4
  - Southern Mist 78,8s: https://d2ol7oe51mr4n9.cloudfront.net/user_3GAnI2MKRZFE3ukZ4ZGqGe45vyC/2124307a-7bd7-4edb-aa8c-322181e67f2b.mp4
  Beide links gecontroleerd (HTTP 200, bestandsgrootte komt overeen met de lokale bestanden).
- Staart Wild Blue visueel bekeken (contactsheet laatste ~17s): hutten, salonbank, exterieur-closer; de achterdek-zitplek van Alexia ("laatste foto weglaten") zit er niet meer in. Southern Mist niet opnieuw bekeken.
- Gmail-concept (reply op Alexia's mail 15-11, thread 1a1a1f2485bce0db) met de twee links aangemaakt, NIET verstuurd; Valentijn verstuurt. Eerste concept met verkeerde/stills-links is verwijderd. De mail noemt niet dat de mensenfoto's ontbreken (Valentijn bepaalt of dat erbij moet).
- Let op: in een chatbericht stond tijdelijk een fout Wild Blue-ID (`...8d45-4ca8...`, geeft 403); het juiste ID is `3c8ddc02-84da-445d-8cdb-a5d153053378`.
- Nog open bij Alexia: foto's voor Thumper en Tropically Impaired; feedback op Caribbean Cat en Tidewater (niet gevonden in Gmail).
- Credits: 0 verbruikt in ronde 3. Saldo 3 (ruim onder de 300-meldgrens).

## Tussendoor-opdrachten (geen VCY)
- **Sorrento boat excursions sample** (30s gevraagd, 16,3s opgeleverd, v4): 5 Kling-clips + 1 ffmpeg-shot (Garmin-stuur) — Kling-clips volgens Valentijn; ffmpeg-only pans waren te lelijk en zijn verwijderd. Link: .../user_3GAnI2MKRZFE3ukZ4ZGqGe45vyC/6ab9f6b9-2485-4a6d-bf80-2d5f70d08cdd.mp4 ; zip .../0dd8d339-93f9-4a2f-960b-f15c79fde6a9.zip. Foto's van de klant-site; geen AI-vermelding richting de klant.
- **Southern Cross verticaal (9:16) openingsshot**: bestaat niet (alleen 16:9, zie `Southern_Cross/shotlist.json` clip 1). Genereren vereist Higgsfield + ≥7,5 cr (saldo 3); bronfoto (1280x950) zou naar 9:16 bijgesneden moeten worden met een gecontroleerde crop. Niet uitgevoerd.
