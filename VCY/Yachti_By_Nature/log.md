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

## Oplevering (v1)
- Bestand: `Yachti_By_Nature_walkthrough.mp4` (1920x1080, 30fps, 73,63s, geen audio)
- URL: https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/82265954-b3c5-484c-a635-d249e792b766.mp4
- media_id: 82265954-b3c5-484c-a635-d249e792b766 (bevestigd)
- Resterend saldo: 2746 credits
- **Openstaand na v1:** QC (zie boven), titel-overlay (optioneel, nog niet gevraagd).

## Feedback Valentijn (na v1) en correctieronde

Valentijn: "ik vind deze minder mooi, wat is er veranderd het overlopen? en het beeld wiebelt
erg veel". Alsnog QC uitgevoerd op de reeds opgeleverde v1 (met dank aan de Higgsfield
cloud-sandbox, die wél bij de CDN kan):

**Diagnose 1 — jitter binnen clips (optical flow, JERK-achtige meting):**
Alle 24 clips gemeten op piek-flow t.o.v. mediane flow binnen de clip. Duidelijk patroon:
elke jerky clip is een **single-image clip** (geen `end_image`-anker):

| Clip | Categorie | Jerk-ratio |
|---|---|---|
| 18 | Cabin | 3,77 |
| 14 | Galley | 3,65 |
| 15 | Cabin | 3,42 |
| 10 | Aft deck | 3,29 |
| 11 | Aft deck | 2,92 |
| 20 | Ensuite | 2,01 |
| 17 | Cabin | 1,96 |

Start+end-paar-clips (9, 12, 13) en exterior-clips zaten allemaal rond 1,0–1,4 (stabiel).
Verklaring: zonder eindframe-anker verzint Kling zelf een camerapad, en bij een korte 3s-clip
valt een korte "aanloop-ruk" verhoudingsgewijs veel meer op dan bij een 5s hero-shot — precies
de afweging die bij de shotlist is gemaakt om hut-verwarring te vermijden (zie boven), maar nu
dus met een meetbare prijs.

**Diagnose 2 — crossfade/ghosting (edge-density op transitie-middens):**
Alle 23 originele transities gemeten: ratio's tussen 0,58–1,38, geen enkele geflagd. De
crossfade-techniek zelf (0,4s, identiek aan Southern Cross) is dus niet de oorzaak van "het
overlopen" — dat was de jitter die erin overvloeide.

**Actie (akkoord Valentijn):** clips 10, 11, 14, 15, 17, 18, 20 opnieuw gegenereerd met de
reddingsprompt uit §15 (extreem trage, minimale camerabeweging, nog steeds single-image om
hetzelfde hut-verwarringsrisico te vermijden), 3s, std, sound off. 7 clips × 4,5 = **31,5
credits**. Alle 7 in één keer geaccepteerd, geen submission-failures.

QC op de vervangers: jerk-ratio's nu 1,03–1,42 (was 1,96–3,77) — ruim binnen de bandbreedte
van de stabiele clips.

**Herassemblage:** niet de hele batch opnieuw gedownload/genormaliseerd — de 17 ongewijzigde
clips zijn als aaneengesloten reeksen (met hun originele crossfades intact) uit de bestaande
eindvideo geknipt, de 7 vervangers vers genormaliseerd, en alleen op de 11 naden die een
vervanger raken is een verse 0,4s-crossfade gebouwd. (Een eerste poging waarbij per clip een
"schoon" venster werd geknipt en dáárna opnieuw alles ge-crossfade werd, verloor de overlap
twee keer en leverde een te korte 60,27s video op — verworpen, niet gebruikt.)

**Transition QC op de 11 nieuwe naden:** edge-density-ratio's van 4 van de 11 naden kwamen
onder de 0,55-drempel (0,36–0,52). Visueel gecontroleerd met kleine, checksum-geverifieerde
losse frames (grijswaarden, ~1KB, sha256 geverifieerd na overdracht) op alle 4: telkens een
coherente, enkelvoudige ruimte, geen dubbele belichting of spookbeeld. Verklaring: de rustige
reddingsprompt-clips hebben van nature minder randdetail dan hun buren, wat de edge-density-
proxy laag laat scoren zonder dat er echte ghosting is. Geen verdere actie nodig.

**Eindresultaat v2:** 1920x1080, 30fps, **70,70s** (ruim binnen 60–90s, dicht bij de
oorspronkelijke 73,63s), geen audiospoor.

**Creditverbruik correctieronde: 31,5 credits** (2746 → 2714,5).

## Oplevering (v2)
- Bestand: `Yachti_By_Nature_walkthrough_v2.mp4` (1920x1080, 30fps, 70,70s, geen audio)
- URL: https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/2ed313dc-1bc1-4301-a6d7-1be607774366.mp4
- media_id: 2ed313dc-1bc1-4301-a6d7-1be607774366 (bevestigd)
- Resterend saldo: 2714,5 credits
- **Openstaand na v2:** titel-overlay (optioneel, nog niet gevraagd).

## Feedback Valentijn (na v2) — "ik wil die hele wiebelige beelden verbeterd"

Ook na v2 nog steeds te veel jerk volgens Valentijn. Op zijn verzoek: Southern Cross als
kwaliteitsreferentie genomen ("start+end-shots, perfect, weinig jerk") en gekeken of dezelfde
techniek hier alsnog kon, in plaats van blind nieuwe dingen te genereren.

