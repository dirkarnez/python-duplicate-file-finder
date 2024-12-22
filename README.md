duplicate-file-finder
=====================
### Using
- [Duplicate-Finder · PyPI](https://pypi.org/project/Duplicate-Finder/)

### TODO
- [ ] ignore some files ([duplicates/duplicates.py#L29](https://github.com/akcarsten/Duplicate-Finder/blob/master/duplicates/duplicates.py#L29))
  - [python - Excluding directories in os.walk - Stack Overflow](https://stackoverflow.com/questions/19859840/excluding-directories-in-os-walk)
    - ```python
      # exclude = set(['New folder', 'Windows', 'Desktop'])
      for root, dirs, files in os.walk(top, topdown=True):
          dirs[:] = [d for d in dirs if d not in exclude]
      ```

### Reference
- [filecmp — File and Directory Comparisons — Python 3.13.1 documentation](https://docs.python.org/3/library/filecmp.html)
- [difflib — Helpers for computing deltas — Python 3.13.1 documentation](https://docs.python.org/3/library/difflib.html)
- [Finding Duplicate Files with Python - GeeksforGeeks](https://www.geeksforgeeks.org/finding-duplicate-files-with-python/)
