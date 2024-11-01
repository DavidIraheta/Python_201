# Add the code for the file counter script that you wrote in the course.
# In the previous module of this course, you wrote a script that was able to move all your screenshots from your 
# messy desktop into a new folder. In this project, you'll revisit your file mover code and expand on it 
# with the knowledge of some additional data types in order to make it more flexible and powerful.
# When you built your file mover, you used the pathlib module that worked with Path() objects. 
# You can consider Path() objects as yet another data type, one that is more custom and not considered a built-in
# type. As you might remember, you'll have to import it from the standard library in order to work with it.
# In this project, you'll continue to work with pathlib and files, 
# but you'll also use some of the additional built-in data types that you got to know in this section.

from pathlib import Path
file_count = {}
desktop = Path.home() / "Desktop"
screenshot_folder = desktop / "Screenshots"
screenshot_folder.mkdir(exist_ok=True)
for file in desktop.iterdir():
    
    if file.is_file():
      
        file_extension = file.suffix.lower()
        if file_extension in file_count:
            file_count[file_extension] += 1
        else:
            file_count[file_extension] = 1
        if "screenshot" in file.stem.lower():
            destination = screenshot_folder / file.name
            file.rename(destination)
        if "screenshot" in file.stem.lower():
            destination = screenshot_folder / file.name
            file.rename(destination)
for ext, count in file_count.items():
    print(f"There are {count} file(s) with the '{ext}' extension on your desktop.")

