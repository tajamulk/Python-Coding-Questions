# Deleting files on condition based

for file in os.listdir(): # First have a dry run 
    if file.endswith('.txt'):
        print(file)

for file in os.listdir(): # Then delete files
    if file.endswith('.txt'):
        os.unlink(file)

# Removing file from folder and sub folder
for folder, subfolder, file in os.walk(r'c:\Users\u487062\Downloads'):
    for f in file:
        if f.endswith('.py'):
            os.unlink(f)
