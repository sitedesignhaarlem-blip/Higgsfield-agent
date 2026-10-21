# Log — Fasoulias Lines 90s promo video

Vervolg op de gratis sample (zie log.md). Doel: volledige 90 sec promo met de mooiste en
schoonste shots, met muziek, inclusief de 5 sample-clips hergebruikt.

## Bronmateriaal

Naast de originele 30 foto's (sample) zijn 2 nieuwe WhatsApp-batches ontvangen (56 foto's,
20-10 en 21-10). Volledige inventarisatie op volledig formaat (niet alleen thumbnail-grid):

| Bron | Aantal | Uitgesloten (mensen) | Bruikbaar |
|---|---|---|---|
| WhatsApp 20-10 | 28 | 2 | 26 |
| WhatsApp 21-10 | 28 | 4 | 24 |

**Belangrijke les tijdens dit project**: een eerste quick-scan via een thumbnail-contactsheet
miste 6 foto's met mensen (kleine bootjes met passagiers op afstand in grotten, een zwemmer,
mensen op een terras op de achtergrond) — pas bij losse full-size inspectie van elke
kandidaat-foto zijn deze gevonden. Dit kostte tijd maar voorkwam dat er alsnog mensen in de
eindvideo terechtkwamen. Voor toekomstige grotere batches: altijd full-size controleren, nooit
op een thumbnail-grid vertrouwen voor de finale selectie.

## Shotlist

27 clips: 5 hergebruikt van de sample (01, 02, 03, 04, 27 — 0 extra credits) + 22 nieuw
gegenereerd. 7 clips op 5s (hero), 20 op 3s. Volledige foto-naar-clip mapping staat in
`Fasoulias_Lines/photos_v2/` (bestandsnamen corresponderen met clipnummer).

### Portretfoto's vooraf bijgesneden naar 16:9

15 van de 22 nieuwe bronfoto's waren portret of vierkant. Zelfde probleem als bij de sample:
Kling volgt de bronoriëntatie, niet de `aspect_ratio`-parameter. Alle 15 zijn vooraf
bijgesneden naar 16:9 vóór upload — de meeste met een simpele center-crop, 3 met een
grid-geverifieerde custom crop omdat een blinde center-crop het onderwerp (grotopening,
boegdetail) eruit sneed.

### Preset-deflectie tijdens batch-generatie

5 van de 22 requests (herhaaldelijk "gentle pan across a moored speedboat..."-achtige
prompts) werden door het platform afgewisseld voor een preset-aanbeveling ("IN THE DARK") in
plaats van als normale job ingediend — geen credit-issue, geen fout, waarschijnlijk
patroonherkenning op de herhaalde prompt-formulering. Opgelost door de prompt te herformuleren
(andere bewoording, zelfde inhoud) en opnieuw in te dienen; alle 5 zijn daarna normaal
doorgegaan. Geen extra credits gekost (mislukte submissions worden niet in rekening gebracht).

## QC laag 2 — visueel (alle 22 nieuwe clips)

Alle clips bekeken op een middenframe. Geen mensen, geen verzonnen meubels/dieren/boten, geen
morphing, stabiele geometrie. Merknamen/bootnamen (FASOULIAS LINES, IDEA 53, RAPHAEL, AMOPE IV)
staan al fysiek op de boten — getrouwe reproductie.

## Transition QC (verplicht, na montage)

26 crossfades gecontroleerd (middenframe van elke overgang) + start- en eindframe. Alle 26
tonen een normale dissolve-blend van exact de twee aangrenzende clips — geen ghosting, geen
restmateriaal, geen zwarte frames. Geen surgical splice (alle clips vers gegenereerd), dus het
oude-naad-risico uit CLAUDE.md §12 is hier niet van toepassing.

## Montage

27 clips, genormaliseerd naar 1920×1080/30fps, assemble.py, xfade 0,4s.
Eindlengte: **85,5s** — binnen het 90s-doel.

## Formaten

Op uitdrukkelijk verzoek: eerst 16:9 (het geplande/goedgekeurde formaat), plus een gratis
9:16-afleiding uit dezelfde 16:9-master (center-crop + upscale, geen extra credits). De
verticale crop werkt goed bij scenery-shots (van nature verticaal composeerbaar) maar snijdt
bij sommige bootshots tekst aan de randen af (bijv. "FASOULIAS LINES" wordt "FAS...") — dit is
een bekende beperking van een blinde center-crop, geen bug. Als de klant de 9:16-versie
definitief wil gebruiken, raad ik aan om per shot een handmatige crop-positie te kiezen
(zelfde methode als de portretfoto-fix), of de duurdere native-9:16-generatie (zie hieronder).

**Alternatief voor later**: native 9:16-generatie is getest (testclip, zie eerdere sessie) en
werkt, maar kost evenveel credits per clip als 16:9 — een volledige native 9:16-versie van
deze video zou dus nog eens ±114 credits kosten (huidig saldo 113,5 — niet haalbaar zonder
nieuwe credits).

## Muziek

Track: "Majestic" — Diego Nava (Mixkit Stock Music Free License), zelfde track als bij VCY.
Getrimd naar 85,53s, fade-in 1,5s / fade-out 2s, volume 90%, AAC 192kbps.

## Credits

22 nieuwe clips: 5× 5s/std (7,5cr) + 17× 3s/std (4,5cr) = 37,5 + 76,5 = **114 credits**.
Saldo voor: 227,5. Saldo na: **113,5**.

## Oplevering

- 16:9 met muziek: Fasoulias_Lines_90s_music.mp4 (85,5s) —
  https://d2ol7oe51mr4n9.cloudfront.net/user_3GAnI2MKRZFE3ukZ4ZGqGe45vyC/a3d998e6-0322-4f0c-84c1-a653a272b9b5.mp4
- 9:16 met muziek: Fasoulias_Lines_90s_916_music.mp4 (85,5s) —
  https://d2ol7oe51mr4n9.cloudfront.net/user_3GAnI2MKRZFE3ukZ4ZGqGe45vyC/a38666d0-fbb0-4a43-816f-fc463a5c4153.mp4

## Openstaande punten

1. Saldo is nu 113,5 credits — ruim onder de 300-creditmeldgrens. Voor eventuele
   herkansingen of een native 9:16-versie zijn nieuwe credits nodig.
2. 9:16-versie is een snelle center-crop-afleiding, geen per-shot geoptimaliseerde vertical
   cut — bij definitief gebruik overwegen om dit te verfijnen.
3. Dit is nog geen definitieve klantlevering — Valentijn beoordeelt en levert aan Fasoulias
   Lines.
