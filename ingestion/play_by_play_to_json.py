import nflreadpy as nfl
import json
from pathlib import Path

# Load 2026 NFL play-by-play data
pbp = nfl.load_pbp(2026)

# Create output directory
output_dir = Path("data")
output_dir.mkdir(exist_ok=True)

# Export pretty-printed JSON
with open(output_dir / "pbp_2026.json", "w") as f:
    json.dump(
        pbp.to_dicts(),
        f,
        indent=2,
        default=str
    )

# Display dataset information
print(f"Rows: {pbp.height:,}")
print(f"Columns: {pbp.width:,}")
print(f"Games: {pbp['game_id'].n_unique()}")

print("\nAvailable columns:")
for col in pbp.columns:
    print(col)

print("\nPretty-printed JSON exported successfully!")