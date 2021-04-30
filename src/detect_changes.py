import subprocess
import os

# Fetch public repository into public directory
working_directory = os.getcwd()
os.chdir("./public")
subprocess.run(["git", "fetch"])

# Get all the added or changed .py files in all sub-directories
result = subprocess.run(["git", "diff", "--name-only", "master..remotes/origin/master", "--", "***.py"], stdout=subprocess.PIPE)
diff = result.stdout.decode("utf-8")
changed_files = diff.split("\n")

# Print and move changed Python files to the 'ready-files' volume
# Only uniquely named files will be copied (no duplicates)
print("Changed Python files: ")
for changed_file in changed_files:
  last_path_piece = changed_file.split("/")[-1]
  source = f"{working_directory}/public/{changed_file}"
  destination = f"{working_directory}/ready-files/{last_path_piece}"
  if !os.path.exists(destination):
    os.rename(source, destination)
  print(last_path_piece)

# Pull directory to merge changes
# subprocess.run(["git", "pull", "origin", "master"])

# Change current path to default directory
os.chdir(working_directory)
