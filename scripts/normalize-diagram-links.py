"""Project entry point for the local versioned diagram utility."""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).resolve().parents[1] / 'tools/method/tooling/normalize-diagram-links.py'), run_name='__main__')
