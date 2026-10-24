"""rs 与 infra 的源文件结构必须镜像：一边多/少一个模块就红。"""

from pathlib import Path

ROOT = Path.cwd()
LEFT = ROOT / "eba-rs" / "eba-rs" / "src"
RIGHT = ROOT / "eba-rs" / "eba-rs-infra" / "src"


def files(base: Path) -> set[str]:
    return {str(p.relative_to(base)) for p in base.rglob("*.rs")}


left = files(LEFT)
right = files(RIGHT)
# no_std 端口刻意不带 Drive/wake：这些只属于 rs；Drive 的子模块同样只属于 rs。
ALLOWED_RS_ONLY = {"drive.rs", "wake.rs"}


def rs_only(path: str) -> bool:
    return path in ALLOWED_RS_ONLY or path.startswith("drive/")


extra_rs = {path for path in left - right if not rs_only(path)}
extra_infra = right - left
if extra_rs or extra_infra:
    print(f"structure drift: only rs={sorted(extra_rs)} only infra={sorted(extra_infra)}")
    raise SystemExit(1)
print(f"structure: {len(right)} mirrored files (+{len(left - right)} rs-only)")
