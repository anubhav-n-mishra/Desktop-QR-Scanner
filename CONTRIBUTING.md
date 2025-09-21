# Contributing to QRiftly

Thank you for your interest in contributing to QRiftly! We welcome contributions from the community and are grateful for your support.

## 🎯 Ways to Contribute

### 🐛 Bug Reports
- Use the GitHub issue tracker to report bugs
- Include steps to reproduce the issue
- Provide system information (Windows version, Python version)
- Attach screenshots if applicable

### 💡 Feature Requests
- Search existing issues before creating new ones
- Clearly describe the feature and its benefits
- Provide examples of how it would be used

### 🔧 Code Contributions
- Fork the repository
- Create a new branch for your feature
- Write clean, documented code
- Test your changes thoroughly
- Submit a pull request

### 📚 Documentation
- Help improve README, documentation, and comments
- Add examples and tutorials
- Fix typos and clarify explanations

## 🚀 Development Setup

1. **Fork and Clone**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Desktop-QR-Scanner.git
   cd Desktop-QR-Scanner
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # Development dependencies
   ```

4. **Run Tests**
   ```bash
   python -m pytest tests/
   ```

## 📋 Development Guidelines

### Code Style
- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and concise

### Security
- Validate all user inputs
- Use secure coding practices
- Don't introduce vulnerabilities
- Test security-related features thoroughly

### Testing
- Write unit tests for new features
- Test on different Windows versions
- Verify security features work correctly
- Test with various QR code types

### Documentation
- Update README if adding new features
- Add docstrings to new functions
- Include usage examples
- Update changelog

## 🔄 Pull Request Process

1. **Before Submitting**
   - Ensure your code follows the style guidelines
   - Run all tests and ensure they pass
   - Update documentation as needed
   - Test on Windows systems

2. **Pull Request Description**
   - Clearly describe what your PR does
   - Link any related issues
   - Include screenshots for UI changes
   - List any breaking changes

3. **Review Process**
   - Maintainers will review your PR
   - Address any feedback promptly
   - Be open to suggestions and changes
   - PR will be merged once approved

## 🐛 Reporting Issues

### Security Issues
For security vulnerabilities, please email directly instead of creating a public issue.

### Bug Reports
Include the following information:
- **Environment**: Windows version, Python version
- **Steps to Reproduce**: Detailed steps
- **Expected Behavior**: What should happen
- **Actual Behavior**: What actually happens
- **Screenshots**: If applicable
- **Error Messages**: Full error text

### Feature Requests
- Check if the feature already exists
- Explain the use case and benefits
- Provide examples of how it would work
- Consider implementation complexity

## 💬 Community Guidelines

- Be respectful and inclusive
- Help other contributors
- Ask questions if you're unsure
- Provide constructive feedback
- Follow the code of conduct

## 🏆 Recognition

Contributors will be recognized in:
- README acknowledgments
- Release notes
- Contributors list

## 📞 Getting Help

- **Documentation**: Check the docs/ folder
- **Issues**: Search existing GitHub issues
- **Discussions**: Use GitHub Discussions for questions
- **Email**: Contact the maintainer for urgent matters

## 📝 License

By contributing to QRiftly, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to QRiftly! Your help makes this project better for everyone. 🎉