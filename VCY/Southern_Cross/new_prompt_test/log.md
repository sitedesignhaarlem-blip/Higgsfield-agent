# Southern Cross — test van Valentijns nieuwe prompts (19-11-2026)
Doel: nieuwe prompt 1 (foto verbeteren) + prompt 2 (walkthrough, ~25-40s) uitproberen op de Southern Cross-foto's uit `vcy videosouthern cross_3.zip` (44 foto's: 21 hutten, 23 overig).

## Kosten (saldo 75 -> 28)
- Prompt 1, test op 1 foto (salon): 2 cr. Aangevraagd Nano Banana Pro 2K, het systeem draaide Nano Banana 2. Job 3fdd7ae0-9abb-4bce-9ef6-9dc32238675b.
- Prompt 2: 8 clips Kling 3.0 std, sound off, 16:9 = 45 cr (30,3s). Geen herkansingen.

## Prompt 1 — resultaat: NIET gebruikt
Verbeterde salonfoto veranderde de geometrie (linker bank, tafelpositie, bredere ruimte), ondanks 'geometry lock' in de prompt. Zie `enhancement_test_salon_before_after.jpg`. Besluit Valentijn: zonder verbetering verder; de overige 7 foto's zijn niet verbeterd. Voor een boot die klanten kunnen boeken is een andere bank/tafel onaanvaardbaar (zie CLAUDE.md §12 laag 2).

## Prompt 2 — uitvoering
Foto's (originelen, 4:3 -> 16:9 bijgesneden, 1920x1080): exterieur (2025-aquila...), flybridge (a41a66ea), helm (4b9481c6), voordek (651f28e2), achterdek (8395cb94), salon (4bcec540), hoofdhut A2 (SC cabin A2), drone-sluitshot (dji ...120416). Foto 04 (26_4.jpg, mensen op paddleboards) niet gebruikt.
Volgorde = VCY-volgorde (sectie 6), alleen de 8 beste foto's, niet de hele reeks. Eén cameramove per shot binnen de gefotografeerde ruimte, harde cuts (geen crossfade), 24 fps.
| # | Shot | Duur | Move | Job |
|---|---|---|---|---|
| 1 | Exterieur | 5s | tracking mee met de boot | 000e88a3-78fd-4bc6-af2b-1cda77748955 |
| 2 | Flybridge | 4s | lateraal slider links-rechts | ef8b679e-b19e-4a7d-bb63-96fd220aba26 |
| 3 | Helm | 3s | dolly-in | f0785abb-6b53-4e39-b372-e773bdf3a9c1 |
| 4 | Voordek | 3s | voorwaartse glijbeweging | 011c9e53-d1ac-407f-ba0b-c42a6d7e696c |
| 5 | Achterdek | 4s | lateraal slider | 2120468b-2c29-44ed-bc37-be3ddc82b404 |
| 6 | Salon | 4s | dolly-in | 499158ed-c9f0-41d7-a490-3b3480607de7 |
| 7 | Hoofdhut | 4s | dolly-in | 20847f63-43f1-45f0-a5a8-afcf746dedbe |
| 8 | Drone-sluitshot | 3s | zachte push-in | 82949d4c-4041-4b24-bacb-4550322a9ae6 |
Media_id's (16:9-crops): 1 ad6cbe9f-fdf9-4919-a515-48412011f135, 2 fbd31937-068a-43d5-9def-af52322e4235, 3 3598720c-72f3-4415-bf91-6e99ec75e52d, 4 d2ec2ae1-a672-46eb-9e12-208466867a6c, 5 6d103714-55a0-4d66-a137-1f3fb91263bf, 6 1eecd874-445c-42b0-89cc-16e0a4af4063, 7 3bca93be-3623-406b-9342-43983d6403e8, 8 6d2c24bb-8ce4-4dc2-8b8d-45825e2bd09b.

## QC (laag 2, contactsheets in sheets/)
Alle 8 clips: geen mensen, geen tekst, geen verzonnen meubels of boten, geometrie stabiel. Kanttekeningen: clip 4 (voordek) de reling lijkt wat naar rechts te schuiven ten opzichte van de zonnebank; clip 8 (drone) de boot draait licht mee (meer een lichte orbit dan een push-in). qc_check.py (laag 1, incl. TEXT-OCR) NIET gedraaid: geen OCR beschikbaar in deze omgeving.

## Montage
Genormaliseerd 1920x1080 24fps (Kling std levert 1280x720, dus opgeschaald, geen echte 1080p), harde cuts, muziek Majestic (zelfde track als VCY) fade-in 1,5s/fade-out 2s. Resultaat 30,33s. Bestand `Southern_Cross_new_prompt_test.mp4` (37 MB) staat niet in de repo.

## Besluit Valentijn (19-11-2026)
Het nieuwe prompt-concept (prompt 1 foto's verbeteren + prompt 2 walkthrough met harde cuts en één move per shot) bevalt niet. We blijven voortaan bij de bestaande werkwijze uit CLAUDE.md (start+end-frames, promptbibliotheek, crossfade 0,4s, QC in twee lagen). De bestanden in deze map zijn alleen een proef en worden niet gebruikt.
