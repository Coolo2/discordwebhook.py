

class MutuallyExclusiveError(Exception):
    message = "Allowed Mentions are mutually exclusive"

class FileTooLarge(Exception):
    pass