# Contributing to RobotEvo

Thank you for your interest in contributing to RobotEvo! This document provides guidelines and instructions for contributing.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/robotevo.git
   cd robotevo
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install in development mode:
   ```bash
   pip install -e .
   ```

## Code Style Guidelines

RobotEvo prioritizes **human readability** over strict tool compliance:

- **Good naming**: Choose clear, descriptive names (especially for functions and variables)
- **Vertical formatting**: Use vertical alignment for readability, especially in:
  - Function definitions with many parameters
  - Complex conditional statements (`if` with many conditions)
  - Series of related assignments
- **PEP8 compliance**: Follow PEP8 when it doesn't compromise readability
- **Line length**: 130 characters max (optimal for dual-monitor setup)

## Development Workflow

1. Create a new branch for your feature/fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes following the code style guidelines

3. Test your changes:
   ```bash
   python tests.py
   ```

4. Commit with clear, descriptive messages:
   ```bash
   git commit -m "Add description of what you changed and why"
   ```

5. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

6. Create a Pull Request on GitHub with a clear description

## Protocol Contributions

If you're contributing a new protocol:

1. Place it in the `robotevo/protocols/` directory following existing naming conventions
2. Create a subpackage (directory with `__init__.py`) for your protocol
3. Document parameters and usage in docstrings
4. Include example usage in comments
5. Add to the protocol registry if applicable

Example protocol structure:
```
robotevo/protocols/
├── my_protocol/
│   ├── __init__.py
│   ├── my_protocol.py
│   └── README.md
```

## Reporting Issues

- Use GitHub Issues to report bugs
- Include:
  - Python version
  - robotevo version
  - Steps to reproduce
  - Expected vs. actual behavior
  - Any error messages or tracebacks

## Code of Conduct

Be respectful and constructive in all interactions. We're building a community!

## Questions?

Feel free to open an issue for questions or discussions about contributions.

Thank you for contributing to RobotEvo!
