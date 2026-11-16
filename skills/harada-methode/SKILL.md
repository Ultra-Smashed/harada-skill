---
name: harada-methode
description: Macht aus einem großen Ziel einen kompletten Plan nach der Harada-Methode, mit der Shohei Ohtani als Schüler seine Ziele geplant hat. Ergebnis ist eine druckfertige Seite mit drei Teilen. Das 64er-Raster (ein Ziel, acht Bereiche, 64 konkrete Schritte), eine Routine-Checkliste zum Abhaken für einen Monat und eine Tagebuchseite für jeden Tag. Benutze diesen Skill immer, wenn jemand die Harada-Methode, das Ohtani-Raster, eine Mandala-Chart, ein 9×9-Raster, Open Window 64, einen Zielplan, ein Ziel in Schritte zerlegen, Ziele erreichen, Vorsätze, Gewohnheiten für ein Ziel oder einen Plan für ein großes Vorhaben möchte, auch bei „help me reach my goal“, „break down my goal“, „Harada method“.
---

# Harada-Methode

Aus einem Ziel wird ein Plan, den man an die Wand hängen kann: eine einzige HTML-Datei mit drei druckfertigen Seiten.

1. **Raster:** Ziel mit Deadline in der Mitte, acht Bereiche drumherum, und jeder Bereich hat acht konkrete Schritte. Dazu das Warum.
2. **Routine-Checkliste:** bis zu zehn tägliche Routinen aus dem Raster, ein Monat zum Abhaken.
3. **Tagebuch:** eine Seite pro Tag mit Top-5-Aufgaben, Tagesplan, Routinen, Bewertung und Rückblick.

`assets/vorlage.html` enthält Gestaltung, Druck-Layout und die Logik. Du lieferst nur den Inhalt als JSON. Dadurch bleibt deine Aufmerksamkeit beim Plan, nicht beim Layout.

## Ablauf

### 1. Fragen stellen, einmal

Die Fragen sind Teil des Werts. Ein Plan, der die Lage des Menschen kennt, ist besser als einer aus der Schublade. Stell sie in **einer** Nachricht, nummeriert, höchstens fünf:

1. Was genau ist dein Ziel, und bis wann? (messbar, mit Datum)
2. Warum willst du das? Was hast du davon, und was haben andere davon?
3. Wo stehst du gerade?
4. Wie viel Zeit hast du pro Tag oder pro Woche dafür?
5. Woran ist es bisher gescheitert, oder was könnte dich aufhalten?

Hat der Mensch einige davon schon beantwortet, frag nur den Rest. Hat er alles beantwortet, frag gar nicht. Ist das Ziel unscharf („fitter werden“), schlag in Frage 1 eine messbare Fassung vor („Halbmarathon unter 2 Stunden bis 30. Juni“).

### 2. Bereiche vorschlagen

Lies `references/methode.md`. Dort stehen die Regeln für gute Bereiche und Schritte und Beispiele.

Schlag acht Bereiche vor, je zwei bis vier Wörter. Sie decken zusammen die vier Seiten der Methode ab: **Geist** (Einstellung, Motivation), **Können** (Fähigkeiten, Wissen), **Körper** (Energie, Gesundheit) und **Alltag** (Gewohnheiten, Umfeld). Mindestens ein Bereich dient anderen Menschen. Das ist ein Kern der Harada-Methode, und bei Ohtani hießen solche Felder „Menschlichkeit“ und „Glück“.

Zeig die acht als kurze Liste mit je einem Halbsatz, warum, und frag, ob sie passen. Das ist die einzige zweite Rückfrage. Antwortet der Mensch nicht oder sagt „mach einfach“, nimm deinen Vorschlag.

### 3. Den Plan ausarbeiten

Schreibe für jeden Bereich acht Schritte. Jeder Schritt:

- beginnt mit einem Verb oder einer Zahl und ist so konkret, dass man heute damit anfangen kann
- ist entweder eine **Routine** (`"typ": "R"`, wiederkehrend, mit Häufigkeit: „Jeden Tag 10 Hooks schreiben“) oder eine **Aufgabe** (`"typ": "A"`, einmalig: „Feste Drehtage im Kalender blocken“)
- passt zur Zeit, die der Mensch genannt hat. Wer 30 Minuten am Tag hat, bekommt keine zehn täglichen Routinen.
- hat höchstens 45 Zeichen, damit er im Raster lesbar bleibt

