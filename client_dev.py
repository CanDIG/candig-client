"""
Simple shim for running the client program during development.
"""

import dev_glue  # NOQA
import candig.client.cli as cli

if __name__ == "__main__":
    cli.client_main()
