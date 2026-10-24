"""四端 Inbox/Receiver/Subscription 契约名必须在源码里：少一个就红。"""

from pathlib import Path

ROOT = Path.cwd()
EXPECTED = {
    "py": (
        ("eba-py/eba/mail/inbox.py", "eba-py/eba/mail/bus.py", "eba-py/eba/mail/routes.py", "eba-py/eba/mail/routes_types.py", "eba-py/eba/mail/routes_detach.py", "eba-py/eba/mail/receiver.py", "eba-py/eba/mail/inbox_ops.py", "eba-py/eba/mail/bus_deliver.py", "eba-py/eba/rendezvous/records_routes.py", "eba-py/eba/rendezvous/records_submit.py", "eba-py/eba/rendezvous/records_take.py", "eba-py/eba/rendezvous/record.py", "eba-py/eba/runtime/runtime.py", "eba-py/eba/runtime/lifecycle.py", "eba-py/eba/runtime/spent.py", "eba-py/eba/runtime/add.py", "eba-py/eba/runtime/advance.py", "eba-py/eba/runtime/view.py", "eba-py/eba/runtime/drain.py", "eba-py/eba/runtime/close.py"),
        ("def receiver", "def is_closed", "def has_read", "def remaining", "def try_recv",
         "def close", "def borrow", "def take", "def is_active", "def active", "def disarm",
         "def add", "def advance", "def schedule", "def shutdown"),
    ),
    "ts": (
        ("eba-ts/src/mail/inbox.ts", "eba-ts/src/mail/inbox_ops.ts", "eba-ts/src/mail/bus.ts", "eba-ts/src/mail/bus/base.ts", "eba-ts/src/mail/bus/types.ts", "eba-ts/src/mail/routes.ts", "eba-ts/src/mail/routes/detach.ts", "eba-ts/src/mail/routes/base.ts", "eba-ts/src/mail/routes/types.ts", "eba-ts/src/mail/routes/subscribe.ts", "eba-ts/src/mail/receiver.ts", "eba-ts/src/runtime/runtime.ts", "eba-ts/src/runtime/base.ts", "eba-ts/src/runtime/admission.ts", "eba-ts/src/runtime/advance.ts", "eba-ts/src/runtime/lifecycle.ts"),
        ("receiver(", "get isClosed", "get hasRead", "remaining(", "tryRecv(", "close(",
         "borrow(", "take(", "get isActive", "active(", "disarm(",
         "add(", "advance(", "schedule(", "shutdown("),
    ),
    "rs": (
        ("eba-rs/eba-rs/src/mail/inbox.rs", "eba-rs/eba-rs/src/mail/inbox/receiver.rs", "eba-rs/eba-rs/src/mail/inbox/routes.rs", "eba-rs/eba-rs/src/mail/inbox/ops.rs", "eba-rs/eba-rs/src/mail/inbox/wakers.rs", "eba-rs/eba-rs/src/mail/inbox/state.rs", "eba-rs/eba-rs/src/mail/inbox/route.rs", "eba-rs/eba-rs/src/mail/inbox/core.rs", "eba-rs/eba-rs/src/mail/bus/mod.rs", "eba-rs/eba-rs/src/mail/bus/grants.rs", "eba-rs/eba-rs/src/mail/bus/grants/subscribe.rs", "eba-rs/eba-rs/src/mail/bus/grants/view.rs", "eba-rs/eba-rs/src/mail/bus/deliver.rs", "eba-rs/eba-rs/src/mail/bus/deliver/entry.rs", "eba-rs/eba-rs/src/mail/bus/waits.rs", "eba-rs/eba-rs/src/mail/bus/lease.rs", "eba-rs/eba-rs/src/mail/bus/vote.rs", "eba-rs/eba-rs/src/runtime/runtime/mod.rs", "eba-rs/eba-rs/src/runtime/runtime/close.rs", "eba-rs/eba-rs/src/runtime/runtime/advance.rs", "eba-rs/eba-rs/src/runtime/runtime/add.rs"),
        ("pub fn receiver", "pub fn is_closed", "pub fn has_read", "pub fn remaining",
         "pub fn try_recv", "pub fn close", "pub fn borrow", "pub fn take",
         "pub fn is_active", "pub fn active", "pub fn disarm",
         "pub fn add", "pub fn advance", "pub fn schedule", "pub fn shutdown"),
    ),
    "infra": (
        ("eba-rs/eba-rs-infra/src/mail/inbox.rs", "eba-rs/eba-rs-infra/src/mail/inbox/receiver.rs", "eba-rs/eba-rs-infra/src/mail/inbox/routes.rs", "eba-rs/eba-rs-infra/src/mail/inbox/ops.rs", "eba-rs/eba-rs-infra/src/mail/inbox/wakers.rs", "eba-rs/eba-rs-infra/src/mail/inbox/state.rs", "eba-rs/eba-rs-infra/src/mail/inbox/route.rs", "eba-rs/eba-rs-infra/src/mail/inbox/core.rs", "eba-rs/eba-rs-infra/src/mail/bus/mod.rs", "eba-rs/eba-rs-infra/src/mail/bus/grants.rs", "eba-rs/eba-rs-infra/src/mail/bus/grants/subscribe.rs", "eba-rs/eba-rs-infra/src/mail/bus/grants/view.rs", "eba-rs/eba-rs-infra/src/mail/bus/deliver.rs", "eba-rs/eba-rs-infra/src/mail/bus/deliver/entry.rs", "eba-rs/eba-rs-infra/src/mail/bus/waits.rs", "eba-rs/eba-rs-infra/src/mail/bus/lease.rs", "eba-rs/eba-rs-infra/src/mail/bus/vote.rs", "eba-rs/eba-rs-infra/src/runtime/runtime/mod.rs", "eba-rs/eba-rs-infra/src/runtime/runtime/close.rs", "eba-rs/eba-rs-infra/src/runtime/runtime/advance.rs", "eba-rs/eba-rs-infra/src/runtime/runtime/add.rs"),
        ("pub fn receiver", "pub fn is_closed", "pub fn has_read", "pub fn remaining",
         "pub fn try_recv", "pub fn close", "pub fn borrow", "pub fn take",
         "pub fn is_active", "pub fn active", "pub fn disarm",
         "pub fn add", "pub fn advance", "pub fn schedule", "pub fn shutdown"),
    ),
}
for end, (paths, tokens) in EXPECTED.items():
    text = "\n".join((ROOT / p).read_text(encoding="utf-8") for p in paths)
    missing = [token for token in tokens if token not in text]
    if missing:
        print(f"api missing: {end} {missing}")
        raise SystemExit(1)
