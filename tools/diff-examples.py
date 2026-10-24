# -*- coding: utf-8 -*-
# 同一个故事讲四遍：py / rs / infra / ts 各自的 examples 跑同一次下单、同一台满箱，
# 把「事实」从各语言的打印写法里剥出来对表。打印形状天生不同（py 打字典、ts 打对象、
# rs 的 Payload 是 Arc<dyn Any>），比的是事实，不是句子。
import re, os, subprocess, sys
from pathlib import Path
R = str(Path.cwd())
def run(cmd, cwd):
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, shell=isinstance(cmd, str))
    if p.returncode != 0:
        raise SystemExit(f"跑不动 {cmd} @ {cwd}\n{p.stderr[-800:]}")
    return p.stdout
def facts_order(out):
    ids = re.findall(r"\b[0-9a-f]{32}\b", out)
    sku = [t for line in out.splitlines() if line.startswith("甲")
           for t in re.findall(r"sku['\"]?\s*[:=]\s*['\"]?([A-Za-z0-9_-]+)", line)]
    err = [t for line in out.splitlines() if line.startswith("乙")
           for t in re.findall(r"[a-z][a-z_]{3,}", line) if t not in ("ok",)]
    return dict(ids=ids, sku=sku, refusal=err)
def facts_bus(out):
    rows = []
    best = []
    for line in out.splitlines():
        topic = re.match(r"([a-z_]+(?:\.[a-z_]+)+)", line)
        pairs = re.findall(r"['\"]([\u4e00-\u9fff]+)['\"],\s*['\"](child-\d+)['\"]", line)
        if topic and pairs:
            rows.append((topic.group(1), pairs))
        found = re.match(r"best-effort (\d+) (\S+) (\S+)", line)
        if found:
            best.append(found.groups())
    return dict(grants=rows, best=best)
CASES = {
    "order": [("py", R + "/eba-py", ["python3", "examples/order.py"], {"PYTHONPATH": "."}),
              ("rs", R + "/eba-rs", ["cargo", "run", "-q", "--example", "order", "-p", "eba-rs"], {}),
              ("infra", R + "/eba-rs", ["cargo", "run", "-q", "--example", "order", "-p", "eba-rs-infra"], {}),
              ("ts", R + "/eba-ts", ["node", "examples/order.ts"], {})],
    "bus":   [("py", R + "/eba-py", ["python3", "examples/bus.py"], {"PYTHONPATH": "."}),
              ("rs", R + "/eba-rs", ["cargo", "run", "-q", "--example", "bus", "-p", "eba-rs"], {}),
              ("infra", R + "/eba-rs", ["cargo", "run", "-q", "--example", "bus", "-p", "eba-rs-infra"], {}),
              ("ts", R + "/eba-ts", ["node", "examples/bus.ts"], {})],
}
bad = 0
def run(cmd, cwd, extra):
    env = dict(os.environ)
    env.update(extra)
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, env=env)
    if p.returncode != 0:
        raise SystemExit(f"跑不动 {cmd} @ {cwd}\n{p.stderr[-800:]}")
    return p.stdout
for case, spec in CASES.items():
    grab = facts_order if case == "order" else facts_bus
    got = {name: grab(run(cmd, cwd, extra)) for name, cwd, cmd, extra in spec}
    names = [name for name, _, _, _ in spec]
    base = got["py"]
    print(f"== {case}: py {base}")
    for name in names[1:]:
        diff = {k: (base.get(k), got[name].get(k)) for k in base if base.get(k) != got[name].get(k)}
        if diff:
            bad += 1
            print(f"   {name:6s} 不一致 {diff}")
        else:
            print(f"   {name:6s} 一致")
print("examples differ:", bad)
sys.exit(1 if bad else 0)
