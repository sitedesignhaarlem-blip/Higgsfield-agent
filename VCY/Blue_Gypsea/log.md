# Log — Blue Gypsea

## Inventarisatie
- 38 foto's totaal. Meeste ≥1280px breed; 5 kleiner (800-960px: Southern-mist-2, image12/17/23,
  image4(3), image6(2), wildblue-serie) — bruikbaar, iets zachter.
- **Geen aparte Bow-foto aangeleverd** — overgeslagen, niet opgevuld met een andere ruimte.
- **Geen aparte Helm-foto** — de bestuurdersstoel staat op de flybridge zelf (single-level
  layout), dus Helm is niet als losse categorie gebruikt.
- **Niet gebruikt (mensen zichtbaar):** image12.jpeg (mensen op flybridge), image4(3).jpeg
  (mensen op dek), wildblue-11/12/13 (zonnend stel, vrouw op trampoline, arm door luik).
- **Cabin D mist een en-suite badkamerfoto** — alleen 1 slaapkamerfoto (cabin d1.jpg)
  aangeleverd. Single-image clip zonder bath-shot.
- **Tekstrisico:** foto 344202867 (exterieur bij de marina) toont goed leesbaar "BLUE GYPSEA"
  + "MY6" op de romp — meegenomen met een expliciete `no boat name`-guard in de prompt.
- Paren gevonden en gebruikt: Flybridge (344139580+344154658), Salon (343966803+344145769),
  Galley (344224139+344278896), Cabin A (a1+a3), Cabin B (b1+b2), Cabin C (c1+c2).