THREE_END = {
    "py": (
        ("eba-py/eba/job/caller.py", "eba-py/eba/runtime/drive.py", "eba-py/eba/runtime/drive_open.py", "eba-py/eba/runtime/drive_run.py", "eba-py/eba/runtime/drive_release.py", "eba-py/eba/envelope/build.py", "eba-py/eba/envelope/header_ops.py"),
        ("def admit", "def cancel", "def open", "def kick"),
    ),
    "ts": (
        ("eba-ts/src/job/caller.ts", "eba-ts/src/runtime/drive.ts", "eba-ts/src/runtime/drive/base.ts", "eba-ts/src/runtime/drive/open.ts"),
        ("admit(", "cancel(", "open(", "kick("),
    ),
    "rs": (
        ("eba-rs/eba-rs/src/job/caller/mod.rs", "eba-rs/eba-rs/src/drive.rs", "eba-rs/eba-rs/src/drive/base.rs", "eba-rs/eba-rs/src/drive/types.rs", "eba-rs/eba-rs/src/drive/lifecycle.rs", "eba-rs/eba-rs/src/drive/open.rs", "eba-rs/eba-rs/src/drive/release.rs", "eba-rs/eba-rs/src/drive/run.rs"),
        ("pub fn admit", "pub fn cancel", "pub fn open", "pub fn kick"),
    ),
}
for end, (paths, tokens) in THREE_END.items():
    text = "\n".join((ROOT / p).read_text(encoding="utf-8") for p in paths)
    missing = [token for token in tokens if token not in text]
    if missing:
        print(f"api missing: {end} {missing}")
        raise SystemExit(1)
print(
    f"api: {len(EXPECTED)} ends x {len(next(iter(EXPECTED.values()))[1])} symbols; "
    f"{len(THREE_END)} ends x {len(next(iter(THREE_END.values()))[1])} symbols"
)
