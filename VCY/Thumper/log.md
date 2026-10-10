# Log — Thumper

## Context (29-09-2026)
Baseline-versie, zelfde aanpak/reden als de vorige boten in deze batch (zie Caribbean Cat/log.md
voor de volledige uitleg). GEEN room-categorieen (geen bruikbare bestandsnamen, visuele
inspectie technisch onmogelijk in deze sessie). Geen gedeelde bestanden met andere boten
gevonden.

**Kwaliteitswaarschuwing (zie brief.md)**: de volledige gallery bestaat uit "Screenshot-NN"-
benoemde bestanden, geen normale fotografie-bestandsnamen. Slechts 2 van 22 bronbestanden
halen de normale 1280px-norm; voor deze baseline is de resolutienorm versoepeld naar >=956px.
Iedere clip in shotlist.json heeft een notitie met de exacte bronresolutie. Alexia moet
expliciet bevestigen of dit geschikt bronmateriaal is voor klantgebruik.

## Shotlist
18 clips: opener (wide, pro, 5s) + 3 extra wide (3s) + 13 detail (3-5s, ongecategoriseerd) +
closer (dezelfde bronfoto als opener, pull-back, 5s). Clip 9 kreeg 5s i.p.v. 3s om de
doellengte te halen (61,2s beoogd).

## QC laag 1 (qc_check.py: JERK/EDGE/TEXT — DRIFT niet actief, geen lokale bronfoto's)
Eerste ronde: 2 van 18 clips geflagd.
- **Clip 16** (JERK 2,697, boven de 2,5-drempel): motion-profile toonde een sterke versnelling
  naar het einde van de clip (van ~0,1 naar >1,0) -- een echte camera/geometrie-hobbel, geen
  ruis. Geregenereerd met de reddingsprompt (single-axis movement, 3s, "absolutely stable
  geometry"). Vervanger: JERK 0,825 (ruim onder de drempel) -- opgelost.
- **Clip 8** (TEXT, 2 lage-confidence fragmenten: "wee" conf55, "ae" conf50): geen leesbaar of
  herhaald patroon -- geaccepteerd als gewone Kling-OCR-ruis, geen brontekst.
- Clip 16's vervanger had zelf ook 1 laag-confidence TEXT-treffer ("at" conf62), ander fragment
  dan de eerste poging ("ws") -- zelfde ruis-conclusie, geaccepteerd.

Eindresultaat: 17/18 clips schoon bij eerste poging, 1 clip (16) hergenereerd en daarna schoon,
2 clips geaccepteerd op basis van niet-herhaalde lage-confidence TEXT-ruis.

## QC laag 2 — alsnog uitgevoerd (10-10-2026) — **AFKEURING gevonden**

Zelfde methode als de andere boten in deze batch (`sandbox_exec` image_paths).

**Clips 1, 3 en 18 tonen echte mensen aan boord** — meerdere personen op de
flybridge van de boot terwijl die vaart (bronfoto's `Screenshot-21.png`
[clip 1 opener, hergebruikt als clip 18 closer] en `Screenshot-22.png`
[clip 3]). Bevestigd met scherpe close-ups, ondubbelzinnig. Zelfde patroon
als bij Southern Mist: dit zijn vermoedelijk actie-/vaart-opnames uit het
fabrieksmateriaal van de site-gallery (niet dekshots van dit specifieke
exemplaar), en Kling reproduceert de mensen getrouw ondanks `no people` in
de prompt. Clips 2 en 4 (tussen clip 1 en 3 in) zijn wél schoon — dus dit
is geen doorlopend probleem door de hele opener-sectie, maar 3 specifieke
clips.

**Overige clips (5 t/m 17) zijn schoon**: geen mensen, geen verzonnen
meubels/dieren, geen morphing. **TEXT:** alleen OCR-ruis ("Lull"/"Milf"/
"cane"), geen bootnaam of logo gevonden.

**Transition QC:** de ogenschijnlijke "watermerk"-waas rond t≈10s in de
mosaic bleek bij nader onderzoek een gewone crossfade-ghost (palmbomen van
de volgende clip doorschemerend), geen echt watermerk en geen restmateriaal
van een oude naad. Geen surgical-splice-geschiedenis (alle 18 clips vers
gegenereerd), dus dat risico is sowieso niet van toepassing.

**Niet opgelost deze sessie:** credits op 0, geen nieuwe generatie mogelijk.
Clips 1, 3, 18 zijn NIET aangepast — keuze voor Valentijn (uitknippen/
vervangen vs. wachten op credits), zie Openstaande punten.

## Montage
18 clips, genormaliseerd naar 1920x1080/30fps, assemble.py, xfade 0,4s.
Eindlengte: 61,83s (binnen 60-90s doel).
Technische eindcontrole: 1920x1080, 30fps, geen audiospoor (stille versie), geen zwarte
frames aan begin/eind.

## Muziek
Track: "Majestic" — Diego Nava (Mixkit Stock Music Free License), zelfde track als de
vorige boten in deze batch.

## Oplevering
- Stille versie: Thumper.mp4 (61,83s) —
  https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/510c9479-abc9-4265-ba9f-85db4e1134a5.mp4
- Met muziek: Thumper_music.mp4 —
  https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/001a1f2d-37ff-4d4c-9c42-c709b2392525.mp4

## Credits
Balance na deze boot: 804 (gecheckt tijdens productie, ruim boven de 300-credit-meldgrens).

## Openstaande punten voor Alexia/Valentijn
1. **Bronmateriaal-kwaliteit**: de volledige gallery bestaat uit screenshot-achtige bestanden,
   niet uit normale fotografie. Alexia moet bevestigen of dit representatief en bruikbaar is.
2. **AFGEKEURD: clips 1, 3 en 18 (opener, 3e clip, closer) tonen echte mensen aan boord —
   harde regelovertreding, zie QC laag 2 hierboven.** Niet naar Alexia/eindklant sturen
   voordat dit is opgelost. Opties: (a) uitknippen (gratis, surgical splice, maar de opener
   én closer vervallen dan — grote impact op dit jacht) of (b) vervangen met mensvrije
   bronfoto's zodra credits beschikbaar zijn (nu 0). Wacht op akkoord Valentijn.
3. GEEN room-categorieen — volgorde is site-gallery-volgorde.
4. Baseline op basis van site-foto's — Alexia's bevestiging nog nodig voor definitieve
   oplevering.
