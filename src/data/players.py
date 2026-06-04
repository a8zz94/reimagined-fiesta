"""
Key player data for WC 2026 squads.

Full starting XI + key bench for top 12 teams.
Summary squad data (captain + key 6) for remaining 36 teams.
rating: FIFA-style overall (50–99). form: season form 0–10. is_key: top-6 impact players.
"""

SQUADS: dict[str, list[dict]] = {
    "ARG": [
        # Goalkeepers
        {"name": "Emiliano Martínez", "pos": "GK", "club": "Aston Villa", "age": 32, "rating": 89, "form": 8.5, "caps": 72, "int_goals": 0, "is_key": False},
        {"name": "Juan Musso", "pos": "GK", "club": "Atlético Madrid", "age": 30, "rating": 82, "form": 7.5, "caps": 28, "int_goals": 0, "is_key": False},
        {"name": "Gerónimo Rulli", "pos": "GK", "club": "Marseille", "age": 33, "rating": 81, "form": 7.5, "caps": 18, "int_goals": 0, "is_key": False},
        # Defenders
        {"name": "Leonardo Balerdi", "pos": "CB", "club": "Marseille", "age": 25, "rating": 80, "form": 7.5, "caps": 8, "int_goals": 0, "is_key": False},
        {"name": "Nicolás Tagliafico", "pos": "LB", "club": "Lyon", "age": 32, "rating": 80, "form": 7.0, "caps": 72, "int_goals": 4, "is_key": False},
        {"name": "Gonzalo Montiel", "pos": "RB", "club": "River Plate", "age": 28, "rating": 79, "form": 7.5, "caps": 40, "int_goals": 2, "is_key": False},
        {"name": "Lisandro Martínez", "pos": "CB", "club": "Man Utd", "age": 27, "rating": 86, "form": 7.5, "caps": 35, "int_goals": 3, "is_key": False},
        {"name": "Cristian Romero", "pos": "CB", "club": "Tottenham", "age": 26, "rating": 86, "form": 8.0, "caps": 45, "int_goals": 2, "is_key": True},
        {"name": "Nicolás Otamendi", "pos": "CB", "club": "Benfica", "age": 37, "rating": 81, "form": 7.0, "caps": 110, "int_goals": 6, "is_key": False},
        {"name": "Facundo Medina", "pos": "CB", "club": "Marseille", "age": 25, "rating": 81, "form": 7.5, "caps": 12, "int_goals": 0, "is_key": False},
        {"name": "Nahuel Molina", "pos": "RB", "club": "Atlético Madrid", "age": 27, "rating": 82, "form": 7.5, "caps": 50, "int_goals": 7, "is_key": False},
        # Midfielders
        {"name": "Leandro Paredes", "pos": "CM", "club": "Boca Juniors", "age": 31, "rating": 81, "form": 7.5, "caps": 65, "int_goals": 4, "is_key": False},
        {"name": "Rodrigo De Paul", "pos": "CM", "club": "Inter Miami", "age": 31, "rating": 83, "form": 8.0, "caps": 68, "int_goals": 4, "is_key": False},
        {"name": "Valentín Barco", "pos": "LB", "club": "Strasbourg", "age": 21, "rating": 78, "form": 7.5, "caps": 8, "int_goals": 0, "is_key": False},
        {"name": "Giovani Lo Celso", "pos": "CM", "club": "Real Betis", "age": 28, "rating": 82, "form": 7.5, "caps": 48, "int_goals": 7, "is_key": False},
        {"name": "Exequiel Palacios", "pos": "CM", "club": "Bayer Leverkusen", "age": 26, "rating": 82, "form": 8.0, "caps": 32, "int_goals": 2, "is_key": False},
        {"name": "Alexis Mac Allister", "pos": "CM", "club": "Liverpool", "age": 26, "rating": 86, "form": 8.5, "caps": 47, "int_goals": 6, "is_key": True},
        {"name": "Enzo Fernández", "pos": "CM", "club": "Chelsea", "age": 25, "rating": 86, "form": 8.0, "caps": 40, "int_goals": 5, "is_key": True},
        # Forwards
        {"name": "Thiago Almada", "pos": "FW", "club": "Atlético Madrid", "age": 24, "rating": 82, "form": 7.5, "caps": 20, "int_goals": 3, "is_key": False},
        {"name": "Julián Álvarez", "pos": "FW", "club": "Atlético Madrid", "age": 25, "rating": 88, "form": 8.5, "caps": 45, "int_goals": 20, "is_key": True},
        {"name": "Nicolás González", "pos": "FW", "club": "Atlético Madrid", "age": 27, "rating": 82, "form": 7.5, "caps": 28, "int_goals": 5, "is_key": False},
        {"name": "José Manuel López", "pos": "FW", "club": "Palmeiras", "age": 22, "rating": 78, "form": 7.5, "caps": 6, "int_goals": 1, "is_key": False},
        {"name": "Lautaro Martínez", "pos": "FW", "club": "Inter Milan", "age": 27, "rating": 89, "form": 9.0, "caps": 65, "int_goals": 30, "is_key": True},
        {"name": "Lionel Messi", "pos": "FW", "club": "Inter Miami", "age": 38, "rating": 90, "form": 8.5, "caps": 195, "int_goals": 112, "is_key": True},
        {"name": "Nicolás Paz", "pos": "CM", "club": "Como", "age": 20, "rating": 83, "form": 8.0, "caps": 10, "int_goals": 1, "is_key": False},
        {"name": "Giuliano Simeone", "pos": "FW", "club": "Atlético Madrid", "age": 22, "rating": 80, "form": 7.5, "caps": 8, "int_goals": 1, "is_key": False},
    ],
    "BRA": [
        # Goalkeepers
        {"name": "Alisson", "pos": "GK", "club": "Liverpool", "age": 33, "rating": 89, "form": 8.5, "caps": 78, "int_goals": 0, "is_key": True},
        {"name": "Ederson", "pos": "GK", "club": "Fenerbahçe", "age": 31, "rating": 86, "form": 8.0, "caps": 22, "int_goals": 0, "is_key": False},
        {"name": "Weverton", "pos": "GK", "club": "Grêmio", "age": 38, "rating": 81, "form": 7.5, "caps": 12, "int_goals": 0, "is_key": False},
        # Defenders
        {"name": "Marquinhos", "pos": "CB", "club": "PSG", "age": 31, "rating": 87, "form": 8.0, "caps": 87, "int_goals": 9, "is_key": False},
        {"name": "Gabriel", "pos": "CB", "club": "Arsenal", "age": 27, "rating": 87, "form": 8.5, "caps": 28, "int_goals": 3, "is_key": False},
        {"name": "Bremer", "pos": "CB", "club": "Juventus", "age": 27, "rating": 85, "form": 7.5, "caps": 20, "int_goals": 1, "is_key": False},
        {"name": "Ibañez", "pos": "CB", "club": "Al Ahli", "age": 26, "rating": 80, "form": 7.5, "caps": 8, "int_goals": 0, "is_key": False},
        {"name": "Leo Pereira", "pos": "CB", "club": "Flamengo", "age": 28, "rating": 81, "form": 8.0, "caps": 14, "int_goals": 1, "is_key": False},
        {"name": "Wesley", "pos": "RB", "club": "Roma", "age": 21, "rating": 79, "form": 7.5, "caps": 6, "int_goals": 0, "is_key": False},
        {"name": "Danilo", "pos": "RB", "club": "Flamengo", "age": 33, "rating": 80, "form": 7.0, "caps": 88, "int_goals": 7, "is_key": False},
        {"name": "Alex Sandro", "pos": "LB", "club": "Flamengo", "age": 33, "rating": 79, "form": 7.0, "caps": 48, "int_goals": 3, "is_key": False},
        {"name": "Douglas Santos", "pos": "LB", "club": "Zenit", "age": 32, "rating": 78, "form": 7.5, "caps": 10, "int_goals": 0, "is_key": False},
        # Midfielders
        {"name": "Casemiro", "pos": "CM", "club": "Man Utd", "age": 34, "rating": 83, "form": 7.0, "caps": 83, "int_goals": 8, "is_key": False},
        {"name": "Bruno Guimarães", "pos": "CM", "club": "Newcastle", "age": 27, "rating": 87, "form": 8.5, "caps": 40, "int_goals": 4, "is_key": True},
        {"name": "Fabinho", "pos": "CM", "club": "Al-Ittihad", "age": 31, "rating": 82, "form": 7.5, "caps": 35, "int_goals": 1, "is_key": False},
        {"name": "Danilo", "pos": "CM", "club": "Botafogo", "age": 24, "rating": 81, "form": 8.0, "caps": 12, "int_goals": 2, "is_key": False},
        {"name": "Lucas Paquetá", "pos": "CM", "club": "Flamengo", "age": 28, "rating": 84, "form": 8.0, "caps": 60, "int_goals": 11, "is_key": False},
        # Forwards
        {"name": "Vinicius Jr", "pos": "FW", "club": "Real Madrid", "age": 25, "rating": 93, "form": 9.5, "caps": 40, "int_goals": 12, "is_key": True},
        {"name": "Raphinha", "pos": "FW", "club": "Barcelona", "age": 28, "rating": 86, "form": 9.0, "caps": 45, "int_goals": 15, "is_key": True},
        {"name": "Matheus Cunha", "pos": "FW", "club": "Man Utd", "age": 26, "rating": 84, "form": 8.5, "caps": 22, "int_goals": 7, "is_key": False},
        {"name": "Luiz Henrique", "pos": "FW", "club": "Zenit", "age": 23, "rating": 80, "form": 7.5, "caps": 8, "int_goals": 2, "is_key": False},
        {"name": "Igor Thiago", "pos": "FW", "club": "Brentford", "age": 23, "rating": 80, "form": 7.5, "caps": 6, "int_goals": 2, "is_key": False},
        {"name": "Endrick", "pos": "FW", "club": "Real Madrid", "age": 19, "rating": 84, "form": 8.0, "caps": 14, "int_goals": 5, "is_key": True},
        {"name": "Gabriel Martinelli", "pos": "FW", "club": "Arsenal", "age": 24, "rating": 83, "form": 8.0, "caps": 20, "int_goals": 4, "is_key": False},
        {"name": "Rayan", "pos": "FW", "club": "Bournemouth", "age": 17, "rating": 78, "form": 7.5, "caps": 2, "int_goals": 0, "is_key": False},
        {"name": "Neymar", "pos": "FW", "club": "Santos", "age": 34, "rating": 85, "form": 7.5, "caps": 128, "int_goals": 79, "is_key": True},
    ],
    "FRA": [
        # Goalkeepers
        {"name": "Mike Maignan", "pos": "GK", "club": "AC Milan", "age": 30, "rating": 87, "form": 8.5, "caps": 32, "int_goals": 0, "is_key": True},
        {"name": "Robin Risser", "pos": "GK", "club": "Lens", "age": 23, "rating": 79, "form": 7.5, "caps": 2, "int_goals": 0, "is_key": False},
        {"name": "Brice Samba", "pos": "GK", "club": "Rennes", "age": 31, "rating": 83, "form": 7.5, "caps": 8, "int_goals": 0, "is_key": False},
        # Defenders
        {"name": "Lucas Digne", "pos": "LB", "club": "Aston Villa", "age": 32, "rating": 81, "form": 7.5, "caps": 45, "int_goals": 2, "is_key": False},
        {"name": "Malo Gusto", "pos": "RB", "club": "Chelsea", "age": 22, "rating": 82, "form": 8.0, "caps": 14, "int_goals": 0, "is_key": False},
        {"name": "Lucas Hernandez", "pos": "CB", "club": "PSG", "age": 29, "rating": 83, "form": 8.0, "caps": 42, "int_goals": 1, "is_key": False},
        {"name": "Theo Hernandez", "pos": "LB", "club": "Al-Hilal", "age": 28, "rating": 85, "form": 8.0, "caps": 38, "int_goals": 6, "is_key": False},
        {"name": "Ibrahima Konaté", "pos": "CB", "club": "Liverpool", "age": 26, "rating": 86, "form": 8.5, "caps": 18, "int_goals": 0, "is_key": False},
        {"name": "Jules Koundé", "pos": "RB", "club": "Barcelona", "age": 27, "rating": 86, "form": 8.5, "caps": 52, "int_goals": 1, "is_key": True},
        {"name": "Maxence Lacroix", "pos": "CB", "club": "Crystal Palace", "age": 25, "rating": 81, "form": 7.5, "caps": 8, "int_goals": 0, "is_key": False},
        {"name": "William Saliba", "pos": "CB", "club": "Arsenal", "age": 24, "rating": 88, "form": 9.0, "caps": 18, "int_goals": 0, "is_key": True},
        {"name": "Dayot Upamecano", "pos": "CB", "club": "Bayern Munich", "age": 27, "rating": 85, "form": 8.0, "caps": 35, "int_goals": 1, "is_key": False},
        # Midfielders
        {"name": "N'Golo Kanté", "pos": "CM", "club": "Fenerbahçe", "age": 35, "rating": 83, "form": 7.5, "caps": 55, "int_goals": 2, "is_key": False},
        {"name": "Manu Koné", "pos": "CM", "club": "Roma", "age": 23, "rating": 82, "form": 8.0, "caps": 12, "int_goals": 1, "is_key": False},
        {"name": "Adrien Rabiot", "pos": "CM", "club": "AC Milan", "age": 31, "rating": 82, "form": 7.5, "caps": 48, "int_goals": 5, "is_key": False},
        {"name": "Aurélien Tchouaméni", "pos": "DM", "club": "Real Madrid", "age": 26, "rating": 86, "form": 8.5, "caps": 42, "int_goals": 4, "is_key": True},
        {"name": "Warren Zaïre-Emery", "pos": "CM", "club": "PSG", "age": 20, "rating": 84, "form": 8.5, "caps": 14, "int_goals": 1, "is_key": True},
        # Forwards
        {"name": "Maghnes Akliouche", "pos": "FW", "club": "Monaco", "age": 23, "rating": 82, "form": 8.0, "caps": 8, "int_goals": 2, "is_key": False},
        {"name": "Bradley Barcola", "pos": "FW", "club": "PSG", "age": 22, "rating": 84, "form": 8.5, "caps": 16, "int_goals": 5, "is_key": False},
        {"name": "Rayan Cherki", "pos": "FW", "club": "Man City", "age": 22, "rating": 84, "form": 8.5, "caps": 10, "int_goals": 2, "is_key": False},
        {"name": "Ousmane Dembélé", "pos": "FW", "club": "PSG", "age": 28, "rating": 85, "form": 9.0, "caps": 50, "int_goals": 6, "is_key": False},
        {"name": "Désiré Doué", "pos": "FW", "club": "PSG", "age": 20, "rating": 83, "form": 8.5, "caps": 8, "int_goals": 2, "is_key": False},
        {"name": "Jean-Philippe Mateta", "pos": "FW", "club": "Crystal Palace", "age": 28, "rating": 82, "form": 8.0, "caps": 10, "int_goals": 3, "is_key": False},
        {"name": "Kylian Mbappé", "pos": "FW", "club": "Real Madrid", "age": 26, "rating": 93, "form": 9.0, "caps": 83, "int_goals": 48, "is_key": True},
        {"name": "Michael Olise", "pos": "FW", "club": "Bayern Munich", "age": 24, "rating": 85, "form": 8.5, "caps": 12, "int_goals": 3, "is_key": False},
        {"name": "Marcus Thuram", "pos": "FW", "club": "Inter Milan", "age": 28, "rating": 84, "form": 8.5, "caps": 28, "int_goals": 10, "is_key": False},
    ],
    "ENG": [
        # Goalkeepers
        {"name": "Jordan Pickford", "pos": "GK", "club": "Everton", "age": 32, "rating": 84, "form": 8.0, "caps": 70, "int_goals": 0, "is_key": False},
        {"name": "Dean Henderson", "pos": "GK", "club": "Crystal Palace", "age": 29, "rating": 81, "form": 7.5, "caps": 6, "int_goals": 0, "is_key": False},
        {"name": "James Trafford", "pos": "GK", "club": "Man City", "age": 23, "rating": 80, "form": 7.5, "caps": 2, "int_goals": 0, "is_key": False},
        # Defenders
        {"name": "Reece James", "pos": "RB", "club": "Chelsea", "age": 26, "rating": 84, "form": 7.5, "caps": 28, "int_goals": 2, "is_key": False},
        {"name": "Ezri Konsa", "pos": "CB", "club": "Aston Villa", "age": 27, "rating": 83, "form": 8.0, "caps": 14, "int_goals": 1, "is_key": False},
        {"name": "Jarell Quansah", "pos": "CB", "club": "Bayer Leverkusen", "age": 22, "rating": 82, "form": 8.0, "caps": 8, "int_goals": 0, "is_key": False},
        {"name": "John Stones", "pos": "CB", "club": "Man City", "age": 31, "rating": 84, "form": 7.5, "caps": 75, "int_goals": 4, "is_key": False},
        {"name": "Marc Guéhi", "pos": "CB", "club": "Man City", "age": 25, "rating": 84, "form": 8.0, "caps": 18, "int_goals": 1, "is_key": False},
        {"name": "Dan Burn", "pos": "LB", "club": "Newcastle", "age": 33, "rating": 79, "form": 7.5, "caps": 8, "int_goals": 0, "is_key": False},
        {"name": "Nico O'Reilly", "pos": "LB", "club": "Man City", "age": 20, "rating": 79, "form": 7.5, "caps": 4, "int_goals": 0, "is_key": False},
        {"name": "Djed Spence", "pos": "RB", "club": "Tottenham", "age": 25, "rating": 79, "form": 7.5, "caps": 4, "int_goals": 0, "is_key": False},
        {"name": "Tino Livramento", "pos": "RB", "club": "Newcastle", "age": 22, "rating": 80, "form": 8.0, "caps": 6, "int_goals": 0, "is_key": False},
        # Midfielders
        {"name": "Declan Rice", "pos": "DM", "club": "Arsenal", "age": 27, "rating": 88, "form": 9.0, "caps": 48, "int_goals": 5, "is_key": True},
        {"name": "Elliot Anderson", "pos": "CM", "club": "Nottingham Forest", "age": 22, "rating": 80, "form": 7.5, "caps": 6, "int_goals": 0, "is_key": False},
        {"name": "Kobbie Mainoo", "pos": "CM", "club": "Man Utd", "age": 20, "rating": 83, "form": 8.0, "caps": 14, "int_goals": 1, "is_key": False},
        {"name": "Jordan Henderson", "pos": "CM", "club": "Brentford", "age": 36, "rating": 79, "form": 7.0, "caps": 82, "int_goals": 3, "is_key": False},
        {"name": "Morgan Rogers", "pos": "CM", "club": "Aston Villa", "age": 22, "rating": 81, "form": 8.0, "caps": 8, "int_goals": 1, "is_key": False},
        {"name": "Jude Bellingham", "pos": "AM", "club": "Real Madrid", "age": 22, "rating": 91, "form": 9.0, "caps": 40, "int_goals": 10, "is_key": True},
        {"name": "Eberechi Eze", "pos": "AM", "club": "Arsenal", "age": 27, "rating": 84, "form": 8.5, "caps": 14, "int_goals": 3, "is_key": False},
        # Forwards
        {"name": "Harry Kane", "pos": "FW", "club": "Bayern Munich", "age": 33, "rating": 90, "form": 9.0, "caps": 98, "int_goals": 68, "is_key": True},
        {"name": "Ivan Toney", "pos": "FW", "club": "Al Ahli", "age": 30, "rating": 82, "form": 7.5, "caps": 10, "int_goals": 2, "is_key": False},
        {"name": "Ollie Watkins", "pos": "FW", "club": "Aston Villa", "age": 30, "rating": 83, "form": 8.5, "caps": 20, "int_goals": 5, "is_key": False},
        {"name": "Bukayo Saka", "pos": "FW", "club": "Arsenal", "age": 24, "rating": 88, "form": 9.0, "caps": 42, "int_goals": 16, "is_key": True},
        {"name": "Marcus Rashford", "pos": "FW", "club": "Barcelona", "age": 28, "rating": 85, "form": 8.0, "caps": 58, "int_goals": 17, "is_key": True},
        {"name": "Anthony Gordon", "pos": "FW", "club": "Barcelona", "age": 24, "rating": 83, "form": 8.0, "caps": 10, "int_goals": 2, "is_key": False},
        {"name": "Noni Madueke", "pos": "FW", "club": "Arsenal", "age": 23, "rating": 82, "form": 8.0, "caps": 8, "int_goals": 2, "is_key": False},
    ],
    "ESP": [
        # Goalkeepers
        {"name": "Unai Simón", "pos": "GK", "club": "Athletic Club", "age": 28, "rating": 84, "form": 8.0, "caps": 35, "int_goals": 0, "is_key": False},
        {"name": "David Raya", "pos": "GK", "club": "Arsenal", "age": 30, "rating": 86, "form": 8.5, "caps": 14, "int_goals": 0, "is_key": False},
        {"name": "Joan Garcia", "pos": "GK", "club": "Barcelona", "age": 24, "rating": 80, "form": 7.5, "caps": 4, "int_goals": 0, "is_key": False},
        # Defenders
        {"name": "Aymeric Laporte", "pos": "CB", "club": "Athletic Club", "age": 31, "rating": 83, "form": 7.5, "caps": 32, "int_goals": 3, "is_key": False},
        {"name": "Marc Cucurella", "pos": "LB", "club": "Chelsea", "age": 26, "rating": 82, "form": 8.0, "caps": 22, "int_goals": 0, "is_key": False},
        {"name": "Marcos Llorente", "pos": "RB", "club": "Atlético Madrid", "age": 30, "rating": 83, "form": 8.0, "caps": 30, "int_goals": 4, "is_key": False},
        {"name": "Eric Garcia", "pos": "CB", "club": "Barcelona", "age": 24, "rating": 82, "form": 8.0, "caps": 18, "int_goals": 0, "is_key": False},
        {"name": "Pedro Porro", "pos": "RB", "club": "Tottenham", "age": 26, "rating": 83, "form": 8.0, "caps": 20, "int_goals": 2, "is_key": False},
        {"name": "Alex Grimaldo", "pos": "LB", "club": "Bayer Leverkusen", "age": 29, "rating": 85, "form": 8.5, "caps": 16, "int_goals": 2, "is_key": False},
        {"name": "Pau Cubarsí", "pos": "CB", "club": "Barcelona", "age": 18, "rating": 84, "form": 8.5, "caps": 10, "int_goals": 0, "is_key": False},
        {"name": "Marc Pubill", "pos": "RB", "club": "Atlético Madrid", "age": 22, "rating": 80, "form": 7.5, "caps": 6, "int_goals": 0, "is_key": False},
        # Midfielders
        {"name": "Rodri", "pos": "DM", "club": "Man City", "age": 29, "rating": 91, "form": 9.0, "caps": 50, "int_goals": 7, "is_key": True},
        {"name": "Fabián Ruiz", "pos": "CM", "club": "PSG", "age": 29, "rating": 85, "form": 8.5, "caps": 38, "int_goals": 5, "is_key": False},
        {"name": "Mikel Merino", "pos": "CM", "club": "Arsenal", "age": 29, "rating": 85, "form": 8.5, "caps": 26, "int_goals": 6, "is_key": False},
        {"name": "Pedri", "pos": "CM", "club": "Barcelona", "age": 23, "rating": 89, "form": 9.0, "caps": 40, "int_goals": 5, "is_key": True},
        {"name": "Gavi", "pos": "CM", "club": "Barcelona", "age": 22, "rating": 85, "form": 8.5, "caps": 48, "int_goals": 4, "is_key": False},
        {"name": "Martín Zubimendi", "pos": "DM", "club": "Arsenal", "age": 27, "rating": 85, "form": 8.5, "caps": 20, "int_goals": 1, "is_key": False},
        {"name": "Alex Baena", "pos": "CM", "club": "Atlético Madrid", "age": 24, "rating": 82, "form": 8.0, "caps": 12, "int_goals": 2, "is_key": False},
        # Forwards
        {"name": "Ferran Torres", "pos": "FW", "club": "Barcelona", "age": 25, "rating": 82, "form": 7.5, "caps": 50, "int_goals": 18, "is_key": False},
        {"name": "Mikel Oyarzabal", "pos": "FW", "club": "Real Sociedad", "age": 28, "rating": 83, "form": 8.0, "caps": 40, "int_goals": 16, "is_key": False},
        {"name": "Dani Olmo", "pos": "FW", "club": "Barcelona", "age": 27, "rating": 86, "form": 8.5, "caps": 36, "int_goals": 10, "is_key": True},
        {"name": "Nico Williams", "pos": "FW", "club": "Athletic Club", "age": 22, "rating": 87, "form": 9.0, "caps": 22, "int_goals": 5, "is_key": True},
        {"name": "Lamine Yamal", "pos": "FW", "club": "Barcelona", "age": 18, "rating": 90, "form": 9.5, "caps": 16, "int_goals": 5, "is_key": True},
        {"name": "Yeremy Pino", "pos": "FW", "club": "Crystal Palace", "age": 23, "rating": 82, "form": 7.5, "caps": 22, "int_goals": 4, "is_key": False},
        {"name": "Borja Iglesias", "pos": "FW", "club": "Celta Vigo", "age": 32, "rating": 80, "form": 7.5, "caps": 10, "int_goals": 2, "is_key": False},
        {"name": "Víctor Muñoz", "pos": "FW", "club": "Osasuna", "age": 21, "rating": 79, "form": 7.5, "caps": 4, "int_goals": 0, "is_key": False},
    ],
    "GER": [
        # Goalkeepers
        {"name": "Oliver Baumann", "pos": "GK", "club": "Hoffenheim", "age": 35, "rating": 82, "form": 7.5, "caps": 8, "int_goals": 0, "is_key": False},
        {"name": "Manuel Neuer", "pos": "GK", "club": "Bayern Munich", "age": 40, "rating": 84, "form": 7.5, "caps": 124, "int_goals": 0, "is_key": False},
        {"name": "Alexander Nübel", "pos": "GK", "club": "Bayern Munich", "age": 29, "rating": 82, "form": 7.5, "caps": 4, "int_goals": 0, "is_key": False},
        # Defenders
        {"name": "Waldemar Anton", "pos": "CB", "club": "Dortmund", "age": 29, "rating": 83, "form": 8.0, "caps": 22, "int_goals": 1, "is_key": False},
        {"name": "Nathaniel Brown", "pos": "RB", "club": "Eintracht Frankfurt", "age": 22, "rating": 79, "form": 7.5, "caps": 6, "int_goals": 0, "is_key": False},
        {"name": "David Raum", "pos": "LB", "club": "RB Leipzig", "age": 27, "rating": 82, "form": 7.5, "caps": 28, "int_goals": 2, "is_key": False},
        {"name": "Antonio Rüdiger", "pos": "CB", "club": "Real Madrid", "age": 32, "rating": 85, "form": 8.0, "caps": 72, "int_goals": 4, "is_key": True},
        {"name": "Nico Schlotterbeck", "pos": "CB", "club": "Dortmund", "age": 26, "rating": 84, "form": 8.0, "caps": 20, "int_goals": 0, "is_key": False},
        {"name": "Jonathan Tah", "pos": "CB", "club": "Bayern Munich", "age": 29, "rating": 85, "form": 8.0, "caps": 32, "int_goals": 2, "is_key": False},
        {"name": "Malick Thiaw", "pos": "CB", "club": "Newcastle", "age": 24, "rating": 82, "form": 8.0, "caps": 10, "int_goals": 0, "is_key": False},
        # Midfielders
        {"name": "Pascal Groß", "pos": "CM", "club": "Brighton", "age": 34, "rating": 80, "form": 7.5, "caps": 20, "int_goals": 2, "is_key": False},
        {"name": "Joshua Kimmich", "pos": "CM", "club": "Bayern Munich", "age": 31, "rating": 87, "form": 8.5, "caps": 90, "int_goals": 8, "is_key": True},
        {"name": "Felix Nmecha", "pos": "CM", "club": "Dortmund", "age": 25, "rating": 81, "form": 7.5, "caps": 12, "int_goals": 1, "is_key": False},
        {"name": "Aleksandar Pavlović", "pos": "CM", "club": "Bayern Munich", "age": 21, "rating": 82, "form": 8.0, "caps": 8, "int_goals": 0, "is_key": False},
        {"name": "Angelo Stiller", "pos": "CM", "club": "Stuttgart", "age": 24, "rating": 81, "form": 8.0, "caps": 8, "int_goals": 0, "is_key": False},
        {"name": "Leon Goretzka", "pos": "CM", "club": "Bayern Munich", "age": 31, "rating": 83, "form": 7.5, "caps": 60, "int_goals": 15, "is_key": False},
        {"name": "Florian Wirtz", "pos": "AM", "club": "Liverpool", "age": 22, "rating": 91, "form": 9.5, "caps": 28, "int_goals": 8, "is_key": True},
        {"name": "Jamie Leweling", "pos": "FW", "club": "Stuttgart", "age": 24, "rating": 80, "form": 7.5, "caps": 8, "int_goals": 1, "is_key": False},
        # Forwards
        {"name": "Maximilian Beier", "pos": "FW", "club": "Dortmund", "age": 23, "rating": 82, "form": 8.0, "caps": 10, "int_goals": 3, "is_key": False},
        {"name": "Kai Havertz", "pos": "FW", "club": "Arsenal", "age": 26, "rating": 85, "form": 8.5, "caps": 55, "int_goals": 21, "is_key": True},
        {"name": "Lennart Karl", "pos": "FW", "club": "Bayern Munich", "age": 20, "rating": 78, "form": 7.5, "caps": 4, "int_goals": 0, "is_key": False},
        {"name": "Jamal Musiala", "pos": "FW", "club": "Bayern Munich", "age": 23, "rating": 90, "form": 9.0, "caps": 36, "int_goals": 12, "is_key": True},
        {"name": "Leroy Sané", "pos": "FW", "club": "Galatasaray", "age": 30, "rating": 84, "form": 8.0, "caps": 60, "int_goals": 16, "is_key": False},
        {"name": "Deniz Undav", "pos": "FW", "club": "Stuttgart", "age": 29, "rating": 82, "form": 8.0, "caps": 12, "int_goals": 4, "is_key": False},
        {"name": "Nick Woltemade", "pos": "FW", "club": "Newcastle", "age": 23, "rating": 80, "form": 7.5, "caps": 6, "int_goals": 1, "is_key": False},
    ],
    "POR": [
        # Goalkeepers
        {"name": "Diogo Costa", "pos": "GK", "club": "Porto", "age": 26, "rating": 86, "form": 8.5, "caps": 25, "int_goals": 0, "is_key": False},
        {"name": "José Sá", "pos": "GK", "club": "Wolves", "age": 32, "rating": 83, "form": 7.5, "caps": 10, "int_goals": 0, "is_key": False},
        {"name": "Rui Silva", "pos": "GK", "club": "Sporting", "age": 31, "rating": 81, "form": 7.5, "caps": 6, "int_goals": 0, "is_key": False},
        {"name": "Ricardo Velho", "pos": "GK", "club": "Gençlerbirliği", "age": 25, "rating": 77, "form": 7.0, "caps": 2, "int_goals": 0, "is_key": False},
        # Defenders
        {"name": "Diogo Dalot", "pos": "RB", "club": "Man Utd", "age": 26, "rating": 84, "form": 8.0, "caps": 30, "int_goals": 2, "is_key": False},
        {"name": "Matheus Nunes", "pos": "CM", "club": "Man City", "age": 27, "rating": 83, "form": 8.0, "caps": 20, "int_goals": 1, "is_key": False},
        {"name": "Nélson Semedo", "pos": "RB", "club": "Fenerbahçe", "age": 31, "rating": 81, "form": 7.5, "caps": 32, "int_goals": 1, "is_key": False},
        {"name": "João Cancelo", "pos": "RB", "club": "Barcelona", "age": 31, "rating": 84, "form": 8.0, "caps": 65, "int_goals": 6, "is_key": False},
        {"name": "Nuno Mendes", "pos": "LB", "club": "PSG", "age": 23, "rating": 87, "form": 8.5, "caps": 32, "int_goals": 1, "is_key": True},
        {"name": "Gonçalo Inácio", "pos": "CB", "club": "Sporting", "age": 24, "rating": 84, "form": 8.0, "caps": 18, "int_goals": 0, "is_key": False},
        {"name": "Renato Veiga", "pos": "CB", "club": "Villarreal", "age": 22, "rating": 81, "form": 7.5, "caps": 8, "int_goals": 0, "is_key": False},
        {"name": "Rúben Dias", "pos": "CB", "club": "Man City", "age": 28, "rating": 89, "form": 8.5, "caps": 72, "int_goals": 4, "is_key": True},
        {"name": "Tomás Araújo", "pos": "CB", "club": "Benfica", "age": 23, "rating": 82, "form": 8.0, "caps": 10, "int_goals": 0, "is_key": False},
        # Midfielders
        {"name": "Rúben Neves", "pos": "DM", "club": "Al-Hilal", "age": 28, "rating": 84, "form": 8.0, "caps": 50, "int_goals": 4, "is_key": False},
        {"name": "Samuel Costa", "pos": "CM", "club": "Mallorca", "age": 28, "rating": 78, "form": 7.5, "caps": 8, "int_goals": 0, "is_key": False},
        {"name": "João Neves", "pos": "CM", "club": "PSG", "age": 21, "rating": 86, "form": 8.5, "caps": 18, "int_goals": 2, "is_key": True},
        {"name": "Vitinha", "pos": "CM", "club": "PSG", "age": 25, "rating": 86, "form": 8.5, "caps": 30, "int_goals": 3, "is_key": True},
        {"name": "Bruno Fernandes", "pos": "AM", "club": "Man Utd", "age": 31, "rating": 87, "form": 8.0, "caps": 76, "int_goals": 22, "is_key": False},
        {"name": "Bernardo Silva", "pos": "CM", "club": "Man City", "age": 31, "rating": 88, "form": 8.5, "caps": 86, "int_goals": 12, "is_key": True},
        # Forwards
        {"name": "João Félix", "pos": "FW", "club": "Al Nassr", "age": 26, "rating": 84, "form": 8.0, "caps": 42, "int_goals": 10, "is_key": False},
        {"name": "Francisco Trincão", "pos": "FW", "club": "Sporting", "age": 25, "rating": 82, "form": 8.0, "caps": 20, "int_goals": 4, "is_key": False},
        {"name": "Francisco Conceição", "pos": "FW", "club": "Juventus", "age": 23, "rating": 84, "form": 8.5, "caps": 14, "int_goals": 3, "is_key": False},
        {"name": "Pedro Neto", "pos": "FW", "club": "Chelsea", "age": 25, "rating": 85, "form": 8.5, "caps": 24, "int_goals": 4, "is_key": False},
        {"name": "Rafael Leão", "pos": "FW", "club": "AC Milan", "age": 26, "rating": 86, "form": 8.0, "caps": 30, "int_goals": 7, "is_key": True},
        {"name": "Gonçalo Guedes", "pos": "FW", "club": "Real Sociedad", "age": 28, "rating": 81, "form": 7.5, "caps": 40, "int_goals": 8, "is_key": False},
        {"name": "Gonçalo Ramos", "pos": "FW", "club": "PSG", "age": 24, "rating": 84, "form": 8.0, "caps": 20, "int_goals": 12, "is_key": False},
        {"name": "Cristiano Ronaldo", "pos": "FW", "club": "Al Nassr", "age": 41, "rating": 84, "form": 8.0, "caps": 213, "int_goals": 130, "is_key": False},
    ],
    "NED": [
        # Goalkeepers
        {"name": "Bart Verbruggen", "pos": "GK", "club": "Brighton", "age": 23, "rating": 83, "form": 8.0, "caps": 12, "int_goals": 0, "is_key": False},
        {"name": "Mark Flekken", "pos": "GK", "club": "Bayer Leverkusen", "age": 31, "rating": 82, "form": 7.5, "caps": 8, "int_goals": 0, "is_key": False},
        {"name": "Robin Roefs", "pos": "GK", "club": "Sunderland", "age": 24, "rating": 79, "form": 7.5, "caps": 2, "int_goals": 0, "is_key": False},
        # Defenders
        {"name": "Virgil van Dijk", "pos": "CB", "club": "Liverpool", "age": 34, "rating": 87, "form": 8.5, "caps": 70, "int_goals": 6, "is_key": True},
        {"name": "Jan Paul van Hecke", "pos": "CB", "club": "Brighton", "age": 25, "rating": 82, "form": 8.0, "caps": 12, "int_goals": 0, "is_key": False},
        {"name": "Nathan Aké", "pos": "CB", "club": "Man City", "age": 31, "rating": 84, "form": 7.5, "caps": 48, "int_goals": 3, "is_key": False},
        {"name": "Micky van de Ven", "pos": "CB", "club": "Tottenham", "age": 24, "rating": 84, "form": 8.0, "caps": 14, "int_goals": 1, "is_key": False},
        {"name": "Denzel Dumfries", "pos": "RB", "club": "Inter Milan", "age": 29, "rating": 84, "form": 8.0, "caps": 55, "int_goals": 10, "is_key": False},
        {"name": "Jorrel Hato", "pos": "LB", "club": "Chelsea", "age": 19, "rating": 81, "form": 8.0, "caps": 6, "int_goals": 0, "is_key": False},
        {"name": "Jurriën Timber", "pos": "CB", "club": "Arsenal", "age": 24, "rating": 84, "form": 8.5, "caps": 18, "int_goals": 0, "is_key": False},
        # Midfielders
        {"name": "Frenkie de Jong", "pos": "CM", "club": "Barcelona", "age": 28, "rating": 87, "form": 8.0, "caps": 58, "int_goals": 7, "is_key": True},
        {"name": "Tijjani Reijnders", "pos": "CM", "club": "Man City", "age": 27, "rating": 87, "form": 9.0, "caps": 20, "int_goals": 6, "is_key": True},
        {"name": "Justin Kluivert", "pos": "FW", "club": "Bournemouth", "age": 28, "rating": 82, "form": 8.0, "caps": 18, "int_goals": 5, "is_key": False},
        {"name": "Quinten Timber", "pos": "CM", "club": "Marseille", "age": 24, "rating": 81, "form": 7.5, "caps": 8, "int_goals": 0, "is_key": False},
        {"name": "Teun Koopmeiners", "pos": "CM", "club": "Juventus", "age": 28, "rating": 85, "form": 8.5, "caps": 24, "int_goals": 5, "is_key": True},
        {"name": "Ryan Gravenberch", "pos": "CM", "club": "Liverpool", "age": 23, "rating": 86, "form": 9.0, "caps": 22, "int_goals": 2, "is_key": True},
        {"name": "Marten de Roon", "pos": "DM", "club": "Atalanta", "age": 34, "rating": 81, "form": 7.5, "caps": 42, "int_goals": 3, "is_key": False},
        {"name": "Guus Til", "pos": "CM", "club": "PSV", "age": 28, "rating": 80, "form": 7.5, "caps": 8, "int_goals": 1, "is_key": False},
        {"name": "Mats Wieffer", "pos": "DM", "club": "Brighton", "age": 26, "rating": 81, "form": 8.0, "caps": 10, "int_goals": 0, "is_key": False},
        # Forwards
        {"name": "Cody Gakpo", "pos": "FW", "club": "Liverpool", "age": 26, "rating": 87, "form": 8.5, "caps": 30, "int_goals": 15, "is_key": False},
        {"name": "Donyell Malen", "pos": "FW", "club": "Roma", "age": 27, "rating": 82, "form": 8.0, "caps": 26, "int_goals": 8, "is_key": False},
        {"name": "Brian Brobbey", "pos": "FW", "club": "Sunderland", "age": 24, "rating": 83, "form": 8.0, "caps": 14, "int_goals": 5, "is_key": False},
        {"name": "Noa Lang", "pos": "FW", "club": "Galatasaray", "age": 26, "rating": 83, "form": 8.0, "caps": 12, "int_goals": 3, "is_key": False},
        {"name": "Memphis Depay", "pos": "FW", "club": "Corinthians", "age": 32, "rating": 81, "form": 7.5, "caps": 93, "int_goals": 46, "is_key": False},
        {"name": "Wout Weghorst", "pos": "FW", "club": "Ajax", "age": 33, "rating": 80, "form": 7.0, "caps": 48, "int_goals": 14, "is_key": False},
        {"name": "Crysencio Summerville", "pos": "FW", "club": "West Ham", "age": 23, "rating": 82, "form": 8.0, "caps": 8, "int_goals": 2, "is_key": False},
    ],
    "BEL": [
        # Goalkeepers
        {"name": "Thibaut Courtois", "pos": "GK", "club": "Real Madrid", "age": 33, "rating": 89, "form": 8.5, "caps": 108, "int_goals": 0, "is_key": True},
        {"name": "Senne Lammens", "pos": "GK", "club": "Man Utd", "age": 22, "rating": 79, "form": 7.5, "caps": 4, "int_goals": 0, "is_key": False},
        {"name": "Mike Penders", "pos": "GK", "club": "Strasbourg", "age": 21, "rating": 78, "form": 7.5, "caps": 2, "int_goals": 0, "is_key": False},
        # Defenders
        {"name": "Timothy Castagne", "pos": "RB", "club": "Fulham", "age": 29, "rating": 81, "form": 7.5, "caps": 50, "int_goals": 3, "is_key": False},
        {"name": "Zeno Debast", "pos": "CB", "club": "Sporting", "age": 22, "rating": 82, "form": 8.0, "caps": 18, "int_goals": 0, "is_key": False},
        {"name": "Maxim De Cuyper", "pos": "LB", "club": "Brighton", "age": 25, "rating": 82, "form": 8.0, "caps": 14, "int_goals": 0, "is_key": False},
        {"name": "Koni De Winter", "pos": "CB", "club": "AC Milan", "age": 24, "rating": 80, "form": 7.5, "caps": 8, "int_goals": 0, "is_key": False},
        {"name": "Brandon Mechele", "pos": "CB", "club": "Club Brugge", "age": 34, "rating": 79, "form": 7.0, "caps": 20, "int_goals": 0, "is_key": False},
        {"name": "Thomas Meunier", "pos": "RB", "club": "Lille", "age": 33, "rating": 80, "form": 7.5, "caps": 62, "int_goals": 5, "is_key": False},
        {"name": "Nathan Ngoy", "pos": "CB", "club": "Lille", "age": 20, "rating": 78, "form": 7.5, "caps": 4, "int_goals": 0, "is_key": False},
        {"name": "Joaquin Seys", "pos": "RB", "club": "Club Brugge", "age": 22, "rating": 78, "form": 7.5, "caps": 4, "int_goals": 0, "is_key": False},
        {"name": "Arthur Theate", "pos": "CB", "club": "Eintracht Frankfurt", "age": 25, "rating": 82, "form": 8.0, "caps": 18, "int_goals": 1, "is_key": False},
        # Midfielders
        {"name": "Kevin De Bruyne", "pos": "AM", "club": "Napoli", "age": 35, "rating": 88, "form": 8.0, "caps": 103, "int_goals": 26, "is_key": True},
        {"name": "Amadou Onana", "pos": "DM", "club": "Aston Villa", "age": 23, "rating": 84, "form": 8.5, "caps": 28, "int_goals": 3, "is_key": False},
        {"name": "Nicolas Raskin", "pos": "CM", "club": "Rangers", "age": 23, "rating": 81, "form": 7.5, "caps": 12, "int_goals": 0, "is_key": False},
        {"name": "Youri Tielemans", "pos": "CM", "club": "Aston Villa", "age": 28, "rating": 82, "form": 8.0, "caps": 68, "int_goals": 15, "is_key": False},
        {"name": "Hans Vanaken", "pos": "CM", "club": "Club Brugge", "age": 32, "rating": 81, "form": 7.5, "caps": 28, "int_goals": 4, "is_key": False},
        {"name": "Axel Witsel", "pos": "DM", "club": "Girona", "age": 36, "rating": 79, "form": 7.0, "caps": 135, "int_goals": 12, "is_key": False},
        # Forwards
        {"name": "Charles De Ketelaere", "pos": "FW", "club": "Atalanta", "age": 24, "rating": 84, "form": 8.5, "caps": 24, "int_goals": 5, "is_key": True},
        {"name": "Jeremy Doku", "pos": "FW", "club": "Man City", "age": 23, "rating": 85, "form": 8.5, "caps": 28, "int_goals": 6, "is_key": True},
        {"name": "Matías Fernández-Pardo", "pos": "FW", "club": "Lille", "age": 22, "rating": 79, "form": 7.5, "caps": 8, "int_goals": 1, "is_key": False},
        {"name": "Romelu Lukaku", "pos": "FW", "club": "Napoli", "age": 31, "rating": 85, "form": 8.0, "caps": 110, "int_goals": 85, "is_key": True},
        {"name": "Dodi Lukebakio", "pos": "FW", "club": "Benfica", "age": 28, "rating": 80, "form": 7.5, "caps": 20, "int_goals": 5, "is_key": False},
        {"name": "Diego Moreira", "pos": "FW", "club": "Strasbourg", "age": 20, "rating": 79, "form": 7.5, "caps": 6, "int_goals": 1, "is_key": False},
        {"name": "Alexis Saelemaekers", "pos": "FW", "club": "AC Milan", "age": 26, "rating": 81, "form": 7.5, "caps": 20, "int_goals": 2, "is_key": False},
        {"name": "Leandro Trossard", "pos": "FW", "club": "Arsenal", "age": 30, "rating": 84, "form": 8.5, "caps": 35, "int_goals": 8, "is_key": False},
    ],
    "CRO": [
        # Goalkeepers
        {"name": "Dominik Livaković", "pos": "GK", "club": "Dinamo Zagreb", "age": 30, "rating": 84, "form": 7.5, "caps": 50, "int_goals": 0, "is_key": False},
        {"name": "Dominik Kotarski", "pos": "GK", "club": "Copenhagen", "age": 28, "rating": 80, "form": 7.5, "caps": 8, "int_goals": 0, "is_key": False},
        {"name": "Ivor Pandur", "pos": "GK", "club": "Hull", "age": 25, "rating": 77, "form": 7.0, "caps": 4, "int_goals": 0, "is_key": False},
        # Defenders
        {"name": "Joško Gvardiol", "pos": "CB", "club": "Man City", "age": 23, "rating": 87, "form": 8.5, "caps": 38, "int_goals": 4, "is_key": True},
        {"name": "Duje Ćaleta-Car", "pos": "CB", "club": "Real Sociedad", "age": 29, "rating": 81, "form": 7.5, "caps": 38, "int_goals": 1, "is_key": False},
        {"name": "Josip Šutalo", "pos": "CB", "club": "Ajax", "age": 24, "rating": 81, "form": 7.5, "caps": 14, "int_goals": 0, "is_key": False},
        {"name": "Josip Stanišić", "pos": "RB", "club": "Bayern Munich", "age": 25, "rating": 81, "form": 8.0, "caps": 12, "int_goals": 0, "is_key": False},
        {"name": "Marin Pongračić", "pos": "CB", "club": "Fiorentina", "age": 27, "rating": 80, "form": 7.5, "caps": 22, "int_goals": 0, "is_key": False},
        {"name": "Martin Erlić", "pos": "CB", "club": "Midtjylland", "age": 28, "rating": 79, "form": 7.5, "caps": 14, "int_goals": 0, "is_key": False},
        {"name": "Luka Vušković", "pos": "CB", "club": "Hamburg", "age": 20, "rating": 80, "form": 7.5, "caps": 6, "int_goals": 0, "is_key": False},
        # Midfielders
        {"name": "Luka Modrić", "pos": "CM", "club": "AC Milan", "age": 40, "rating": 85, "form": 7.5, "caps": 175, "int_goals": 24, "is_key": True},
        {"name": "Mateo Kovačić", "pos": "CM", "club": "Man City", "age": 32, "rating": 84, "form": 8.0, "caps": 110, "int_goals": 4, "is_key": True},
        {"name": "Mario Pašalić", "pos": "CM", "club": "Atalanta", "age": 30, "rating": 82, "form": 7.5, "caps": 58, "int_goals": 12, "is_key": False},
        {"name": "Nikola Vlašić", "pos": "CM", "club": "Torino", "age": 28, "rating": 81, "form": 7.5, "caps": 52, "int_goals": 8, "is_key": False},
        {"name": "Luka Sučić", "pos": "CM", "club": "Real Sociedad", "age": 23, "rating": 82, "form": 8.0, "caps": 18, "int_goals": 3, "is_key": False},
        {"name": "Martin Baturina", "pos": "CM", "club": "Como", "age": 22, "rating": 82, "form": 8.0, "caps": 12, "int_goals": 2, "is_key": False},
        {"name": "Kristijan Jakić", "pos": "DM", "club": "Augsburg", "age": 28, "rating": 79, "form": 7.5, "caps": 28, "int_goals": 0, "is_key": False},
        {"name": "Petar Sučić", "pos": "CM", "club": "Inter Milan", "age": 21, "rating": 81, "form": 8.0, "caps": 10, "int_goals": 1, "is_key": False},
        {"name": "Nikola Moro", "pos": "CM", "club": "Bologna", "age": 27, "rating": 79, "form": 7.5, "caps": 14, "int_goals": 1, "is_key": False},
        {"name": "Toni Fruk", "pos": "CM", "club": "Rijeka", "age": 24, "rating": 77, "form": 7.0, "caps": 6, "int_goals": 0, "is_key": False},
        # Forwards
        {"name": "Ivan Perišić", "pos": "FW", "club": "PSV", "age": 36, "rating": 81, "form": 7.0, "caps": 135, "int_goals": 34, "is_key": False},
        {"name": "Andrej Kramarić", "pos": "FW", "club": "Hoffenheim", "age": 34, "rating": 82, "form": 8.0, "caps": 80, "int_goals": 22, "is_key": True},
        {"name": "Ante Budimir", "pos": "FW", "club": "Osasuna", "age": 33, "rating": 81, "form": 7.5, "caps": 28, "int_goals": 7, "is_key": False},
        {"name": "Marco Pašalić", "pos": "FW", "club": "Orlando City", "age": 26, "rating": 78, "form": 7.5, "caps": 8, "int_goals": 1, "is_key": False},
        {"name": "Petar Muša", "pos": "FW", "club": "FC Dallas", "age": 29, "rating": 79, "form": 7.5, "caps": 12, "int_goals": 3, "is_key": False},
        {"name": "Igor Matanović", "pos": "FW", "club": "Freiburg", "age": 23, "rating": 80, "form": 7.5, "caps": 8, "int_goals": 2, "is_key": False},
    ],
    "COL": [
        # Goalkeepers
        {"name": "Camilo Vargas", "pos": "GK", "club": "Atlas", "age": 35, "rating": 80, "form": 7.5, "caps": 45, "int_goals": 0, "is_key": False},
        {"name": "Álvaro Montero", "pos": "GK", "club": "Vélez", "age": 31, "rating": 79, "form": 7.5, "caps": 8, "int_goals": 0, "is_key": False},
        {"name": "David Ospina", "pos": "GK", "club": "Atlético Nacional", "age": 38, "rating": 81, "form": 7.0, "caps": 110, "int_goals": 0, "is_key": False},
        # Defenders
        {"name": "Davinson Sánchez", "pos": "CB", "club": "Galatasaray", "age": 29, "rating": 82, "form": 7.5, "caps": 58, "int_goals": 3, "is_key": False},
        {"name": "Jhon Lucumí", "pos": "CB", "club": "Bologna", "age": 26, "rating": 82, "form": 8.0, "caps": 20, "int_goals": 1, "is_key": False},
        {"name": "Yerry Mina", "pos": "CB", "club": "Cagliari", "age": 30, "rating": 80, "form": 7.0, "caps": 60, "int_goals": 5, "is_key": False},
        {"name": "Willer Ditta", "pos": "CB", "club": "Cruz Azul", "age": 29, "rating": 78, "form": 7.5, "caps": 10, "int_goals": 0, "is_key": False},
        {"name": "Daniel Muñoz", "pos": "RB", "club": "Crystal Palace", "age": 29, "rating": 82, "form": 8.0, "caps": 28, "int_goals": 2, "is_key": True},
        {"name": "Santiago Arias", "pos": "RB", "club": "Independiente", "age": 33, "rating": 78, "form": 7.0, "caps": 50, "int_goals": 2, "is_key": False},
        {"name": "Johan Mojica", "pos": "LB", "club": "Mallorca", "age": 32, "rating": 80, "form": 7.5, "caps": 28, "int_goals": 0, "is_key": False},
        {"name": "Deiver Machado", "pos": "LB", "club": "Nantes", "age": 29, "rating": 78, "form": 7.5, "caps": 12, "int_goals": 0, "is_key": False},
        # Midfielders
        {"name": "Richard Ríos", "pos": "CM", "club": "Benfica", "age": 25, "rating": 83, "form": 8.0, "caps": 16, "int_goals": 3, "is_key": True},
        {"name": "Jefferson Lerma", "pos": "DM", "club": "Crystal Palace", "age": 30, "rating": 81, "form": 7.5, "caps": 60, "int_goals": 4, "is_key": False},
        {"name": "Kevin Castaño", "pos": "CM", "club": "River Plate", "age": 26, "rating": 79, "form": 7.5, "caps": 8, "int_goals": 0, "is_key": False},
        {"name": "Juan Camilo Portilla", "pos": "CM", "club": "Athletico Paranaense", "age": 24, "rating": 79, "form": 7.5, "caps": 6, "int_goals": 0, "is_key": False},
        {"name": "Gustavo Puerta", "pos": "CM", "club": "Racing Santander", "age": 22, "rating": 79, "form": 7.5, "caps": 4, "int_goals": 0, "is_key": False},
        {"name": "Jhon Arias", "pos": "FW", "club": "Palmeiras", "age": 27, "rating": 82, "form": 8.0, "caps": 20, "int_goals": 5, "is_key": False},
        {"name": "Jorge Carrascal", "pos": "CM", "club": "Flamengo", "age": 27, "rating": 81, "form": 8.0, "caps": 14, "int_goals": 3, "is_key": False},
        {"name": "Juan Fernando Quintero", "pos": "AM", "club": "River Plate", "age": 32, "rating": 82, "form": 7.5, "caps": 40, "int_goals": 8, "is_key": False},
        {"name": "James Rodríguez", "pos": "AM", "club": "Minnesota Utd", "age": 34, "rating": 82, "form": 7.5, "caps": 102, "int_goals": 31, "is_key": True},
        {"name": "Jaminton Campaz", "pos": "FW", "club": "Rosario Central", "age": 25, "rating": 79, "form": 7.5, "caps": 8, "int_goals": 2, "is_key": False},
        # Forwards
        {"name": "Juan Camilo Hernández", "pos": "FW", "club": "Real Betis", "age": 25, "rating": 83, "form": 8.0, "caps": 32, "int_goals": 14, "is_key": False},
        {"name": "Luis Díaz", "pos": "FW", "club": "Bayern Munich", "age": 28, "rating": 88, "form": 9.0, "caps": 42, "int_goals": 10, "is_key": True},
        {"name": "Luis Suárez", "pos": "FW", "club": "Sporting", "age": 22, "rating": 80, "form": 7.5, "caps": 8, "int_goals": 2, "is_key": False},
        {"name": "Carlos Andrés Gómez", "pos": "FW", "club": "Vasco", "age": 24, "rating": 78, "form": 7.5, "caps": 6, "int_goals": 1, "is_key": False},
        {"name": "Jhon Córdoba", "pos": "FW", "club": "Krasnodar", "age": 31, "rating": 80, "form": 7.5, "caps": 22, "int_goals": 5, "is_key": False},
    ],
    "MAR": [
        # Goalkeepers
        {"name": "Yassine Bounou", "pos": "GK", "club": "Al-Hilal", "age": 33, "rating": 86, "form": 8.0, "caps": 60, "int_goals": 0, "is_key": True},
        {"name": "Munir Mohamedi", "pos": "GK", "club": "RS Berkane", "age": 33, "rating": 78, "form": 7.5, "caps": 12, "int_goals": 0, "is_key": False},
        {"name": "Ahmed Tagnaouti", "pos": "GK", "club": "Royal Armed Forces", "age": 29, "rating": 77, "form": 7.0, "caps": 8, "int_goals": 0, "is_key": False},
        # Defenders
        {"name": "Noussair Mazraoui", "pos": "RB", "club": "Man Utd", "age": 27, "rating": 83, "form": 8.0, "caps": 42, "int_goals": 2, "is_key": False},
        {"name": "Anass Salah-Eddine", "pos": "RB", "club": "PSV", "age": 25, "rating": 80, "form": 7.5, "caps": 8, "int_goals": 0, "is_key": False},
        {"name": "Youssef Belammari", "pos": "CB", "club": "Al-Ahly", "age": 25, "rating": 77, "form": 7.0, "caps": 6, "int_goals": 0, "is_key": False},
        {"name": "Nayef Aguerd", "pos": "CB", "club": "Marseille", "age": 28, "rating": 83, "form": 8.0, "caps": 38, "int_goals": 1, "is_key": False},
        {"name": "Chadi Riad", "pos": "CB", "club": "Crystal Palace", "age": 22, "rating": 81, "form": 7.5, "caps": 10, "int_goals": 0, "is_key": False},
        {"name": "Issa Diop", "pos": "CB", "club": "Fulham", "age": 28, "rating": 81, "form": 8.0, "caps": 12, "int_goals": 0, "is_key": False},
        {"name": "Redouane Halhal", "pos": "LB", "club": "KV Mechelen", "age": 28, "rating": 78, "form": 7.5, "caps": 8, "int_goals": 0, "is_key": False},
        {"name": "Achraf Hakimi", "pos": "RB", "club": "PSG", "age": 27, "rating": 87, "form": 8.5, "caps": 72, "int_goals": 6, "is_key": True},
        {"name": "Zakaria El Ouahdi", "pos": "RB", "club": "Genk", "age": 23, "rating": 80, "form": 7.5, "caps": 8, "int_goals": 0, "is_key": False},
        # Midfielders
        {"name": "Samir El Mourabet", "pos": "CM", "club": "Strasbourg", "age": 22, "rating": 79, "form": 7.5, "caps": 6, "int_goals": 0, "is_key": False},
        {"name": "Ayyoub Bouaddi", "pos": "CM", "club": "Lille", "age": 20, "rating": 81, "form": 8.0, "caps": 8, "int_goals": 1, "is_key": False},
        {"name": "Neil El Aynaoui", "pos": "CM", "club": "Roma", "age": 24, "rating": 82, "form": 8.0, "caps": 12, "int_goals": 1, "is_key": False},
        {"name": "Sofyan Amrabat", "pos": "DM", "club": "Real Betis", "age": 28, "rating": 83, "form": 8.0, "caps": 52, "int_goals": 1, "is_key": True},
        {"name": "Azzedine Ounahi", "pos": "CM", "club": "Girona", "age": 25, "rating": 81, "form": 7.5, "caps": 30, "int_goals": 3, "is_key": False},
        {"name": "Bilal El Khannouss", "pos": "CM", "club": "Stuttgart", "age": 21, "rating": 82, "form": 8.0, "caps": 14, "int_goals": 2, "is_key": False},
        {"name": "Ismael Saibari", "pos": "CM", "club": "PSV", "age": 23, "rating": 82, "form": 8.0, "caps": 10, "int_goals": 2, "is_key": False},
        # Forwards
        {"name": "Abdessamad Ezzalzouli", "pos": "FW", "club": "Real Betis", "age": 23, "rating": 82, "form": 8.0, "caps": 14, "int_goals": 4, "is_key": False},
        {"name": "Chemsdine Talbi", "pos": "FW", "club": "Sunderland", "age": 20, "rating": 81, "form": 7.5, "caps": 8, "int_goals": 2, "is_key": False},
        {"name": "Soufiane Rahimi", "pos": "FW", "club": "Al Ain", "age": 27, "rating": 82, "form": 8.0, "caps": 18, "int_goals": 7, "is_key": False},
        {"name": "Ayoub El Kaabi", "pos": "FW", "club": "Olympiacos", "age": 28, "rating": 82, "form": 8.0, "caps": 20, "int_goals": 8, "is_key": False},
        {"name": "Brahim Díaz", "pos": "FW", "club": "Real Madrid", "age": 26, "rating": 83, "form": 8.0, "caps": 22, "int_goals": 5, "is_key": True},
        {"name": "Yassine Gessime", "pos": "FW", "club": "Strasbourg", "age": 22, "rating": 79, "form": 7.5, "caps": 6, "int_goals": 1, "is_key": False},
        {"name": "Amaimouni", "pos": "FW", "club": "Eintracht Frankfurt", "age": 22, "rating": 79, "form": 7.5, "caps": 6, "int_goals": 1, "is_key": False},
    ],
}

