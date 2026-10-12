import nflreadpy as nfl
import json
from pathlib import Path

# Load 2026 NFL weekly player statistics
player_stats = nfl.load_player_stats(
    2026,
    summary_level="week"
)

# Create output directory
output_dir = Path("data")
output_dir.mkdir(exist_ok=True)

# Export pretty-printed JSON
with open(output_dir / "player_stats_2026.json", "w") as f:
    json.dump(
        player_stats.to_dicts(),
        f,
        indent=2,
        default=str
    )

# Display dataset information
print(f"Rows: {player_stats.height:,}")
print(f"Columns: {player_stats.width:,}")

print("\nAvailable columns:")
for col in player_stats.columns:
    print(col)

print("\nPretty-printed JSON exported successfully!")