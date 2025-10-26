#!/usr/bin/env python3
"""
Keyboard Chatter Detection Tool
Monitors keystrokes and detects if any key is pressed more than 40 times (key chatter).
Press Ctrl+C to stop monitoring and view results.
"""

import sys
import time
from pynput import keyboard
from collections import defaultdict


EXPECTED_KEYSTROKE_COUNT = 40


class KeyMonitor:
    def __init__(self):
        self.key_counts = defaultdict(int)
        self.listener = None

    def on_press(self, key):
        """Handle key press events"""
        # Convert key to string representation
        try:
            if hasattr(key, "char") and key.char is not None:
                # Regular character key (a-z, 0-9, etc.)
                key_name = key.char
            elif hasattr(key, "name"):
                # Special keys (space, enter, tab, function keys, etc.)
                key_name = key.name
            else:
                # Fallback for other keys
                key_name = str(key)
        except:
            key_name = str(key)

        # Increment count for this key
        self.key_counts[key_name] += 1

    def on_release(self, key):
        """Handle key release events"""
        pass

    def start_monitoring(self):
        """Start listening to keyboard events"""
        print("Keyboard monitoring started. Press Ctrl+C to stop and view results.")
        print("=" * 70)
        print("Listening to keystrokes...")
        print("=" * 70)

        # Create and start listener
        self.listener = keyboard.Listener(
            on_press=self.on_press, on_release=self.on_release, suppress=False
        )
        self.listener.start()

        # Keep the listener running until interrupted
        try:
            # This loop allows Ctrl+C to be caught properly
            while self.listener.is_alive():
                time.sleep(0.1)
        except KeyboardInterrupt:
            print("\n\nStopping monitoring...")
        finally:
            # Stop the listener
            if self.listener is not None and self.listener.is_alive():
                self.listener.stop()
                self.listener.join()

    def print_results(self):
        """Print the monitoring results"""
        print("\n" + "=" * 70)
        print("KEYBOARD MONITORING RESULTS")
        print("=" * 70)

        if not self.key_counts:
            print("\nNo keystrokes detected.")
            return

        # Sort by count (descending)
        sorted_keys = sorted(self.key_counts.items(), key=lambda x: x[1], reverse=True)

        print(f"\nTotal unique keys pressed: {len(self.key_counts)}")
        print(f"Total keystrokes: {sum(self.key_counts.values())}")
        print("\n" + "-" * 70)
        print(f"{'Key':<25} {'Count':<10} {'Status'}")
        print("-" * 70)

        # Track if chatter was detected
        chatter_detected = False

        for key_name, count in sorted_keys:
            status = ""
            if count > EXPECTED_KEYSTROKE_COUNT:
                status = "⚠ CHATTER DETECTED"
                chatter_detected = True

            print(f"{key_name:<25} {count:<10} {status}")

        print("-" * 70)

        if chatter_detected:
            print(
                "\n⚠ WARNING: Key chatter detected! This indicates a potential hardware issue."
            )
        else:
            print(
                "\n✓ No key chatter detected. All keys appear to be functioning normally."
            )

        print("=" * 70)


def main():
    """Main entry point"""
    monitor = KeyMonitor()

    try:
        # Start monitoring
        monitor.start_monitoring()
    except Exception as e:
        print(f"\nError occurred: {e}")
        sys.exit(1)
    finally:
        # Print results when stopped
        monitor.print_results()


if __name__ == "__main__":
    main()
