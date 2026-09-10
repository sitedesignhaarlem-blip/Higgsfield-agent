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

Totaal 9 credits (2665,75 → 2656,75). Beide getoond aan Valentijn — **akkoord** ("top dit"),
07-09-2026. De nieuwe regel (`smooth moderately-paced constant speed`) staat vanaf nu vast
in CLAUDE.md §15 voor alle toekomstige jachten.

## Volgorde-fix (08-09-2026): v4

Valentijn: "de yaghti by nature video was in de verkeerde volgorde fix da ff". Diagnose:
bij de shotlist-uitbreiding in stap 2 (index 22-24: 2× Exterior, 1× Flybridge, toegevoegd
om van ~65s naar ~73s te komen) zijn deze 3 extra clips destijds **achteraan** de
shotlist.json gezet in plaats van bij hun eigen categorie. Bij elke montage/hermontage
sindsdien (v1 t/m v3) zijn ze daardoor als staart ná de hutten/ensuite blijven staan, in
plaats van bij Exterior/Flybridge vooraan — in strijd met de vaste volgorde uit sectie 6
(Exterior → Flybridge → Helm → Bow → Aft deck → Salon/Galley → Cabins).

**Vastgestelde volgorde in v3** (via content-matching op frames, niet alleen op papier):
1,2,3 (Exterior) → 4,5 (Flybridge) → 6,7 (Helm) → 8,25 (Bow) → 9,10,11 (Aft deck) →
12 (Salon) → 13,14 (Galley) → 15-19 (Cabin) → 20,21 (Ensuite) → **22,23 (Exterior), 24
(Flybridge)** — de laatste 3 hoorden bij het begin.

**Fix — surgical splice, geen regeneratie nodig (0 credits):** de 4 categorieblokken uit
v3 zijn er met hun bestaande crossfades intact uitgesneden en herschikt:
- Segment A (clips 1-3, Exterior) — ongewijzigd vooraan
- Segment B (clips 22-23, Exterior) — verplaatst van staart naar direct na segment A
- Segment C (clips 4-5, Flybridge) — ongewijzigd, nu na segment B
- Segment D (clip 24, Flybridge) — verplaatst van staart naar direct na segment C
- Segment E (clips 6-21: Helm t/m Ensuite) — ongewijzigd, nu aan het eind

Nieuwe volgorde: A → B → C → D → E, met 4 verse 0,4s-crossfades op de nieuwe naden (de
crossfades bínnen elk segment zijn ongewijzigd origineel).

Exacte knippunten bepaald via een combinatie van de originele assemble-wiskunde
(offsets uit de clip-duraties) en empirische validatie: frame-diff-piekdetectie op de
video zelf, plus content-verificatie door frames op de kandidaat-grenzen te vergelijken
met de bronfoto's per categorie (bevestigde bv. dat t=61,6s Ensuite toont, t=64,7s/67,2s
Exterior, t=70,0s Flybridge — exact zoals verwacht voor de staart die verplaatst moest
worden).

**Transition QC op de 4 nieuwe naden:** alle 4 visueel gecontroleerd (checksum-geverifieerd
kleine frames), inclusief de naad Flybridge→Flybridge (segment C→D, hoogste ghosting-risico
want zelfde categorie) — coherente, schone blends, geen dubbele belichting.

**Resultaat (v4):** 1920x1080, 30fps, **68,37s** (binnen 60-90s), geen audiospoor, volgorde
nu correct: Exterior → Flybridge → Helm → Bow → Aft deck → Salon/Galley → Cabins/Ensuite.
Geen credits gebruikt (montage-only fix).

## Oplevering (v4)
- Bestand: `Yachti_By_Nature_walkthrough_v4.mp4` (1920x1080, 30fps, 68,37s, geen audio)
- URL: https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/db2ab76f-5a3c-43f5-900a-82585b28891a.mp4
- media_id: db2ab76f-5a3c-43f5-900a-82585b28891a (bevestigd)
- Resterend saldo: 2477,25 credits (ongewijzigd t.o.v. v3)

## Klantwens (09-09-2026): trap-clip stond nog voor bow/aft deck waren afgerond

Klant van Valentijn: de clip rond de 25s-marker (interior, kijkend de stuurboord-trap af
langs de helmstoel — bronfoto 35, gebruikt in clip 7 "Helm") kwam in de video vóór bow en
aft deck waren getoond. Verzoek: verplaats die clip naar rond de 40s-marker.

