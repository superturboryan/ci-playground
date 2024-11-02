import subprocess
import emoji

# Get all commit messages
commits = subprocess.check_output(['git', 'log', '--pretty=format:%s']).decode().strip().split('\n')

all_commits_valid = True

# Check each commit message for emojis
for commit_message in commits:
    if not any(char for char in commit_message if emoji.is_emoji(char)):
        print(f'❌ Commit message "{commit_message}" does not contain an emoji.')
        all_commits_valid = False

# Exit with an error code if any commit message is invalid
if not all_commits_valid:
    exit(1)
else:
    print(f"🥳 All commits contain emojis")