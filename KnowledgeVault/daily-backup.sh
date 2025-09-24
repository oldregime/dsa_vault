#!/bin/bash
# Daily DSA Backup Script
# Usage: ./daily-backup.sh [optional message]

cd /home/theoldregime/Documents/LearnignDSA/dsa-knowledge-vault

# Check if anything to commit
if [[ -z $(git status -s) ]]; then
    echo "📝 No changes to backup today"
    exit 0
fi

# Show what's being backed up
echo "📊 Backing up today's changes:"
git status --short

# Add all changes
git add .

# Use custom message or default
if [ -n "$1" ]; then
    commit_msg="Daily DSA: $(date +%Y-%m-%d) - $1"
else
    commit_msg="Daily DSA: $(date +%Y-%m-%d)"
fi

# Commit and push
git commit -m "$commit_msg"
git push

echo "✅ Daily backup complete!"

# Show learning streak
commits_today=$(git rev-list --count --since="$(date +%Y-%m-%d) 00:00:00" HEAD)
echo "📈 Total commits today: $commits_today"

# Show recent activity
echo "📚 Recent activity:"
git log --oneline -5
