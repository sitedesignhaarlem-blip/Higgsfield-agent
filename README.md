# Setup — Villa Video Agent in Claude Code

## 1. Map plaatsen
Zet deze map (`villa-video-agent/`) ergens lokaal neer, bijv. op je Desktop of in Documenten.
Open die map in Claude Code (desktop app).

## 2. MCP-connectors koppelen
Claude Code moet toegang hebben tot dezelfde connectors die je nu in de Claude-app gebruikt:
- **Higgsfield** (voor het genereren van de clips)
- **Google Drive** (voor het ophalen van de foto's per villa)

Dit stel je in via de MCP-instellingen van Claude Code — zelfde koppelingen als in je
browser/app-account, dus geen nieuwe accounts nodig.

## 3. ffmpeg checken
Open een terminal en test:
```
ffmpeg -version
```
Zie je een versienummer? Dan is dit klaar. Zo niet, installeer ffmpeg eerst
(op Mac: `brew install ffmpeg`, op Windows: via winget of de ffmpeg site).

## 4. villas.csv invullen
Open `villas.csv` en vul per villa een rij in:
```
villa_naam,drive_folder_link,status,notes
Villa The Rock,https://drive.google.com/drive/folders/XXXXX,todo,
```
Laat `status` op `todo` staan — dat vertelt de agent welke villa's nog gedaan moeten worden.

## 5. Starten
Zeg tegen Claude Code, bijvoorbeeld:
> "Verwerk de eerste 2 villa's uit villas.csv als test"

of later, als de test goed is:
> "Verwerk alle villa's met status todo uit villas.csv"

Claude Code volgt dan automatisch het draaiboek in `CLAUDE.md` — geen handmatige
tussenstappen meer nodig zoals in de chat.

## Aanbevolen volgorde
1. Eerst 2-3 villa's als test laten draaien.
2. Output checken op kwaliteit (camera-beweging, volgorde, montage).
3. Pas daarna de rest van de 200 in batches laten verwerken (bijv. per 10-20 tegelijk,
   zodat je tussentijds kunt controleren en niet in één keer je hele credit-budget verbruikt).
