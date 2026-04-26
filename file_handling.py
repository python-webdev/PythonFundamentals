# =============================================================================
# PYTHON FILE HANDLING
# =============================================================================
# File handling allows programs to persist data beyond runtime by reading
# from and writing to files on disk.

import os


# =============================================================================
# 1. OPENING FILES — open()
# =============================================================================
# Syntax: open(file_path, mode, encoding)
# Returns a file object. Must be closed after use (or use `with`).

f = open("example.txt", "w")   # open for writing (creates file if needed)
f.write("Hello, file!")
f.close()                       # always close manually-opened files

# open() without `with` is risky — if an exception occurs before close(),
# the file handle leaks and data may not be flushed to disk.


# =============================================================================
# 2. FILE MODES
# =============================================================================
#
#  Mode   | Description
#  -------|-----------------------------------------------------------
#  'r'    | Read (default). File must exist. Cursor at start.
#  'w'    | Write. Creates file or TRUNCATES existing content.
#  'a'    | Append. Creates file or adds to end of existing content.
#  'x'    | Exclusive create. Fails if file already exists.
#  'r+'   | Read + write. File must exist. Does NOT truncate.
#  'w+'   | Read + write. Creates or TRUNCATES.
#  'rb'   | Read binary  (images, audio, PDFs, etc.)
#  'wb'   | Write binary
#  'ab'   | Append binary
#
# Text mode ('r', 'w', 'a') handles newline translation and encoding.
# Binary mode ('rb', 'wb') reads/writes raw bytes — no translation.


# =============================================================================
# 3. READING FILES
# =============================================================================

# --- read() — entire file as one string ---
with open("example.txt", "r") as f:
    content = f.read()          # returns str
    print(content)              # Hello, file!

# --- readline() — one line at a time ---
with open("example.txt", "r") as f:
    line = f.readline()         # reads up to and including '\n'
    print(line)

# --- readlines() — all lines as a list ---
with open("example.txt", "r") as f:
    lines = f.readlines()       # ['Hello, file!']
    print(lines)

# --- iterating line by line (memory-efficient for large files) ---
with open("example.txt", "r") as f:
    for line in f:
        print(line.strip())     # strip() removes trailing newline


# =============================================================================
# 4. WRITING FILES
# =============================================================================

# --- 'w' mode: overwrites the entire file ---
with open("log.txt", "w") as f:
    f.write("First line\n")     # write() does NOT add newlines automatically
    f.write("Second line\n")

# --- writelines(): write a list of strings (no newlines added) ---
lines = ["apple\n", "banana\n", "cherry\n"]
with open("fruits.txt", "w") as f:
    f.writelines(lines)

# --- 'a' mode: appends without touching existing content ---
with open("log.txt", "a") as f:
    f.write("New entry appended\n")


# =============================================================================
# 5. BINARY FILES — 'rb' / 'wb'
# =============================================================================
# Use binary mode whenever the file is not plain text:
# images, audio, video, compressed archives, serialized data, etc.

# Write binary data
data = bytes([0x50, 0x4B, 0x03, 0x04])  # ZIP magic bytes
with open("archive.bin", "wb") as f:
    f.write(data)

# Read binary data
with open("archive.bin", "rb") as f:
    raw = f.read()              # returns bytes, not str
    print(raw)                  # b'PK\x03\x04'
    print(type(raw))            # <class 'bytes'>

# Copying a binary file
with open("archive.bin", "rb") as src, open("copy.bin", "wb") as dst:
    dst.write(src.read())       # two context managers on one `with`


# =============================================================================
# 6. THE WITH CONTEXT MANAGER
# =============================================================================
# `with open(...) as f:` is the idiomatic Python way to handle files.
# It guarantees f.close() is called even if an exception is raised inside
# the block — no manual close(), no resource leaks, no lost data.

# How it works under the hood:
#   1. open() returns a file object that implements __enter__ and __exit__
#   2. __enter__ returns the file object (bound to `f`)
#   3. __exit__ calls f.close() — always, even on exception

with open("example.txt", "r", encoding="utf-8") as f:
    content = f.read()
# f is closed here automatically

# Multiple files in one `with` statement (Python 3.1+)
with open("fruits.txt", "r") as src, open("output.txt", "w") as dst:
    for line in src:
        dst.write(line.upper())


# =============================================================================
# 7. ENCODING
# =============================================================================
# Always specify encoding for text files to avoid platform differences.
# UTF-8 is the universal standard for modern text.

with open("unicode.txt", "w", encoding="utf-8") as f:
    f.write("Привет мир\n")     # Cyrillic — works fine with utf-8

with open("unicode.txt", "r", encoding="utf-8") as f:
    print(f.read())


# =============================================================================
# 8. FILE CURSOR — tell() and seek()
# =============================================================================
# The cursor tracks the current read/write position in bytes.

with open("example.txt", "r") as f:
    print(f.read(5))            # reads first 5 chars, cursor moves to 5
    print(f.tell())             # 5 — current cursor position
    f.seek(0)                   # jump back to the beginning
    print(f.read(5))            # reads first 5 chars again


# =============================================================================
# 9. CHECKING FILE STATE
# =============================================================================
path = "example.txt"

print(os.path.exists(path))     # True if file/dir exists
print(os.path.isfile(path))     # True only if it's a file
print(os.path.getsize(path))    # file size in bytes


# =============================================================================
# 10. COMMON PATTERNS SUMMARY
# =============================================================================

# Read entire file
with open("file.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Write new file (or overwrite)
with open("file.txt", "w", encoding="utf-8") as f:
    f.write("content")

# Append to file
with open("file.txt", "a", encoding="utf-8") as f:
    f.write("more content\n")

# Read all lines into a list
with open("file.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Process large file line by line
with open("file.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# Copy binary file
with open("src.bin", "rb") as src, open("dst.bin", "wb") as dst:
    dst.write(src.read())
