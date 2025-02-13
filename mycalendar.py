import csv
import calendar

# Traduction des noms des mois en français
MOIS_FR = [
    "Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
    "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"
]

def generate_calendar(year):
    months = []
    for month in range(1, 13):
        month_days = []
        cal = calendar.monthcalendar(year, month)
        for week in cal:
            week_days = [day if day != 0 else '' for day in week]  # Remplace les zéros par ''
            month_days.append(week_days)
        months.append((MOIS_FR[month - 1], month_days))  # Utilise le nom du mois en français
    return months

def save_to_csv(months, filename, group_size=3):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        for i in range(0, len(months), group_size):
            group = months[i:i + group_size]

            # Écrit les noms des mois
            row = []
            for month, _ in group:
                row.extend([month] + [''] * 6)  # Nom du mois centré sur 7 colonnes
            writer.writerow(row)

            # Écrit les en-têtes des jours
            row = []
            for _ in group:
                row.extend(["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"])
            writer.writerow(row)

            # Trouve le nombre max de semaines dans le groupe
            max_weeks = max(len(weeks) for _, weeks in group)

            # Remplit les semaines
            for week_idx in range(max_weeks):
                row = []
                for _, weeks in group:
                    if week_idx < len(weeks):
                        row.extend(weeks[week_idx])  # Ajoute la semaine actuelle
                    else:
                        row.extend([''] * 7)  # Remplit avec des vides
                writer.writerow(row)
            
            writer.writerow([])  # Séparation entre groupes

year = 2025
months = generate_calendar(year)
save_to_csv(months, 'calendrier_2025.csv')

print("✅ Fichier 'calendrier_2025.csv' généré avec succès ! 📅")

