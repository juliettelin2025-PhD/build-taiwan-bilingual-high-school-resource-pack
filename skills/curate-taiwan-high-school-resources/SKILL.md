---
name: curate-taiwan-high-school-resources
description: Curate legally accessible teaching resources for Taiwanese senior-high learners. Use when a user wants subject materials inventoried, downloaded from an account they may lawfully use, rights-checked, renamed, deduplicated, classified by subject and grade, or prepared as a reusable bilingual-school resource library.
---

# Curate Taiwan High-School Resources

## Workflow

1. Confirm the destination and the subjects, grades, languages, and file types in scope.
2. Check whether each source requires a login, subscription, purchase, or separate permission. Never start a trial, purchase, bypass access controls, or redistribute restricted files without explicit authority.
3. Create the taxonomy in `references/taxonomy.md`. Put a cross-disciplinary item in its primary subject folder and record secondary subjects in the manifest.
4. Download only files the user can lawfully access. Preserve the original; do not silently alter it.
5. Run `scripts/inventory_resources.py DESTINATION --output manifest.csv` to create a reproducible inventory with SHA-256 hashes.
6. Complete the pedagogical and rights fields in the manifest: subject, topic, grade, CEFR or language load, teacher guide, answer key, source URL, license/access note, and reuse decision.
7. Flag duplicates, unknown rights, low scan quality, missing attribution, or content that is not suitable for Taiwanese senior-high learners.
8. Report downloaded, skipped, blocked, and needs-review counts separately. Never claim a download succeeded unless the file exists and is readable.

## Quality bar

- Prefer authentic subject content with explicit objectives, teacher guidance, answer keys, editable tasks, and language scaffolds.
- Keep source URL, author, title, access date, and rights note beside every file.
- Use Traditional Chinese folder labels and stable ASCII filenames when cross-platform Git use matters.
- Do not commit copyrighted teaching files to a public repository unless redistribution is clearly allowed. Commit the skill, taxonomy, manifests, and source links instead.

## Resources

- Read `references/taxonomy.md` before creating folders.
- Use `scripts/inventory_resources.py` after every download batch and before handoff.
