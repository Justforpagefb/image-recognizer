#!/usr/bin/env python3

import sys
from os.path import dirname
from appevents.GUI_loop import GUI_loop

sys.path.insert(0, dirname(
    dirname(__file__)))  # Ensure main module can be found by Python.


def main() -> None:
    """GUI entry point.

    ---

    :return: start GUI program.
    :rtype: None
    """

    # logger.info("Starting Image Processing App-...\n")

    return GUI_loop()


if __name__ == '__main__':
    main()
