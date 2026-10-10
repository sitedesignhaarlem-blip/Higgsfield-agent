# Log — Wild Blue

## Context (29-09-2026)
Baseline-versie, zelfde aanpak/reden als de vorige boten in deze batch (zie Caribbean Cat/log.md
voor de volledige uitleg). GEEN room-categorieen (geen bruikbare bestandsnamen, visuele
inspectie technisch onmogelijk in deze sessie). Numerieke wide/detail-classificatie
(blue_ratio/top_blue heuristiek) gebruikt voor volgorde/prompt-keuze.

**Laatste boot van deze batch van 10.** 3 bestanden uit de bekende gedeelde cluster met
Elysium/Southern Mist/Tidewater (19A8645, 19A8647-2, 19A8872_1) zijn uitgesloten -- dit is
Wild Blue's eigen pagina, dus de "wildblue-N"-bestanden die bij Elysium/Southern Mist eerder
als vreemd materiaal werden uitgesloten, zijn hier terecht wél gebruikt. 1 layout-diagram
(MY44-layout.png) uitgesloten. 1 extra bestand (19A8895) is uit voorzorg niet gebruikt omdat
het exact dezelfde top_blue-score/resolutie had als een foto uit Tidewater's gallery --
vermoedelijk hetzelfde gedeelde/generieke bestand, niet met zekerheid te bevestigen zonder
visuele inspectie.

## Shotlist
18 clips: opener (wide, pro, 5s) + 3 extra wide (3s) + 12 detail (3-5s, ongecategoriseerd) +
1 extra wide (3s) + closer (dezelfde bronfoto als opener, pull-back, 5s).

## QC laag 1 (qc_check.py: JERK/EDGE/TEXT — DRIFT niet actief, geen lokale bronfoto's)
Beste resultaat van de hele batch: slechts 2 van 18 clips geflagd, allebei op TEXT.
- Clip 9: 1 fragment ("ARAN" conf51) -- geen coherent patroon, geaccepteerd als Kling-ruis.
- Clip 15: 5 lage-confidence fragmenten (conf 46-71, o.a. "at", "‘Se", "ve", "pe", "Ste") --
  geen coherent of herhaald patroon, geen overlap met een bootnaam of caption zoals bij
  Tidewater/Tropically Impaired -- geaccepteerd als gewone Kling-OCR-ruis.

Geen regeneraties nodig deze boot. Eindresultaat: 18/18 clips schoon of geaccepteerd bij
eerste poging.

## QC laag 2 — alsnog uitgevoerd (10-10-2026) — **AFKEURING, ernstigste geval van de batch**

Zelfde methode als de andere boten. Dit is de meest aangetaste video van de
10: **4 van de 18 clips tonen echte mensen aan boord**, bevestigd met
close-ups, geen twijfelgevallen:

- **Clip 1 (opener, t≈0-4,6s, bronfoto `wildblue-12-1...jpg`)**: vrouw in
  zwempak zittend op het voornet/de bow.
- **Clip 14 (t≈45,8-48,4s, bronfoto `19A8881-1280x950.jpg`)**: 3 mensen op
  de flybridge — kapitein aan het roer, twee personen aan de dinettetafel.
- **Clip 16 (t≈53,0-55,6s, bronfoto `wildblue-13-1...jpg`)**: luchtfoto met
  een man en vrouw liggend/zittend op het zonnedek.
- **Clip 18 (closer, t≈58,2-63,2s)**: hergebruikt dezelfde bronfoto als
  clip 1 (`wildblue-12-1...jpg`) — dus dezelfde vrouw op de bow, nu als
  slotshot.