# Summary data for remaining 36 teams (captain + avg squad rating)
SQUAD_SUMMARY: dict[str, dict] = {
    "USA": {"captain": "Christian Pulisic", "captain_club": "AC Milan", "captain_rating": 86, "avg_rating": 78, "star_player": "Christian Pulisic"},
    "MEX": {"captain": "Edson Álvarez", "captain_club": "Fenerbahçe", "captain_rating": 83, "avg_rating": 76, "star_player": "Santiago Giménez"},
    "CAN": {"captain": "Alphonso Davies", "captain_club": "Bayern Munich", "captain_rating": 87, "avg_rating": 79, "star_player": "Jonathan David"},
    "SCO": {"captain": "Andy Robertson", "captain_club": "Liverpool", "captain_rating": 85, "avg_rating": 75, "star_player": "Scott McTominay"},
    "URU": {"captain": "Federico Valverde", "captain_club": "Real Madrid", "captain_rating": 88, "avg_rating": 79, "star_player": "Darwin Núñez"},
    "ECU": {"captain": "Moisés Caicedo", "captain_club": "Chelsea", "captain_rating": 87, "avg_rating": 76, "star_player": "Piero Hincapié"},
    "PAR": {"captain": "Miguel Almirón", "captain_club": "Atlanta United", "captain_rating": 81, "avg_rating": 75, "star_player": "Julio Enciso"},
    "SEN": {"captain": "Kalidou Koulibaly", "captain_club": "Al-Hilal", "captain_rating": 83, "avg_rating": 77, "star_player": "Nicolas Jackson"},
    "EGY": {"captain": "Mohamed Salah", "captain_club": "Liverpool", "captain_rating": 89, "avg_rating": 73, "star_player": "Omar Marmoush"},
    "CIV": {"captain": "Seko Fofana", "captain_club": "Porto", "captain_rating": 82, "avg_rating": 74, "star_player": "Amad Diallo"},
    "COD": {"captain": "Chancel Mbemba", "captain_club": "Lille", "captain_rating": 80, "avg_rating": 72, "star_player": "Yoane Wissa"},
    "ZAF": {"captain": "Ronwen Williams", "captain_club": "Mamelodi Sundowns", "captain_rating": 80, "avg_rating": 70, "star_player": "Oswin Appollis"},
    "GHA": {"captain": "Thomas Partey", "captain_club": "Villarreal", "captain_rating": 83, "avg_rating": 74, "star_player": "Antoine Semenyo"},
    "ALG": {"captain": "Riyad Mahrez", "captain_club": "Al-Ahli", "captain_rating": 84, "avg_rating": 76, "star_player": "Mohamed Amoura"},
    "CPV": {"captain": "Stopira", "captain_club": "Torreense", "captain_rating": 72, "avg_rating": 68, "star_player": "Jovane Cabral"},
    "TUN": {"captain": "Ellyes Skhiri", "captain_club": "Eintracht Frankfurt", "captain_rating": 80, "avg_rating": 71, "star_player": "Hannibal Mejbri"},
    "NOR": {"captain": "Martin Ødegaard", "captain_club": "Arsenal", "captain_rating": 88, "avg_rating": 80, "star_player": "Erling Haaland"},
    "SWE": {"captain": "Victor Lindelöf", "captain_club": "Aston Villa", "captain_rating": 82, "avg_rating": 78, "star_player": "Viktor Gyökeres"},
    "SUI": {"captain": "Granit Xhaka", "captain_club": "Sunderland", "captain_rating": 83, "avg_rating": 77, "star_player": "Breel Embolo"},
    "TUR": {"captain": "Hakan Çalhanoğlu", "captain_club": "Inter Milan", "captain_rating": 86, "avg_rating": 79, "star_player": "Arda Güler"},
    "AUT": {"captain": "David Alaba", "captain_club": "Real Madrid", "captain_rating": 83, "avg_rating": 77, "star_player": "Marcel Sabitzer"},
    "CZE": {"captain": "Tomáš Souček", "captain_club": "West Ham", "captain_rating": 82, "avg_rating": 75, "star_player": "Patrik Schick"},
    "BIH": {"captain": "Edin Džeko", "captain_club": "Schalke", "captain_rating": 80, "avg_rating": 73, "star_player": "Ermedin Demirović"},
    "JPN": {"captain": "Wataru Endo", "captain_club": "Liverpool", "captain_rating": 82, "avg_rating": 77, "star_player": "Takefusa Kubo"},
    "KOR": {"captain": "Son Heung-min", "captain_club": "LAFC", "captain_rating": 87, "avg_rating": 76, "star_player": "Lee Kang-in"},
    "AUS": {"captain": "Mat Ryan", "captain_club": "Levante", "captain_rating": 80, "avg_rating": 72, "star_player": "Nestory Irankunda"},
    "SAU": {"captain": "Salem Al-Dawsari", "captain_club": "Al-Hilal", "captain_rating": 80, "avg_rating": 70, "star_player": "Saud Abdulhamid"},
    "IRN": {"captain": "Ehsan Hajsafi", "captain_club": "Sepahan", "captain_rating": 75, "avg_rating": 71, "star_player": "Mehdi Taremi"},
    "QAT": {"captain": "Hassan Al-Haydos", "captain_club": "Al-Sadd", "captain_rating": 76, "avg_rating": 67, "star_player": "Akram Afif"},
    "UZB": {"captain": "Eldor Shomurodov", "captain_club": "İstanbul Başakşehir", "captain_rating": 79, "avg_rating": 67, "star_player": "Abdukodir Khusanov"},
    "JOR": {"captain": "Musa Al-Taamari", "captain_club": "Rennes", "captain_rating": 74, "avg_rating": 64, "star_player": "Musa Al-Taamari"},
    "HAI": {"captain": "Jean-Ricner Bellegarde", "captain_club": "Wolves", "captain_rating": 78, "avg_rating": 66, "star_player": "Wilson Isidor"},
    "CUW": {"captain": "Leandro Bacuna", "captain_club": "Igdir", "captain_rating": 74, "avg_rating": 65, "star_player": "Tahith Chong"},
    "IRQ": {"captain": "Ali Al-Hamadi", "captain_club": "Luton Town", "captain_rating": 75, "avg_rating": 65, "star_player": "Zidane Iqbal"},
    "NZL": {"captain": "Chris Wood", "captain_club": "Nottingham Forest", "captain_rating": 79, "avg_rating": 68, "star_player": "Chris Wood"},
    "PAN": {"captain": "Amir Murillo", "captain_club": "Beşiktaş", "captain_rating": 76, "avg_rating": 68, "star_player": "Ismael Díaz"},
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
