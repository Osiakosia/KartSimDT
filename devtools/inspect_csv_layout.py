from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> None:

    file_path = ROOT / "tests" / "data" / "aim" / "rotena_session.csv"

    with file_path.open(encoding="utf-8") as file:

        for number, line in enumerate(file, start=1):

            print(f"{number:3d}: {repr(line)}")

            if number == 60:
                break


if __name__ == "__main__":
    main()
