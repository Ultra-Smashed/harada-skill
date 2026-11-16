# Harada-Methode

Ein Skill für Claude. Du nennst dein Ziel, Claude stellt dir ein paar Fragen und baut daraus deinen kompletten Plan nach der Harada-Methode, mit der Shohei Ohtani schon als Schüler seine Ziele geplant hat. Kostenlos, MIT-Lizenz.

Heraus kommt eine einzige HTML-Datei mit drei druckfertigen Seiten:

| Seite | Was drauf ist |
| --- | --- |
| **Raster** | Dein Ziel mit Deadline in der Mitte, acht Bereiche drumherum, 64 konkrete Schritte, dazu dein Warum |
| **Routine-Checkliste** | Bis zu zehn tägliche Routinen aus dem Raster, ein Monat zum Abhaken |
| **Tagebuch** | Eine Seite pro Tag: Top 5, Tagesplan, Routinen, Bewertung, Rückblick |

Ein fertiges Beispiel liegt im Ordner [`demos/`](demos/). Herunterladen und im Browser öffnen.

## Installation

### Claude-App (Web, Desktop)

1. [`harada-methode.zip`](https://github.com/Ultra-Smashed/harada-skill/raw/main/harada-methode.zip) herunterladen.
2. In Claude unter **Settings → Capabilities** den Schalter **Code execution and file creation** einschalten. In der neueren Ansicht heißt er **Create and edit files**.
3. **Customize → Skills** öffnen, auf **+** klicken, dann **Create skill → Upload a skill** und die ZIP-Datei wählen.

Die Menünamen stehen hier so, wie Anthropic sie in der Hilfe nennt. In der deutschen Oberfläche können sie übersetzt sein.

### Claude Code

Als Plugin:

```
/plugin marketplace add Ultra-Smashed/harada-skill
/plugin install harada-methode@harada-methode
```

Oder den Ordner kopieren:

```bash
git clone https://github.com/Ultra-Smashed/harada-skill.git
cp -r harada-skill/skills/harada-methode ~/.claude/skills/
```

Nur für ein Projekt: denselben Ordner nach `.claude/skills/` im Projekt kopieren. Zum Zusammensetzen der Datei braucht der Skill Python 3.

## Benutzen

Schreib einfach dein Ziel, zum Beispiel:

> Hilf mir mit der Harada-Methode: Ich will bis 30. Juni einen Halbmarathon unter 2 Stunden laufen.

Claude fragt dann nach, was noch fehlt (Warum, Ausgangslage, Zeit, Hindernisse), schlägt acht Bereiche vor und baut nach deinem Okay den kompletten Plan.

In der fertigen Seite:

- **Ändern:** Jedes Feld anklicken und überschreiben.
- **Drucken:** Knopf „Drucken“ oder Strg/Cmd + P. „Als PDF speichern“ geht auch. Raster und Tagebuch drucken im Hochformat, die Checkliste im Querformat.
- **Tagebuch:** Die Seite für jeden Tag neu drucken.

Nach einem Monat: Prozent pro Routine eintragen, Claude die Zahlen schicken und den Plan anpassen lassen.

## Die Methode in Kürze

Takashi Harada war Sportlehrer an einer Mittelschule in Osaka und hat die Methode für seine Schülerinnen und Schüler entwickelt. Sie hat vier Werkzeuge: ein Blatt für das Ziel und das Warum, das 64er-Raster, eine Routine-Checkliste und ein Tagebuch. Die acht Bereiche decken vier Seiten ab, die nach Harada zusammengehören: Geist, Können, Körper und Alltag. Dazu kommt mindestens ein Bereich, der anderen Menschen dient.

## Dateien

```
skills/harada-methode/SKILL.md              Ablauf, Fragen, Regeln
skills/harada-methode/references/methode.md Hintergrund, Regeln für Bereiche und Schritte, Beispiele
skills/harada-methode/assets/vorlage.html   Druckvorlage mit Raster, Checkliste und Tagebuch
skills/harada-methode/scripts/bauen.py      prüft den Plan und setzt ihn in die Vorlage ein
skills/harada-methode/beispiele/            Beispielplan als JSON
harada-methode.zip                          derselbe Skill-Ordner als ZIP für die Claude-App
demos/                                      fertiges Beispiel als HTML
.claude-plugin/                             plugin.json, marketplace.json
```

Nach einer Änderung im Skill-Ordner die ZIP neu bauen: `cd skills && zip -r ../harada-methode.zip harada-methode`.

MIT-Lizenz, siehe [LICENSE](LICENSE). Von [Christopher Thanisch](https://thanisch.co).
