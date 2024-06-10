from pathlib import Path

root_dir = Path('files')

if not root_dir.exists() or not root_dir.is_dir():
  print(
      f"Error: The directory {root_dir} does not exist or is not a directory.")
  exit()

file_paths = root_dir.iterdir()
print(f"Current working directory: {Path.cwd()}")

for path in file_paths:
  if path.is_file():
    new_filename = "new-" + path.stem + path.suffix
    new_filepath = path.with_name(new_filename)
    print(f"Renaming {path} to {new_filepath}")

    path.rename(new_filepath)

print("Renaming complete.")
