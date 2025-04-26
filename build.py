import subprocess
import os
import shutil

# Config
script_name = "appCnl.py"
spec_folder = "specs"
dist_folder = "dist"
build_folder = "build"

# Read version number
with open("version.txt", "r") as f:
    version = f.read().strip()

# Output EXE name with version
output_name = f"cnl_{version}.exe"

# Make sure spec folder exists
os.makedirs(spec_folder, exist_ok=True)

command = [
    "pyinstaller",
    "--noconsole",
    "--onefile",
    "--add-data", f"{os.path.abspath('icon.png')};.",  # <--- ADD THIS
    f"--name={output_name}",
    f"--distpath={dist_folder}",
    f"--specpath={spec_folder}",
    f"--icon={os.path.abspath('icon.ico')}",
    script_name
]

# Optional Windows metadata via version info file
version_file_content = f"""
# UTF-8
VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=({','.join(version.lstrip('v').split('.'))},0),
    prodvers=({','.join(version.lstrip('v').split('.'))},0),
    mask=0x3f,
    flags=0x0,
    OS=0x40004,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
    ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        '040904B0',
        [
        StringStruct('CompanyName', 'imkenough'),
        StringStruct('FileDescription', 'CNL'),
        StringStruct('FileVersion', '{version}'),
        StringStruct('InternalName', 'ChatGPT_Ninja'),
        StringStruct('OriginalFilename', '{output_name}'),
        StringStruct('ProductName', 'chatgpt launcher - imkenough'),
        StringStruct('ProductVersion', '{version}')
        ])
      ]),
    VarFileInfo([VarStruct('Translation', [1033, 1200])])
  ]
)
"""

# Save version info file
version_file = os.path.abspath(os.path.join("version_info.txt"))
with open(version_file, "w", encoding="utf-8") as f:
    f.write(version_file_content)

# Append --version-file argument
command.append(f"--version-file={version_file}")

# Run PyInstaller build
subprocess.run(command, check=True)

# Clean up version info file after build
os.remove(version_file)

print(f"\n✅ Build complete: {dist_folder}/{output_name}")
