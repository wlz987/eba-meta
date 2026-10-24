"""四端例子名必须完全对齐：少一条、多一条都红。"""

from pathlib import Path

ROOT = Path.cwd()
ENDS = {
    "py": (ROOT / "eba-py" / "examples", ".py"),
    "ts": (ROOT / "eba-ts" / "examples", ".ts"),
    "rs": (ROOT / "eba-rs" / "eba-rs" / "examples", ".rs"),
    "infra": (ROOT / "eba-rs" / "eba-rs-infra" / "examples", ".rs"),
}

sets: dict[str, set[str]] = {}
for end, (folder, suffix) in ENDS.items():
    sets[end] = {
        path.stem
        for path in folder.glob(f"*{suffix}")
        if path.is_file() and not path.name.startswith("__")
    }

union = set().union(*sets.values())
failed = False
for end, names in sets.items():
    missing = sorted(union - names)
    extra = sorted(names - union)
    if missing or extra:
        failed = True
        print(f"{end}: missing {missing} extra {extra}")
if failed:
    raise SystemExit(1)
print(f"examples parity: {len(union)} names")
