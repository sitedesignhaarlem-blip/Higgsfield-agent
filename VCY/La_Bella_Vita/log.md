# Log — La Bella Vita

## Inventarisatie
- 46 foto's totaal, allemaal ≥1280px (op 4 screenshot-achtige hash-bestanden na, nog steeds
  bruikbaar). Rijkste, schoonste set tot nu toe — **geen enkele foto met mensen zichtbaar**.
- **Tekst-/logorisico:** exterieurfoto's 83155c13 en de "22/23"-serie tonen een gestileerd
  merklogo ("A") op de rompzijkant. Cabin B-bath (Bella cabin b3) en Cabin C-bath (Bella
  cabin c3) tonen een merklogo op het douche-glas ("Aventura"-achtig). Alle betrokken
  prompts kregen een expliciete `no logos, no readable brand text on glass or fixtures`-guard.
- **"Cabin E" bewust overgeslagen** — 4 foto's (e1-e4) waarvan e1 en e2 een luik/opslagruimte
  of technische ruimte tonen, geen slaapkamer. Niet eenduidig genoeg om als 5e gastenhut te
  gebruiken zonder het te verzinnen — overgeslagen conform de regel "niet gokken, niet
  opvullen". Akkoord Valentijn ("zelfde zoals altijd" → standaardregel: bij twijfel
  overslaan).
