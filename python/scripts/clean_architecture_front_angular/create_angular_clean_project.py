"""
Script: create_angular_clean_project.py
Description: Creates an Angular project with Clean Architecture structure
Author: Andrés Mira
"""

import os
import sys
import subprocess
import json


# ---------- CONFIGURATION ----------

STRUCTURE = {
    "domain": {
        "models": {},
        "repositories": {},
        "use-cases": {}
    },
    "infrastructure": {
        "datasource": {},
        "repositories": {}
    },
    "presentation": {
        "features": {
            "ingaamira": {
                "components": {},
                "facades": {},
                "pages": {},
                "view-models": {}
            },
        }
    },
    "shared": {
        "components": {},
        "services": {},
        "utils": {}
    }
}

BASE_PATH = os.path.join("src")

COMPONENTS = [
    "navbar",
    "footer",
    "layout",
    "whatsappbutton"
]


# ---------- FUNCTIONS ----------

def run_command(command):
    """Execute shell command"""
    print(f"\nRunning: {' '.join(command)}\n")
    subprocess.run(command, check=True)


def create_structure(base_path, structure):
    """Create Clean Architecture folders recursively"""

    for folder, subfolders in structure.items():

        folder_path = os.path.join(base_path, folder)

        os.makedirs(folder_path, exist_ok=True)
        print(f"Created folder: {folder_path}")

        index_file = os.path.join(folder_path, "index.ts")

        if not os.path.exists(index_file):
            with open(index_file, "w") as f:
                f.write("// Barrel export file\n")

        create_structure(folder_path, subfolders)


def update_tsconfig():
    """Add path aliases to tsconfig.json safely"""

    tsconfig_path = "tsconfig.json"

    with open(tsconfig_path, "r") as f:
        content = f.read()

    if '"paths"' in content:
        print("Paths already configured in tsconfig.json")
        return

    paths_block = """
        "baseUrl": "./",
        "paths": {
            "@domain/*": ["src/domain/*"],
            "@infrastructure/*": ["src/infrastructure/*"],
            "@presentation/*": ["src/presentation/*"]
        },
    """

    content = content.replace(
        '"compilerOptions": {',
        '"compilerOptions": {\n' + paths_block
    )

    with open(tsconfig_path, "w") as f:
        f.write(content)

    print("Updated tsconfig.json paths")


def update_angular_json_assets(project_name):
    """Replace public assets config with src/assets"""

    angular_json_path = "angular.json"

    with open(angular_json_path, "r") as f:
        data = json.load(f)

    assets_path = data["projects"][project_name]["architect"]["build"]["options"]

    # Replace assets configuration
    assets_path["assets"] = [
        "src/favicon.ico",
        "src/assets",
        "src/robots.txt",
        "src/sitemap.xml"   
    ]

    # Write updated file
    with open(angular_json_path, "w") as f:
        json.dump(data, f, indent=2)

    print("angular.json assets updated to src/assets")


def generate_components():
    """Generate shared components in presentation layer"""

    for component in COMPONENTS:

        run_command([
            "ng",
            "g",
            "component",
            component,
            "--path",
            "src/presentation/shared/components",
            "--standalone",
            "--skip-tests"
        ])


# ---------- MAIN SCRIPT ----------

def main():

    if len(sys.argv) < 2:
        print("Usage: python create_angular_clean_project.py <project-name>")
        return

    project_name = sys.argv[1]

    # 1️⃣ Create Angular project
    run_command([
        "ng",
        "new",
        project_name,
        "--standalone",
        "--routing",
        "--style=css",
        "--skip-tests"
    ])

    # 2️⃣ Enter project folder
    os.chdir(project_name)

    # 3️⃣ Create Clean Architecture structure
    create_structure(BASE_PATH, STRUCTURE)

    # 4️⃣ Update tsconfig paths
    update_tsconfig()

    # 5️⃣ Update angular.json assets
    update_angular_json_assets(project_name)

    # 6️⃣ Generate shared components
    generate_components()

    print("\n✅ Angular Clean Architecture project created successfully!")


if __name__ == "__main__":
    main()
