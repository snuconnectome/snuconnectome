# Suggested Commands

## Essential Workflow Commands

### Start Development Session
```bash
# Start MCP servers and launch Gemini CLI
./run_gemini.sh
```

### Git Operations (Darwin/macOS)
```bash
# Check status
git status

# Check current branch
git branch

# View recent commits
git log --oneline -5

# Stage changes
git add <file>

# Commit with message
git commit -m "descriptive message"

# Push to remote
git push origin main
```

### File Operations (macOS)
```bash
# List files
ls -la

# Search for files
find . -name "*.md"

# Search in files
grep -r "search term" .

# View file
cat <filename>

# Create directory
mkdir <dirname>

# Remove file
rm <filename>
```

## Claude Code Custom Commands

### Document Design Analysis
```bash
# Analyze document design with Korean typography expertise
/doc-design <file_path>

# Examples:
/doc-design Hakone_Retreat_Fore_vs_Kajikaso_Report.pdf
/doc-design README.md
```

### MCP Server Integration
```bash
# Load project context (via Serena)
/sc:load

# Save session state
/sc:save

# Deep research (via Tavily)
/sc:research <topic>
```

## Document Generation Workflow

### Creating New Proposals
1. Create `.md` file with descriptive name
2. Use `proposal_prompt.md` as template/guide
3. Write content following Korean typography standards
4. Review with `/doc-design <file>`
5. Export to PDF
6. Commit to git

### Editing Existing Documents
1. Open `.md` source file
2. Make changes following style conventions
3. Check typography: line-height 1.7+, Korean font size +1pt
4. Export to PDF
5. Review and commit

## Quality Checks Before Completion
- [ ] Line-height ≥1.7 for Korean text
- [ ] Korean font size is English size +1-2pt
- [ ] No italic formatting on Korean text
- [ ] Page numbers present
- [ ] Consistent heading hierarchy
- [ ] Git committed with descriptive message
