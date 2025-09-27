"""
Script to generate a clean architecture folder structure for an Angular (frontend), NestJS (backend), and Python ETL module.
Author: IngAamira
"""

import os

# === BASE CONFIGURATION ===
BASE_PATH = os.getcwd()

FOLDERS = {
    "backend": [
        "src",
        "src/config",
        "src/constants",
        "src/decorators",
        "src/guards",
        "src/modules",
        "src/modules/domain",
        "src/modules/domain/entities",
        "src/modules/domain/services",
        "src/modules/domain/use-cases",
        "src/modules/infrastructure",
        "src/modules/infrastructure/models",
        "src/modules/infrastructure/services",
        "src/modules/infrastructure/validations",
        "src/modules/presentation",
        "src/pipes",
        "src/repositories",
        "test",
        "test/acceptanceTests"
    ],
    "frontend": [
        "src/app",
        "src/app/core",
        "src/app/core/guards",
        "src/app/core/interceptors",
        "src/app/core/services",
        "src/app/core/state",
        "src/app/core/utils",

        "src/app/domain",
        "src/app/domain/models",
        "src/app/domain/repositories",
        "src/app/domain/use-cases",

        "src/app/infrastructure",
        "src/app/infrastructure/http",

        "src/app/presentation",
        "src/app/presentation/interfaces",
        "src/app/presentation/layout",
        "src/app/presentation/modules",
        "src/app/presentation/modules/dashboard",
        "src/app/presentation/modules/dashboard/components",
        "src/app/presentation/modules/dashboard/pages",
        "src/app/presentation/shared",
        "src/app/presentation/shared/sidebar",
        "src/app/presentation/shared/header",
        "src/app/presentation/shared/footer",

        "src/assets",
        "src/environments",
        "test",
        "test/acceptanceTests"
    ],
    "etl": [
        "scripts",
        "data",
        "logs"
    ],
}

FILES = {
    "backend": [
        ".env",
        "README.md",
        "src/config/local-config.ts",
    ],
    "frontend": [
        "src/environments/environment.ts",
        "src/environments/environment.prod.ts",
        "README.md",
    ],
    "etl": [
        "etl_upsert.py",
        "requirements.txt",
        "README.md"
    ]
}


def create_structure(base_path, folders_dict, files_dict):
    """Creates folders and empty files based on the given dictionaries."""
    for root_folder, subfolders in folders_dict.items():
        root_path = os.path.join(base_path, root_folder)
        print(f"\n📁 Creating structure in: {root_path}")
        os.makedirs(root_path, exist_ok=True)

        # Create subfolders
        for folder in subfolders:
            path = os.path.join(root_path, folder)
            os.makedirs(path, exist_ok=True)
            print(f"  ✅ Folder created: {path}")

        # Create empty files
        for file_name in files_dict.get(root_folder, []):
            file_path = os.path.join(root_path, file_name)
            if not os.path.exists(file_path):
                with open(file_path, "w", encoding="utf-8") as f:
                    # Basic starter content
                    if file_name == "README.md":
                        f.write(f"# {root_folder.capitalize()}\n\nBase structure generated automatically.\n")
                    elif file_name.endswith(".ts"):
                        f.write("// Auto-generated starter file\n")
                    elif file_name.endswith(".py"):
                        f.write("# Auto-generated ETL script\n")
                    elif file_name == ".env":
                        f.write("# Environment variables\n")
                print(f"  📄 File created: {file_path}")


if __name__ == "__main__":
    print("🚀 Generating clean architecture structure for Backend, Frontend, and ETL...")
    create_structure(BASE_PATH, FOLDERS, FILES)
    print("\n✅ Project structure successfully created.\n")
