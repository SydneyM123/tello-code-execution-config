import subprocess
import os
import shutil
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

# Move changed Python files to the 'ready-files' directory (only uniquely named files will be copied, no duplicates)
print("Changed Python files: ")
for changed_file in changed_files:
  last_path_piece = changed_file.split("/")[-1]
  source = f"{working_directory}/public/{changed_file}"
  destination = f"{working_directory}/ready-files/{last_path_piece}"
  if not os.path.isfile(source):
    continue
  if os.path.exists(destination):
      os.remove(destination)
  shutil.copy2(source, destination)
  print(changed_file)
print("----------")

# Get all the ready-files
root = f"{working_directory}/ready-files/"
ready_files = []
for file in os.listdir(root):
    if fnmatch.fnmatch(file, "*.py"):
        ready_files.append(root + file)

if not len(ready_files) == 0:
  ready_files.sort(key=os.path.getmtime, reverse=True)
  
  # Print file with earliest modification date
  print("Ready-file to be executed: ")
  print(ready_files[0].split("/")[-1])
  print("----------")
  
  # Move file to execute to root and rename it to exe.py
  os.replace(ready_files[0], f"{working_directory}/exe.py")

# Change current path to default directory
os.chdir(working_directory)
