import subprocess
import os
import fnmatch


# Compare ready-files with public git Python files to get the earliest modified file (first in queue)
def find_first_in_queue(public_files, ready_files):
  public_files.sort(key=os.path.getmtime, reverse=True)
  for public_file in public_files:
    public_filename = public_file.split("/")[-1]
    ready_file = find_ready_file(public_filename, ready_files)
    if ready_file:
      return ready_file
  return False


def find_ready_file(public_filename, ready_files):
  for ready_file in ready_files:
      if ready_file == public_filename:
        return ready_file
  return False


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
if not changed_files:
  print("No changed Python files...")
else:
  print("Changed Python files: ")
  for changed_file in changed_files:
    last_path_piece = changed_file.split("/")[-1]
    source = f"{working_directory}/public/{changed_file}"
    destination = f"{working_directory}/ready-files/{last_path_piece}"
    if not os.path.isfile(source):
      continue
    if os.path.exists(destination):
        os.remove(destination)
    os.replace(source, destination)
    print(changed_file)
  
# Get all the public Python files
root = f"{working_directory}/public/"
public_files = []
for path, subdirs, files in os.walk(root):
    for file in files:
        if fnmatch.fnmatch(file, "*.py"):
            public_files.append(os.path.join(path, file))

# Get all the ready-files
root = f"{working_directory}/ready-files/"
ready_files = []
for file in os.listdir(root):
    if fnmatch.fnmatch(file, "*.py"):
        # TODO: Consider using os.path.join
        ready_files.append(file)

# Print file with earliest modification date (if the file is found)
file_to_execute = find_first_in_queue(public_files, ready_files)
if file_to_execute:
  print("Ready-file to be executed: ")
  print(file_to_execute)
  # Move file to execute to root and rename it to exe.py
  os.replace(file_to_execute, f"{working_directory}/exe.py")

# Change current path to default directory
os.chdir(working_directory)
