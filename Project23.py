import os

# Get the list of files in the current working directory
emmafiles = os.listdir()

# Create a list of dictionaries, where each dictionary represents a file
emmalist = []
for file in emmafiles:
    emmadictionaries = {}
    emmadictionaries['filename'] = file
    emmadictionaries['size'] = os.path.getsize(file)
    emmadictionaries['created_at'] = os.path.getctime(file)
    emmalist.append(emmadictionaries)

# Print the list of file dictionaries
print(emmalist)
