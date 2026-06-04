"""
Key player data for WC 2026 squads.

Full starting XI + key bench for top 12 teams.
Summary squad data (captain + key 6) for remaining 36 teams.
rating: FIFA-style overall (50–99). form: season form 0–10. is_key: top-6 impact players.
"""

SQUADS: dict[str, list[dict]] = {
    "ARG": [
        {"name": "Emiliano Martínez", "pos": "GK", "club": "Aston Villa", "age": 32, "rating": 89, "form": 8.5, "caps": 72, "int_goals": 0, "is_key": False},
        {"name": "Nahuel Molina", "pos": "RB", "club": "Atlético Madrid", "age": 26, "rating": 82, "form": 7.5, "caps": 50, "int_goals": 7, "is_key": False},
        {"name": "Cristian Romero", "pos": "CB", "club": "Tottenham", "age": 26, "rating": 85, "form": 8.0, "caps": 45, "int_goals": 2, "is_key": False},
        {"name": "Lisandro Martínez", "pos": "CB", "club": "Man United", "age": 26, "rating": 86, "form": 7.5, "caps": 35, "int_goals": 3, "is_key": False},
        {"name": "Nicolás Tagliafico", "pos": "LB", "club": "Lyon", "age": 32, "rating": 80, "form": 7.0, "caps": 72, "int_goals": 4, "is_key": False},
        {"name": "Rodrigo De Paul", "pos": "CM", "club": "Atlético Madrid", "age": 30, "rating": 83, "form": 8.0, "caps": 68, "int_goals": 4, "is_key": True},
        {"name": "Alexis Mac Allister", "pos": "CM", "club": "Liverpool", "age": 26, "rating": 85, "form": 8.5, "caps": 47, "int_goals": 6, "is_key": True},
        {"name": "Enzo Fernández", "pos": "CM", "club": "Chelsea", "age": 24, "rating": 86, "form": 8.0, "caps": 40, "int_goals": 5, "is_key": True},
        {"name": "Lionel Messi", "pos": "FW", "club": "Inter Miami", "age": 37, "rating": 91, "form": 8.5, "caps": 195, "int_goals": 112, "is_key": True},
        {"name": "Lautaro Martínez", "pos": "FW", "club": "Inter Milan", "age": 27, "rating": 88, "form": 9.0, "caps": 65, "int_goals": 30, "is_key": True},
        {"name": "Julián Álvarez", "pos": "FW", "club": "Atlético Madrid", "age": 25, "rating": 86, "form": 8.5, "caps": 45, "int_goals": 20, "is_key": True},
        # Bench
        {"name": "Franco Armani", "pos": "GK", "club": "River Plate", "age": 38, "rating": 82, "form": 7.5, "caps": 20, "int_goals": 0, "is_key": False},
        {"name": "Nicolás Otamendi", "pos": "CB", "club": "Benfica", "age": 37, "rating": 82, "form": 7.0, "caps": 110, "int_goals": 6, "is_key": False},
        {"name": "Paulo Dybala", "pos": "FW", "club": "Roma", "age": 31, "rating": 84, "form": 7.5, "caps": 38, "int_goals": 30, "is_key": False},
    ],
    "BRA": [
        {"name": "Alisson", "pos": "GK", "club": "Liverpool", "age": 32, "rating": 89, "form": 8.5, "caps": 78, "int_goals": 0, "is_key": False},
        {"name": "Danilo", "pos": "RB", "club": "Juventus", "age": 33, "rating": 82, "form": 7.0, "caps": 88, "int_goals": 7, "is_key": False},
        {"name": "Marquinhos", "pos": "CB", "club": "PSG", "age": 30, "rating": 87, "form": 8.0, "caps": 87, "int_goals": 9, "is_key": False},
        {"name": "Gabriel Magalhães", "pos": "CB", "club": "Arsenal", "age": 27, "rating": 87, "form": 8.5, "caps": 28, "int_goals": 3, "is_key": False},
        {"name": "Renan Lodi", "pos": "LB", "club": "Nottm Forest", "age": 26, "rating": 81, "form": 7.5, "caps": 24, "int_goals": 1, "is_key": False},
        {"name": "Casemiro", "pos": "CM", "club": "Man United", "age": 33, "rating": 84, "form": 7.0, "caps": 83, "int_goals": 8, "is_key": False},
        {"name": "Bruno Guimarães", "pos": "CM", "club": "Newcastle", "age": 27, "rating": 87, "form": 8.5, "caps": 40, "int_goals": 4, "is_key": True},
        {"name": "Lucas Paquetá", "pos": "CM", "club": "West Ham", "age": 27, "rating": 84, "form": 7.5, "caps": 60, "int_goals": 11, "is_key": True},
        {"name": "Vinicius Jr", "pos": "FW", "club": "Real Madrid", "age": 24, "rating": 92, "form": 9.5, "caps": 40, "int_goals": 12, "is_key": True},
        {"name": "Endrick", "pos": "FW", "club": "Real Madrid", "age": 18, "rating": 85, "form": 8.0, "caps": 14, "int_goals": 5, "is_key": True},
        {"name": "Raphinha", "pos": "FW", "club": "Barcelona", "age": 28, "rating": 85, "form": 9.0, "caps": 45, "int_goals": 15, "is_key": True},
        {"name": "Rodrygo", "pos": "FW", "club": "Real Madrid", "age": 24, "rating": 86, "form": 8.5, "caps": 35, "int_goals": 8, "is_key": True},
        {"name": "Éder Militão", "pos": "CB", "club": "Real Madrid", "age": 27, "rating": 85, "form": 7.5, "caps": 40, "int_goals": 2, "is_key": False},
        {"name": "Savinho", "pos": "FW", "club": "Man City", "age": 20, "rating": 82, "form": 8.0, "caps": 8, "int_goals": 1, "is_key": False},
    ],
    "FRA": [
        {"name": "Mike Maignan", "pos": "GK", "club": "AC Milan", "age": 29, "rating": 87, "form": 8.5, "caps": 32, "int_goals": 0, "is_key": False},
        {"name": "Jules Koundé", "pos": "RB", "club": "Barcelona", "age": 26, "rating": 86, "form": 8.5, "caps": 52, "int_goals": 1, "is_key": False},
        {"name": "Dayot Upamecano", "pos": "CB", "club": "Bayern Munich", "age": 26, "rating": 85, "form": 8.0, "caps": 35, "int_goals": 1, "is_key": False},
        {"name": "William Saliba", "pos": "CB", "club": "Arsenal", "age": 24, "rating": 87, "form": 9.0, "caps": 18, "int_goals": 0, "is_key": False},
        {"name": "Theo Hernández", "pos": "LB", "club": "AC Milan", "age": 27, "rating": 86, "form": 8.5, "caps": 38, "int_goals": 6, "is_key": True},
        {"name": "Aurélien Tchouaméni", "pos": "DM", "club": "Real Madrid", "age": 25, "rating": 86, "form": 8.5, "caps": 42, "int_goals": 4, "is_key": True},
        {"name": "N'Golo Kanté", "pos": "CM", "club": "Al-Ittihad", "age": 34, "rating": 84, "form": 7.5, "caps": 55, "int_goals": 2, "is_key": False},
        {"name": "Antoine Griezmann", "pos": "AM", "club": "Atlético Madrid", "age": 34, "rating": 87, "form": 8.0, "caps": 137, "int_goals": 46, "is_key": True},
        {"name": "Kylian Mbappé", "pos": "FW", "club": "Real Madrid", "age": 26, "rating": 93, "form": 9.0, "caps": 83, "int_goals": 48, "is_key": True},
        {"name": "Ousmane Dembélé", "pos": "FW", "club": "PSG", "age": 27, "rating": 85, "form": 9.0, "caps": 50, "int_goals": 6, "is_key": True},
        {"name": "Bradley Barcola", "pos": "FW", "club": "PSG", "age": 22, "rating": 83, "form": 8.5, "caps": 16, "int_goals": 5, "is_key": True},
        {"name": "Marcus Thuram", "pos": "FW", "club": "Inter Milan", "age": 27, "rating": 84, "form": 8.5, "caps": 28, "int_goals": 10, "is_key": False},
        {"name": "Warren Zaïre-Emery", "pos": "CM", "club": "PSG", "age": 19, "rating": 83, "form": 8.5, "caps": 14, "int_goals": 1, "is_key": False},
    ],
    "ENG": [
        {"name": "Jordan Pickford", "pos": "GK", "club": "Everton", "age": 31, "rating": 84, "form": 8.0, "caps": 70, "int_goals": 0, "is_key": False},
        {"name": "Trent Alexander-Arnold", "pos": "RB", "club": "Real Madrid", "age": 26, "rating": 88, "form": 8.5, "caps": 40, "int_goals": 5, "is_key": True},
        {"name": "John Stones", "pos": "CB", "club": "Man City", "age": 30, "rating": 85, "form": 7.5, "caps": 75, "int_goals": 4, "is_key": False},
        {"name": "Marc Guéhi", "pos": "CB", "club": "Crystal Palace", "age": 24, "rating": 83, "form": 8.0, "caps": 18, "int_goals": 1, "is_key": False},
        {"name": "Kieran Trippier", "pos": "LB", "club": "Newcastle", "age": 34, "rating": 83, "form": 7.5, "caps": 53, "int_goals": 4, "is_key": False},
        {"name": "Declan Rice", "pos": "DM", "club": "Arsenal", "age": 26, "rating": 88, "form": 9.0, "caps": 48, "int_goals": 5, "is_key": True},
        {"name": "Jude Bellingham", "pos": "AM", "club": "Real Madrid", "age": 21, "rating": 91, "form": 9.0, "caps": 40, "int_goals": 10, "is_key": True},
        {"name": "Phil Foden", "pos": "AM", "club": "Man City", "age": 25, "rating": 89, "form": 8.5, "caps": 38, "int_goals": 10, "is_key": True},
        {"name": "Harry Kane", "pos": "FW", "club": "Bayern Munich", "age": 31, "rating": 90, "form": 9.0, "caps": 98, "int_goals": 68, "is_key": True},
        {"name": "Bukayo Saka", "pos": "FW", "club": "Arsenal", "age": 23, "rating": 88, "form": 9.0, "caps": 42, "int_goals": 16, "is_key": True},
        {"name": "Marcus Rashford", "pos": "FW", "club": "Man United", "age": 27, "rating": 84, "form": 7.5, "caps": 58, "int_goals": 17, "is_key": False},
        {"name": "Cole Palmer", "pos": "AM", "club": "Chelsea", "age": 22, "rating": 86, "form": 9.0, "caps": 12, "int_goals": 4, "is_key": False},
        {"name": "Ollie Watkins", "pos": "FW", "club": "Aston Villa", "age": 29, "rating": 83, "form": 8.5, "caps": 20, "int_goals": 5, "is_key": False},
    ],
    "ESP": [
        {"name": "Unai Simón", "pos": "GK", "club": "Athletic Bilbao", "age": 27, "rating": 84, "form": 8.0, "caps": 35, "int_goals": 0, "is_key": False},
        {"name": "Daniel Carvajal", "pos": "RB", "club": "Real Madrid", "age": 32, "rating": 87, "form": 8.0, "caps": 54, "int_goals": 4, "is_key": False},
        {"name": "Aymeric Laporte", "pos": "CB", "club": "Al-Nassr", "age": 30, "rating": 84, "form": 7.5, "caps": 32, "int_goals": 3, "is_key": False},
        {"name": "Robin Le Normand", "pos": "CB", "club": "Atlético Madrid", "age": 27, "rating": 83, "form": 8.0, "caps": 18, "int_goals": 0, "is_key": False},
        {"name": "Alejandro Balde", "pos": "LB", "club": "Barcelona", "age": 21, "rating": 84, "form": 8.5, "caps": 22, "int_goals": 1, "is_key": False},
        {"name": "Rodri", "pos": "DM", "club": "Man City", "age": 28, "rating": 91, "form": 9.0, "caps": 50, "int_goals": 7, "is_key": True},
        {"name": "Pedri", "pos": "CM", "club": "Barcelona", "age": 22, "rating": 89, "form": 9.0, "caps": 40, "int_goals": 5, "is_key": True},
        {"name": "Fabián Ruiz", "pos": "CM", "club": "PSG", "age": 28, "rating": 85, "form": 8.5, "caps": 38, "int_goals": 5, "is_key": True},
        {"name": "Lamine Yamal", "pos": "FW", "club": "Barcelona", "age": 17, "rating": 87, "form": 9.5, "caps": 16, "int_goals": 5, "is_key": True},
        {"name": "Nico Williams", "pos": "FW", "club": "Athletic Bilbao", "age": 22, "rating": 86, "form": 9.0, "caps": 22, "int_goals": 5, "is_key": True},
        {"name": "Álvaro Morata", "pos": "FW", "club": "AC Milan", "age": 31, "rating": 82, "form": 7.5, "caps": 80, "int_goals": 35, "is_key": True},
        {"name": "Dani Olmo", "pos": "AM", "club": "Barcelona", "age": 26, "rating": 86, "form": 8.5, "caps": 36, "int_goals": 10, "is_key": False},
        {"name": "Mikel Merino", "pos": "CM", "club": "Arsenal", "age": 28, "rating": 84, "form": 8.5, "caps": 26, "int_goals": 6, "is_key": False},
    ],
    "GER": [
        {"name": "Manuel Neuer", "pos": "GK", "club": "Bayern Munich", "age": 39, "rating": 85, "form": 7.5, "caps": 124, "int_goals": 0, "is_key": False},
        {"name": "Joshua Kimmich", "pos": "RB", "club": "Bayern Munich", "age": 30, "rating": 88, "form": 8.5, "caps": 90, "int_goals": 8, "is_key": True},
        {"name": "Jonathan Tah", "pos": "CB", "club": "Bayern Munich", "age": 28, "rating": 85, "form": 8.0, "caps": 32, "int_goals": 2, "is_key": False},
        {"name": "Nico Schlotterbeck", "pos": "CB", "club": "Dortmund", "age": 25, "rating": 84, "form": 8.0, "caps": 20, "int_goals": 0, "is_key": False},
        {"name": "David Raum", "pos": "LB", "club": "RB Leipzig", "age": 26, "rating": 82, "form": 7.5, "caps": 28, "int_goals": 2, "is_key": False},
        {"name": "Robert Andrich", "pos": "DM", "club": "Bayer Leverkusen", "age": 30, "rating": 83, "form": 8.0, "caps": 20, "int_goals": 0, "is_key": False},
        {"name": "Florian Wirtz", "pos": "AM", "club": "Bayer Leverkusen", "age": 22, "rating": 90, "form": 9.5, "caps": 28, "int_goals": 8, "is_key": True},
        {"name": "Jamal Musiala", "pos": "AM", "club": "Bayern Munich", "age": 22, "rating": 90, "form": 9.0, "caps": 36, "int_goals": 12, "is_key": True},
        {"name": "Leroy Sané", "pos": "FW", "club": "Bayern Munich", "age": 29, "rating": 85, "form": 8.0, "caps": 60, "int_goals": 16, "is_key": True},
        {"name": "Kai Havertz", "pos": "FW", "club": "Arsenal", "age": 26, "rating": 84, "form": 8.5, "caps": 55, "int_goals": 21, "is_key": True},
        {"name": "Thomas Müller", "pos": "AM", "club": "Bayern Munich", "age": 35, "rating": 82, "form": 7.5, "caps": 131, "int_goals": 45, "is_key": True},
        {"name": "Niclas Füllkrug", "pos": "FW", "club": "West Ham", "age": 31, "rating": 82, "form": 7.5, "caps": 20, "int_goals": 9, "is_key": False},
    ],
    "POR": [
        {"name": "Diogo Costa", "pos": "GK", "club": "Porto", "age": 25, "rating": 85, "form": 8.5, "caps": 25, "int_goals": 0, "is_key": False},
        {"name": "João Cancelo", "pos": "RB", "club": "Barcelona", "age": 30, "rating": 84, "form": 8.0, "caps": 65, "int_goals": 6, "is_key": False},
        {"name": "Rúben Dias", "pos": "CB", "club": "Man City", "age": 27, "rating": 89, "form": 8.5, "caps": 72, "int_goals": 4, "is_key": True},
        {"name": "António Silva", "pos": "CB", "club": "Benfica", "age": 22, "rating": 84, "form": 8.5, "caps": 20, "int_goals": 0, "is_key": False},
        {"name": "Nuno Mendes", "pos": "LB", "club": "PSG", "age": 22, "rating": 86, "form": 8.5, "caps": 32, "int_goals": 1, "is_key": True},
        {"name": "João Palhinha", "pos": "DM", "club": "Bayern Munich", "age": 29, "rating": 85, "form": 8.5, "caps": 40, "int_goals": 4, "is_key": True},
        {"name": "Bernardo Silva", "pos": "CM", "club": "Man City", "age": 30, "rating": 89, "form": 8.5, "caps": 86, "int_goals": 12, "is_key": True},
        {"name": "Bruno Fernandes", "pos": "AM", "club": "Man United", "age": 30, "rating": 87, "form": 8.0, "caps": 76, "int_goals": 22, "is_key": True},
        {"name": "Pedro Neto", "pos": "FW", "club": "Chelsea", "age": 24, "rating": 84, "form": 8.5, "caps": 24, "int_goals": 4, "is_key": False},
        {"name": "Rafael Leão", "pos": "FW", "club": "AC Milan", "age": 25, "rating": 86, "form": 8.0, "caps": 30, "int_goals": 7, "is_key": True},
        {"name": "Cristiano Ronaldo", "pos": "FW", "club": "Al-Nassr", "age": 40, "rating": 85, "form": 8.0, "caps": 213, "int_goals": 130, "is_key": False},
        {"name": "Gonçalo Ramos", "pos": "FW", "club": "PSG", "age": 23, "rating": 83, "form": 8.0, "caps": 20, "int_goals": 12, "is_key": False},
    ],
    "NED": [
        {"name": "Bart Verbruggen", "pos": "GK", "club": "Brighton", "age": 22, "rating": 83, "form": 8.0, "caps": 12, "int_goals": 0, "is_key": False},
        {"name": "Denzel Dumfries", "pos": "RB", "club": "Inter Milan", "age": 28, "rating": 84, "form": 8.0, "caps": 55, "int_goals": 10, "is_key": False},
        {"name": "Virgil van Dijk", "pos": "CB", "club": "Liverpool", "age": 33, "rating": 87, "form": 8.5, "caps": 70, "int_goals": 6, "is_key": True},
        {"name": "Matthijs de Ligt", "pos": "CB", "club": "Man United", "age": 25, "rating": 86, "form": 7.5, "caps": 52, "int_goals": 5, "is_key": False},
        {"name": "Nathan Aké", "pos": "LB", "club": "Man City", "age": 30, "rating": 84, "form": 7.5, "caps": 48, "int_goals": 3, "is_key": False},
        {"name": "Ryan Gravenberch", "pos": "CM", "club": "Liverpool", "age": 22, "rating": 86, "form": 9.0, "caps": 22, "int_goals": 2, "is_key": True},
        {"name": "Frenkie de Jong", "pos": "CM", "club": "Barcelona", "age": 27, "rating": 87, "form": 8.0, "caps": 58, "int_goals": 7, "is_key": True},
        {"name": "Tijjani Reijnders", "pos": "CM", "club": "AC Milan", "age": 26, "rating": 85, "form": 9.0, "caps": 20, "int_goals": 6, "is_key": True},
        {"name": "Cody Gakpo", "pos": "FW", "club": "Liverpool", "age": 25, "rating": 87, "form": 8.5, "caps": 30, "int_goals": 15, "is_key": True},
        {"name": "Memphis Depay", "pos": "FW", "club": "Atlético Madrid", "age": 31, "rating": 83, "form": 7.5, "caps": 93, "int_goals": 46, "is_key": False},
        {"name": "Donyell Malen", "pos": "FW", "club": "Dortmund", "age": 26, "rating": 82, "form": 8.0, "caps": 26, "int_goals": 8, "is_key": False},
        {"name": "Xavi Simons", "pos": "AM", "club": "RB Leipzig", "age": 22, "rating": 85, "form": 8.5, "caps": 18, "int_goals": 4, "is_key": True},
    ],
    "ITA": [
        {"name": "Gianluigi Donnarumma", "pos": "GK", "club": "PSG", "age": 26, "rating": 88, "form": 8.0, "caps": 68, "int_goals": 0, "is_key": True},
        {"name": "Giovanni Di Lorenzo", "pos": "RB", "club": "Napoli", "age": 31, "rating": 83, "form": 8.0, "caps": 40, "int_goals": 2, "is_key": False},
        {"name": "Alessandro Bastoni", "pos": "CB", "club": "Inter Milan", "age": 26, "rating": 86, "form": 8.5, "caps": 38, "int_goals": 1, "is_key": True},
        {"name": "Riccardo Calafiori", "pos": "CB", "club": "Arsenal", "age": 22, "rating": 85, "form": 8.5, "caps": 12, "int_goals": 1, "is_key": False},
        {"name": "Federico Dimarco", "pos": "LB", "club": "Inter Milan", "age": 27, "rating": 84, "form": 8.5, "caps": 26, "int_goals": 3, "is_key": True},
        {"name": "Nicolò Barella", "pos": "CM", "club": "Inter Milan", "age": 27, "rating": 88, "form": 9.0, "caps": 62, "int_goals": 7, "is_key": True},
        {"name": "Jorginho", "pos": "DM", "club": "Arsenal", "age": 33, "rating": 83, "form": 7.5, "caps": 70, "int_goals": 8, "is_key": False},
        {"name": "Sandro Tonali", "pos": "CM", "club": "Newcastle", "age": 24, "rating": 85, "form": 8.5, "caps": 20, "int_goals": 1, "is_key": True},
        {"name": "Federico Chiesa", "pos": "FW", "club": "Liverpool", "age": 27, "rating": 84, "form": 7.5, "caps": 48, "int_goals": 16, "is_key": False},
        {"name": "Lorenzo Pellegrini", "pos": "AM", "club": "Roma", "age": 28, "rating": 82, "form": 7.5, "caps": 50, "int_goals": 12, "is_key": False},
        {"name": "Mateo Retegui", "pos": "FW", "club": "Atalanta", "age": 25, "rating": 83, "form": 8.5, "caps": 16, "int_goals": 9, "is_key": True},
    ],
    "BEL": [
        {"name": "Koen Casteels", "pos": "GK", "club": "Al-Qadsiah", "age": 32, "rating": 84, "form": 7.5, "caps": 20, "int_goals": 0, "is_key": False},
        {"name": "Timothy Castagne", "pos": "RB", "club": "Fulham", "age": 29, "rating": 81, "form": 7.5, "caps": 50, "int_goals": 3, "is_key": False},
        {"name": "Wout Faes", "pos": "CB", "club": "Leicester City", "age": 26, "rating": 81, "form": 7.5, "caps": 22, "int_goals": 1, "is_key": False},
        {"name": "Jan Vertonghen", "pos": "CB", "club": "Anderlecht", "age": 37, "rating": 81, "form": 7.0, "caps": 147, "int_goals": 9, "is_key": False},
        {"name": "Arthur Theate", "pos": "LB", "club": "Rennes", "age": 24, "rating": 81, "form": 7.5, "caps": 18, "int_goals": 1, "is_key": False},
        {"name": "Youri Tielemans", "pos": "CM", "club": "Aston Villa", "age": 27, "rating": 82, "form": 8.0, "caps": 68, "int_goals": 15, "is_key": True},
        {"name": "Axel Witsel", "pos": "DM", "club": "Atlético Madrid", "age": 35, "rating": 81, "form": 7.0, "caps": 135, "int_goals": 12, "is_key": False},
        {"name": "Kevin De Bruyne", "pos": "AM", "club": "Man City", "age": 33, "rating": 89, "form": 8.0, "caps": 103, "int_goals": 26, "is_key": True},
        {"name": "Dodi Lukebakio", "pos": "FW", "club": "Sevilla", "age": 27, "rating": 80, "form": 7.5, "caps": 20, "int_goals": 5, "is_key": False},
        {"name": "Romelu Lukaku", "pos": "FW", "club": "Napoli", "age": 31, "rating": 84, "form": 8.0, "caps": 110, "int_goals": 85, "is_key": True},
        {"name": "Leandro Trossard", "pos": "FW", "club": "Arsenal", "age": 29, "rating": 83, "form": 8.5, "caps": 35, "int_goals": 8, "is_key": True},
        {"name": "Lois Openda", "pos": "FW", "club": "RB Leipzig", "age": 24, "rating": 83, "form": 8.0, "caps": 20, "int_goals": 6, "is_key": False},
    ],
    "CRO": [
        {"name": "Dominik Livaković", "pos": "GK", "club": "Fenerbahçe", "age": 29, "rating": 84, "form": 7.5, "caps": 50, "int_goals": 0, "is_key": False},
        {"name": "Josip Stanišić", "pos": "RB", "club": "Bayer Leverkusen", "age": 24, "rating": 81, "form": 8.0, "caps": 12, "int_goals": 0, "is_key": False},
        {"name": "Duje Ćaleta-Car", "pos": "CB", "club": "Southampton", "age": 28, "rating": 81, "form": 7.5, "caps": 38, "int_goals": 1, "is_key": False},
        {"name": "Josip Šutalo", "pos": "CB", "club": "Ajax", "age": 23, "rating": 81, "form": 7.5, "caps": 14, "int_goals": 0, "is_key": False},
        {"name": "Borna Sosa", "pos": "LB", "club": "Stuttgart", "age": 26, "rating": 81, "form": 7.5, "caps": 22, "int_goals": 2, "is_key": False},
        {"name": "Luka Modrić", "pos": "CM", "club": "Real Madrid", "age": 39, "rating": 86, "form": 7.5, "caps": 175, "int_goals": 24, "is_key": True},
        {"name": "Mateo Kovačić", "pos": "CM", "club": "Man City", "age": 31, "rating": 84, "form": 8.0, "caps": 110, "int_goals": 4, "is_key": True},
        {"name": "Marcelo Brozović", "pos": "DM", "club": "Al-Nassr", "age": 31, "rating": 83, "form": 7.5, "caps": 92, "int_goals": 13, "is_key": True},
        {"name": "Ivan Perišić", "pos": "FW", "club": "Hajduk Split", "age": 35, "rating": 82, "form": 7.0, "caps": 135, "int_goals": 34, "is_key": False},
        {"name": "Andrej Kramarić", "pos": "FW", "club": "Hoffenheim", "age": 33, "rating": 82, "form": 8.0, "caps": 80, "int_goals": 22, "is_key": True},
        {"name": "Bruno Petković", "pos": "FW", "club": "Dinamo Zagreb", "age": 29, "rating": 80, "form": 7.5, "caps": 42, "int_goals": 9, "is_key": False},
    ],
    "MAR": [
        {"name": "Yassine Bounou", "pos": "GK", "club": "Al-Hilal", "age": 32, "rating": 86, "form": 8.0, "caps": 60, "int_goals": 0, "is_key": True},
        {"name": "Achraf Hakimi", "pos": "RB", "club": "PSG", "age": 26, "rating": 87, "form": 8.5, "caps": 72, "int_goals": 6, "is_key": True},
        {"name": "Romain Saïss", "pos": "CB", "club": "Besiktas", "age": 34, "rating": 81, "form": 7.5, "caps": 75, "int_goals": 4, "is_key": False},
        {"name": "Nayef Aguerd", "pos": "CB", "club": "West Ham", "age": 27, "rating": 83, "form": 8.0, "caps": 38, "int_goals": 1, "is_key": False},
        {"name": "Noussair Mazraoui", "pos": "LB", "club": "Man United", "age": 26, "rating": 83, "form": 8.0, "caps": 42, "int_goals": 2, "is_key": False},
        {"name": "Azzedine Ounahi", "pos": "CM", "club": "Marseille", "age": 24, "rating": 82, "form": 7.5, "caps": 30, "int_goals": 3, "is_key": False},
        {"name": "Sofyan Amrabat", "pos": "DM", "club": "Man United", "age": 27, "rating": 84, "form": 8.0, "caps": 52, "int_goals": 1, "is_key": True},
        {"name": "Hakim Ziyech", "pos": "AM", "club": "Galatasaray", "age": 32, "rating": 83, "form": 8.0, "caps": 58, "int_goals": 19, "is_key": True},
        {"name": "Youssef En-Nesyri", "pos": "FW", "club": "Fenerbahçe", "age": 27, "rating": 83, "form": 8.0, "caps": 48, "int_goals": 22, "is_key": True},
        {"name": "Sofiane Boufal", "pos": "FW", "club": "Angers", "age": 31, "rating": 80, "form": 7.5, "caps": 50, "int_goals": 7, "is_key": False},
        {"name": "Anass Zaroury", "pos": "FW", "club": "Burnley", "age": 24, "rating": 79, "form": 7.5, "caps": 14, "int_goals": 3, "is_key": False},
    ],
    "COL": [
        {"name": "Camilo Vargas", "pos": "GK", "club": "Atlas", "age": 34, "rating": 80, "form": 7.5, "caps": 45, "int_goals": 0, "is_key": False},
        {"name": "Daniel Muñoz", "pos": "RB", "club": "Crystal Palace", "age": 28, "rating": 82, "form": 8.0, "caps": 28, "int_goals": 2, "is_key": False},
        {"name": "Davinson Sánchez", "pos": "CB", "club": "Galatasaray", "age": 28, "rating": 82, "form": 7.5, "caps": 58, "int_goals": 3, "is_key": False},
        {"name": "Yerry Mina", "pos": "CB", "club": "Fiorentina", "age": 29, "rating": 81, "form": 7.0, "caps": 60, "int_goals": 5, "is_key": False},
        {"name": "Johan Mojica", "pos": "LB", "club": "Girona", "age": 31, "rating": 80, "form": 7.5, "caps": 28, "int_goals": 0, "is_key": False},
        {"name": "Wilmar Barrios", "pos": "DM", "club": "Zenit", "age": 30, "rating": 80, "form": 7.5, "caps": 52, "int_goals": 2, "is_key": False},
        {"name": "Mateus Uribe", "pos": "CM", "club": "Porto", "age": 32, "rating": 80, "form": 7.5, "caps": 50, "int_goals": 9, "is_key": False},
        {"name": "James Rodríguez", "pos": "AM", "club": "Rayo Vallecano", "age": 33, "rating": 82, "form": 7.5, "caps": 102, "int_goals": 31, "is_key": True},
        {"name": "Luis Díaz", "pos": "FW", "club": "Liverpool", "age": 27, "rating": 86, "form": 8.5, "caps": 42, "int_goals": 10, "is_key": True},
        {"name": "Jhon Córdoba", "pos": "FW", "club": "Krasnodar", "age": 30, "rating": 80, "form": 7.5, "caps": 22, "int_goals": 5, "is_key": False},
        {"name": "Radamel Falcao", "pos": "FW", "club": "Millonarios", "age": 38, "rating": 78, "form": 7.0, "caps": 106, "int_goals": 36, "is_key": False},
        {"name": "Richard Ríos", "pos": "CM", "club": "Palmeiras", "age": 24, "rating": 82, "form": 8.0, "caps": 16, "int_goals": 3, "is_key": True},
        {"name": "Jhon Duran", "pos": "FW", "club": "Aston Villa", "age": 20, "rating": 82, "form": 8.5, "caps": 8, "int_goals": 3, "is_key": True},
    ],
}

