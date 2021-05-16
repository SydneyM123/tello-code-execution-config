import subprocess
import os
import fnmatch

# Fetch public repository into public directory
working_directory = os.getcwd()
os.chdir("./public")
subprocess.run(["git", "fetch"])

# Get all the added or changed .py files in all sub-directories
result = subprocess.run(["git", "diff", "--name-only", "master..remotes/origin/master", "--", "***.py"], stdout=subprocess.PIPE)
diff = result.stdout.decode("utf-8")
changed_files = diff.split("\n")

# Pull directory to merge changes
subprocess.run(["git", "pull", "origin", "master"])

# Print and move changed Python files to the 'ready-files' volume
print("Changed files (.py): ")

# Only uniquely named files will be copied (no duplicates)
for changed_file in changed_files:
  last_path_piece = changed_file.split("/")[-1]
  source = f"{working_directory}/public/{changed_file}"
  destination = f"{working_directory}/ready-files/{last_path_piece}"
  if not os.path.isfile(source):
    break
  if os.path.exists(destination):
      os.remove(destination)
  os.replace(source, destination)
  print(changed_file)

# Get all the ready-files
source = f"{working_directory}/ready-files/"
files = []
for file in os.listdir(source):
    if fnmatch.fnmatch(file, '*.py'):
        files.append(source + file)
files.sort(key=os.path.getmtime, reverse=True)

# Print file with earliest modification date
file_to_execute = files[0].split("/")[-1]
print("Ready-file to be executed: ")
print(file_to_execute)

# Move file to execute to root and rename it to exe.py
os.replace(files[0], working_directory)
  
# Change current path to default directory
os.chdir(working_directory)