Opvallend: bronfoto `19A8881` (clip 14, mensen) is een ANDER bestand dan het
al eerder uit voorzorg uitgesloten `19A8895` (zie Openstaande punten #4) —
dat eerdere vermoeden ("gedeeld/generiek materiaal met Tidewater") blijkt
dus niet de oorzaak; het echte probleem is steeds een los geval van mensen
in de specifieke bronfoto, net als bij Southern Mist/Thumper/Tidewater/
Tropically Impaired in dezelfde batch.

Clips 2-13, 15, 17 zijn schoon: geen mensen, geen verzonnen meubels/dieren,
geen morphing. **TEXT:** geen enkele OCR-treffer (ook geen ruis) — wel is
"FOUNTAINE PAJOT" (de botenbouwer, geen Wild Blue-specifiek merk) zichtbaar
op de romp in clip 1/18, net als de LEOPARD-naam bij Sandpiper: een
getrouwe reproductie van wat al op de romp staat, geen hallucinatie.

## Transition QC
Crossfades in de mosaic ogen normaal, geen ghosting. Geen surgical splice
(alle clips vers gegenereerd), dus het oude-naad-risico uit sectie 12 van
CLAUDE.md is hier niet van toepassing.

**Niet opgelost deze sessie:** credits op 0. Clips 1, 14, 16, 18 zijn NIET
aangepast — keuze voor Valentijn, zie Openstaande punten. Let op: clips 1
én 18 delen dezelfde bronfoto, dus een vervangende, mensvrije foto lost
in één keer zowel opener als closer op.

## Montage
18 clips, genormaliseerd naar 1920x1080/30fps, assemble.py, xfade 0,4s.
Eindlengte: 63,83s (binnen 60-90s doel).
Technische eindcontrole: 1920x1080, 30fps, geen audiospoor (stille versie), geen zwarte
frames aan begin/eind.

## Muziek
Track: "Majestic" — Diego Nava (Mixkit Stock Music Free License), zelfde track als de
vorige boten in deze batch.

## Credits
18 gegenereerde clips, geen regeneraties nodig. Balance vóór deze boot: 561,50.
Ruim boven de 300-credit-meldgrens.

## Oplevering
- Stille versie: Wild_Blue.mp4 (63,83s) —
  https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/0b903c43-dd5a-40a3-8ece-5d84d6492b33.mp4
- Met muziek: Wild_Blue_music.mp4 —
  https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/d6d83704-86cc-48f2-84cd-156b30d8edc0.mp4

## Openstaande punten voor Alexia/Valentijn
1. GEEN room-categorieen — volgorde is site-gallery-volgorde.
2. **AFGEKEURD: clips 1, 14, 16 en 18 tonen echte mensen aan boord — harde regelovertreding,
   ernstigste geval van de hele batch, zie QC laag 2 hierboven.** Niet naar Alexia/eindklant
   sturen voordat dit is opgelost. Clips 1 en 18 delen dezelfde bronfoto (dus 1 vervangende
   foto lost beide op). Opties: (a) uitknippen (gratis, surgical splice, -4 clips, incl.
   opener én closer — grote impact) of (b) vervangen met mensvrije bronfoto's zodra credits
   beschikbaar zijn (nu 0). Wacht op akkoord Valentijn.
3. Baseline op basis van site-foto's — Alexia's bevestiging nog nodig voor definitieve
   oplevering.
4. 1 bestand (19A8895) uit voorzorg niet gebruikt wegens vermoeden van gedeeld/generiek
   materiaal met Tidewater — kan alsnog toegevoegd worden als Alexia bevestigt dat het een
   uniek Wild Blue-bestand is.

## BATCH-AFRONDING
Dit is de 10e en laatste boot van deze productieronde. Alle 10 boten (Sandpiper, Caribbean
Cat, Elysium, One Life, Southern Mist, ThreeQuartersFull, Thumper, Tidewater, Tropically
Impaired, Wild Blue) zijn nu geleverd als baseline-versie, elk met stille en muziek-variant,
en elk met een brief.md die de methodologiebeperkingen en boot-specifieke bijzonderheden
documenteert voor Alexia's review.
