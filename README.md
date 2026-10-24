# eba-meta

Cross-port gate for [eba-py](https://github.com/wlz987/eba-py),
[eba-ts](https://github.com/wlz987/eba-ts), and
[eba-rs](https://github.com/wlz987/eba-rs).

`tools/` vendors the workspace audits: example parity, rs/infra structure,
Inbox/Receiver API surface, duplicate ratio, and cross-end facts
(`diff-examples`). The full workspace `make release-check` remains the
developer gate.