## Shotlist
17 clips, 16:9 (VCY-standaard). Akkoord Valentijn ("ja zelfde zoals altijd") — ~55s
eindlengte geaccepteerd ondanks minder categorieën dan gebruikelijk (vergelijkbaar met
Freedom's aanpak bij beperkt bronmateriaal). Zie `shotlist.json` voor het volledige plan.

Kostenraming vooraf: 18 clips ≈ 91 credits. Uiteindelijk 17 clips (1 exterieur-single minder
dan eerst voorgesteld) ingediend.

## Uploads
23/23 geüpload en bevestigd (headless route, `curl -X PUT -H "Content-Type: image/jpeg"`,
alle HTTP 200, geen retries nodig behalve later bij La Bella Vita cabin C-bath — zie dat
log).

## Testclip
Clip 1 (openingsshot, aerial anker, single image, pro, 5s): job
fdf6407a-c6bd-4ab5-bf0a-5e773aab6d89, `completed`. Geen aparte goedkeuringsstop — op
uitdrukkelijk verzoek van Valentijn ("geen test clips gelijk starten") direct doorgegaan
naar de volle batch.

## Generaties (volle batch)
Clips 2-17 (16 clips) ingediend in 2 batches van 12. **Clip 7 (aft deck) kreeg de bekende
"IN THE DARK"-preset-submission_failed** — opnieuw ingediend met `declined_preset_id` en
toen in één keer geslaagd. Alle overige 15 clips direct geaccepteerd, geen andere
mislukkingen.

**Creditverbruik totaal (incl. testclip): 187 credits verdeeld over Blue Gypsea + La Bella
Vita** — zie hieronder voor de exacte Blue Gypsea-portie. Saldo vóór batch: 2032,5. Saldo
na alle 37 clips (beide jachten): 1845,5.

| Clip | Categorie | Job ID |
|---|---|---|
| 1 | Exterior (opening, aerial, pro) | fdf6407a-c6bd-4ab5-bf0a-5e773aab6d89 |
| 2 | Exterior (varend) | 37a6b1bf-5795-481a-8ecc-bbe31c4a0eee |
| 3 | Exterior (marina, naam-guard) | 2a4c5ea4-38c1-43e9-8949-4ab9c64276cb |
| 4 | Flybridge (paar) | 2211a8fc-2994-49b1-a4a2-1f26de4bc684 |
| 5 | Flybridge | 21e6963c-299e-476d-8c77-89e464ee0a93 |
| 6 | Flybridge | 311d1c13-49b0-49cf-9366-b1e406b3f304 |
| 7 | Aft deck (preset-fix) | 265aab5b-fa2b-40c6-bfbc-fc7347c18d08 |
| 8 | Salon (paar) | ef53738e-2965-4d94-bff0-6e1b5bcd04e6 |
| 9 | Salon | 23dd37f6-420a-4cb0-bdc2-263f49473970 |
| 10 | Galley (paar) | f0be58f7-8de0-4777-a9a1-99ebcc89c008 |
| 11 | Cabin A bed (paar) | 45123364-d3c4-40ba-9953-2c9b57b221af |
| 12 | Cabin A bath | 40b538f8-f28c-4e09-b41f-854f4ec2fb12 |
| 13 | Cabin B bed (paar) | 11a9f321-b6c0-4f99-83cf-7c383c5a4e71 |
| 14 | Cabin B bath | 6a9fa0d6-d02e-411e-94a9-2873f178b0b9 |
| 15 | Cabin C bed (paar) | be75df5c-10d4-4bc2-bc6b-d5355532be3e |
| 16 | Cabin C bath | 3b49af3f-fee2-4438-990a-77e915ed7c75 |
| 17 | Cabin D bed (geen bath) | 993118db-be35-4906-a0a5-aac15575398e |

## QC laag 1 — automatisch (JERK/EDGE/TEXT)
Alle 17 clips gemeten. **1 clip gemarkeerd:**

| Clip | JERK | EDGE | TEXT | Flag |
|---|---|---|---|---|
| 04_flybridge | 1,04 | 0,030 | 1 hit: "ae" (conf 48) | TEXT |

Alle overige 16 clips ruim onder de drempels (hoogste JERK 2,05, hoogste EDGE 0,139).

## QC laag 2 — visueel
De TEXT-gemarkeerde clip (04_flybridge) visueel bekeken via een gecombineerd contactsheet
(chunked base64-relay + sha256-verificatie per chunk, samen met 5 gemarkeerde La Bella
Vita-clips). **Vals-positief**: de treffer "ae" is een los, niet-leesbaar 2-letter-fragment
met lage confidence (48) — geen woord, geen bootnaam. Op de bekeken frames geen leesbare
tekst, logo of ander verzonnen object zichtbaar. Waarschijnlijke bron: OCR die een
lichtreflectie of randdetail als letter-achtige vorm interpreteert.

Geen van de 17 clips afgekeurd. Geen regeneratie nodig.

## Montage
17 clips genormaliseerd (1920x1080/30fps/yuv420p/geen audio) en met `assemble.py`
(xfade 0,4s, 16 crossfades) aan elkaar gemonteerd.

- Ruwe totaallengte: 57,58s
- Crossfade-verlies: 6,40s (16 × 0,4s)
- **Eindlengte: 51,2s** — korter dan de gebruikelijke 60-90s, zoals vooraf besproken en
  geaccepteerd (geen Bow, maar 1 bruikbare Aft deck-foto, Cabin D zonder bath-foto).

Technische eindcontrole: 1920×1080, 30fps, h264, **geen audiospoor**, geen zwarte frames
aan begin/eind. Volgorde exact zoals shotlist: Exterior → Flybridge → Aft deck → Salon →
Galley → Cabin A → B → C → D.

## Oplevering
- Bestand: `Blue_Gypsea.mp4` (1920×1080, 30fps, 51,2s, geen audio)
- URL: https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/b552d088-b514-49b2-aafd-fbcc59acbca6.mp4
- media_id: b552d088-b514-49b2-aafd-fbcc59acbca6 (bevestigd)
- **Nog niet opgeleverd aan klant** — Valentijn levert, per de vaste regel in CLAUDE.md.
- Resterend saldo (na beide jachten): 1845,5 credits.
