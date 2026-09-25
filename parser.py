from models import Connection, Hub


def parse_file(filename: str) -> tuple[list[Hub], list[Connection]]:
    hubs: list[Hub] = []
    connections: list[Connection] = []
    reading_connections = False

    with open(filename, encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            if line == "[connections]":
                reading_connections = True
                continue

            parts = line.split()

            if not reading_connections:
                if len(parts) != 4:
                    raise ValueError(
                        f"Invalid hub at line {line_number}: {line}"
                    )

                name, x, y, color = parts

                hubs.append(
                    Hub(
                        name=name,
                        x=float(x),
                        y=float(y),
                        color=color,
                    )
                )
            else:
                if len(parts) != 2:
                    raise ValueError(
                        f"Invalid connection at line {line_number}: {line}"
                    )

                source, destination = parts

                connections.append(
                    Connection(
                        source=source,
                        destination=destination,
                    )
                )

    return hubs, connections