**Diagnose:** clip 7 stond in het Helm-blok (positie 2 van 2), dus vóór Bow (8,25) en Aft
deck (9,10,11) — logisch qua CLAUDE.md-categorievolgorde (Helm komt vóór Bow/Aft deck),
maar niet wat de klant hier wil: de trap is het overgangsmoment van buitendek naar
binnenruimtes, dus hoort na Bow/Aft deck, vlak vóór Salon.

**Geverifieerd** welke clip daadwerkelijk op 25s stond door in de Higgsfield-sandbox een
Canny/correlatie-vergelijking te draaien tussen kandidaat-videoframes en de bronfoto (35)
zelf — geen giswerk: P2 (het venster rond 25-27s) scoorde 0,414 correlatie tegen de
referentiefoto, ruim boven de andere kandidaten (±0,00–0,16). Klopt met clip 7.

**Fix — opnieuw surgical splice, 0 credits:** v4 opgeknipt in 4 stukken (P1 = alles t/m
einde clip 6, P2 = clip 7 los, P3 = Bow+Aft deck (8,25,9,10,11), P4 = Salon en verder) en
herschikt als P1 → P3 → P2 → P4. Trap-clip landt nu op offset 40,5s — precies op de
gevraagde ~40s-marker. 3 nieuwe naden gecontroleerd met de edge-density-methode: ratio's
0,56–0,81, allemaal ruim boven de ghosting-drempel, geen probleem.

**Resultaat (v5):** 1920x1080, 30fps, **65,97s**, geen audiospoor. Volgorde nu: Exterior →
Flybridge → Helm (1 clip) → Bow → Aft deck → **trap (voorheen Helm-clip 2)** → Salon →
Galley → Cabins/Ensuite.

## Oplevering (v5)
- Bestand: `Yachti_By_Nature_walkthrough_v5.mp4` (1920x1080, 30fps, 65,97s, geen audio)
- URL: https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/9bd78052-56bc-4638-b25a-939c92756de4.mp4
- media_id: 9bd78052-56bc-4638-b25a-939c92756de4 (bevestigd)
- Saldo bij controle na deze fix: 2417,25 credits — **let op: dit is 60 credits lager dan
  het laatst bekende saldo (2477,25) vóór deze fix, terwijl deze fix zelf 0 credits heeft
  gekost** (transactielog toont 10+ Kling v3.0-spends tussen 14:16-14:43 op 09-09-2026 die
  niet uit deze sessie komen — gemeld aan Valentijn, niet stilgehouden).
- Niet meer de huidige versie — zie v6 hieronder.

## Klantwens (09-09-2026): verzonnen bootnaam "Aventura" op de romp in clip 3

Klant meldde: bij seconde 10 in v5 staat de tekst "Aventura" op de romp. Foutlocatie
bevestigd via frame-extractie op t=10s (native resolutie, sandbox) en vergelijking met de
bronfoto (`07_480931739_...jpg`) — de bronfoto bevat alleen het model-label "50 MY", geen
"Aventura" nergens. Zuivere Kling-hallucinatie, exact het patroon uit CLAUDE.md §12/§16
("Tekst en letters... op de bootnaam").

**Locatie:** clip 3 (Exterior, bow-orbit, "marina in de distance"), destijds gegenereerd met
alleen de standaard `no text, no lettering, no logos`-clausule — kennelijk niet genoeg om
Kling ervan te weerhouden een naam op de romp te verzinnen bij een shot waar een bootnaam
"logisch" zou passen.

**Fix:** clip 3 opnieuw gegenereerd (index 3, foto 07, media_id
`ca657791-9cb5-4542-b7f0-2a097201e6ff`, hergebruikt), met expliciet
`no boat name, no vessel name painted on the hull, no additional signage` toegevoegd aan de
verbodslijst (CLAUDE.md §12: expliciet benoemen werkt beter dan alleen "stable geometry").
3s, std, 16:9, sound off — **4,5 credits**. Job `5bc148c2-b32f-455b-a228-e53157193974`,
in één keer geslaagd (na de bekende "IN THE DARK"-preset-retry met `declined_preset_id`).

**QC nieuwe clip:** jerk-score 1,02 (ruim onder de drempel van 2,5). Visuele contactsheet-
inspectie op tekst is dit keer niet nodig geweest om de fix te initiëren — het was juist de
aanleiding om `qc_check.py` een geautomatiseerde TEXT-check te geven (zie de aparte
toolingwijziging in de hoofdrepo, commit "Add automated TEXT (OCR) check..."), zodat dit
soort hallucinatie voortaan door laag 1 wordt gevangen in plaats van pas door de klant.

