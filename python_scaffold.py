#!/usr/bin/env python3
"""
Python Project Scaffolder

A command-line tool to generate standardized Python project architecture.
"""

import os
import sys
import argparse
import shutil
from pathlib import Path


class ProjectScaffolder:
    """Class to generate a standardized Python project structure."""

    def __init__(self, project_name, use_tests=True, use_docs=True, use_venv=True, 
                 author="", email="", description=""):
        self.project_name = project_name
        self.use_tests = use_tests
        self.use_docs = use_docs
        self.use_venv = use_venv
        self.author = author
        self.email = email
        self.description = description
        
        # Sanitize project name for package name (if needed)
        self.package_name = project_name.replace("-", "_").lower()
        
        # Base directory is current directory + project name
        self.base_dir = os.path.join(os.getcwd(), project_name)

    def create_directory_structure(self):
        """Create the project directory structure."""
        print(f"Creating project: {self.project_name}")
        
        # Create base directory
        os.makedirs(self.base_dir, exist_ok=True)
        
        # Create package directory
        package_dir = os.path.join(self.base_dir, self.package_name)
        os.makedirs(package_dir, exist_ok=True)
        
        # Create __init__.py in package directory
        with open(os.path.join(package_dir, "__init__.py"), "w") as f:
            f.write(f'"""Main package for {self.project_name}."""\n\n')
            f.write('__version__ = "0.1.0"\n')
        
        # Create tests directory if requested
        if self.use_tests:
            tests_dir = os.path.join(self.base_dir, "tests")
            os.makedirs(tests_dir, exist_ok=True)
            
            # Create __init__.py in tests directory
            with open(os.path.join(tests_dir, "__init__.py"), "w") as f:
                f.write('"""Test package for {self.package_name}."""\n')
            
            # Create a basic test file
            with open(os.path.join(tests_dir, f"test_{self.package_name}.py"), "w") as f:
                f.write(f'"""Tests for `{self.package_name}` package."""\n\n')
                f.write('import pytest\n')
                f.write(f'from {self.package_name} import __version__\n\n\n')
                f.write('def test_version():\n')
                f.write('    """Test version is a string."""\n')
                f.write('    assert isinstance(__version__, str)\n')

        # Create docs directory if requested
        if self.use_docs:
            docs_dir = os.path.join(self.base_dir, "docs")
            os.makedirs(docs_dir, exist_ok=True)
            
            # Create a basic docs file
            with open(os.path.join(docs_dir, "index.md"), "w") as f:
                f.write(f'# {self.project_name.title()}\n\n')
                f.write(f'{self.description}\n\n')
                f.write('## Installation\n\n')
                f.write('```bash\npip install .\n```\n\n')
                f.write('## Usage\n\n')
                f.write('```python\n')
                f.write(f'import {self.package_name}\n')
                f.write('```\n')

    def create_setup_files(self):
        """Create setup.py and related files."""
        # Create setup.py
        with open(os.path.join(self.base_dir, "setup.py"), "w") as f:
            f.write('#!/usr/bin/env python3\n\n')
            f.write('from setuptools import setup, find_packages\n\n')
            f.write('with open("README.md", "r", encoding="utf-8") as f:\n')
            f.write('    long_description = f.read()\n\n')
            f.write('setup(\n')
            f.write(f'    name="{self.project_name}",\n')
            f.write('    version="0.1.0",\n')
            f.write(f'    author="{self.author}",\n')
            f.write(f'    author_email="{self.email}",\n')
            f.write(f'    description="{self.description}",\n')
            f.write('    long_description=long_description,\n')
            f.write('    long_description_content_type="text/markdown",\n')
            f.write(f'    url="https://github.com/{self.author}/{self.project_name}",\n')
            f.write('    packages=find_packages(),\n')
            f.write('    classifiers=[\n')
            f.write('        "Programming Language :: Python :: 3",\n')
            f.write('        "License :: OSI Approved :: MIT License",\n')
            f.write('        "Operating System :: OS Independent",\n')
            f.write('    ],\n')
            f.write('    python_requires=">=3.6",\n')
            f.write('    install_requires=[\n')
            f.write('        # Add your dependencies here\n')
            f.write('    ],\n')
            f.write(')\n')
        
        # Create pyproject.toml for modern Python packaging
        with open(os.path.join(self.base_dir, "pyproject.toml"), "w") as f:
            f.write('[build-system]\n')
            f.write('requires = ["setuptools>=42", "wheel"]\n')
            f.write('build-backend = "setuptools.build_meta"\n')

        # Create setup.cfg
        with open(os.path.join(self.base_dir, "setup.cfg"), "w") as f:
            f.write('[metadata]\n')
            f.write('name = {self.project_name}\n')
            f.write('description = {self.description}\n')
            f.write('author = {self.author}\n')
            f.write('license = MIT\n')
            f.write('license_file = LICENSE\n')
            f.write('platforms = unix, linux, osx, win32\n')
            f.write('classifiers =\n')
            f.write('    Programming Language :: Python :: 3\n')
            f.write('    Programming Language :: Python :: 3 :: Only\n')
            f.write('    Programming Language :: Python :: 3.6\n')
            f.write('    Programming Language :: Python :: 3.7\n')
            f.write('    Programming Language :: Python :: 3.8\n')
            f.write('    Programming Language :: Python :: 3.9\n')
            f.write('\n[options]\n')
            f.write('packages =\n')
            f.write('    {self.package_name}\n')
            f.write('install_requires =\n')
            f.write('python_requires = >=3.6\n')
            f.write('zip_safe = no\n')

    def create_readme(self):
        """Create README.md file."""
        with open(os.path.join(self.base_dir, "README.md"), "w") as f:
            f.write(f'# {self.project_name.title()}\n\n')
            f.write(f'{self.description}\n\n')
            f.write('## Features\n\n')
            f.write('* TODO\n\n')
            f.write('## Installation\n\n')
            f.write('```bash\n')
            f.write('pip install .\n')
            f.write('```\n\n')
            f.write('## Quick Start\n\n')
            f.write('```python\n')
            f.write(f'import {self.package_name}\n\n')
            f.write('# Add example usage\n')
            f.write('```\n\n')
            f.write('## License\n\n')
            f.write('This project is licensed under the MIT License - see the LICENSE file for details.\n')

    def create_license(self):
        """Create LICENSE file with MIT License."""
        with open(os.path.join(self.base_dir, "LICENSE"), "w") as f:
            f.write('MIT License\n\n')
            f.write(f'Copyright (c) {self.get_current_year()} {self.author}\n\n')
            f.write('Permission is hereby granted, free of charge, to any person obtaining a copy\n')
            f.write('of this software and associated documentation files (the "Software"), to deal\n')
            f.write('in the Software without restriction, including without limitation the rights\n')
            f.write('to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n')
            f.write('copies of the Software, and to permit persons to whom the Software is\n')
            f.write('furnished to do so, subject to the following conditions:\n\n')
            f.write('The above copyright notice and this permission notice shall be included in all\n')
            f.write('copies or substantial portions of the Software.\n\n')
            f.write('THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n')
            f.write('IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n')
            f.write('FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n')
            f.write('AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n')
            f.write('LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n')
            f.write('OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n')
            f.write('SOFTWARE.\n')

    def create_gitignore(self):
        """Create .gitignore file."""
        with open(os.path.join(self.base_dir, ".gitignore"), "w") as f:
            f.write('# Byte-compiled / optimized / DLL files\n')
            f.write('__pycache__/\n')
            f.write('*.py[cod]\n')
            f.write('*$py.class\n\n')
            
            f.write('# Distribution / packaging\n')
            f.write('dist/\n')
            f.write('build/\n')
            f.write('*.egg-info/\n\n')
            
            f.write('# Unit test / coverage reports\n')
            f.write('.coverage\n')
            f.write('htmlcov/\n')
            f.write('.pytest_cache/\n\n')
            
            f.write('# Environments\n')
            f.write('.env\n')
            f.write('.venv\n')
            f.write('env/\n')
            f.write('venv/\n')
            f.write('ENV/\n\n')
            
            f.write('# IDE specific files\n')
            f.write('.idea/\n')
            f.write('.vscode/\n')
            f.write('*.swp\n')
            f.write('*.swo\n')

    def create_venv(self):
        """Create a virtual environment if requested."""
        if self.use_venv:
            print("Creating virtual environment...")
            import venv
            venv.create(os.path.join(self.base_dir, "venv"), with_pip=True)
            print("Virtual environment created at ./venv")
            print("Activate it with:")
            if os.name == "nt":  # Windows
                print(f"cd {self.project_name} && .\\venv\\Scripts\\activate")
            else:  # Unix/Linux
                print(f"cd {self.project_name} && source venv/bin/activate")

    def create_makefile(self):
        """Create a simple Makefile with common commands."""
        with open(os.path.join(self.base_dir, "Makefile"), "w") as f:
            f.write('.PHONY: clean clean-test clean-pyc clean-build help\n\n')
            
            f.write('help:\n')
            f.write('\t@echo "clean - remove all build, test, coverage and Python artifacts"\n')
            f.write('\t@echo "clean-build - remove build artifacts"\n')
            f.write('\t@echo "clean-pyc - remove Python file artifacts"\n')
            f.write('\t@echo "clean-test - remove test and coverage artifacts"\n')
            f.write('\t@echo "lint - check style with flake8"\n')
            f.write('\t@echo "test - run tests quickly with the default Python"\n')
            f.write('\t@echo "coverage - check code coverage quickly with the default Python"\n')
            f.write('\t@echo "build - build the package"\n')
            f.write('\t@echo "install - install the package to the active Python site-packages"\n\n')
            
            f.write('clean: clean-build clean-pyc clean-test\n\n')
            
            f.write('clean-build:\n')
            f.write('\trm -fr build/\n')
            f.write('\trm -fr dist/\n')
            f.write('\trm -fr .eggs/\n')
            f.write('\tfind . -name "*.egg-info" -exec rm -fr {} +\n')
            f.write('\tfind . -name "*.egg" -exec rm -f {} +\n\n')
            
            f.write('clean-pyc:\n')
            f.write('\tfind . -name "*.pyc" -exec rm -f {} +\n')
            f.write('\tfind . -name "*.pyo" -exec rm -f {} +\n')
            f.write('\tfind . -name "*~" -exec rm -f {} +\n')
            f.write('\tfind . -name "__pycache__" -exec rm -fr {} +\n\n')
            
            f.write('clean-test:\n')
            f.write('\trm -fr .coverage\n')
            f.write('\trm -fr htmlcov/\n')
            f.write('\trm -fr .pytest_cache\n\n')
            
            f.write('lint:\n')
            f.write('\tflake8 {self.package_name} tests\n\n')
            
            f.write('test:\n')
            f.write('\tpytest\n\n')
            
            f.write('coverage:\n')
            f.write('\tcoverage run --source {self.package_name} -m pytest\n')
            f.write('\tcoverage report -m\n')
            f.write('\tcoverage html\n\n')
            
            f.write('build:\n')
            f.write('\tpython setup.py sdist bdist_wheel\n\n')
            
            f.write('install:\n')
            f.write('\tpip install .\n')

    def get_current_year(self):
        """Get current year for license."""
        from datetime import datetime
        return datetime.now().year

    def scaffold(self):
        """Run the entire scaffolding process."""
        self.create_directory_structure()
        self.create_setup_files()
        self.create_readme()
        self.create_license()
        self.create_gitignore()
        self.create_makefile()
        
        if self.use_venv:
            self.create_venv()
        
        print(f"\nProject {self.project_name} created successfully!")
        print(f"Get started with: cd {self.project_name}")


