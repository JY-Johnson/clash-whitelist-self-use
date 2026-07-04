# Contributing

This repository is primarily maintained for personal use, but the structure is kept public and readable.

## Maintenance rules

1. Keep real node credentials out of the repository.
2. Do not commit downloaded third-party rule files by default.
3. Put custom direct rules in `rules/custom-direct.txt`.
4. Regenerate `dist/whitelist-overlay.yaml` after rule changes:

```powershell
python .\scripts\build_overlay.py
```

5. If you change upstream source usage, update:
   - `README.md`
   - `THIRD_PARTY.md`
   - `CHANGELOG.md`

## Style

- Use UTF-8 text files.
- Prefer LF line endings in repository-managed text files.
- Keep comments short and practical.
- Do not mix sensitive deployment details into examples.

## Release checklist

Before publishing a meaningful change, check:

- `python .\scripts\build_overlay.py`
- `python .\scripts\merge_subscription.py --help`
- the generated YAML still follows whitelist mode
- README examples still match real file paths

