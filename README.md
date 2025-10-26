# Keyboard Chatter Detection Tool

A Python application that monitors keystrokes and detects key chatter (keys pressed more than 40 times).

## Features

- Monitors all keyboard input globally
- Detects alphabet keys, numbers, function keys, and special keys (Tab, Enter, Space, etc.)
- Tracks key press count for each key
- Automatically flags keys pressed more than 40 times as "chatter"
- Clean terminal interface with detailed statistics

## Installation

1. Install Python 3.6 or higher
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```bash
python check_key_chatter.py
```

The application will start monitoring your keystrokes. Continue using your computer normally.

To stop monitoring and view results:
- Press `Ctrl+C` in the terminal where the application is running

## Output

The application will display:
- Total unique keys pressed
- Total keystrokes
- A detailed list showing each key and its press count
- A warning for any keys pressed more than 40 times (key chatter)

## Example Output

```
==============================================================================
KEYBOARD MONITORING RESULTS
==============================================================================

Total unique keys pressed: 15
Total keystrokes: 67

----------------------------------------------------------------------
Key                      Count      Status
----------------------------------------------------------------------
a                         45          ⚠ CHATTER DETECTED
space                     12          
enter                     10          
----------------------------------------------------------------------

⚠ WARNING: Key chatter detected! This indicates a potential hardware issue.
==============================================================================
```

## Notes

- The application runs in the background and continues monitoring even when in other windows
- On Windows, you may need to run the application as Administrator for full keyboard access
- The application only counts key presses, not holds

