
import nflreadpy as nfl
import json
from pathlib import Path

# Load 2026 NFL snap counts
snap_counts = nfl.load_snap_counts(2026)

# Create output directory
output_dir = Path("data")
output_dir.mkdir(exist_ok=True)

# Export pretty-printed JSON
with open(output_dir / "snap_counts_2026.json", "w") as f:
    json.dump(
        snap_counts.to_dicts(),
        f,
        indent=2,
        default=str
    )

# Display dataset information
print(f"Rows: {snap_counts.height:,}")
print(f"Columns: {snap_counts.width:,}")

print("\nAvailable columns:")
for col in snap_counts.columns:
    print(col)

print("\nPretty-printed JSON exported successfully!")