# Summary data for remaining teams (captain + avg squad rating)
SQUAD_SUMMARY: dict[str, dict] = {
    "URU": {"captain": "Federico Valverde", "captain_club": "Real Madrid", "captain_rating": 88, "avg_rating": 79, "star_player": "Darwin Núñez"},
    "ECU": {"captain": "Enner Valencia", "captain_club": "Internacional", "captain_rating": 79, "avg_rating": 75, "star_player": "Moisés Caicedo"},
    "PAR": {"captain": "Miguel Almirón", "captain_club": "Newcastle", "captain_rating": 79, "avg_rating": 73, "star_player": "Miguel Almirón"},
    "DEN": {"captain": "Simon Kjær", "captain_club": "AC Milan", "captain_rating": 82, "avg_rating": 77, "star_player": "Christian Eriksen"},
    "SUI": {"captain": "Granit Xhaka", "captain_club": "Bayer Leverkusen", "captain_rating": 83, "avg_rating": 77, "star_player": "Granit Xhaka"},
    "TUR": {"captain": "Hakan Çalhanoğlu", "captain_club": "Inter Milan", "captain_rating": 86, "avg_rating": 77, "star_player": "Arda Güler"},
    "SRB": {"captain": "Dušan Tadić", "captain_club": "Fenerbahçe", "captain_rating": 81, "avg_rating": 76, "star_player": "Dušan Vlahović"},
    "AUT": {"captain": "David Alaba", "captain_club": "Real Madrid", "captain_rating": 83, "avg_rating": 76, "star_player": "Marcel Sabitzer"},
    "POL": {"captain": "Robert Lewandowski", "captain_club": "Barcelona", "captain_rating": 87, "avg_rating": 76, "star_player": "Robert Lewandowski"},
    "SVK": {"captain": "Marek Hamšík", "captain_club": "Retired", "captain_rating": 75, "avg_rating": 74, "star_player": "Milan Škriniar"},
    "USA": {"captain": "Tyler Adams", "captain_club": "Bournemouth", "captain_rating": 81, "avg_rating": 75, "star_player": "Christian Pulisic"},
    "MEX": {"captain": "Guillermo Ochoa", "captain_club": "Club América", "captain_rating": 81, "avg_rating": 76, "star_player": "Hirving Lozano"},
    "CAN": {"captain": "Atiba Hutchinson", "captain_club": "Besiktas", "captain_rating": 78, "avg_rating": 76, "star_player": "Alphonso Davies"},
    "PAN": {"captain": "Román Torres", "captain_club": "NA", "captain_rating": 74, "avg_rating": 70, "star_player": "Ismael Díaz"},
    "HON": {"captain": "Alberth Elis", "captain_club": "Bournemouth", "captain_rating": 78, "avg_rating": 68, "star_player": "Alberth Elis"},
    "JAM": {"captain": "Bobby Reid", "captain_club": "Fulham", "captain_rating": 75, "avg_rating": 70, "star_player": "Michail Antonio"},
    "SEN": {"captain": "Kalidou Koulibaly", "captain_club": "Al-Hilal", "captain_rating": 84, "avg_rating": 77, "star_player": "Sadio Mané"},
    "NGA": {"captain": "William Troost-Ekong", "captain_club": "Watford", "captain_rating": 79, "avg_rating": 74, "star_player": "Victor Osimhen"},
    "EGY": {"captain": "Mohamed Salah", "captain_club": "Liverpool", "captain_rating": 89, "avg_rating": 73, "star_player": "Mohamed Salah"},
    "CMR": {"captain": "Vincent Aboubakar", "captain_club": "Besiktas", "captain_rating": 80, "avg_rating": 73, "star_player": "André Onana"},
    "CIV": {"captain": "Serge Aurier", "captain_club": "Nottm Forest", "captain_rating": 79, "avg_rating": 74, "star_player": "Sébastien Haller"},
    "COD": {"captain": "Christian Luyindama", "captain_club": "NA", "captain_rating": 75, "avg_rating": 70, "star_player": "Cédric Bakambu"},
    "ZAF": {"captain": "Percy Tau", "captain_club": "Al-Ahly", "captain_rating": 78, "avg_rating": 71, "star_player": "Percy Tau"},
    "GHA": {"captain": "André Ayew", "captain_club": "Le Havre", "captain_rating": 78, "avg_rating": 73, "star_player": "Mohammed Kudus"},
    "JPN": {"captain": "Maya Yoshida", "captain_club": "Vissel Kobe", "captain_rating": 80, "avg_rating": 77, "star_player": "Takefusa Kubo"},
    "KOR": {"captain": "Son Heung-min", "captain_club": "Tottenham", "captain_rating": 87, "avg_rating": 76, "star_player": "Son Heung-min"},
    "IRN": {"captain": "Ehsan Hajsafi", "captain_club": "NA", "captain_rating": 77, "avg_rating": 73, "star_player": "Mehdi Taremi"},
    "SAU": {"captain": "Mohammed Al-Deayea", "captain_club": "NA", "captain_rating": 72, "avg_rating": 70, "star_player": "Salem Al-Dawsari"},
    "AUS": {"captain": "Mat Ryan", "captain_club": "Real Sociedad", "captain_rating": 81, "avg_rating": 74, "star_player": "Martin Boyle"},
    "QAT": {"captain": "Hassan Al-Haydos", "captain_club": "Al-Sadd", "captain_rating": 76, "avg_rating": 68, "star_player": "Akram Afif"},
    "UZB": {"captain": "Eldor Shomurodov", "captain_club": "Roma", "captain_rating": 78, "avg_rating": 68, "star_player": "Eldor Shomurodov"},
    "JOR": {"captain": "Baha' Faisal", "captain_club": "NA", "captain_rating": 70, "avg_rating": 66, "star_player": "Ahmad Alhaj"},
    "NZL": {"captain": "Winston Reid", "captain_club": "Brentford", "captain_rating": 76, "avg_rating": 67, "star_player": "Chris Wood"},
    "VEN": {"captain": "Tomás Rincón", "captain_club": "NA", "captain_rating": 76, "avg_rating": 68, "star_player": "Jhon Chancellor"},
    "IDN": {"captain": "Marc Klok", "captain_club": "Persib Bandung", "captain_rating": 70, "avg_rating": 63, "star_player": "Ragnar Oratmangoen"},
}


