# Mia (Miu Remix)
> Ignore this project if you don't know what it is

## How to use

- Download project
- Change path in `zip_proj.bat` to the path for `main.py` in your context
- Press `Win + R`, type `regedit` and press **Enter**
- Navigate to `HKEY_CLASSES_ROOT\Directory\shell`
- Right-click the shell key, select **New**, and create a new key (folder). Name it something like "Zip Folder" (this will be the name that appears in the context menu).
- Right-click the new key you created (e.g., "Zip Folder"), and create a new key inside it named "command."
- In the right pane, double-click on the (Default) value and set its data to the path to your batch file (e.g., `"C:\path\to\zip_context_menu.bat" "%1"`). Make sure to include the "%1" to pass the selected folder's path to your batch file.
- Close the Registry Editor.
- You should now have the option in the context menu with the name you gave it

![img.png](img.png)

## Where is the ZIP file?
The zip file should automatically pop up once it is created, if it doesn't it should be under the project directory.