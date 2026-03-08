
import os
import shutil

# Files and directories to ignore during the copy process
IGNORE_PATTERNS = {
    '__pycache__',
    'node_modules',
    'venv',
    '.git',
    '.idea',
    '.vscode',
    'dist',
    'build',
    'coverage',
    '*.pyc',
    '*.pyo',
    '*.pyd',
    '.DS_Store',
    'Thumbs.db',
    'credit_ai.db', # Binary DB usually excluded
    '.env',         # Secrets excluded
    'temp',
    'tmp'
}

def copy_files(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    
    shutil.copytree(src, dest, ignore=shutil.ignore_patterns(*IGNORE_PATTERNS))
    print(f"Copied files from {src} to {dest}")

if __name__ == "__main__":
    current_dir = os.getcwd()
    output_dir = os.path.join(current_dir, "GitHub_Upload_Ready")
    
    print(f"Preparing GitHub upload package in: {output_dir}")
    
    try:
        copy_files(current_dir, output_dir)
        
        # Remove the script itself from the package if it was copied
        script_in_package = os.path.join(output_dir, "prepare_github_package.py")
        if os.path.exists(script_in_package):
            os.remove(script_in_package)
            
        # Also remove the output dir from inside itself (copytree prevents this but good to check)
        nested_output = os.path.join(output_dir, "GitHub_Upload_Ready")
        if os.path.exists(nested_output):
            shutil.rmtree(nested_output)
            
        print("\nSuccess! The 'GitHub_Upload_Ready' folder contains clean source code.")
        print("You can drag and drop the contents of this folder to GitHub.")
        
    except Exception as e:
        print(f"Error: {e}")
