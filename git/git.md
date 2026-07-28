| Command                        | Meaning                                                                                                  | Example                            |
| ------------------------------ | -------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| `git status`                   | Shows the current state of your repository (modified, staged, untracked files).                          | `git status`                       |
| `git add .`                    | Stages all changes for the next commit.                                                                  | `git add .`                        |
| `git commit -m "message"`      | Commits the staged changes with a message.                                                               | `git commit -m "Added login page"` |
| `git commit -am "message"`     | Automatically stages **modified/deleted tracked files** and commits them. It **does not** add new files. | `git commit -am "Updated navbar"`  |
| `git push`                     | Uploads your local commits to the remote repository (GitHub).                                            | `git push origin main`             |
| `git pull`                     | Downloads the latest changes from the remote repository and merges them into your local branch.          | `git pull origin main`             |
| `git log`                      | Shows the commit history.                                                                                | `git log`                          |
| `git log --oneline`            | Shows a short commit history (recommended).                                                              | `git log --oneline`                |
| `git reset --hard <commit-id>` | Moves your repository back to a specific commit and **discards all changes after that commit**.          | `git reset --hard a1b2c3d`         |
