import argparse
import json
from pathlib import Path


def print_first_records(file_path: Path, limit: int = 10) -> None:
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    with file_path.open("r", encoding="utf-8") as file:
        for index, line in enumerate(file, start=1):
            if index > limit:
                break

            line = line.strip()
            if not line:
                continue

            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                print(f"[line {index}] Invalid JSON: {exc}")
                continue

            print(f"Record {index}:")
            print(json.dumps(record, ensure_ascii=False, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Read a JSONL file and print the first 10 records."
    )
    parser.add_argument("file", type=Path, help="Path to the JSONL file")
    parser.add_argument(
        "-n",
        "--limit",
        type=int,
        default=10,
        help="Number of records to print, default is 10",
    )
    args = parser.parse_args()

    print_first_records(args.file, args.limit)


if __name__ == "__main__":
    main()
