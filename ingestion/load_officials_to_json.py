
import nflreadpy as nfl
import json
from pathlib import Path

# Load 2026 NFL officials
officials = nfl.load_officials(2026)

# Create output directory
output_dir = Path("data")
output_dir.mkdir(exist_ok=True)

# Export pretty-printed JSON
with open(output_dir / "officials_2026.json", "w") as f:
    json.dump(
        officials.to_dicts(),
        f,
        indent=2,
        default=str
    )

# Display dataset information
print(f"Rows: {officials.height:,}")
print(f"Columns: {officials.width:,}")

print("\nAvailable columns:")
for col in officials.columns:
    print(col)

print("\nPretty-printed JSON exported successfully!")
