import subprocess
import os


working_directory = os.getcwd()
os.chdir("./public")
subprocess.run(["git", "fetch"])

print("Changed Python files: ")
result = subprocess.run(["git", "diff", "--name-only", "master..remotes/origin/master", "--", "***.py"], stdout=subprocess.PIPE)
diff = result.stdout.decode("utf-8")
changed_files = diff.split("\n")

for changed_file in changed_files:
  path_pieces = changed_file.split("/")
  print(path_pieces[-1])
  os.replace(f"{working_directory}/public/{changed_file}", f"{working_directory}/ready-files/{path_pieces[-1]}")

# subprocess.run(["git", "pull", "origin", "master"])
os.chdir(working_directory)
