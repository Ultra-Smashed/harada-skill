#!/usr/bin/env python3
"""Setzt einen Harada-Plan (JSON) in die Vorlage ein und prüft ihn vorher.

Aufruf:  python3 scripts/bauen.py plan.json harada-ziel.html
"""
import json
import sys
from pathlib import Path

PLATZHALTER = "/*__PLAN__*/null"
MAX_SCHRITT = 45
MAX_BEREICH = 28
MAX_ROUTINE = 40


def pruefen(plan):
    fehler, warnungen = [], []

    def text(wert, wo):
        if not isinstance(wert, str) or not wert.strip():
            fehler.append(f"{wo} fehlt oder ist leer.")
            return ""
        return wert.strip()

    text(plan.get("ziel"), "„ziel“")
    text(plan.get("deadline"), "„deadline“")
    if plan.get("sprache", "de") not in ("de", "en"):
        fehler.append("„sprache“ muss „de“ oder „en“ sein.")

    warum = plan.get("warum") or {}
    for k in ("ich_greifbar", "ich_ungreifbar", "andere_greifbar", "andere_ungreifbar"):
        if not str(warum.get(k, "")).strip():
            warnungen.append(f"„warum.{k}“ ist leer.")

    bereiche = plan.get("bereiche")
    if not isinstance(bereiche, list) or len(bereiche) != 8:
        fehler.append(f"„bereiche“ braucht genau 8 Einträge, hat {len(bereiche) if isinstance(bereiche, list) else 0}.")
        bereiche = bereiche if isinstance(bereiche, list) else []

    gesehen = {}
    namen = set()
    for i, b in enumerate(bereiche, 1):
        name = text(b.get("name") if isinstance(b, dict) else None, f"Bereich {i}: „name“")
        if len(name) > MAX_BEREICH:
            warnungen.append(f"Bereich {i} „{name}“ hat {len(name)} Zeichen, besser höchstens {MAX_BEREICH}.")
        if name.lower() in namen:
            fehler.append(f"Bereich „{name}“ kommt doppelt vor.")
        namen.add(name.lower())
        schritte = b.get("schritte") if isinstance(b, dict) else None
        if not isinstance(schritte, list) or len(schritte) != 8:
            fehler.append(f"Bereich {i} „{name}“ braucht genau 8 Schritte, hat {len(schritte) if isinstance(schritte, list) else 0}.")
            continue
        routinen = 0
        for j, s in enumerate(schritte, 1):
            wo = f"Schritt {i}.{j}"
            t = text(s.get("text") if isinstance(s, dict) else None, wo)
            typ = s.get("typ") if isinstance(s, dict) else None
            if typ not in ("R", "A"):
                fehler.append(f"{wo} „{t}“: „typ“ muss „R“ (Routine) oder „A“ (Aufgabe) sein.")
            routinen += typ == "R"
            if len(t) > MAX_SCHRITT:
                warnungen.append(f"{wo} „{t}“ hat {len(t)} Zeichen, bitte auf höchstens {MAX_SCHRITT} kürzen.")
            schluessel = t.lower()
            if schluessel in gesehen:
                fehler.append(f"{wo} „{t}“ steht schon bei {gesehen[schluessel]}.")
            gesehen[schluessel] = wo
        if routinen == 0:
            warnungen.append(f"Bereich „{name}“ hat keine einzige Routine.")
        if routinen == 8:
            warnungen.append(f"Bereich „{name}“ hat nur Routinen, keine einmalige Aufgabe.")

    rl = plan.get("routinen")
    if not isinstance(rl, list) or not (1 <= len(rl) <= 10):
        fehler.append("„routinen“ braucht 1 bis 10 Einträge.")
    else:
        if len(rl) < 5:
            warnungen.append(f"Nur {len(rl)} Routinen für die Checkliste, empfohlen sind 5 bis 10.")
        for r in rl:
            r = text(r, "Eintrag in „routinen“")
            if len(r) > MAX_ROUTINE:
                warnungen.append(f"Routine „{r}“ hat {len(r)} Zeichen, besser höchstens {MAX_ROUTINE}.")

    return fehler, warnungen


def main():
    if len(sys.argv) != 3:
        print(__doc__.strip())
        sys.exit(2)
    quelle, ziel = Path(sys.argv[1]), Path(sys.argv[2])
    try:
        plan = json.loads(quelle.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"FEHLER: {quelle} ist kein gültiges JSON: {e}")
        sys.exit(1)

    fehler, warnungen = pruefen(plan)
    for w in warnungen:
        print("WARNUNG:", w)
    for f in fehler:
        print("FEHLER:", f)
    if fehler:
        print(f"\n{len(fehler)} Fehler. Bitte im JSON beheben und neu bauen.")
        sys.exit(1)

    vorlage = (Path(__file__).resolve().parent.parent / "assets" / "vorlage.html").read_text(encoding="utf-8")
    if PLATZHALTER not in vorlage:
        print("FEHLER: Platzhalter in assets/vorlage.html nicht gefunden.")
        sys.exit(1)
    daten = json.dumps(plan, ensure_ascii=False, indent=1).replace("</", "<\\/")
    ziel.write_text(vorlage.replace(PLATZHALTER, daten), encoding="utf-8")
    print(f"OK: {ziel} gebaut" + (f", {len(warnungen)} Warnung(en)." if warnungen else "."))


if __name__ == "__main__":
    main()
