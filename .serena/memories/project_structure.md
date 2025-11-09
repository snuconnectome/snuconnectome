# Project Structure

## Directory Organization

```
Japan/
├── .claude/                    # Claude Code configuration
│   └── commands/
│       └── doc-design.md      # Custom /doc-design command
├── .serena/                   # Serena MCP server data
├── .venv/                     # Python virtual environment for MCP servers
├── claudedocs/                # Claude-generated documentation
│   └── doc-design-usage-guide.md
├── fonts/                     # KoPub World and other fonts
├── media/                     # Images and graphics for documents
├── styles/                    # Document styling assets
├── *.md                       # Proposal documents (Markdown source)
├── *.pdf                      # Final deliverable documents
├── run_gemini.sh             # MCP server launcher + Gemini CLI
└── README.md                  # Project overview
```

## Key Documents (Root Level)

### Primary Documents
- `Hakone_Retreat_Proposal.md` - Final proposal document
- `Hakone_Retreat_Fore_Comparison.md` - Comparative analysis
- `Hakone_Retreat_Fore_Detailed_Budget_Jan2026.md` - Budget breakdown
- `Group_Booking_Guide_Hakone_Jan2026.md` - Booking guide
- `Quick_Reference_Summary.md` - Summary of recommendations

### Alternative Options
- `Park_Hyatt_Busan_Retreat_Option.md` - Busan alternative venue
- `Professors_Workshop_Proposal_Hakone_Busan.md` - Combined proposal

### Support Files
- `proposal_prompt.md` - Template/guide for proposal writing
- `Hakone_Retreat_Fore_vs_Kajikaso_Report.pdf` - Exported comparison

## Asset Directories

### fonts/
Contains professional Korean fonts:
- KoPub World 바탕체 (Batang) - serif for body text
- KoPub World 돋움체 (Dotum) - sans-serif for headings
- Supporting Latin fonts for mixed-language documents

### media/
Images and graphics:
- Hotel photos
- Location maps
- Facility images
- Charts and diagrams

### styles/
CSS and styling assets for PDF export and document formatting

### claudedocs/
Claude Code documentation:
- Usage guides
- Best practices
- Command references

## Hidden Directories

### .claude/
- Custom Claude Code commands
- Project-specific configurations

### .serena/
- Serena MCP server metadata
- Project indexing data

### .venv/
- Python virtual environment
- MCP server dependencies (sequential-thinking-mcp, serena)

## File Type Distribution
- **Source**: Markdown (.md) - editable, version-controlled
- **Deliverable**: PDF - final format for stakeholders
- **Support**: Images (PNG, JPG), fonts (TTF, OTF), scripts (.sh)
