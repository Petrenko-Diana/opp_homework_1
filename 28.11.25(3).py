filename = input()

try:
    with open(filename, encoding="utf-8") as f:
        s = f.read()
        print(s)

except FileNotFoundError:
    print(f"File {filename} not found")
except PermissionError:
    print(f"Permission to the file {filename} blocked")
except Exception as e:
    print("Виникгуло незрозуміле виключення:", e)