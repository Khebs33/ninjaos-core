# NinjaOS Core

NinjaOS is a modular intelligence operating system that produces enterprise-level diagnostics and opportunity maps across 80 business modules, 46 lenses, and 21 stress points.

## Structure

- `core_engine/`: Primary logic and module engine
- `scripts/`: CLI tools for audits and exports
- `deliverables/`: Output docs (1A, 2, etc.)
- `modules/`: Registry of M01–M80
- `backend/`: Intelligence + LLM pipeline (OpenAI)
- `frontend/`: UI framework (e.g., Streamlit)

## Commands

```bash
python scripts/audit_modules.py
```
