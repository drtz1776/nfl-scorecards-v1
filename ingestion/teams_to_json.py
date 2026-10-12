
import nflreadpy as nfl
import json
from pathlib import Path

# Load NFL team reference data
teams = nfl.load_teams()

# Create output directory
output_dir = Path("data")
output_dir.mkdir(exist_ok=True)

# Export pretty-printed JSON
with open(output_dir / "teams.json", "w") as f:
    json.dump(
        teams.to_dicts(),
        f,
        indent=2,
        default=str
    )

# Display dataset information
print(f"Rows: {teams.height:,}")
print(f"Columns: {teams.width:,}")

print("\nAvailable columns:")
for col in teams.columns:
    print(col)

print("\nPretty-printed JSON exported successfully!")
