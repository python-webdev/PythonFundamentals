# ============================================================
#  PYTHON ERROR HANDLING
# ============================================================


# ────────────────────────────────────────────────────────────
# 1. try / except / else / finally
# ────────────────────────────────────────────────────────────
#
#  try     – code that might raise an exception
#  except  – runs when a specific exception is caught
#  else    – runs only when NO exception was raised in try
#  finally – ALWAYS runs, whether an exception occurred or not
#
# Full skeleton:
#
#   try:
#       <risky code>
#   except SomeError:
#       <handle it>
#   else:
#       <success path>
#   finally:
#       <cleanup, always executed>


# --- Basic except ---

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")


# --- Catching the exception object with 'as' ---

try:
    int("abc")
except ValueError as e:
    print(f"ValueError caught: {e}")


# --- Multiple except clauses ---
# Python tests them top-to-bottom; the first match wins.

def parse_index(data, index):
    try:
        value = data[index]
        return int(value)
    except IndexError:
        print("Index is out of range.")
    except ValueError:
        print("Value cannot be converted to int.")

parse_index(["1", "two", "3"], 1)   # ValueError
parse_index(["1", "2"], 99)         # IndexError


# --- Catching multiple exceptions in one clause ---

try:
    result = int(input("Enter a number: "))   # may raise ValueError
    print(10 / result)                        # may raise ZeroDivisionError
except (ValueError, ZeroDivisionError) as e:
    print(f"Input error: {e}")


# --- Bare 'except Exception' (catch-all) ---
# Use sparingly; it hides unexpected bugs.

try:
    risky_call = {}["missing_key"]
except Exception as e:
    print(f"Unexpected error: {type(e).__name__}: {e}")


# --- else clause ---
# Runs only when the try block completed without raising.

try:
    number = int("42")
except ValueError:
    print("Not a valid integer.")
else:
    print(f"Parsed successfully: {number}")   # runs here


# --- finally clause ---
# Guaranteed to run — ideal for releasing resources.

def read_file(path):
    f = None
    try:
        f = open(path, "r")
        return f.read()
    except FileNotFoundError:
        print(f"File not found: {path}")
    finally:
        if f:
            f.close()   # always closes the file handle
            print("File handle closed.")

read_file("nonexistent.txt")


# --- Context managers (the idiomatic alternative to try/finally) ---
# 'with' handles cleanup automatically; preferred over manual finally.

def read_file_safe(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {path}")

read_file_safe("nonexistent.txt")


# ────────────────────────────────────────────────────────────
# 2. raise
# ────────────────────────────────────────────────────────────
#
#  raise ExceptionType(message)  – raise a new exception
#  raise                         – re-raise the current exception
#
# Use 'raise' to signal that a caller has violated a contract
# or that a situation cannot be handled at this level.


# --- Raising a built-in exception ---

def set_age(age):
    if age < 0:
        raise ValueError(f"Age cannot be negative, got {age}.")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(e)


# --- Re-raising an exception ---
# Catches, logs, then lets it propagate up the call stack.

def process(data):
    try:
        return 100 / data
    except ZeroDivisionError:
        print("Logging: division by zero in process()")
        raise   # re-raises the same ZeroDivisionError

try:
    process(0)
except ZeroDivisionError:
    print("Caller caught the re-raised exception.")


# --- Exception chaining with 'raise ... from' ---
# Attaches the original cause to a new exception, preserving context.

def load_config(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError as e:
        raise RuntimeError(f"Config file missing: {path}") from e

try:
    load_config("config.yaml")
except RuntimeError as e:
    print(e)
    print(f"Caused by: {e.__cause__}")


# ────────────────────────────────────────────────────────────
# 3. Custom Exceptions
# ────────────────────────────────────────────────────────────
#
# Inherit from Exception (or a more specific built-in subclass).
# Custom exceptions let callers catch only the errors they care about
# and carry domain-specific information alongside the message.


# --- Minimal custom exception ---

class AppError(Exception):
    """Base class for all application exceptions."""


class DatabaseError(AppError):
    """Raised when a database operation fails."""


class NetworkError(AppError):
    """Raised when a network operation fails."""


# Callers can catch at any level of the hierarchy:
#   except AppError      → catches both DatabaseError and NetworkError
#   except DatabaseError → catches only database failures

try:
    raise DatabaseError("Connection refused on port 5432.")
except AppError as e:
    print(f"App error: {e}")


# --- Custom exception with extra attributes ---
# Store structured data on the exception object for richer error handling.

class ValidationError(Exception):
    def __init__(self, field, message):
        super().__init__(message)
        self.field = field

    def __str__(self):
        return f"[{self.field}] {super().__str__()}"


def validate_username(username):
    if len(username) < 3:
        raise ValidationError("username", "Must be at least 3 characters.")
    if not username.isalnum():
        raise ValidationError("username", "Only alphanumeric characters allowed.")
    return username

try:
    validate_username("a!")
except ValidationError as e:
    print(e)          # [username] Must be at least 3 characters.
    print(e.field)    # username


# --- Exception hierarchy example ---
#
#  Exception
#  └── AppError
#      ├── DatabaseError
#      │   └── ConnectionError
#      └── ValidationError

class ConnectionError(DatabaseError):
    def __init__(self, host, port):
        super().__init__(f"Cannot connect to {host}:{port}")
        self.host = host
        self.port = port

try:
    raise ConnectionError("localhost", 5432)
except DatabaseError as e:        # catches ConnectionError too
    print(f"DB layer caught: {e}")
except AppError as e:
    print(f"App layer caught: {e}")


# ────────────────────────────────────────────────────────────
# QUICK REFERENCE
# ────────────────────────────────────────────────────────────
#
#  Clause / keyword       When it runs
#  ─────────────────────  ─────────────────────────────────────
#  try                    Always (your guarded code goes here)
#  except SomeError       Only when SomeError (or subclass) raised
#  else                   Only when try completed without exception
#  finally                Always, even after return or re-raise
#
#  raise Error(msg)       Raise a new exception immediately
#  raise                  Re-raise the active exception
#  raise New from orig    Raise New, attaching orig as __cause__
#
#  Best practices
#  • Catch the most specific exception you can handle.
#  • Never silence exceptions with a bare 'except: pass'.
#  • Use 'finally' (or 'with') to guarantee resource cleanup.
#  • Build a shallow exception hierarchy rooted at a custom base.
#  • Add attributes to custom exceptions for structured error data.
