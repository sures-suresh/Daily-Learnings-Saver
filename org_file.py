from pathlib import Path
import shutil

def organize_folder(target_folder):
    folder = Path(target_folder)
    if not folder.exists():
        print("Folder not found!")
        return

    folders = {                #is uesd to ,extenison in this it match right sub folder.
        '.jpg': 'images',
        '.jpeg': 'images',
        '.png': 'images',
        '.pdf': 'pdfs',
        '.mp4': 'videos',
        '.exe': 'installers',
        '.py' : 'python',
    }

    for file in folder.iterdir():          #it loop in the insied the folder
        if file.is_file():                 #check file exit and url
            ext = file.suffix.lower()
            dest_folder = folders.get(ext, 'others') #using get match with right sub floder ,ex have python
            dest_path = folder / dest_folder  #"C:\Users\USER\Music\Desktop\unstr\python"
            dest_path.mkdir(exist_ok=True)
            print(f"Moving {file.name} → {dest_folder}/")
            shutil.move(str(file), str(dest_path / file.name)) #"C:\Users\USER\Music\Desktop\unstr\images\example.py"

    print("\n✅ Done organizing!")

if __name__ == "__main__":
    path = r"C:\Users\USER\Music\Desktop\unstr"  # fixed correct folder
    organize_folder(path)
