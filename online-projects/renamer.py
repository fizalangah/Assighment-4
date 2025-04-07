import os

def bulk_rename(folder_path, prefix="", suffix=""):
  
    # List all items in the folder
    for filename in os.listdir(folder_path):
        # Construct full file path
        old_path = os.path.join(folder_path, filename)
        # Check if it is a file (skip directories)
        if os.path.isfile(old_path):
            # Split filename into name and extension
            name, ext = os.path.splitext(filename)
            # Create new filename based on the provided prefix and suffix
            new_filename = f"{prefix}{suffix}"
            new_path = os.path.join(folder_path, new_filename)
            
            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed '{filename}' to '{new_filename}'")
    print("Bulk renaming completed.")

if __name__ == "__main__":
    # Get folder path and rename conditions from the user
    folder = input("Enter the folder path: ").strip()
    prefix = input("Enter the prefix to add (leave empty for none): ").strip()
    suffix = input("Enter the suffix to add (leave empty for none): ").strip()
    
    # Check if the provided folder path exists
    if os.path.exists(folder) and os.path.isdir(folder):
        bulk_rename(folder, prefix, suffix)
    else:
        print("The provided folder path is invalid. Please check and try again.")

