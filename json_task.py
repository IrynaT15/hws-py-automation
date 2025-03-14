import json


clubs_data = {
    "clubs": [
        {
            "name": "Liverpool",
            "country": "England",
            "wins": 6
        },
        {
            "name": "Real Madrid",
            "country": "Spain",
            "wins": 14
        },
        {
            "name": "AC Milan",
            "country": "Italy",
            "wins": 7
        },
        {
            "name": "Bayern Munich",
            "country": "Germany",
            "wins": 6
        },
        {
            "name": "Barcelona",
            "country": "Spain",
            "wins": 6
        }
    ]
}


with open("clubs_info.json", mode="w", encoding="utf-8") as write_file:
    json.dump(clubs_data, write_file, indent=4)


def read_and_display_club_with_max_wins(filename):
    with open(f"{filename}.json", mode="r", encoding="utf-8") as read_file:
        data = json.load(read_file)

    max_wins = 0
    clubs_with_max_wins = []

    for club in data["clubs"]:
        if club["wins"] > max_wins:
            max_wins = club["wins"]
            clubs_with_max_wins = [club]
        elif club["wins"] == max_wins:
            clubs_with_max_wins.append(club)

    return clubs_with_max_wins


clubs_with_max_wins = read_and_display_club_with_max_wins("clubs_info")

if clubs_with_max_wins:
    print(f"Clubs with most wins:\n")
    for club in clubs_with_max_wins:
        print(f"Club: {club["name"]}")
        print(f"Country: {club["country"]}")
        print(f"Number of wins: {club["wins"]}\n")
else:
    print("No clubs with most wins")
