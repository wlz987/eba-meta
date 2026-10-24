"""量 rs/infra 镜像文件的文本相似度：只报数，不设硬门槛。"""

import difflib
import statistics
from pathlib import Path

ROOT = Path.cwd()
LEFT = ROOT / "eba-rs" / "eba-rs" / "src"
RIGHT = ROOT / "eba-rs" / "eba-rs-infra" / "src"
ratios = []
worst = []
for left in sorted(LEFT.rglob("*.rs")):
    rel = left.relative_to(LEFT)
    right = RIGHT / rel
    if not right.is_file():
        continue
    a = left.read_text(encoding="utf-8")
    b = right.read_text(encoding="utf-8")
    ratio = difflib.SequenceMatcher(None, a, b).ratio()
    ratios.append(ratio)
    worst.append((ratio, str(rel)))
worst.sort()
print(
    f"duplicate: {len(ratios)} pairs, median {statistics.median(ratios):.3f}, "
    f"mean {statistics.mean(ratios):.3f}, min {worst[0][0]:.3f} ({worst[0][1]})"
)
