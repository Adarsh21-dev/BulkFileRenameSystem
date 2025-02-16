# Regular Expression Patterns

The regular expression `.*txt.*` is a pattern that matches any string that contains the characters "txt" with any number of any characters (including none) before and after it.

## Examples of Regular Expressions Using the `re` Module in Python

### 1. Match Any Digit
```python
pattern = ".*\d.*"
```

### 2. Match One or More Digits
```python
pattern = ".*\d+.*"
```

### 3. Match a Word (Sequence of Word Characters)
```python
pattern = ".*\w+.*"
```

### 4. Match a Specific Word
```python
pattern = ".*hello.*"
```

### 5. Match One or More Occurrences of a Specific Word
```python
pattern = ".*hello+.*"
```

### 6. Match Any Whitespace Character
```python
pattern = ".*\s.*"
```

### 7. Match a Specific Sequence of Characters
```python
pattern = ".*abc123.*"
```

### 8. Match Any Character Except a Newline
```python
pattern = "r'.'"
```

### 9. Match a Specific Character Set (e.g., Match Any Vowel)
```python
pattern = ".*[aeiou].*"
```

### 10. Match Any Character Except Those in a Specific Character Set (e.g., Match Any Consonant)
```python
pattern = ".*[^aeiou].*"
```

### 11. Match the Start of a Line
```python
pattern = ".*^start.*"
```

### 12. Match the End of a Line
```python
pattern = ".*end$.*"
```

### 13. Match a Specific Number of Occurrences (e.g., Match Exactly 3 Digits)
```python
pattern = ".*\d{3}.*"
```

### 14. Match Zero or More Occurrences (e.g., Match Any Number of Digits)
```python
pattern = ".*\d*.*"
```

### 15. Match Zero or One Occurrence (e.g., Match an Optional "e" at the End)
```python
pattern = ".*apple?.*"
```

### 16. Match a Specific Number of Occurrences Within a Range (e.g., Match 2 to 4 Digits)
```python
pattern = ".*\d{2,4}.*"
```

### 17. Match Any Character Except a Specific Character (e.g., Match Any Character Except "a")
```python
pattern = ".*[^a].*"
```

### 18. Match a Specific Word at Word Boundaries (e.g., Match "cat" but Not "catch")
```python
pattern = ".*\bcat\b.*"
```

## More Advanced Examples
For more advanced regular expression patterns, visit:
[W3Schools - Python Regex](https://www.w3schools.com/python/python_regex.asp)
