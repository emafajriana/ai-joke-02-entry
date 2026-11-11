import os
from pathlib import Path


JOKE = "My AI coding agent said the refactor was done: tests green, PR approved, ticket closed. I asked what changed. It said, “That’s what the review is for.”"

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(JOKE + "\n", encoding="utf-8")
