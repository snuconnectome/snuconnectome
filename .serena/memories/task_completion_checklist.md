# Task Completion Checklist

## Before Completing Any Document Task

### Quality Validation
- [ ] **Typography Check**
  - Line-height ≥1.7 for Korean text
  - Korean font size = English size +1-2pt (e.g., 13pt Korean = 12pt English)
  - No italic formatting on Korean text (use bold or color)
  - Proper font pairing (KoPub World + Inter/Noto)
  
- [ ] **Structure Check**
  - Clear heading hierarchy (H1 > H2 > H3)
  - Page numbers present (for documents >1 page)
  - Table of contents (for documents >3 pages)
  - Consistent numbering and formatting

- [ ] **Content Check**
  - Formal, professional tone maintained
  - Concrete data included (numbers, dates, percentages)
  - Institutional voice for proposals (서울대학교 ~는, NOT 나는)
  - All claims evidence-based

- [ ] **Accessibility Check**
  - Language tags for screen readers
  - Alt text for images
  - Color contrast meets WCAG standards
  - Logical reading order

### Document Design Analysis
- [ ] Run `/doc-design <file>` for professional review
- [ ] Address HIGH priority issues identified
- [ ] Review MEDIUM priority recommendations
- [ ] Document LOW priority items for future improvement

### File Management
- [ ] Source `.md` file updated and saved
- [ ] PDF exported if final deliverable
- [ ] Descriptive filename with underscores (e.g., `Hotel_Comparison_Report.md`)
- [ ] Files placed in appropriate directories

### Version Control
- [ ] Changes reviewed with `git diff`
- [ ] Changes staged: `git add <file>`
- [ ] Committed with descriptive message: `git commit -m "Update budget analysis with revised pricing"`
- [ ] Consider pushing to remote: `git push origin main`

## Project-Specific Workflows

### Creating New Proposal Document
1. Create `.md` file with descriptive name
2. Reference `proposal_prompt.md` for structure
3. Apply Korean typography standards
4. Include concrete data and evidence
5. Run `/doc-design` for quality check
6. Export to PDF
7. Commit to git with clear message

### Updating Existing Document
1. Read current version to understand context
2. Make targeted changes
3. Verify typography compliance
4. Re-run `/doc-design` if major changes
5. Update PDF if needed
6. Commit changes

### Comparative Analysis
1. Gather data from all sources
2. Create comparison table
3. Use consistent metrics across options
4. Include budget breakdowns
5. Provide clear recommendations
6. Validate with `/doc-design`

## Never Skip
- Typography validation (critical for Korean documents)
- Evidence-based claims (no speculation)
- Git commit (preserve version history)
- Professional tone (academic audience)

## Common Pitfalls to Avoid
- ❌ Line-height <1.6 (Korean text becomes cramped)
- ❌ Using italic for Korean emphasis
- ❌ Same font size for Korean and English
- ❌ Personal voice in institutional proposals ("나는" → "본 학과는")
- ❌ Missing concrete data (percentages, dates, numbers)
- ❌ Committing without descriptive message
