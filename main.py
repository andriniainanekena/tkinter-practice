from parser import parse_file
from viewer import GraphViewer


def main() -> None:
    hubs, connections = parse_file("data.txt")

    viewer = GraphViewer(
        hubs=hubs,
        connections=connections,
    )

    viewer.run()


if __name__ == "__main__":
    main()