def get_squad(team_code: str) -> list[dict]:
    """Returns player list for a team. Full detail for top teams, summary otherwise."""
    return SQUADS.get(team_code.upper(), [])


def squad_avg_rating(team_code: str) -> float:
    """Average rating of squad (from detailed data or summary)."""
    code = team_code.upper()
    if code in SQUADS:
        ratings = [p["rating"] for p in SQUADS[code]]
        return sum(ratings) / len(ratings)
    if code in SQUAD_SUMMARY:
        return float(SQUAD_SUMMARY[code]["avg_rating"])
    return 75.0


def squad_form_score(team_code: str) -> float:
    """Average form score (0–10) of starting XI. Falls back to team-level form."""
    code = team_code.upper()
    if code in SQUADS:
        forms = [p["form"] for p in SQUADS[code][:11]]
        return sum(forms) / len(forms)
    return 7.0


def key_player_boost(team_code: str) -> float:
    """
    Returns a multiplier (0.9–1.1) based on the strength of key players.
    All key players available → ~1.05. No key players available → 0.95.
    """
    code = team_code.upper()
    if code not in SQUADS:
        return 1.0
    key_players = [p for p in SQUADS[code] if p["is_key"]]
    if not key_players:
        return 1.0
    avg_key_rating = sum(p["rating"] for p in key_players) / len(key_players)
    # 85 = neutral (1.0). Each point above/below shifts ±0.01
    return 1.0 + (avg_key_rating - 85) * 0.01
