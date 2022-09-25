import imported

print(f"main.py {__name__}, x = ", imported.x)
imported.x = "modified in main"
