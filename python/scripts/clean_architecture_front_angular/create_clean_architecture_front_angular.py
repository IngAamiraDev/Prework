"""
Script: create_clean_architecture.py
Description: Generates a Clean Architecture folder structure for Angular inside src/app
Author: Andrés Mira
"""

import os

# Base path
BASE_PATH = os.path.join("src")

# Folder structure definition
STRUCTURE = {
    "domain": {
        "models": {},
        "repositories": {},
        "use-cases": {}
    },
    "infrastructure": {
        "api": {},
        "repositories": {}
    },
    "presentation": {
        "features": {
            "components": {},
            "facades": {},
            "pages": {},
            "view-models": {}
        },
        "shared": {
            "components": {},
            "services": {},
            "types": {},
            "utils": {},
        }
    }
}


def create_structure(base_path, structure):
    """
    Recursively creates folders and index.ts files.
    """
    for folder, subfolders in structure.items():
        folder_path = os.path.join(base_path, folder)

        # Create folder
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created folder: {folder_path}")

        # Create index.ts inside folder
        index_file_path = os.path.join(folder_path, "index.ts")
        if not os.path.exists(index_file_path):
            with open(index_file_path, "w") as f:
                f.write("// Barrel export file\n")
            print(f"Created file: {index_file_path}")

        # Recursively create subfolders
        create_structure(folder_path, subfolders)


if __name__ == "__main__":
    create_structure(BASE_PATH, STRUCTURE)
    print("\n✅ Clean Architecture structure created successfully.")