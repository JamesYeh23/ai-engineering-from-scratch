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

## Review queue
