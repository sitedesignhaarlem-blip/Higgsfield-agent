# Log — Southern Mist

## Context (29-09-2026)
Baseline-versie, zelfde aanpak/reden als de vorige boten in deze batch (zie Caribbean Cat/log.md
voor de volledige uitleg). GEEN room-categorieen (geen bruikbare bestandsnamen, visuele
inspectie technisch onmogelijk in deze sessie). 8 foto's gedeeld met Elysium/Tidewater/Wild
Blue uitgesloten.

## Shotlist
20 clips: opener (wide, pro) + 3 extra wide + 12 detail (hi-res 1280x950) + 3 detail (756x567,
onder de resolutienorm, gebruikt voor voldoende lengte) + closer.

## QC laag 1
Eerste ronde: 3 van 20 clips geflagd op TEXT.
- Clip 11: "(Douthern" conf70 -- mogelijk fragment van "Southern" (de eigen bootnaam),
  zichtbaar in de bronfoto. Herkansing gaf een nieuw laag-confidence fragment ('ah' conf45) --
  geaccepteerd na 2 pogingen.
- Clip 12, 15: lage-confidence ruis, beide opgelost met verzwaarde no-text-guard.

Eindresultaat: 19/20 clips schoon, 1 geaccepteerd na 2 pogingen.

## QC laag 2 — alsnog uitgevoerd (10-10-2026) — **AFKEURING gevonden**

Zelfde methode als de vorige boten. Dit keer géén schone uitslag:

**Clips 2, 3 en 4 (t≈4,6-12,4s in de huidige video, bronfoto's
`Southern-mist-2.jpg`, `image6.jpeg`, `image4.jpeg`) tonen echte mensen aan
boord** — een stuurman achter het stuur op de flybridge en losse personen op
het voordek/de zijdeken, duidelijk herkenbaar, niet subtiel. Bevestigd met
close-up crops, geen twijfelgeval. Dit is een harde regel uit CLAUDE.md §4
("Geen mensen in beeld") — zonder uitzondering, in tegenstelling tot
bijvoorbeeld een bootnaam. Alle 3 prompts bevatten al `no people`; de mensen
staan kennelijk al prominent in de bronfoto zelf (vermoedelijk
actie-/vaart-opnames uit het fabrieksmateriaal van de site-gallery, niet
dekshots van dit specifieke, afgemeerde exemplaar) — Kling reproduceert ze
dan getrouw ondanks de prompt-instructie, net als bij de bootnaam-gevallen.
Ook een vage, onleesbare pseudo-tekst op het glas zichtbaar in clip 2
("I_ON"-achtig) — waarschijnlijk OCR/Kling-ruis op donker glas, niet
geverifieerd als een bestaand bootmerk, maar sowieso een TEXT-afkeuring op
zich.

**Alle overige clips (5 t/m 20) zijn schoon**: geen mensen, geen verzonnen
meubels/dieren/vaartuigen, geen morphing, geen leesbare tekst (OCR-check
leverde alleen ruis op, "Must"/"WILD").

**Niet opgelost deze sessie:** credits staan op 0, dus geen nieuwe generatie
mogelijk. Clips 2-4 zijn NIET uit de video geknipt — dat is een keuze voor
Valentijn (zie Openstaande punten): uitknippen (gratis, maar -9s en een
gat in de "Exterior"-sectie) versus wachten op credits + andere bronfoto's
zonder mensen.

## Montage
20 clips, genormaliseerd naar 1920x1080/30fps, assemble.py, xfade 0.4s.
Eindlengte: 65,10s (binnen 60-90s doel).

## Muziek
Track: "Majestic" — Diego Nava (Mixkit Stock Music Free License), zelfde track als de
vorige boten in deze batch.

## Oplevering (v1, afgekeurd — niet versturen)
- Stille versie: Southern_Mist.mp4 (65,10s) —
  https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/45f31ad5-4e2f-41c2-84e0-c207139d60e6.mp4
- Met muziek: Southern_Mist_music.mp4 —
  https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/96536b55-705c-46f8-9b19-68c27156c5ec.mp4

---

## Revisie v2 (10-10-2026) — clips met mensen eruit geknipt

Op verzoek van Valentijn: clips 2, 3 en 4 (de 3 clips met echte mensen aan
boord, zie QC laag 2 hierboven) verwijderd via surgical splice uit de v1-
render, 0 credits (geen nieuwe generatie). Methode: schone segmenten
geknipt met 0,5s veiligheidsmarge aan elke kant van elk knippunt (zelfde
aanpak als de Calypso-reorders), opnieuw aan elkaar gezet met een verse
0,4s crossfade.

Nieuwe opbouw: clip 1 (opener, ongewijzigd) → crossfade → clip 5 t/m 20
(ongewijzigd). Alle 4 nieuwe/overgebleven naden gecontroleerd met scherpe
frame-crops rond de crossfade — schoon, geen ghosting, geen mensen.

**Eindlengte: 55,9s — onder de 60-90s-norm.** Dit is een bewuste trade-off:
de regelovertreding wegen zwaarder dan de lengte-norm. Geen vervangende
mensvrije foto's beschikbaar binnen deze sessie om de 9,2s te compenseren.

### Oplevering (v2, huidige versie)
- Stille versie: Southern_Mist.mp4 (55,9s) —
  https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/9ae39ad1-3a13-4a86-824c-85b4b464ca39.mp4
- media_id: 9ae39ad1-3a13-4a86-824c-85b4b464ca39
- Met muziek: Southern_Mist_music.mp4 (55,9s, track "Majestic" opnieuw op de nieuwe
  lengte geknipt, fade-in 1,5s/fade-out 2s, AAC 192kbps, beeld ongewijzigd) —
  https://d2ol7oe51mr4n9.cloudfront.net/user_3GZorgXJgm7K6l75bC5xyl4LIu6/f2db6bda-b7e9-4a29-b63f-508bb3a47a99.mp4
- Kosten: 0 credits (pure re-splice + audio-mux, geen generatie).

## Openstaande punten voor Alexia/Valentijn
1. GEEN room-categorieen — volgorde is site-gallery-volgorde.
2. **Eindlengte 55,9s, onder de 60-90s-norm** (gevolg van het verwijderen van de
   afgekeurde mensen-clips). Permanente oplossing: 3 mensvrije bronfoto's voor
   het exterior-blok zodra credits beschikbaar zijn.
3. Baseline op basis van site-foto's — Alexia's bevestiging nog nodig voor definitieve
   oplevering.
