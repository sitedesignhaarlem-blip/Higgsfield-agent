# Goelette Alliance — log
## 18-11-2026
- Saldo voor start: 100,5 credits (starter). Genjutsu/Genjutsu Lite (motion transfer, gratis rondes) niet bruikbaar voor deze sample.
- Foto's: crops 16:9 geüpload; media_id's: 1=15bdbd94-8d69-49ec-9bc5-48edab09ef15, 2=d50539d2-0afb-4a31-b573-0da29bf9b760, 3=66ae5ae7-6982-4b38-9182-e1d0051c1edb, 4=59e0a30b-e1ed-4047-8e4e-1045ff55dcf0, 5=0e3ef552-f6e0-4a1c-86bd-3ea9187522ac
- Testclip 1: job 0f1775a6-edeb-410d-9293-e7a4828a051c, kling3_0 std 5s sound off 16:9, 7,5 cr. Prompt: dolly forward, smooth moderately-paced constant speed, standaardstaart + no boat name, no additional boats, no birds.
  URL (door Higgsfield): https://d8j0ntlcm91z4.cloudfront.net/user_3GAnI2MKRZFE3ukZ4ZGqGe45vyC/hf_20261118_121823_0f1775a6-edeb-410d-9293-e7a4828a051c.mp4
  Bestand lokaal: clips/raw/01_exterior.mp4 (1280x720, 24fps, 5,04s).
- QC laag 2 (contactsheet, 12 frames): stabiel, rustige dolly, zeilen/rompijnen/want blijven consistent, geen tekst, geen extra boten of dieren. De kleine figuurtjes op het dek komen uit de bronfoto en blijven klein. qc_check.py niet gedraaid voor deze testclip.
- WACHT op feedback Valentijn voor clips 2-5 (18 cr, saldo na test: 93).

## 18-11-2026 — clips 2-5 en montage
- Saldo voor: 93. Clips 2-5 (kling3_0 std, 3s, geen geluid, 16:9, 4,5 cr per clip = 18 cr), saldo daarna 75. Geen herkansingen.
  - 2 (Shootingvoilier, profiel-orbit): job c558f67a-cb42-4f76-a721-dfecf6b22c28
  - 3 (DSC06298, zijwaartse glijbeweging rotspunt): job 393aee85-1bf4-4787-b948-590f71b26647
  - 4 (zonsondergang, push-in): job f17979e9-4c4d-4444-849f-e559696d9a0d
  - 5 (voordek Oude Haven, glijbeweging): job 518c581f-2394-412d-a287-23ea02d93625
- QC laag 2 (contactsheets qc/02-05): alle vier stabiel, geen tekst/bootnaam, geen extra boten of meubels. Clip 3: schoener wordt iets kleiner t.o.v. de rots (normale camerabeweging). Clip 4: een paar piepkleine donkere stipjes in de lucht komen ook in de bronfoto voor. Clip 5: bron 800px, iets zachter. qc_check.py (laag 1, incl. TEXT) NIET gedraaid in deze sessie: geen OCR beschikbaar.
- Montage: genormaliseerd 1920x1080 30fps, assemble.py xfade 0,4s -> 15,57s, muziek Majestic (fade-in 1,5s, fade-out 2s) -> output/Goelette_Alliance.mp4 (stille versie output/silent.mp4).
- Transition QC: middenframes van alle 4 naden bekeken (qc/transitions.jpg). Naad 1-3 tonen tijdens de dissolve twee schoeners over elkaar (verwacht bij een 0,4s crossfade tussen twee scheepsfoto's, ~0,2s zichtbaar). Niet als defect gemarkeerd; alternatief bij klacht: kortere xfade of harde cut.

## 18-11-2026 — laatste clip verwijderd (opdracht Valentijn)
- Clip 5 (voordek Oude Haven) uit de montage gehaald (bestanden bewaard in clips/removed/). Nieuwe sample: 4 clips, 12,93s, 1920x1080, met muziek (output/Goelette_Alliance.mp4, 10,3 MB, sha256 d54f42f9...). Geen extra credits; 4,5 cr van clip 5 was al uitgegeven. Saldo 75.
- Mailconcept NIET aangemaakt: de Gmail-koppeling accepteert maximaal ~3,1 MB aan bijlagen per aanroep, de video is 10,3 MB. Open vraag aan Valentijn: link in plaats van bijlage.
