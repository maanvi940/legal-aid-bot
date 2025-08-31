# Contributing to Constitutional Rights Assistant

Thank you for your interest in contributing to the Constitutional Rights Assistant project! This document provides guidelines and information for contributors.

## Table of Contents

- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Code Style Guidelines](#code-style-guidelines)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Issue Reporting](#issue-reporting)
- [Feature Requests](#feature-requests)
- [Legal Content Guidelines](#legal-content-guidelines)

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Git
- A GitHub account
- Basic knowledge of HTML, CSS, JavaScript, and Python

### Fork and Clone

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/legal-aid-bot.git
   cd legal-aid-bot
   ```
3. **Add the original repository** as upstream:
   ```bash
   git remote add upstream https://github.com/ORIGINAL_OWNER/legal-aid-bot.git
   ```

## Development Setup

1. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment**:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the development server**:
   ```bash
   python app.py
   ```

5. **Access the application** at `http://localhost:5000`

## Making Changes

### Branch Naming Convention

Create a new branch for each feature or fix:

```bash
git checkout -b feature/your-feature-name
git checkout -b fix/your-bug-fix
git checkout -b docs/your-documentation-update
```

### Commit Message Guidelines

Use clear, descriptive commit messages:

```
Add: Google search integration for legal topics
Fix: Contact form validation error
Update: README with installation instructions
Docs: Add contributing guidelines
```

### Pull Request Process

1. **Create a feature branch** from `main`
2. **Make your changes** following the code style guidelines
3. **Test your changes** thoroughly
4. **Commit your changes** with descriptive messages
5. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Create a Pull Request** on GitHub
7. **Wait for review** and address any feedback

## Code Style Guidelines

### Python (Flask)

- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings for functions and classes
- Keep functions small and focused

```python
def get_legal_topic(topic_id):
    """
    Retrieve legal topic information by ID.
    
    Args:
        topic_id (str): The unique identifier for the topic
        
    Returns:
        dict: Topic information or None if not found
    """
    # Implementation here
    pass
```

### HTML/CSS

- Use semantic HTML elements
- Follow BEM methodology for CSS classes
- Use Tailwind CSS utility classes
- Ensure accessibility standards are met

```html
<!-- Good -->
<main class="legal-topics-container">
  <section class="legal-topics__header">
    <h1 class="legal-topics__title">Legal Topics</h1>
  </section>
</main>

<!-- Avoid -->
<div class="container">
  <div class="header">
    <div class="title">Legal Topics</div>
  </div>
</div>
```

### JavaScript

- Use ES6+ features when possible
- Follow consistent naming conventions
- Add comments for complex logic
- Handle errors gracefully

```javascript
// Good
const handleFormSubmit = async (event) => {
  try {
    event.preventDefault();
    const formData = new FormData(event.target);
    const response = await submitForm(formData);
    showSuccessMessage(response.message);
  } catch (error) {
    console.error('Form submission failed:', error);
    showErrorMessage('Failed to submit form. Please try again.');
  }
};
```

## Testing

### Manual Testing

Before submitting changes, test the following:

- [ ] Application starts without errors
- [ ] All pages load correctly
- [ ] Forms work as expected
- [ ] Responsive design on different screen sizes
- [ ] Links and navigation work properly
- [ ] No console errors in browser

### Automated Testing (Future)

We plan to add automated tests. When implemented, ensure:

- [ ] All tests pass
- [ ] New features have corresponding tests
- [ ] Test coverage is maintained

## Submitting Changes

### Pull Request Template

When creating a Pull Request, use this template:

```markdown
## Description
Brief description of the changes made.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring
- [ ] Performance improvement

## Testing
- [ ] Manual testing completed
- [ ] No console errors
- [ ] Responsive design verified

## Screenshots (if applicable)
Add screenshots for UI changes.

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes
```

## Issue Reporting

### Bug Reports

When reporting bugs, include:

1. **Clear description** of the issue
2. **Steps to reproduce** the problem
3. **Expected behavior** vs actual behavior
4. **Environment details** (OS, browser, Python version)
5. **Screenshots** if applicable
6. **Console errors** if any

### Feature Requests

When requesting features, include:

1. **Clear description** of the feature
2. **Use case** and benefits
3. **Implementation suggestions** (optional)
4. **Priority level** (low, medium, high)

## Legal Content Guidelines

### Content Standards

When contributing legal content:

- **Accuracy**: Ensure all legal information is accurate and up-to-date
- **Sources**: Cite reliable legal sources and references
- **Disclaimer**: Include appropriate disclaimers
- **Language**: Use clear, accessible language
- **Completeness**: Provide comprehensive information

### Content Review Process

1. **Research**: Verify legal information from authoritative sources
2. **Draft**: Create initial content
3. **Review**: Have content reviewed by legal experts (if possible)
4. **Update**: Make necessary revisions
5. **Submit**: Submit for final review

### Legal Disclaimer

Always include appropriate disclaimers:

```html
<div class="legal-disclaimer">
  <p><strong>Disclaimer:</strong> This information is for general guidance only and should not be considered as legal advice. Please consult with a qualified legal professional for specific legal matters.</p>
</div>
```

## Getting Help

If you need help with contributing:

- **Read the documentation** in the README and this file
- **Search existing issues** for similar problems
- **Ask questions** in GitHub Discussions
- **Contact maintainers** at support@constitutionalrights.org

## Recognition

Contributors will be recognized in:

- **README.md** contributors section
- **GitHub contributors** page
- **Release notes** for significant contributions

Thank you for contributing to making legal information more accessible to everyone!
