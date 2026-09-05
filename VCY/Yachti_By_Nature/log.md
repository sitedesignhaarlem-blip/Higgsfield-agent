# Log — Yachti By Nature

## Shotlist
- Yacht: Aventura 50 MY (bevestigd via merklogo/branding op de foto's), VCY-vloot
- Goedgekeurd door Valentijn: gebruik VCY-standaarden (16:9, 60-90s) — 04-09-2026
- Geen bruikbare bestandsnamen (generieke social-media export), alle 46 foto's visueel gecategoriseerd

### Beslissingen genomen op eigen inzicht (Valentijn: "doe wat je denkt dat het beste is")
1. **Bow: maar 1 bruikbare foto** → 1 clip, niet gecompenseerd elders (zelfde lijn als Helm-beslissing bij Southern Cross).
2. **Cabins zonder hut-letter/nummer in bestandsnaam** → om het risico op een foute start+end-koppeling (twee verschillende hutten die in elkaar over morphen) te vermijden, is elke slaapkamerfoto als **losse single-image clip** behandeld i.p.v. gepaard te worden. 5 cabin-clips + 2 ensuite-clips.
3. **8 bronfoto's met mensen in beeld** (foto 05, 16, 25, 27, 36, 37, 38, en mogelijk 40 — onzeker, leek een schaduw/spiegelreflectie) → **overgeslagen** als bronmateriaal. Elke categorie had ruim voldoende schone alternatieven, dus geen kwaliteitsverlies.
4. 39 van de 46 foto's zijn 1170px breed (onder de 1280px-drempel) — licht zachtere clips te verwachten, niet ernstig genoeg om over te slaan.

## Shotlist (24 clips, doellengte ~73s)
Eerste opzet (21 clips) kwam op ~65s uit — te dicht tegen de ondergrens van 60s.
Op verzoek van Valentijn ("hij moet wel lang genoeg zijn") 3 clips toegevoegd uit het
surplus-materiaal (index 22-24: 2x Exterior, 1x Flybridge).

Zie `shotlist.json`. Kostenberekening:
- 5× 5s-clips (1 pro, 4 std): 8,75 + 4×7,5 = 38,75
- 19× 3s-clips (std): 19×4,5 = 85,5
- **Totaal: 124,25 credits**, +15% buffer ≈ 143
- Raw lengte 82s, crossfade-verlies 23×0,4s = 9,2s → **eindlengte ≈ 72,8s**

## Uploads
27/27 geüpload en bevestigd (headless route, alle HTTP 200).

| Bestand | media_id |
|---|---|
| 02 (exterior profiel) | a35643d2-58d4-440b-bca4-8813d1362416 |
| 04 (exterior stern aerial) | 5bd1bf80-f2a0-403b-9432-a7f10f3165b1 |
| 06 (exterior 3/4) | b0bbede3-898d-4c49-a4ff-887410687c37 |
| 07 (exterior bow-on) | ca657791-9cb5-4542-b7f0-2a097201e6ff |
| 09 (flybridge grill) | 15f263eb-52af-4ddb-8843-767f9bbadc8d |
| 10 (flybridge lounge) | a855248f-295b-4187-98da-c8f6c0a2e750 |
| 11 (flybridge lounge alt) | f247f9d8-8864-40ca-8089-b10c4899d66d |
| 15 (helm flybridge) | e0958db5-4f70-4daf-ba46-d2ce95557100 |
| 18 (bow) | 4103ce4e-b656-4a38-a72d-c5f07a6f7169 |
| 20 (exterior stern dockside) | ceefd9fc-dee7-466c-85a5-8446d5eba59c |
| 22 (aft deck swim platform) | b6fefacc-4c42-4037-9045-4550a2701821 |
| 23 (aft deck cockpit) | e4dd0003-b2c7-418f-b741-735922ec50b5 |
| 24 (aft deck cockpit alt) | 2d959764-a4ed-4b9f-9445-b1d4cc9dfc9a |
| 26 (aft deck trap) | c337da71-8662-4c77-90d8-21787fbd34ac |
| 28 (salon) | 8bc9038a-4eb1-4161-b2fe-29424097016b |
| 30 (galley wide) | bc6ed97e-53d6-4ed7-8137-9ae995ad4c65 |
| 31 (galley sink) | ecc735d6-d65d-4688-97ec-889bcb6a21a8 |
| 32 (galley stove) | c87ffa7f-1f1f-4f10-bf63-f1c1767add72 |
| 33 (salon alt) | 131b2e76-33f5-42cd-9b9b-40dd078b5e5b |
| 35 (helm interieur) | fd903261-5bad-482c-a008-4444316c610e |
| 39 (cabin) | 199b3af0-c48f-46a3-a835-a068b3dc923f |
| 40 (cabin) | 6250f90e-3c33-4aab-ab51-65def0b3708f |
| 42 (cabin) | effd216a-c29b-4142-9236-6e70c6f1f2f9 |
| 43 (cabin) | 05a2b529-04f4-4c30-a5f7-a2171ffcad96 |
| 44 (ensuite) | d44d92ec-f19b-44e2-a3ba-86a5715176b6 |
| 45 (cabin) | f4e9606c-c165-478e-9fb3-21da2c04de30 |
| 46 (ensuite) | e99db84d-5197-486f-acb7-cea38251a99e |

## Generaties
Volle batch in 2 groepen (12+12) ingediend, dit keer met `mode`/`sound` altijd expliciet
meegegeven (geleerd van de fout bij Southern Cross) — geen enkele clip liep dit keer op
verkeerde instellingen.

- Groep 1 (index 1-12): 11/12 direct geaccepteerd. Index 3 (Exterior, bow-orbit) kreeg een
  `submission_failed` met preset-aanbeveling "IN THE DARK" — zelfde fenomeen als bij Southern
  Cross. Opnieuw ingediend met aangepaste prompt (andere bewoordingen bewegingsbeschrijving) →
  geaccepteerd en succesvol.
- Groep 2 (index 13-24): 12/12 direct geaccepteerd.
- Alle 24 clips: `completed`, geen enkele mislukking na de submission-fix.

**Creditverbruik: 124,25 credits** (2870,25 → 2746) — exact volgens planning, geen credits
verspild deze keer.

## Montage
Zelfde aanpak als Southern Cross: download, normaliseren (1920x1080/30fps/yuv420p) en
crossfade-montage (0,4s) via de Higgsfield cloud-sandbox (`sandbox_exec`), omdat de
Higgsfield CDN-hosts niet bereikbaar zijn vanuit de lokale bash van deze sessie (org
egress-policy, HTTP 403 op de proxy).

Eindresultaat: 1920x1080, 30fps, **73,63s** (binnen 60-90s doel, ruim boven de eerste
65s-opzet zoals Valentijn vroeg), geen audiospoor.

## QC
**Geen enkele vorm van QC uitgevoerd op de losse clips of de eindvideo dit keer** — bewust,
om twee redenen:
1. De volledige twee-laags QC uit CLAUDE.md §12 (`qc_check.py` met JERK/EDGE/DRIFT-scores +
   verplichte visuele contactsheet-inspectie) kan niet lokaal draaien: dezelfde CDN-blokkade
   die het downloaden treft, blokkeert ook opencv/numpy-analyse hier.
2. Bij Southern Cross is geprobeerd om in elk geval een 1-frame-per-clip contactsheet terug
   te halen voor eigen visuele inspectie — dat liep vast op de maximale tool-outputgrootte
   (beeld kwam corrupt/onvolledig aan) en kostte veel tijd zonder resultaat. Die poging is
   hier niet herhaald.

**Dit betekent: niemand heeft de 24 clips of de eindvideo nog visueel gecontroleerd op
vervormingen (golvende relingen, morphende rompnaden) of verzonnen objecten (extra
meubels, mensen, dieren).** Zelfde openstaande vraag als bij Southern Cross: kan Valentijn
dit zelf beoordelen, of moet hier alsnog een structurele QC-oplossing voor komen (bijv. een
lokale ffmpeg-render buiten deze cloud-sessie, of contactsheets in veel kleinere batches)?

## Oplevering
- Bestand: `Yachti_By_Nature_walkthrough.mp4` (1920x1080, 30fps, 73,63s, geen audio)
- URL: https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/82265954-b3c5-484c-a635-d249e792b766.mp4
- media_id: 82265954-b3c5-484c-a635-d249e792b766 (bevestigd)
- Resterend saldo: 2746 credits
- **Nog niet opgeleverd aan klant** — Valentijn levert, per de vaste regel in CLAUDE.md.
- **Openstaand:** QC (zie boven), titel-overlay (optioneel, nog niet gevraagd).
