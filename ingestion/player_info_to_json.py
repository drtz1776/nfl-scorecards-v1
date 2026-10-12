import nflreadpy as nfl
import json
from pathlib import Path

# Load NFL player database
players = nfl.load_players()

# Create output directory
output_dir = Path("data")
output_dir.mkdir(exist_ok=True)

# Export pretty-printed JSON
with open(output_dir / "players.json", "w") as f:
    json.dump(
        players.to_dicts(),
        f,
        indent=2,
        default=str
    )

# Display dataset information
print(f"Rows: {players.height:,}")
print(f"Columns: {players.width:,}")

print("\nAvailable columns:")
for col in players.columns:
    print(col)

print("\nPretty-printed JSON exported successfully!")