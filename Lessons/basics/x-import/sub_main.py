import imported
import main

print(f"sub_main.py {__name__}", imported.x)
imported.x = "modified in sub_main"
