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

## Oplevering (v1, afgekeurd — niet versturen)
- Stille versie: Thumper.mp4 (61,83s) —
  https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/510c9479-abc9-4265-ba9f-85db4e1134a5.mp4
- Met muziek: Thumper_music.mp4 —
  https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/001a1f2d-37ff-4d4c-9c42-c709b2392525.mp4

## Credits
Balance na deze boot: 804 (gecheckt tijdens productie, ruim boven de 300-credit-meldgrens).

---

## Revisie v2 (10-10-2026) — clips met mensen eruit geknipt

Op verzoek van Valentijn: clips 1, 3 en 18 (opener, 3e clip, closer — alle
3 met echte mensen aan boord, zie QC laag 2) verwijderd via surgical splice,
0 credits. Schone segmenten (0,5s marge per knippunt) herverbonden met
verse 0,4s crossfades: nu clip 2 → clip 4 t/m 17 (de video begint dus met
de voormalige clip 2 en eindigt met de voormalige clip 17). Beide nieuwe
naden gecontroleerd — schoon, geen ghosting, geen mensen.

**Eindlengte: 46,6s — fors onder de 60-90s-norm.** Grootste impact van de
hele batch: zowel opener als closer zijn weg. Dit is een tijdelijke
noodgreep, geen definitieve oplossing — Thumper heeft het dringendst
nieuwe, mensvrije bronfoto's nodig zodra credits beschikbaar zijn (vooral
voor een nieuwe opener/closer).

### Oplevering (v2, huidige versie)
- Stille versie: Thumper.mp4 (46,6s) —
  https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/155369cf-66b4-4671-b73c-e5663cae031b.mp4
- media_id: 155369cf-66b4-4671-b73c-e5663cae031b
- **Met-muziek-versie nog niet opnieuw gemaakt** — zie Openstaande punten.
- Kosten: 0 credits (pure re-splice).

## Openstaande punten voor Alexia/Valentijn
1. **Bronmateriaal-kwaliteit**: de volledige gallery bestaat uit screenshot-achtige bestanden,
   niet uit normale fotografie. Alexia moet bevestigen of dit representatief en bruikbaar is.
2. **Eindlengte 46,6s, fors onder de 60-90s-norm** — gevolg van het verwijderen van opener,
   3e clip én closer (alle 3 afgekeurd wegens mensen in beeld). Dit jacht heeft als eerste
   nieuwe bronfoto's nodig zodra credits beschikbaar zijn.
3. Met-muziek-versie nog opnieuw te maken op de nieuwe lengte.
4. GEEN room-categorieen — volgorde is site-gallery-volgorde.
5. Baseline op basis van site-foto's — Alexia's bevestiging nog nodig voor definitieve
   oplevering.
