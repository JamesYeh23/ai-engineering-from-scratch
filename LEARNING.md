# My AI Engineering Path
<!-- Managed by the ai-engineering-from-scratch learning skills.
     Repo: https://github.com/rohitg00/ai-engineering-from-scratch -->

## Mission
Ship an AI product. Build goal: not sure yet, to be decided along the way.
Teaching style: start from the very beginning and explain everything like I'm a high school student.

## Placement
- Date: 2026-09-30
- Score: self-selected
- Entry point: Phase 0: Setup & Tooling
- Pace: as fast as possible

## Path
| Phase | Name | Status | Est. hours |
|-------|------|--------|------------|
| 0 | Setup & Tooling | Do | 14 |
| 1 | Math Foundations | Do | 23 |
| 2 | ML Fundamentals | Do | 21 |
| 3 | Deep Learning Core | Do | 15 |
| 4 | Computer Vision | Do | 27 |
| 5 | NLP — Foundations to Advanced | Do | 30 |
| 6 | Speech & Audio | Do | 18 |
| 7 | Transformers Deep Dive | Do | 14 |
| 8 | Generative AI | Do | 14 |
| 9 | Reinforcement Learning | Do | 13 |
| 10 | LLMs from Scratch | Do | 26 |
| 11 | LLM Engineering | Do | 19 |
| 12 | Multimodal AI | Do | 65 |
| 13 | Tools & Protocols | Do | 43 |
| 14 | Agent Engineering | Do | 55 |
| 15 | Autonomous Systems | Do | 20 |
| 16 | Multi-Agent & Swarms | Do | 28 |
| 17 | Infrastructure & Production | Do | 32 |
| 18 | Ethics, Safety & Alignment | Do | 31 |
| 19 | Capstone Projects | Do | 620 |
| | **Total** | | **1128** |

## Progress log
| Date | Lesson | Quiz | Note |
|------|--------|------|------|
| 2026-09-30 | 0.01 Dev Environment | 3/3 (+ venv & layer-order checks in dialogue) | verify.py passed (Python 3.12.7 via miniconda, git 2.39.5). Made `.venv`, installed numpy 2.5.3, dot product = 14. Bonus: outer vs cross product. Mac → MPS, not CUDA. Skipped for now: Node/Rust/Julia/PyTorch installs (install when a lesson needs them). |
| 2026-10-07 | 0.02 Git & Collaboration | All concept checks correct | Already knew init/push/merge. Forked to JamesYeh23; `origin` = fork (push progress), `upstream` = rohitg00 (pull new lessons). Branch `my-progress` pushed. .gitignore: models too big/regenerable, .env = secrets. Leaked key stays in history → rotate it. |
| 2026-10-07 | 0.03 GPU Setup & Cloud | All concept checks correct | Apple M5, 32 GB unified memory. torch 2.14.1; CUDA False, MPS True (lesson's gpu_check.py is CUDA-only). Wrote my-work/gpu_bench.py: first run 0.5x (cold start) → added warm-up + synchronize → 2.3x. Learned GPU is async. fp16 rule: 32 GB / 2 bytes ≈ 16B params (practically ~10B; training needs ~4x more). |
| 2026-10-07 | 0.04 APIs & Keys | All concept checks correct | Created Anthropic key → `.env` (ignored by .gitignore:29). Learned .env isn't auto-loaded: `set -a; source .env; set +a`. SDK + raw HTTP calls both worked (18 in / ~75 out tokens). LLM output varies (sampling). Wrong key → server 401 vs missing key → local TypeError. Status codes 400/401/429/5xx. |
| 2026-10-07 | 0.05 Jupyter Notebooks | All concept checks correct | Had used Jupyter in an ML class. Installed jupyterlab 4.6.4 in .venv. Hidden-state trap: re-running a cell → x=40 vs 20 after Restart & Run All; brackets = execution order. Kernel uses .venv Python (sys.executable). %timeit: list comp 2.18 ms vs numpy 447 µs ≈ 5x (vectorization). Explore in notebooks, ship in scripts. |
| 2026-10-15 | 0.06 Python Environments | All concept checks correct | Hit "forgot to activate" 3x (miniconda python/pip is default in new terminals; `which pip` diagnoses). pip freeze: 4 direct → 110 pkgs (transitive deps). Installed uv 0.13.0 (PATH lesson). Built my-work/evn-demo: numpy 1.26.4 vs course 2.5.3 = isolation proven; `uv run` needs no activation. pyproject = intent (2 lines, ranges) vs uv.lock = exact (19). Typosquatting caught ("antropic"). Don't mix pip+conda. env_setup.sh all PASS (added pandas, sklearn, matplotlib). |
| 2026-10-15 | 0.07 Docker for AI | Concepts only (Docker not installed yet; deferred by choice) | Had built an image before. Layer caching: COPY pyproject.toml + uv.lock → uv sync → COPY . . (rarely-changing on top). Needed help recalling volume mounts: `-v ~/models:/models` (no spaces, absolute container path). Containers on Mac = Linux VM → no MPS; run GPU work in native .venv. Compose services reach each other by service name. TODO: install Docker Desktop when a lesson needs it (~Phase 17). |
| 2026-10-15 | 0.08 Editor Setup | All concept checks correct | VS Code already installed (Python/Pylance/debugpy). Added Jupyter, Ruff, Black. Selected .venv via "Python: Select Interpreter" (editor ignores terminal activation). Learned: Ruff = linter you don't import; I001 import grouping fixed with Cmd+. Quick Fix. Lesson settings.json → .vscode/ (gitignored); Black format-on-save verified (spaces + double quotes). Skipped Remote SSH (no remote box yet). |
| 2026-10-18 | 0.09 Data Management | All concept checks correct (val-set role corrected) | `uv pip install datasets` → fsspec downgraded (dependency resolution). Plain `python` = miniconda again → used `uv run python` (finds .venv). data_utils.py all pass: rotten_tomatoes 8530 rows; CSV 59.5k / JSON 68.5k / Parquet 41.4k (columnar; JSON repeats keys ≈ +17 B/row). Train=optimizer, val=you tune, test=final once. Different seed → can't attribute score change to the model. HF cache at ~/.cache/huggingface. |
| 2026-10-18 | 0.10 Terminal & Shell | All concept checks correct | Built pipeline `tail -n 11 log \| awk '{print $4}'`. stdout vs stderr: `>` misses errors; `2>&1` must come AFTER `> file` (left-to-right); worked out stdout buffering → `python -u` / PYTHONUNBUFFERED. Quoting paths with spaces. Added `aie` alias to ~/.zshrc (cd + .venv + .env) — fixes recurring miniconda issue. Installed tmux 3.8; detach/reattach proved session kept counting (step 60). SSH/htop deferred to cloud-GPU phases. |
| 2026-10-27 | 0.11 Linux for AI | All concept checks correct (needed a foothold on case sensitivity) | Permissions: `-rw-r--r--` → Permission denied → `chmod +x` → `-rwxr-xr-x` (u+x for owner only). Disk hunt with `du -sh * \| sort -hr` drill-down: ~/.cache/huggingface 4.4G = two old PDF models (PDF-Extract-Kit 3.7G, layoutreader 680M) from another project; .venv 1.3G; uv cache 520M. Mac case-insensitive vs Linux case-sensitive → `from Model import` breaks on Linux. No Linux box yet; apt/sudo/systemd concepts only. |

## Review queue
