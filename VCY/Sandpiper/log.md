# Log — Sandpiper

## Context (29-09-2026)
Baseline-versie op initiatief van Valentijn: Alexia levert geen foto's meer aan, Higgsfield-
abonnement loopt bijna af (~1715 credits beschikbaar bij start van deze batch). Doel: zoveel
mogelijk boten van de resterende VCY-vloot op een goede basis afkrijgen zodat Alexia later kan
reviewen en aanpassen. Foto's komen rechtstreeks van virgincharteryachts.com/yachts/sandpiper
(media_import_url), geen lokale kopie in photos/.

Sandpiper is de enige van de 10 resterende boten met zelf-beschrijvende bestandsnamen
(sandpiper-flybridge, sandpiper-salon1, enz.) — daardoor als enige met de normale
sectie-6/7/8-categoriepijplijn gedaan i.p.v. de vereenvoudigde baseline-aanpak die voor de
andere 9 boten gebruikt wordt (zie brief.md voor het waarom: visuele inspectie van foto's is
in deze sessie technisch onmogelijk, netwerkbeleid blokkeert alle toegang tot de VCY-site en
Higgsfield's eigen CDN vanuit de hoofdsessie).

## Shotlist
21 clips, zie shotlist.json. Cabin-lettering (A/B/C) niet te bevestigen uit de bestandsnamen
("port-aft-cabin", "port-cabin-foreward", "stb-forward-cabin") — genummerd Cabin 1/2/3.
4 foto's uitgesloten wegens resolutie <1280px.

## Generatie
Batch 1 (12 clips) + batch 2 (9 clips), model kling3_0, 16:9, sound off, mode pro voor clip 1
(opener), std voor de rest. Alle 21 in eerste ronde gesubmit.

## QC laag 1 (automatisch, qc_check.py)
Eerste ronde: 4 clips geflagd.
- Clip 1 (exterior, opener): TEXT 'Si' conf51
- Clip 2 (flybridge): TEXT 'DES./Re/if' conf45-70
- Clip 3 (flybridge): TEXT 'yr/iF/el?' conf47-61
- Clip 7 (bow): EDGE 0.442 (norm 0.22)

Regeneratie ronde 2:
- Clip 2, 3: schoon na reddingsprompt (single-axis movement, 3s)
- Clip 1: NIEUWE TEXT-treffer 'LEOPARD' conf80 (bootmerk, vermoedelijk zichtbaar op de romp
  in de bronfoto) — opgelost met expliciete no-brandname-guard
- Clip 7: VERSLECHTERD (JERK 0.84 -> 3.59) ondanks reddingsprompt

Regeneratie ronde 3:
- Clip 1: NIEUWE TEXT-treffer 'Sand' conf90 — patroon (3 pogingen, telkens een fragment van
  een naam) wijst sterk op een bootnaam/merk die daadwerkelijk op de romp staat in de bronfoto
  (sandpiper-main2.jpg), dus een getrouwe reproductie i.p.v. een hallucinatie. GEACCEPTEERD
  na 3e poging i.p.v. verder regenereren — gemeld aan Valentijn/Alexia.
- Clip 7: bronfoto vervangen (sandpiper-bow-seating7 i.p.v. bow-seating), duration 5s->3s,
  standaardprompt hersteld — schoon.

Eindresultaat automatische QC (na fixes): 20/21 clips schoon, 1 geaccepteerd met bekende
oorzaak (bootnaam in bronfoto, clip 1, ook zichtbaar in clip 21 die dezelfde bronfoto
hergebruikt — zelfde geaccepteerde reden).

## QC laag 2 (visueel)
NIET uitgevoerd — visuele inspectie van individuele frames/contactsheets is in deze sessie
technisch onmogelijk (netwerkbeleid blokkeert alle toegang tot Higgsfield's CDN en de VCY-site
vanuit de hoofdsessie, bevestigd getest, geen workaround). Dit is een bekende, gedocumenteerde
beperking voor deze hele batch — zie brief.md. Verzonnen-objecten-check (extra meubels,
dieren, boten) kon dus niet met eigen ogen gebeuren; alleen de vier geautomatiseerde scores
(JERK/EDGE/DRIFT/TEXT) zijn gebruikt als vangnet.

## Montage
Genormaliseerd naar 1920x1080/30fps, geassembleerd met assemble.py, xfade 0.4s.
Eindlengte: 63,73s (binnen 60-90s doel).
Eindcontrole (technisch): 1920x1080, 30fps, geen audio in de stille versie, geen zwarte
frames aan begin/eind. qc_check.py over de eindvideo gedraaid ter aanvulling (JERK/EDGE op
volledige video zijn niet direct vergelijkbaar met per-clip-drempels vanwege de crossfades
— gebruikt als extra check, geen aparte afkeuring op basis daarvan).
Transition QC: geen surgical splice (alle clips vers gegenereerd, geen hergebruik van
bestaand gemonteerd materiaal), dus het "oude naad"-risico uit sectie 12 is hier niet van
toepassing. Volledige frame-voor-frame visuele controle van elke crossfade kon niet
uitgevoerd worden (zelfde CDN-toegangsbeperking als hierboven) — technische eindcontrole
(resolutie/fps/geen zwarte frames) is wel gedaan.

## Muziek (experiment, op verzoek van Valentijn voor deze hele batch)
Track: "Majestic" — Diego Nava (Mixkit, licentie: Mixkit Stock Music Free License).
Ingekort tot videolengte, fade-in 1,5s, fade-out 2s, AAC 192kbps, beeld ongewijzigd (-c:v copy).

## Oplevering
- Stille versie: Sandpiper.mp4 (63,73s) —
  https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/d459021d-b646-4743-b619-ae9f4c5fe568.mp4
- Met muziek: Sandpiper_music.mp4 —
  https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/8524c7a6-eb1a-4ca5-8eb4-041a104ff921.mp4

## Openstaande punten voor Alexia/Valentijn
1. Cabin-lettering (A/B/C) niet bevestigd — 3 hutten genummerd 1/2/3 op bestandsnaamvolgorde.
2. Clip 1 (opener) en clip 21 (closer) tonen mogelijk de bootnaam/merk op de romp — niet
   weg te prompten, waarschijnlijk echt zichtbaar in de bronfoto.
3. Laag-2 visuele QC (verzonnen objecten, mensen, dieren) niet uitgevoerd — technische
   sessiebeperking, niet doorlopend overgeslagen.
4. Video is een baseline op basis van site-foto's, niet client-aangeleverde/gecategoriseerde
   foto's — Alexia's bevestiging nog nodig voor definitieve oplevering.

## Credits
Balans voor start batch (Sandpiper + Caribbean Cat samen): 1715
Balans na deze batch: 1428 (zie Caribbean_Cat/log.md voor de gecombineerde afrekening)