def main():
    """Main function to handle command-line arguments and run scaffolding."""
    parser = argparse.ArgumentParser(
        description="Generate a standardized Python project structure."
    )
    
    parser.add_argument("project_name", help="Name of the project to create")
    
    parser.add_argument(
        "--no-tests", 
        action="store_true", 
        help="Skip creating tests directory"
    )
    
    parser.add_argument(
        "--no-docs", 
        action="store_true", 
        help="Skip creating docs directory"
    )
    
    parser.add_argument(
        "--no-venv", 
        action="store_true", 
        help="Skip creating virtual environment"
    )
    
    parser.add_argument(
        "-a", "--author", 
        default="", 
        help="Author name for project metadata"
    )
    
    parser.add_argument(
        "-e", "--email", 
        default="", 
        help="Author email for project metadata"
    )
    
    parser.add_argument(
        "-d", "--description", 
        default="A Python package", 
        help="Short description of the project"
    )
    
    args = parser.parse_args()
    
    # Check if project directory already exists
    if os.path.exists(os.path.join(os.getcwd(), args.project_name)):
        print(f"Error: Directory {args.project_name} already exists.")
        sys.exit(1)
    
    # Create scaffolder and run
    scaffolder = ProjectScaffolder(
        project_name=args.project_name,
        use_tests=not args.no_tests,
        use_docs=not args.no_docs,
        use_venv=not args.no_venv,
        author=args.author,
        email=args.email,
        description=args.description,
    )
    
    scaffolder.scaffold()


if __name__ == "__main__":
    main()
