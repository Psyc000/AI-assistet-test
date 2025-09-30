import sqlite3

# Verbindung zur Datenbank
conn = sqlite3.connect("faq.db")
c = conn.cursor()

# Tabelle erstellen
c.execute("""
CREATE TABLE IF NOT EXISTS faq (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    question TEXT,
    answer TEXT
)
""")

# Typische FAQs (Restaurant, Fitnessstudio, Friseur etc.)
faqs = [
    ("Restaurant", "Welche Öffnungszeiten habt ihr?", "Wir haben täglich von 11:00 bis 22:00 Uhr geöffnet."),
    ("Restaurant", "Habt ihr vegetarische Gerichte?", "Ja, wir bieten verschiedene vegetarische und vegane Optionen an."),
    ("Restaurant", "Kann man bei euch reservieren?", "Ja, bitte rufen Sie uns an oder reservieren Sie online."),
    ("Fitnessstudio", "Welche Öffnungszeiten habt ihr?", "Wir sind werktags von 6:00 bis 23:00 Uhr und am Wochenende von 8:00 bis 20:00 Uhr geöffnet."),
    ("Fitnessstudio", "Bietet ihr Probetrainings an?", "Ja, das erste Probetraining ist kostenlos."),
    ("Fitnessstudio", "Habt ihr Personal Trainer?", "Ja, unsere zertifizierten Trainer unterstützen Sie gerne."),
    ("Friseur", "Macht ihr auch Färben?", "Ja, wir bieten Färben, Strähnen und Balayage an."),
    ("Friseur", "Braucht man einen Termin?", "Wir empfehlen eine Terminvereinbarung, spontane Besuche sind aber oft auch möglich."),
    ("Friseur", "Welche Preise habt ihr?", "Die Preise variieren je nach Schnitt und Service, ab 25€ für einen Haarschnitt.")
]

# FAQs einfügen
c.executemany("INSERT INTO faq (category, question, answer) VALUES (?, ?, ?)", faqs)

conn.commit()
conn.close()

print("✅ FAQ-Datenbank erstellt und befüllt!")
