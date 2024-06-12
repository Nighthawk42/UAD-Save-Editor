import json
import tkinter as tk
from tkinter import filedialog
import shutil

def beautify_ua_dreadnoughts_save():
    try:
        # Open a file dialog to select the JSON save file
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")], title="Select Ultimate Admiral: Dreadnoughts Save File")
        
        if not file_path:
            print("No file selected")
            return
        
        # Create a backup of the original file
        backup_path = file_path + '.bak'
        shutil.copy(file_path, backup_path)
        print(f"Backup created at: {backup_path}")
        
        # Read the JSON save file
        with open(file_path, 'r') as file:
            parsed_json = json.load(file)
        
        # Convert the parsed JSON back to a string with indentation
        beautified_json = json.dumps(parsed_json, indent=4)
        
        # Write the beautified JSON back to the original file
        with open(file_path, 'w') as file:
            file.write(beautified_json)
        
        print(f"Beautified save file saved to: {file_path}")
        
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Error: {e}")

# Call the function to run the beautification process
beautify_ua_dreadnoughts_save()