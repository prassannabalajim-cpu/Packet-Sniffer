#!/usr/bin/env python3
"""
Setup configuration for packet-sniffer package
Allows installation via: pip install -e .
"""

from setuptools import setup, find_packages

# Read long description from README
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements from requirements.txt
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="packet-sniffer",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Advanced network packet sniffer with filtering and analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/packet-sniffer",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/packet-sniffer/issues",
        "Documentation": "https://github.com/yourusername/packet-sniffer/blob/main/README.md",
        "Source Code": "https://github.com/yourusername/packet-sniffer",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: System :: Networking",
        "Topic :: System :: Networking :: Monitoring",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "packet-sniffer=main:main",
        ],
    },
    keywords="packet sniffer network analysis cybersecurity",
    include_package_data=True,
    zip_safe=False,
)
