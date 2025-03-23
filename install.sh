#!/bin/bash
# Script to install the Python Project Scaffolder for both Bash and Zsh

# Save the directory of this script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "Installing Python Project Scaffolder..."

# Create directories for the tool
mkdir -p "$HOME/.local/bin"
mkdir -p "$HOME/.local/lib/pyscaffold"

# Check if python_scaffold.py exists in the current directory
if [ ! -f "$SCRIPT_DIR/python_scaffold.py" ]; then
    echo "Error: python_scaffold.py not found in $SCRIPT_DIR"
    exit 1
fi

echo "Copying python_scaffold.py to ~/.local/lib/pyscaffold/"
# Copy the python script to the lib directory
cp "$SCRIPT_DIR/python_scaffold.py" "$HOME/.local/lib/pyscaffold/"

# Make it executable
chmod +x "$HOME/.local/lib/pyscaffold/python_scaffold.py"

# Remove existing symlink or directory if it exists
if [ -e "$HOME/.local/bin/pyscaffold" ]; then
    echo "Removing existing pyscaffold in ~/.local/bin/"
    rm -rf "$HOME/.local/bin/pyscaffold"
fi

echo "Creating symlink in ~/.local/bin/"
# Create a symlink in the bin directory
ln -sf "$HOME/.local/lib/pyscaffold/python_scaffold.py" "$HOME/.local/bin/pyscaffold"

# Make the symlink executable
chmod +x "$HOME/.local/bin/pyscaffold"

# Function to update shell configuration
update_shell_config() {
    local shell_type="$1"
    local shell_rc="$2"
    
    if [[ -f "$shell_rc" ]]; then
        if ! grep -q 'export PATH="$HOME/.local/bin:$PATH"' "$shell_rc"; then
            echo "Adding ~/.local/bin to your PATH in $shell_rc"
            echo '' >> "$shell_rc"
            echo '# Add ~/.local/bin to PATH for Python Project Scaffolder' >> "$shell_rc"
            echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$shell_rc"
            echo "Please run 'source $shell_rc' or restart your terminal to update your PATH"
        else
            echo "$shell_type: ~/.local/bin is already in your PATH"
        fi
    else
        echo "$shell_type: Configuration file $shell_rc not found. Creating it..."
        echo '# Add ~/.local/bin to PATH for Python Project Scaffolder' > "$shell_rc"
        echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$shell_rc"
        echo "Please run 'source $shell_rc' or restart your terminal to update your PATH"
    fi
}

# Update Bash configuration
update_shell_config "Bash" "$HOME/.bashrc"

# Update Zsh configuration
update_shell_config "Zsh" "$HOME/.zshrc"

# Verify the installation
echo -e "\nVerifying installation..."
if [ -x "$HOME/.local/lib/pyscaffold/python_scaffold.py" ] && [ -L "$HOME/.local/bin/pyscaffold" ]; then
    echo "✅ Installation successful!"
    echo -e "\nTo start using pyscaffold, run:"
    echo "  For Bash: source ~/.bashrc"
    echo "  For Zsh:  source ~/.zshrc"
    echo -e "\nThen you can create a new project with:"
    echo "  pyscaffold my_project --author 'Your Name' --email 'your.email@example.com'"
else
    echo "❌ Installation encountered issues."
    echo "Try running the script directly:"
    echo "  python $HOME/.local/lib/pyscaffold/python_scaffold.py my_project"
fi
