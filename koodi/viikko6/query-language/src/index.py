from statistics import Statistics
from player_reader import PlayerReader
from matchers.and_matcher import And
from matchers.has_at_least import HasAtLeast
from matchers.plays_in import PlaysIn


def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(5, "assists"),
        PlaysIn("PHI")
    )

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
