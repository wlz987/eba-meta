"""Check that all four example ends expose the same example names."""

from pathlib import Path
import sys

ROOT = Path.cwd()
if not (ROOT / "eba-py").is_dir():
    ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = {
    "py": ROOT / "eba-py" / "examples",
    "ts": ROOT / "eba-ts" / "examples",
    "rs": ROOT / "eba-rs" / "eba-rs" / "examples",
    "infra": ROOT / "eba-rs" / "eba-rs-infra" / "examples",
}
SUFFIX = {"py": ".py", "ts": ".ts", "rs": ".rs", "infra": ".rs"}

sets = {}
for end, folder in EXAMPLES.items():
    sets[end] = {item.stem for item in folder.glob(f"*{SUFFIX[end]}")}

base = sets["py"]
if len(base) != 33:
    sys.exit(f"expected 33 py examples, got {len(base)}")
for end, names in sets.items():
    missing = sorted(base - names)
    extra = sorted(names - base)
    if missing or extra:
        sys.exit(f"{end}: missing={missing} extra={extra}")
print("parity ok: 33 examples x 4 ends")
