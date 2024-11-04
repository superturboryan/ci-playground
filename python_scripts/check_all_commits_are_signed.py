import subprocess
import sys

def check_signed_commits():
    # Get the list of commit hashes
    try:
        commits = subprocess.check_output(
            ["git", "rev-list", "--all"], text=True
        ).strip().splitlines()
    except subprocess.CalledProcessError as e:
        print(f"Error while fetching commits: {e}", file=sys.stderr)
        sys.exit(1)

    # Check the signature of each commit
    for commit in commits:
        try:
            # Use git verify-commit to check the signature
            output = subprocess.check_output(
                ["git", "verify-commit", commit], text=True
            )
            print(f"Commit {commit} is signed and verified.")
        except subprocess.CalledProcessError:
            print(f"Commit {commit} is not signed or verification failed.")
            sys.exit(1)

    print("All commits are signed.")
    sys.exit(0)

if __name__ == "__main__":
    check_signed_commits()