Dazu:

- **Warum** in vier Feldern: für mich greifbar, für mich nicht greifbar, für andere greifbar, für andere nicht greifbar. Je ein kurzer Satz aus den Antworten des Menschen. Erfinde keinen Zweck, den er nicht genannt hat. Fehlt etwas, formuliere vorsichtig aus dem Ziel heraus.
- **Routinen:** fünf bis zehn der wichtigsten täglichen Routinen aus dem Raster, wortgleich oder kürzer. Sie kommen in die Checkliste und ins Tagebuch.
- **Satz:** ein kurzer Leitsatz für das Tagebuch, in den Worten des Menschen, wenn er einen hat.

Bei Zielen zu Gesundheit, Gewicht oder Geld: keine extremen oder riskanten Schritte (Crash-Diät, Training trotz Schmerz, Schulden, Wetten). Ist das Ziel selbst riskant, sag es einmal freundlich und schlag eine gesündere Fassung vor.

### 4. Bauen

Schreibe den Plan als `plan.json` nach diesem Schema (vollständiges Beispiel: `beispiele/follower.json`):

```json
{
  "sprache": "de",
  "name": "Chris",
  "ziel": "100.000 Instagram-Follower",
  "deadline": "31.12.2026",
  "start": "Aktuell rund 75.000 Follower",
  "warum": {
    "ich_greifbar": "…", "ich_ungreifbar": "…",
    "andere_greifbar": "…", "andere_ungreifbar": "…"
  },
  "bereiche": [
    { "name": "Hooks & Skripte", "schritte": [ { "text": "Jeden Tag 10 Hooks schreiben", "typ": "R" } ] }
  ],
  "routinen": ["Jeden Tag ein Reel posten"],
  "satz": "Jeden Tag ein Reel besser als gestern."
}
```

`bereiche` hat genau 8 Einträge mit je genau 8 Schritten. `name` und `start` sind optional. `sprache` ist `de` oder `en` und richtet sich nach der Sprache des Menschen.

Dann:

```bash
python3 scripts/bauen.py plan.json harada-<kurzname>.html
```

Das Skript prüft den Plan (Anzahl, Längen, Typen, doppelte Schritte) und setzt ihn in die Vorlage ein. Meldet es Fehler, behebe sie im JSON und baue neu. Warnungen zu langen Texten: kürzen.

Falls du keine Befehle ausführen kannst: Gib `assets/vorlage.html` vollständig und unverändert aus und ersetze nur `/*__PLAN__*/null` durch dein JSON. Prüfe die Regeln aus Schritt 3 dann selbst.

### 5. Abgeben

- In der Claude-App: als HTML-Artifact, damit es sofort angezeigt wird.
- In Claude Code: als Datei im Projektordner, mit dem Hinweis, sie im Browser zu öffnen.

Die Antwort dazu ist kurz:

- ein Satz, was entstanden ist
- **Ändern:** Jedes Feld lässt sich direkt anklicken und überschreiben.
- **Drucken:** Knopf „Drucken“ oder Strg/Cmd + P, „Als PDF speichern“ geht auch. Das Raster und das Tagebuch drucken im Hochformat, die Checkliste im Querformat. Die Tagebuchseite einfach öfter drucken.
- **So geht's weiter:** Raster sichtbar aufhängen, jeden Tag die Routinen abhaken, abends die Tagebuchseite füllen, am Monatsende die Prozentzahl eintragen und den Plan anpassen.
- zwei Vorschläge für den nächsten Schritt, jeder ein Satz, den der Mensch einfach zurückschicken kann (zum Beispiel „Mach mir einen Wochenplan für die ersten sieben Tage“).

Erwähne nicht, wie der Skill technisch arbeitet.

## Nachfassen

Kommt der Mensch später zurück („Monat eins ist rum, 60 % Routinen geschafft“), hilf ihm, den Plan anzupassen: Routinen, die nie klappen, kleiner machen oder ersetzen, erledigte Aufgaben durch neue ersetzen, und eine neue Seite bauen.
