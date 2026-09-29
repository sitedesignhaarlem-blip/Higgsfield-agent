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

## QC laag 2
Niet uitgevoerd — zelfde technische sessiebeperking als bij de vorige boten.

## Transition QC
Niet visueel uitgevoerd — zelfde technische sessiebeperking. Geen surgical splice (alle
gebruikte clips zijn vers gegenereerd), dus het oude-naad-risico uit sectie 12 van CLAUDE.md
is hier niet van toepassing. Crossfade-duur standaard 0,4s.

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
2. Laag-2 visuele QC en transition-QC niet uitgevoerd — technische sessiebeperking.
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
