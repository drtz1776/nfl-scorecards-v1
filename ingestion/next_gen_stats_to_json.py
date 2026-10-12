
import nflreadpy as nfl
import json
from pathlib import Path

# Create output directory
output_dir = Path("data")
output_dir.mkdir(exist_ok=True)

# Load all three Next Gen Stats categories
stat_types = ["passing", "rushing", "receiving"]

for stat_type in stat_types:

    stats = nfl.load_nextgen_stats(
        2026,
        stat_type=stat_type
    )

    # Export pretty-printed JSON
    filename = output_dir / f"nextgen_{stat_type}_2026.json"

    with open(filename, "w") as f:
        json.dump(
            stats.to_dicts(),
            f,
            indent=2,
            default=str
        )

    # Display dataset information
    print(f"\n{'=' * 60}")
    print(f"NEXT GEN STATS: {stat_type.upper()}")
    print(f"{'=' * 60}")

    print(f"Rows: {stats.height:,}")
    print(f"Columns: {stats.width:,}")

    print("\nAvailable columns:")
    for col in stats.columns:
        print(col)

    print(f"\nExported: {filename}")
