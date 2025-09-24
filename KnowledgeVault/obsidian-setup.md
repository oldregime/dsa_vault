# 🔧 Obsidian Setup Guide

## 📥 Installation & Initial Setup

### 1. Download Obsidian
1. Visit [obsidian.md](https://obsidian.md)
2. Download for your platform (Windows/Mac/Linux)
3. Install and create new vault
4. Point vault to `dsa-knowledge-vault` folder

### 2. Essential Settings
```json
{
  "dailyNotes": {
    "folder": "01-daily-notes/2025/09-September",
    "template": "04-resources/templates/daily-template.md",
    "format": "YYYY-MM-DD"
  },
  "newFileLocation": "00-inbox",
  "attachmentFolderPath": "04-resources/images",
  "useMarkdownLinks": true,
  "showLineNumber": true
}
```

## 🔌 Required Plugins

### Core Plugins (Enable)
- [ ] **Daily notes** - For structured daily practice
- [ ] **Templates** - For consistent note format
- [ ] **Graph view** - For visualizing connections
- [ ] **Search** - For finding notes quickly
- [ ] **Tag pane** - For organizing by tags
- [ ] done

### Community Plugins (Install)
1. **Calendar** - Visual daily notes navigation
2. **Templater** - Advanced template functionality
3. **Dataview** - Query and display data from notes
4. **Tag Wrangler** - Better tag management
5. **Obsidian Git** - Git integration for backup
6. **Advanced Tables** - Better table editing
7. **Mind Map** - Visual concept mapping
8. **Obsidian to Anki** - Flashcard export

## 🎨 Theme & Appearance

### Recommended Themes:
- **Minimal** - Clean, distraction-free
- **Blue Topaz** - Professional look
- **Things** - Simple and elegant

### Appearance Settings:
- **Font**: Roboto or Inter
- **Font Size**: 16px for readability
- **Line Width**: 45-50 characters
- **Dark/Light**: Based on preference

## 🏷️ Tag System Setup

### Hierarchical Tags:
```
#concept/
  ├── arrays
  ├── sorting
  ├── searching
  └── hashing

#problem/
  ├── leetcode
  ├── gfg
  └── contests

#difficulty/
  ├── easy
  ├── medium
  └── hard

#status/
  ├── learning
  ├── reviewing
  └── mastered

#language/
  ├── java
  └── python
```

## 📊 Dataview Queries

### Daily Problems Dashboard
```dataview
TABLE 
  platform,
  difficulty,
  status
FROM #problem 
WHERE contains(file.name, "2025-09")
SORT date DESC
```

### Concept Mastery Progress
```dataview
TABLE 
  tags,
  file.ctime as "Created",
  file.mtime as "Last Modified"
FROM #concept 
SORT file.mtime DESC
```

## 🎴 Anki Integration

### Setup Steps:
1. Install Anki desktop application
2. Install "Obsidian to Anki" plugin in Obsidian
3. Configure plugin settings:
   - **Anki Port**: 8765
   - **Deck Name**: DSA Master
   - **Note Type**: Basic

### Anki Card Format in Obsidian:
```markdown
## 🎴 Anki Cards

Q: What is the time complexity of binary search?
A: O(log n) because we eliminate half the search space in each step.

Q: When should you use a HashMap?
A: When you need O(1) average-case lookup, insertion, and deletion operations.
```

## 🔄 Daily Workflow Setup

### Morning Routine Template:
1. Open today's daily note (Ctrl+Shift+D)
2. Review yesterday's problems (click links)
3. Set today's learning goals
4. Do Anki reviews (external app)

### Evening Routine Template:
1. Complete today's reflection section
2. Create Anki cards for new concepts
3. Update problem tracker
4. Commit changes to Git

## 📱 Mobile Setup

### Obsidian Mobile:
1. Install Obsidian mobile app
2. Set up sync with desktop vault
3. Configure for quick note capture
4. Use for reviewing notes on-the-go

### Quick Capture Setup:
- **Templates**: Simple problem template
- **Location**: 00-inbox folder
- **Format**: Brief notes for later processing

## 🔧 Hotkeys Configuration

### Essential Shortcuts:
- **Ctrl+N**: New note
- **Ctrl+Shift+D**: Today's daily note
- **Ctrl+E**: Edit/Preview mode toggle
- **Ctrl+Shift+F**: Global search
- **Ctrl+G**: Open graph view
- **Ctrl+P**: Command palette

### Custom Shortcuts:
- **Alt+T**: Insert template
- **Alt+L**: Insert link
- **Alt+D**: Insert date
- **Alt+C**: Create concept note

## 🔍 Search & Discovery

### Search Operators:
- `tag:#concept` - Find all concept notes
- `path:"02-concepts"` - Notes in concepts folder
- `"binary search"` - Exact phrase search
- `line:(TODO)` - Find TODO items

### Graph View Settings:
- **Filters**: Show only linked notes
- **Groups**: Color by folder or tag
- **Forces**: Adjust for clarity

## 💾 Backup Strategy

### Local Backup:
- **Git**: Version control integration
- **Manual**: Weekly folder backup
- **Export**: Periodic markdown export

### Cloud Backup:
- **Google Drive**: Sync vault folder
- **Obsidian Sync**: Official sync service
- **Dropbox**: Alternative cloud storage

---
*Follow this guide to set up your optimal learning environment*