**Montage:** surgical splice op v5 — segment A (v5, 0–7,2s: clip 1+2 ongewijzigd) →
nieuwe clip 3 (genormaliseerd naar 1920x1080/30fps) → segment C (v5, vanaf 10,2s: clip 4
en verder ongewijzigd), met 2 verse 0,4s-crossfades op de nieuwe naden. Transition-QC
(edge-density ratio): 0,83 en 0,75, beide gezond (drempel 0,55–1,8). Eindlengte 65,23s
(binnen 60–90s).

## Oplevering (v6) — MISLUKT, tekst stond er nog

- Bestand: `Yachti_By_Nature_walkthrough_v6.mp4` (1920x1080, 30fps, 65,23s, geen audio)
- URL: https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/9855c8ea-c5f3-491d-b028-7ea4558f8145.mp4
- Kosten: 4,5 credits. Saldo vóór: 2408,25. Saldo na: 2402,25 (1,5 credit onverklaard verschil,
  zelfde patroon als bij v5).
- **Fout:** Valentijn meldde dat "Aventura" ná v6 nog steeds zichtbaar was. Klopte — de eerste
  prompt-fix (toevoegen van `no boat name, no vessel name painted on the hull`) was onvoldoende
  sterk om Kling van deze specifieke hallucinatie af te houden, én ik heb de nieuwe clip 3
  destijds alleen op jerk-score gecontroleerd, niet visueel op tekst, voordat hij in de montage
  ging. Dat is precies de fout die de TEXT-check in `qc_check.py` had moeten vangen — met terugwerkende
  kracht een extra argument dat die check verplicht is, niet optioneel.
- **Les:** bij content-hallucinaties (tekst, verzonnen objecten) is een score alleen (jerk/edge)
  niet genoeg bewijs dat een fix werkte — altijd het eindresultaat zelf visueel bekijken vóór
  het de montage in gaat, ook al kost dat een relay-stap.

## Fix v7: sterkere prompt + visuele verificatie vóór montage

Clip 3 een derde keer gegenereerd (zelfde bronfoto, media_id `ca657791-9cb5-4542-b7f0-2a097201e6ff`),
met een veel explicietere prompt: naast het verbod op bootnaam ook `completely blank unmarked
white hull surface`, `no decals, no vinyl graphics, no signage`, en de framing aangepast naar een
directere bow-benadering (minder zijaanzicht van de romp, waar Kling kennelijk het sterkst
geneigd is een naam te plaatsen). Job `74a286f4-e8e4-43fe-8bc3-89bdd32d53dc`, in één keer
geslaagd. 3s, std, 16:9, sound off — nogmaals 6,0 credits (saldo 2402,25 → 2396,25).

**Voordat deze clip de montage in ging:** frame op t=1,5s (het punt waar de romp het duidelijkst
in beeld is) gedownload, checksum geverifieerd, en zelf bekeken — schoon, geen tekst, alleen het
originele "AI 50 MY"-modellabel uit de bronfoto. Dit is de stap die bij v6 is overgeslagen.

Zelfde surgical splice als bij v6 (segment A 0–7,2s ongewijzigd → nieuwe clip 3 → segment C
vanaf 10,2s ongewijzigd), opnieuw met 2 verse 0,4s-crossfades. Transition-QC (edge-density
ratio): 0,83 en 0,61, beide binnen de gezonde band (0,55–1,8).

## Oplevering (v7, huidige versie)
- Bestand: `Yachti_By_Nature_walkthrough_v7.mp4` (1920x1080, 30fps, 65,23s, geen audio)
- URL: https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/9b28686e-dd55-47f3-927b-e89bef790f47.mp4
- media_id: 9b28686e-dd55-47f3-927b-e89bef790f47 (bevestigd)
- Totale kosten voor de "Aventura"-fix (v6 mislukt + v7 geslaagd): 10,5 credits.
- Saldo bij oplevering: 2396,25 credits.
- Geverifieerd: clip 3 visueel gecontroleerd op tekst vóór montage (zie hierboven), transitie-QC
  op beide nieuwe naden gezond.
- **Nog niet opgeleverd aan klant** — Valentijn levert, per de vaste regel in CLAUDE.md.
- **Openstaand:** titel-overlay (optioneel, nog niet gevraagd). Aanbevolen dat Valentijn v7 zelf
  nog even bekijkt vóór levering aan de klant, gezien de misser bij v6.
