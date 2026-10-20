# Log — Fasoulias Lines (gratis sample)

## Generaties

| Clip | Bronfoto | Duration | Mode | Job-id | Credits |
|---|---|---|---|---|---|
| 1 Exterior opener | photos/01_opener_sunset.jpg | 5s | std | 539d0417-1153-4b87-a585-77a1a65b1319 | 7,5 |
| 2 Exterior detail | photos/02_idea53_clearwater.jpg (origineel, portret) | 3s | std | efdb1145-78af-476b-aebe-b5208d6ce642 | 4,5 (vervangen, zie hieronder) |
| 3 Scenery | photos/03_rockarch_scenery.jpg | 3s | std | a3536cd5-5223-402d-b709-cfba1fdfb91b | 4,5 |
| 4 Exterior detail (RIB) | photos/04_rib_closeup.jpg (origineel, portret) | 3s | std | 4740a25d-6c97-4718-ae91-1aa58b600c4d | 4,5 (vervangen, zie hieronder) |
| 5 Exterior closer | photos/05_closer_clearwater.jpg | 5s | std | b81f0c1b-56c4-45c5-9717-de3a45dbac7b | 7,5 |

**mode pro → std**: oorspronkelijke shotlist had clip 1 en 5 op `pro` (hero-shots). Geblokkeerd met
"Requires plus plan or higher" — huidig abonnement is starter, pro is niet beschikbaar.
Teruggezet naar std na akkoord Valentijn ("1"). Zie shotlist.json-notes.

## Technisch defect gevonden bij QC: portretoriëntatie clip 2 en 4

`02_idea53_clearwater.jpg` (1536×2048) en `04_rib_closeup.jpg` (1200×1600) zijn beide
portretfoto's. Ondanks expliciete `aspect_ratio: "16:9"` in de request kwamen clip 2 en 4
terug als 828×1108 (portret) — Kling volgde blijkbaar de oriëntatie van de bronfoto in
plaats van de parameter. Clip 1, 3, 5 (landscape bronfoto's) kwamen wel correct terug als
1108×832/828.

**Fix**: beide bronfoto's handmatig gecrop naar 16:9 (center op de boot, niet geometrisch
midden van de foto — eerste center-crop-poging sneed de boot er per ongeluk uit, gecorrigeerd
met een grid-overlay om de juiste y-range te bepalen), opnieuw geüpload, en alleen clip 2 en 4
opnieuw gegenereerd met dezelfde prompt:

| Clip | Nieuwe job-id | Resultaat |
|---|---|---|
| 2 | e5ce73f2-4324-493d-8cf3-83c95658c5a2 | 1280×720, correct landscape |
| 4 | 83ce3ab0-ae8e-4bad-8039-c6afd5db7405 | 1280×720, correct landscape |

Extra kosten: 2× 3s/std = 9 credits (goedgekeurd door Valentijn).

## QC laag 2 — visueel (alle 5 clips)

Alle 5 clips bekeken op gesamplede frames (1fps). Geen mensen, geen verzonnen meubels/dieren/
boten, geen morphing, stabiele geometrie. "FASOULIAS LINES" / "IDEA 53" / "KATERINA T.A. 630" /
telefoonnummers staan al fysiek op de boten in de bronfoto's — getrouwe reproductie, geen
hallucinatie (zelfde aanpak als bootnamen bij VCY, bijv. LEOPARD bij Sandpiper).

Geen qc_check.py (JERK/EDGE/DRIFT/TEXT) gedraaid dit keer — kleine sample van 5 clips, visuele
inspectie volstond. Voor toekomstige grotere Fasoulias Lines-batches wel qc_check.py gebruiken
zoals bij VCY.

## Transition QC (verplicht, na montage)

4 crossfades (opener→detail, detail→scenery, scenery→rib, rib→closer), elk 0,4s. Frame
gesampled op het midden van elke transitie: alle 4 tonen een normale dissolve-blend van exact
de twee aangrenzende clips, geen ghosting of restmateriaal van een andere clip. Geen surgical
splice gebruikt (alle clips vers gegenereerd), dus het oude-naad-risico uit CLAUDE.md §12 is
hier niet van toepassing. Start- en eindframe gecontroleerd: geen zwarte frames.

## Montage

5 clips, genormaliseerd naar 1920×1080/30fps, assemble.py, xfade 0,4s.
Eindlengte: **17,6s** — binnen het 15-25s sample-doel.
Technische eindcontrole: 1920×1080, 30fps, geen audiospoor, geen zwarte frames.

## Credits

Totaal: 1 testclip (7,5) + 4 batchclips (21) + 2 regeneraties na aspect-ratio-fix (9) = 37,5
credits. Saldo voor sessie: 272,5. Saldo na: **235**.

## Oplevering

- Fasoulias_Lines_sample.mp4 (17,6s, stil, geen muziek — dit is pas een ruwe sample) —
  https://d2ol7oe51mr4n9.cloudfront.net/user_3GAnI2MKRZFE3ukZ4ZGqGe45vyC/12f07729-4281-4de5-af12-c590f3a14296.mp4
- media_id: 12f07729-4281-4de5-af12-c590f3a14296

## Openstaande punten

1. Dit is een **gratis sample** voor een nieuwe prospect — geen definitieve levering. Valentijn
   beoordeelt eerst voordat dit richting Fasoulias Lines gaat.
2. Geen muziek toegevoegd — optioneel, alleen na akkoord Valentijn (zelfde regel als VCY §13).
3. Oriëntatie 16:9 was een aanname (niet expliciet gevraagd door de klant) — te bevestigen als
   dit tot een echte opdracht leidt.
4. Opener/closer-bronfoto's zijn onder de 1280px-norm (877×658) — zichtbaar iets zachter dan de
   andere 3 clips. Geaccepteerd voor deze sample, geen betere foto's beschikbaar.
