# watch.py  -- simple, clean, full-refresh version
import os
import time
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MAIN = ROOT / "main.py"
POLL_INTERVAL = 0.2  # seconds

def gather_files():
    return [p for p in ROOT.rglob("*.py")]

def snapshot(files):
    snap = {}
    for p in files:
        try:
            snap[str(p)] = p.stat().st_mtime
        except FileNotFoundError:
            snap[str(p)] = 0
    return snap

def run_main():
    """Run main.py freshly and clear screen before."""
    os.system('cls')
    print("Running main.py ...")
    print("---------------------------------------")
    try:
        subprocess.run([sys.executable, str(MAIN)], check=False)
    except Exception as e:
        print("Error running main.py:", e)
    print("---------------------------------------")

def main():
    if not MAIN.exists():
        print("Waiting for main.py ...")
    watched = gather_files()
    last = snapshot(watched)

    try:
        if MAIN.exists():
            run_main()

        while True:
            watched = gather_files()
            current = snapshot(watched)

            changed = False
            for path, mtime in current.items():
                if path not in last or last[path] != mtime:
                    changed = True
                    break
            for path in list(last.keys()):
                if path not in current:
                    changed = True
                    break

            if changed:
                last = current
                if MAIN.exists():
                    run_main()
                else:
                    os.system('cls')
                    print("Waiting for main.py ...")

            time.sleep(POLL_INTERVAL)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
