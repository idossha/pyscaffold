# Python Project Scaffolder

A command-line tool to generate standardized Python project architecture quickly and efficiently.

## Features

- Create a fully structured Python project with a single command
- Follows Python best practices and modern packaging standards
- Includes tests, documentation, and virtual environment setup
- Generates all necessary project files (README, LICENSE, setup.py, etc.)
- Creates standardized directory structure
- Customizable through command-line options

## Installation

### For macOS and Linux (Bash/Zsh)

1. Clone this repository or download the source files
2. Make the install script executable:
   ```bash
   chmod +x install.sh
   ```
3. Run the installation script:
   ```bash
   ./install.sh
   ```
4. Update your shell environment:
   ```bash
   # For Bash
   source ~/.bashrc
   
   # For Zsh
   source ~/.zshrc
   ```

## Usage

Create a new Python project with the default settings:

```bash
pyscaffold my_project
```

Customize the project with command-line options:

```bash
pyscaffold my_project --author "Your Name" --email "your.email@example.com" --description "A fantastic Python project"
```

### Command Line Options

| Option | Description |
|--------|-------------|
| `project_name` | Name of the project to create (required) |
| `--no-tests` | Skip creating tests directory |
| `--no-docs` | Skip creating docs directory |
| `--no-venv` | Skip creating virtual environment |
| `-a, --author` | Author name for project metadata |
| `-e, --email` | Author email for project metadata |
| `-d, --description` | Short description of the project |

## Project Structure

The generated project structure follows Python best practices:

```
my_project/                  # Root directory
├── my_project/             # Main package directory
│   └── __init__.py         # Package initializer
├── tests/                  # Test directory
│   ├── __init__.py
│   └── test_my_project.py  # Basic test file
├── docs/                   # Documentation
│   └── index.md            # Basic documentation
├── venv/                   # Virtual environment (if requested)
├── .gitignore              # Git ignore file with Python defaults
├── LICENSE                 # MIT license
├── Makefile                # Common development commands
├── README.md               # Project readme with usage instructions
├── pyproject.toml          # PEP 517/518 build system specification
├── setup.cfg               # Package metadata and config
└── setup.py                # Setup script for installing package
```

## Customization

You can modify the `python_scaffold.py` script to customize the template further:

- Add additional directories (like `data/` or `examples/`)
- Change the default license
- Add configuration for specific frameworks (Django, Flask, etc.)
- Include CI/CD configuration files (.github/workflows, etc.)

## Development

To contribute to this project:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Troubleshooting

### Permission Denied

If you get a "permission denied" error when running `pyscaffold`:

```bash
# Make the script executable
chmod +x ~/.local/lib/pyscaffold/python_scaffold.py
chmod +x ~/.local/bin/pyscaffold
```

### Command Not Found

If the `pyscaffold` command is not found:

1. Ensure `~/.local/bin` is in your PATH:
   ```bash
   echo $PATH
   ```
2. If not, add it manually:
   ```bash
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc  # or ~/.zshrc
   source ~/.bashrc  # or ~/.zshrc
   ```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
