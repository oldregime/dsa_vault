# DSA Git Shortcuts
# Add these to your ~/.bashrc or ~/.zshrc file

# Quick navigation to DSA vault
alias dsa='cd ~/Documents/LearnignDSA/dsa-knowledge-vault'

# Git shortcuts for DSA learning
alias dsa-backup='~/Documents/LearnignDSA/dsa-knowledge-vault/daily-backup.sh'
alias dsa-status='cd ~/Documents/LearnignDSA/dsa-knowledge-vault && git status'
alias dsa-log='cd ~/Documents/LearnignDSA/dsa-knowledge-vault && git log --oneline -10'
alias dsa-pull='cd ~/Documents/LearnignDSA/dsa-knowledge-vault && git pull'
alias dsa-diff='cd ~/Documents/LearnignDSA/dsa-knowledge-vault && git diff'

# Quick daily commands
alias dsa-today='cd ~/Documents/LearnignDSA/dsa-knowledge-vault && code 01-daily-notes/2025/$(date +%m-%B)/$(date +%Y-%m-%d).md'
alias dsa-quick='cd ~/Documents/LearnignDSA/dsa-knowledge-vault && git add . && git commit -m "Quick save: $(date +%Y-%m-%d)" && git push'

# Learning analytics
alias dsa-streak='cd ~/Documents/LearnignDSA/dsa-knowledge-vault && git log --since="30 days ago" --pretty=format:"%ad" --date=short | sort | uniq | wc -l'
alias dsa-week='cd ~/Documents/LearnignDSA/dsa-knowledge-vault && git log --since="1 week ago" --oneline'

# To add these aliases:
# 1. Open your shell config file:
#    nano ~/.bashrc    (for bash)
#    or
#    nano ~/.zshrc     (for zsh)
# 
# 2. Add the aliases above to the file
# 
# 3. Reload your shell:
#    source ~/.bashrc
#    or
#    source ~/.zshrc
#
# Then you can use commands like:
# dsa              # Go to DSA vault
# dsa-backup       # Daily backup
# dsa-status       # Check what changed
# dsa-today        # Open today's note
# dsa-quick        # Quick save and push
