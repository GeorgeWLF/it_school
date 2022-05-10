#Log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL

def log(msg, level):
    print("[", level, "]", msg )

log("Start script", "INFO")

# debug("Mesaj") -> [DEBUG] Mesaj
# info("Mesaj") -> [INFO] Mesaj
# warining("Mesaj") -> [WARNING] Mesaj
# error("Mesaj") -> [ERROR] Mesaj
# critical("Mesaj") -> [CRITICAL] Mesaj

def debug(msg):
    log(msg, "DEBUG")

debug("A debug message")

def info(msg):
    log(msg, "INFO")

info("An info message")

def warning(msg):
    log(msg, "WARNING")

warning("Something is not right.")

def error(msg):
    log(msg, "ERROR")

error("A Major error has happened.")

def critical(msg):
    log(msg, "CRITICAL")

critical("Fatal error. Cannot continue")

