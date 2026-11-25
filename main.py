"""
Owner: 1 (Integration lead). Entry point: `python main.py`.

What to implement:
- Import methods.METHODS and gui.run_app, then call run_app(METHODS).
- Keep this file tiny. Merge everyone's work, review pull requests, and make sure the whole app runs before the deadline.

Also yours: repo structure, README, and checking that every file follows the rule: grayscale uint8 in, grayscale uint8 out.
"""

from methods import METHODS
from gui import run_app


def main():
    run_app(METHODS)


if __name__ == "__main__":
    main()
