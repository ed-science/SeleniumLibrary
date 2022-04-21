import platform


def ctrl_or_command_key():
    return "COMMAND" if platform.system() == "Darwin" else "CONTROL"