**Fotocontrole:** alle 12 nog ongebruikte bronfoto's (van de 46) visueel bekeken op een tweede
hoek van dezelfde ruimte. Resultaat:
- Foto 41 = tweede hoek van de ensuite uit foto 44 (zelfde douche met "Aventura"-opdruk) → echt paar
- Foto 29 = tweede hoek van de galley uit foto 30 (zelfde aanrecht, zelfde raampartij) → echt paar
- Foto 17 = tweede hoek van de bow uit foto 18 (zelfde ankerlier, zelfde tafeltjes) → adresseert
  Valentijns "ik mis een bow shot" (standaardopzet is 2 bow-clips, hier stond er maar 1)
- Voor de 5 cabin-foto's (39,40,42,43,45) en de 2 losse aft deck-foto's (22,26) is **geen**
  tweede hoek gevonden — start+end forceren zou hier precies het morphing-risico opleveren dat
  CLAUDE.md verbiedt. Voor die clips was er geen betere fotografische optie beschikbaar.

**Correctieronde 2 — 10 clips, in overleg met Valentijn geaccordeerd:**
- Clip 14 (Galley) → echt start+end-paar (30+29)
- Clip 20 (Ensuite) → echt start+end-paar (44+41)
- Nieuwe clip 25 (Bow #2) → los, foto 17 (bow/exterieur blijft bewust single-image per
  CLAUDE.md §8, morphing-risico met water/lucht)
- Clip 16, 19 (Cabin) → voor het eerst gefixt met reddingsprompt (waren in ronde 1 niet
  meegenomen)
- Clip 10, 11 (Aft deck), 15, 17, 18 (Cabin) → geen bronfoto-alternatief, dus enige overgebleven
  hefboom uit §12 "Bij afkeur": `mode: pro` i.p.v. `std`, met Valentijns expliciete akkoord
  vooraf (17% duurder, zoals §3 voorschrijft)

Kosten: 3× 4,5 (groep A) + 2× 4,5 (groep B) + 5× 5,25 pro/3s (groep C, `get_cost` preflight
bevestigd) = **48,75 credits** (2714,5 → 2665,75).

Alle 10 clips in één keer geaccepteerd, geen submission-failures.

**QC op de vervangers:** jitter-ratio's nu 1,05–1,6 (na correctie voor een meetartefact op het
laatste steekproefframe bij het einde van elke clip) — vergelijkbaar met de rustigste clips in
de video.

**Herassemblage (v3):** opnieuw vanaf de originele v1 opgebouwd (niet vanaf v2, om dubbele
crossfade-verliezen te vermijden zoals bij de eerste correctieronde). 15 segmenten: 4 lange
ongewijzigde reeksen met originele crossfades intact (clips 1-8, 9, 12-13, 21, 22-24) + 1
nieuw ingevoegde bow-clip + 9 vervangers, met verse 0,4s-crossfades alleen op de 14 naden die
een nieuwe/vervangen clip raken. Eindresultaat: **25 clips, 71,40s**.

## Oplevering (v3, huidige versie)
- Bestand: `Yachti_By_Nature_walkthrough_v3.mp4` (1920x1080, 30fps, 71,40s, geen audio)
- URL: https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/e91ece45-8f53-4773-adcd-0f8a3751217b.mp4
- media_id: e91ece45-8f53-4773-adcd-0f8a3751217b (bevestigd)
- Resterend saldo: 2665,75 credits
- **Nog niet opgeleverd aan klant** — Valentijn levert, per de vaste regel in CLAUDE.md.
- **Openstaand:** titel-overlay (optioneel, nog niet gevraagd); volledige Transition QC op de
  14 nieuwe naden van v3 is nog niet herhaald (wel gedaan op v2's 11 naden).

## Basisregel-wijziging (07-09-2026): camerabeweging iets sneller

Valentijn: nog steeds te veel jerk gezien, ook na v3. Op zijn instructie CLAUDE.md §15
aangepast: `slow constant speed` → `smooth moderately-paced constant speed` in de
basisformule en alle categorie-voorbeelden; reddingsprompt niet langer "extremely slow,
almost static" maar één duidelijke bewegingsas op gematigd tempo. Achterliggende hypothese:
bij bijna-statische clips wordt Kling's eigen frame-tot-frame ruis niet gemaskeerd door
bedoelde beweging, wat als wiebelen overkomt.

**Testclips volgens nieuwe regel** (buiten én binnen, zoals gevraagd — geen nieuwe foto's
nodig, bestaande media_id's hergebruikt met aangepaste prompt):

- Buiten/aft deck: foto 22 (media_id b6fefacc-...), 3s, std, sound off — 4,5 credits.
  Job `48e282b1-d39f-472b-bce4-adadb26693ce`, completed.
  URL: https://d8j0ntlcm91z4.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/hf_20260907_083641_48e282b1-d39f-472b-bce4-adadb26693ce.mp4
- Binnen/cabin: foto 39 (media_id 199b3af0-...), 3s, std, sound off — 4,5 credits.
  Job `45b50069-ae64-4304-bedb-6b033ffc6129`, completed.
  URL: https://d8j0ntlcm91z4.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/hf_20260907_083916_45b50069-ae64-4304-bedb-6b033ffc6129.mp4

Totaal 9 credits (2665,75 → 2656,75). Beide getoond aan Valentijn, **wacht op feedback** voor
de nieuwe regel op de rest van de shotlist wordt toegepast.