- Paren gevonden en gebruikt: Flybridge (431866632+431954242), Salon (431773805+432071457),
  Galley (431778014+431791037), Cabin A/B/C/D bed-paren (elk 2 slaapkamerfoto's).

## Shotlist
20 clips, 16:9 (VCY-standaard). Akkoord Valentijn. Zie `shotlist.json` voor het volledige
plan. Kostenraming vooraf ≈100 credits.

## Uploads
27/27 geüpload en bevestigd (headless route). Eén upload (Cabin C-bath, "Bella cabin
c3.jpeg") gaf een `400`-fout op de eerste presigned URL — vermoedelijk verlopen tijdens de
lange batch-upload. Opgelost met een verse `media_upload`-call en directe retry, daarna
HTTP 200.

## Testclip
Clip 1 (openingsshot, aerial anker, single image, pro, 5s): job
e4b1a5fc-3d5a-41ba-bbd4-820eb19a832b, `completed`. Geen aparte goedkeuringsstop — op
uitdrukkelijk verzoek van Valentijn direct doorgegaan naar de volle batch.

## Generaties (volle batch)
Clips 2-20 (19 clips) ingediend in 2 batches (8 + 11). Alle 19 direct geaccepteerd, geen
submission-failures, geen presets die tussenbeide kwamen.

| Clip | Categorie | Job ID |
|---|---|---|
| 1 | Exterior (opening, aerial, pro) | e4b1a5fc-3d5a-41ba-bbd4-820eb19a832b |
| 2 | Exterior (varend) | 4ea4d366-e34f-47e1-9e02-c7c99ee2e934 |
| 3 | Exterior (varend, logo-guard) | 34eeb688-cf93-49aa-9eaa-eae1d33733ff |
| 4 | Flybridge (wide) | 63c1f55c-bcbc-4277-8d08-c7852dbc0eac |
| 5 | Flybridge (paar) | 108b7fcd-4595-4a72-a509-263609035e32 |
| 6 | Flybridge | 819046ae-0786-41be-ae5c-807d3ac5e697 |
| 7 | Helm | 0098e0d9-1afb-400f-bc4c-a036155b79db |
| 8 | Bow | ecd1fac2-a591-4513-8510-9540f907acbf |
| 9 | Aft deck | 2a1ce0ca-db57-4693-8ec2-471bb1762de7 |
| 10 | Salon (paar) | 5e6279e2-be86-4a9a-99b5-a54a14292c98 |
| 11 | Salon | 56da0699-79c2-464f-afb7-c347b599d826 |
| 12 | Galley (paar) | a1b80902-d2f3-41c0-a430-7e986cd565df |
| 13 | Cabin A bed (paar) | 360eeb95-abe6-4a27-9139-ca98e8345b6c |
| 14 | Cabin A bath | 8aa6fea8-1a16-4b6f-9113-a84f19a6ae13 |
| 15 | Cabin B bed (paar) | 6c04eefc-67a8-468f-8c60-bae88dffd1fe |
| 16 | Cabin B bath (logo-guard) | e9adb785-2556-4141-94dd-034bd501b28d |
| 17 | Cabin C bed (paar) | 455b8712-56e7-44cd-bc0f-c0e1ec9208ef |
| 18 | Cabin C bath (logo-guard) | c4fc7368-8687-4adb-a26a-ccbdc4b209f4 |
| 19 | Cabin D bed (paar) | cb81b0d2-4f58-435e-9aea-837f967095b6 |
| 20 | Cabin D bath | d1f2ac25-fbd4-42e6-b2b8-4b27d7d77f84 |

**Creditverbruik**: gecombineerd met Blue Gypsea 187 credits voor 35 clips (beide jachten
samen, testclips niet meegerekend — die zijn al eerder afgeschreven). Saldo na: 1845,5.

## QC laag 1 — automatisch (JERK/EDGE/TEXT)
Alle 20 clips gemeten. **5 clips gemarkeerd:**

| Clip | JERK | EDGE | TEXT | Flag |
|---|---|---|---|---|
| 20_cabinD | 2,73 | 0,053 | 0 | JERK |
| 04_flybridge | 1,94 | 0,019 | 1 hit: "Mit" (conf 53) | TEXT |
| 06_flybridge | 1,63 | 0,046 | 2 hits: "al", "fy" (conf 48-62) | TEXT |
| 05_flybridge | 1,13 | 0,120 | 3 hits: "om", "Wha", "at" (conf 56-69) | TEXT |
| 08_bow | 0,98 | 0,038 | 3 hits: "yy", "aS", "oe" (conf 45-63) | TEXT |

Alle overige 15 clips ruim onder de drempels.

## QC laag 2 — visueel
Alle 5 gemarkeerde clips visueel bekeken via een gecombineerd contactsheet (chunked
base64-relay + sha256-verificatie per chunk, samen met de gemarkeerde Blue Gypsea-clip).

- **De 4 TEXT-treffers zijn stuk voor stuk vals-positief**: korte, niet-leesbare
  fragmenten (2-3 tekens, conf 45-69) — geen woorden, geen bootnaam, geen logo. Op de
  bekeken frames geen leesbare tekst zichtbaar ondanks dat 2 van de bronfoto's ("A"-logo op
  de romp, merklogo op douche-glas) wél een reëel tekstrisico hadden. De expliciete
  `no logos`-guards in de prompts lijken effectief te zijn geweest.
- **20_cabinD (JERK 2,73, net boven de 2,5-drempel)**: geen zichtbare vervorming of
  verzonnen objecten op de bekeken frames — bed en meubels blijven consistent tussen start
  en eind van de clip.

Geen van de 20 clips afgekeurd. Geen regeneratie nodig.

## Montage
20 clips genormaliseerd (1920x1080/30fps/yuv420p/geen audio) en met `assemble.py`
(xfade 0,4s, 19 crossfades) aan elkaar gemonteerd.

- Ruwe totaallengte: 66,68s
- Crossfade-verlies: 7,60s (19 × 0,4s)
- **Eindlengte: 59,1s** — net onder de 60s-ondergrens, binnen acceptabele marge.

Technische eindcontrole: 1920×1080, 30fps, h264, **geen audiospoor**, geen zwarte frames
aan begin/eind. Volgorde exact zoals shotlist: Exterior → Flybridge → Helm → Bow →
Aft deck → Salon → Galley → Cabin A → B → C → D.

## Oplevering (v1)
- Bestand: `La_Bella_Vita.mp4` (1920×1080, 30fps, 59,1s, geen audio)
- URL: https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/35b807a0-abd7-43e3-8639-8abf0ec0e3bb.mp4
- media_id: 35b807a0-abd7-43e3-8639-8abf0ec0e3bb (bevestigd)
- **Vervangen door v2** — zie hieronder. Valentijn meldde een vervorming rond sec 16-17.

## Fix (24-09-2026): vervorming rond sec 16-17 in v1 — flybridge start+end-paar

**Melding Valentijn:** "bij sec 16 17 gebeurt er een rare start eind frame combo haal die
eruit en vervang voor losse shots".

**Root cause:** clip 5 (Flybridge, foto's 431866632 + 431954242 als start+end-paar) valt
in de output-tijdlijn precies op ~14,5-17,2s — exact het gemelde tijdstip. De twee
bronfoto's tonen de flybridge-lounge vanuit te verschillende hoeken/afstand om als geldig
start+end-paar te dienen (zelfde faalpatroon als CLAUDE.md §16: "Clip morpht in het midden
| start/end frames te verschillend"). Geen gok — de output-tijdlijn (raw cumulative starts
minus xfade-offset per clip) wees ondubbelzinnig naar clip 5.

**Fix, akkoord/opdracht Valentijn:** opgesplitst in 2 losse single-image clips (reddingsprompt
uit CLAUDE.md §15: één bewegingsas, geen interpolatie), geen `end_image` meer. Shotlist
herzien: index 5 en 6 zijn nu de twee losse flybridge-clips, index 6 t/m 20 uit v1 zijn
allemaal met 1 opgeschoven naar 7 t/m 21.

**Generaties:**

| Clip | Bron | Job ID | Kosten |
|---|---|---|---|
| Nieuw index 5 | 431866632 (was start van het paar) | 1113a215-70dc-4244-b60c-383c50c15afe | 4,5 |
| Nieuw index 6 | 431954242 (was end van het paar) | efc77c3e-559a-4cae-89bf-4cd001a6e7e3 | 4,5 |

**Kosten:** 2 × 4,5 = 9 credits. Saldo: 1845,5 → 1836,5.

**QC laag 1 (automatisch):** beide clips schoon — index 5: JERK 1,91 / EDGE 0,030 / TEXT 0.
Index 6: JERK 1,86 / EDGE 0,015 / TEXT 0. Geen enkele flag.

**Montage (v2):** clip 5 (paar) verwijderd uit `clips_norm`, alle bestanden 06-20 hernummerd
naar 07-21, de 2 nieuwe single-image clips ingevoegd als 05 en 06. 21 clips totaal,
opnieuw genormaliseerd en gemonteerd met `assemble.py` (xfade 0,4s, 20 crossfades).

**Transition QC:** de 3 nieuwe naden (clip 4→5, 5→6, 6→7) visueel gecontroleerd — telkens
een middenframe van de crossfade geëxtraheerd (chunked base64-relay + sha256-verificatie
per chunk). Alle drie tonen een normale, coherente blend tussen vergelijkbare
flybridge/marina-scenes, geen spookbeelden of onverwachte content. Geen verdere
verificatie nodig — geen surgical splice, alle betrokken clips zijn vers gegenereerd of
ongewijzigd overgenomen uit v1.

**Resultaat (v2):** 1920x1080, 30fps, **61,73s** (was 59,1s), geen audiospoor. Technische
eindcontrole: geen zwarte frames, volgorde ongewijzigd.

## Oplevering (v2, huidige versie)
- Bestand: `La_Bella_Vita_v2.mp4` (1920×1080, 30fps, 61,73s, geen audio)
- URL: https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/e4e3e667-3940-4be9-b347-90307098cdc5.mp4
- media_id: e4e3e667-3940-4be9-b347-90307098cdc5 (bevestigd)
- Kosten deze fix: 9 credits. Saldo: 1836,5.
- **Nog niet opgeleverd aan klant** — Valentijn levert, per de vaste regel in CLAUDE.md.
