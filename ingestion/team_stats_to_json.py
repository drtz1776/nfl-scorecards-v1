import nflreadpy as nfl
import json
from pathlib import Path

# Load 2026 NFL team statistics
team_stats = nfl.load_team_stats(2026)

# Create output directory
output_dir = Path("data")
output_dir.mkdir(exist_ok=True)

# Export pretty-printed JSON
with open(output_dir / "team_stats_2026.json", "w") as f:
    json.dump(
        team_stats.to_dicts(),
        f,
        indent=2,
        default=str
    )

# Display dataset information
print(f"Rows: {team_stats.height:,}")
print(f"Columns: {team_stats.width:,}")
print(f"Teams: {team_stats['team'].n_unique()}")

print("\nAvailable columns:")
for col in team_stats.columns:
    print(col)

print("\nPretty-printed JSON exported successfully!")