# Log — Tropically Impaired

## Context (29-09-2026)
Baseline-versie, zelfde aanpak/reden als de vorige boten in deze batch (zie Caribbean Cat/log.md
voor de volledige uitleg). GEEN room-categorieen (geen bruikbare bestandsnamen, visuele
inspectie technisch onmogelijk in deze sessie). Numerieke wide/detail-classificatie
(blue_ratio/top_blue heuristiek) gebruikt voor volgorde/prompt-keuze.

Grootste gallery tot nu toe in deze batch: 63 bruikbare bronfoto's na dedup (1 duplicaat via
MD5-hash samengevoegd, 1 lageresolutie-portret en 1 layout-diagram uitgesloten). Slechts een
representatieve selectie is gebruikt, niet alle 63.

## Shotlist (origineel)
19 clips: opener (wide, pro, 5s) + 3 extra wide (3s) + 13 detail (3-5s, ongecategoriseerd) +
1 extra wide (3s) + closer (dezelfde bronfoto als opener, pull-back, 5s).

## QC laag 1 (qc_check.py: JERK/EDGE/TEXT — DRIFT niet actief, geen lokale bronfoto's)
Eerste ronde: 13 van 19 clips geflagd op TEXT — ongewoon hoog aantal vergeleken met de
vorige boten in deze batch.

**Watermarkreeks ontdekt**: 4 clips (oorspronkelijk index 4 = IMG_3449, 5 = IMG_3451,
6 = IMG_3452, 18 = IMG_3447) toonden hoge-confidence coherente tekst:
- "TROPICALLY" (conf 91-93), "IMPAIRED" (conf 89-96) in alle 4
- Clip 6 ook: "New" (conf 96), "Castle," (conf 52), "NH" (conf 96)

Dit is duidelijk geen Kling-ruis maar een naam+locatie-caption die al in de bronfoto gebrand
staat (zelfde patroon als Tidewater's "Tidewater — Beaufort, SC"). Getest met een herkansing
van clip 6 met verzwaarde no-caption/no-watermark-prompt: resultaat kwam vrijwel identiek terug
("TROPICALLY" conf92, "IMPAIRED" conf96, "New" conf96, "NH" conf96) — bevestigd gebrand in de
bron, niet oplosbaar via prompting.

**Besluit**: alle 4 betrokken clips uitgesloten. Omdat deze boot de grootste gallery van de
batch heeft (63 bronfoto's, slechts 17 gebruikt), is er ruim voldoende ongebruikt materiaal om
te vervangen in plaats van de eindvideo korter te laten uitvallen (zoals bij Caribbean Cat).
4 nieuwe bronfoto's (IMG_3513, IMG_3517, IMG_3522, IMG_3546) uit een ander deel van de gallery
zijn geïmporteerd en gegenereerd als vervanging op dezelfde posities (index 4, 5, 6, 18).

Vervangers QC:
- IMG_3513 (nieuwe index 4): schoon, geen flags.
- IMG_3517 (nieuwe index 5): 5 lage-confidence TEXT-fragmenten (conf 48-67), geen coherent
  patroon -- geaccepteerd als Kling-ruis.
- IMG_3522 (nieuwe index 6): schoon, geen flags.
- IMG_3546 (nieuwe index 18): 20 lage-confidence TEXT-fragmenten (conf 45-69), geen coherent
  patroon, geen herhaling van "TROPICALLY IMPAIRED" -- geaccepteerd als Kling-ruis.

Overige 9 oorspronkelijk geflagde clips (08, 09, 10, 11, 14, 15, 16, 17, plus enkele lage-
confidence hits binnen de nu vervangen clips): allemaal lage-confidence garbled fragmenten
(conf 45-73), geen coherent of herhaald patroon, geen overlap met de watermarktekst --
geaccepteerd als gewone Kling-OCR-ruis.

Eindresultaat: 19/19 clips in de definitieve montage schoon of geaccepteerd; 4 van de
oorspronkelijke 19 clips definitief vervangen wegens bevestigde brontekst.

## QC laag 2
Niet uitgevoerd — zelfde technische sessiebeperking als bij de vorige boten.

## Transition QC
Niet visueel uitgevoerd — zelfde technische sessiebeperking. Geen surgical splice (alle
gebruikte clips zijn vers gegenereerd), dus het oude-naad-risico uit sectie 12 van CLAUDE.md
is hier niet van toepassing. Crossfade-duur standaard 0,4s.

## Montage
19 clips (4 vervangen na QC), genormaliseerd naar 1920x1080/30fps, assemble.py, xfade 0,4s.
Eindlengte: 62,47s (binnen 60-90s doel).
Technische eindcontrole: 1920x1080, 30fps, geen audiospoor (stille versie), geen zwarte
frames aan begin/eind.

## Muziek
Track: "Majestic" — Diego Nava (Mixkit Stock Music Free License), zelfde track als de
vorige boten in deze batch.

## Credits
23 gegenereerde clips totaal (19 shotlist + 4 vervangers, geen dubbele pogingen op dezelfde
prompt). Balance vóór deze boot: 691,75. Ruim boven de 300-credit-meldgrens.

## Oplevering
- Stille versie: Tropically_Impaired.mp4 (62,47s) —
  https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/bb55c57e-3582-41c6-996b-1d53d7b9e086.mp4
- Met muziek: Tropically_Impaired_music.mp4 —
  https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/4512ca12-fcea-49ba-85f8-d5bf14f84725.mp4

## Openstaande punten voor Alexia/Valentijn
1. **Watermarkreeks ontdekt in bronmateriaal**: de foto's IMG_3447/3449/3451/3452 (mogelijk
   de hele upload-batch eromheen) hebben een gebrande "TROPICALLY IMPAIRED / New Castle, NH"
   caption. Dit is opgelost voor déze video door vervanging, maar is relevant voor Alexia om
   te weten voor toekomstig gebruik van diezelfde bronfoto's (ook buiten deze pijplijn).
2. GEEN room-categorieen — volgorde is site-gallery-volgorde.
3. Laag-2 visuele QC en transition-QC niet uitgevoerd — technische sessiebeperking.
4. Baseline op basis van site-foto's — Alexia's bevestiging nog nodig voor definitieve
   oplevering.
