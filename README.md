# Branching & Feature Development

## Objective
Work with branches and manage feature development separately without affecting the main codebase.

---

# Tasks Performed

## 1. Create a New Branch

Created a new feature branch:

```bash
git branch feature_update
```

---

## 2. Switch to the New Branch

Moved from the main branch to the feature branch:

```bash
git switch feature_update
```

---

## 3. Modify `app.py` with New Feature Logic

Updated the Python application by adding new feature logic in `app.py`.

Example:

```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1
```

---

## 4. Stage and Commit the Changes

Added modified files to staging area:

```bash
git add .
```

Committed the changes:

```bash
git commit -m "Added binary search feature"
```

---

## 5. Switch Back to Main Branch

Returned to the main branch:

```bash
git switch master
```

---

## 6. Merge Feature Branch into Main

Merged the feature branch into the main branch:

```bash
git merge feature_update
```

---

## 7. Verify Changes Are Merged

Checked commit history:

```bash
git log --oneline
```

Verified updated code exists in the project files.

---

## 8. Delete the Branch Safely

Deleted the merged feature branch safely:

```bash
git branch -d feature_update
```

---

# Result

Successfully created a feature branch, developed new functionality separately, merged it into the main branch, verified the changes, and safely deleted the branch.

# History of Commands used for above tasks

<img width="1333" height="673" alt="image" src="https://github.com/user-attachments/assets/54f3b47f-b254-4f34-9271-28128052b1d3" />
