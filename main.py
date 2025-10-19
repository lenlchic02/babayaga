import subprocess

subprocess.run(["pyuic6", "design.ui", "-o", "design.py"])