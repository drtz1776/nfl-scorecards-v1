
import nflreadpy as nfl
import json
from pathlib import Path

# Load 2026 NFL schedule
schedules = nfl.load_schedules(2026)

# Create output directory
output_dir = Path("data")
output_dir.mkdir(exist_ok=True)

# Export pretty-printed JSON
with open(output_dir / "schedules_2026.json", "w") as f:
    json.dump(
        schedules.to_dicts(),
        f,
        indent=2,
        default=str
    )

# Display dataset information
print(f"Rows: {schedules.height:,}")
print(f"Columns: {schedules.width:,}")

if "game_id" in schedules.columns:
    print(f"Games: {schedules['game_id'].n_unique()}")

print("\nAvailable columns:")
for col in schedules.columns:
    print(col)

print("\nPretty-printed JSON exported successfully!")
