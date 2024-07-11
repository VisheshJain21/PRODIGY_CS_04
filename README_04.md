## PRODIDGY_CS-04


## Keylogger

This Python script implements a simple keylogger using the keyboard library. It logs all keystrokes to a file named keylog.txt. The script starts logging when executed and stops when the 'Esc' key is pressed.

## Requirements
 - Python 3.x
 - Keyboard Library
## Installation


1. Install Python 3.x from python.org.

2. Install the keyboard library by running

```bash
pip install keyboard

```
3. Install dependencies :

```bash
pip install -r requirements.txt

```

4. Run the project :


```bash
python main.py

```

## Usage

1. Save the script to a file, for example, keylogger.py.

2. Run the script

```bash
python keylogger.py

```
3. The keylogger will start and create/clear the keylog.txt file

4. Press the 'Esc' key to stop the keylogger.


## Script Explanation

## keylogger()

This is the main function that starts the keylogger. It does the following :

- Clears the previous log file (keylog.txt).

- Prints a message indicating that the keylogger has started.

- Starts recording keystrokes by calling keyboard.on_release with a callback to the write_to_log function.

- Waits for the 'Esc' key to stop the keylogger.

- Prints a message indicating that the keylogger has stopped.

## write_to_log(event, log_file)

This function writes the captured keystrokes to the log file. It handles both normal alphanumeric keys and special keys (e.g., space, enter).

## Notes

Use this keylogger responsibly and only on systems you own or have permission to monitor. Unauthorized use of keyloggers is illegal and unethical.

## Contact
If you have any questions or suggestions, feel free to contact me at visheshjain353@gmail.com