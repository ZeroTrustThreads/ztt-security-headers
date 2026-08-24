# 🛡️ Zero Trust Threads Security Headers Checker

A beginner-friendly cybersecurity education tool for learning how websites use **HTTP security headers**.

Built by **Zero Trust Threads** to help students, developers, system administrators, and cybersecurity learners understand browser security controls through hands-on practice.

---

# 📌 Project Status

**Current Version:** v1.0.0

This project is an educational cybersecurity tool designed to teach:

- HTTP security headers
- Browser security concepts
- Defensive security practices
- Python security tooling development
- Testing and automation workflows

---

# 🎯 Project Purpose

Cybersecurity can feel overwhelming when you are first starting.

Many security tools are built for experienced professionals and provide large amounts of technical information without explaining the fundamentals.

Zero Trust Threads Security Headers Checker takes a different approach:

1. Scan a website
2. Identify common HTTP security headers
3. Explain what each header does
4. Explain why each header matters
5. Provide educational references
6. Generate learning-focused reports

The goal is not to replace professional security tools.

The goal is to help people **learn security concepts through practice.**

---

# 💡 Why This Project Exists

Security knowledge is built through understanding.

Before learning advanced topics like:

- vulnerability management
- penetration testing
- cloud security
- security engineering
- governance and compliance

learners need strong fundamentals.

HTTP security headers are a great starting point because they introduce important concepts:

- How browsers communicate with websites
- How servers influence browser behavior
- How security controls reduce risk
- How defenders think about protection

This project turns those concepts into hands-on learning.

---

# 📚 What You Will Learn

By completing this project, you will gain experience with:

## Cybersecurity Concepts

- HTTP fundamentals
- HTTP headers
- HTTPS security
- Browser security controls
- Content Security Policy (CSP)
- Security best practices
- Defensive security concepts

---

## Technical Skills

- Python CLI applications
- Git and GitHub workflows
- Automated testing
- JSON data formats
- HTML reporting
- Security tooling architecture
- Open-source development practices

---

# ⚙️ Features

## 🔎 Security Header Checking

The tool evaluates common security headers:

| Header | Purpose | Difficulty |
|---|---|---|
| Strict-Transport-Security (HSTS) | Forces HTTPS usage | Beginner |
| Content-Security-Policy (CSP) | Controls browser resources | Intermediate |
| X-Content-Type-Options | Prevents MIME sniffing | Beginner |
| Referrer-Policy | Controls referrer information | Beginner |
| Permissions-Policy | Controls browser features | Intermediate |
| X-Frame-Options | Helps prevent clickjacking | Beginner |

---

# 🧠 Learning Mode

Run:

```bash
python -m src.cli https://example.com --learn
```

Learning mode explains:

- What the header does
- Why it matters
- Difficulty level
- Security benefits
- Educational references

Example:

```
Content-Security-Policy

Status:
MISSING

What is it?
Controls which resources a browser is allowed to load.

Why does it matter?
Helps reduce certain client-side attacks.

Difficulty:
Intermediate
```

---

# 📄 JSON Output

Run:

```bash
python -m src.cli https://example.com --json
```

Useful for learning:

- Structured data
- Automation concepts
- Security tooling workflows
- Data processing

Example:

```json
{
    "target": "https://example.com/",
    "status_code": 200,
    "findings": [
        {
            "name": "Content-Security-Policy",
            "status": "missing"
        }
    ]
}
```

---

# 🌐 HTML Learning Reports

Run:

```bash
python -m src.cli https://example.com --report html
```

Creates an educational report containing:

- Scan results
- Header explanations
- Security concepts
- References

Reports are saved locally.

---

# 🏗️ How It Works

The project follows a simple security tooling workflow:

```
Website URL
     |
     v
HTTP Request
     |
     v
Collect Response Headers
     |
     v
Analyze Security Headers
     |
     v
Lookup Educational Content
     |
     v
Generate Learning Output
```

---

# 📂 Project Architecture

```
ztt-security-headers/

├── src/
│
│   ├── cli.py
│   │   Command line interface
│
│   ├── scanner.py
│   │   Handles scanning workflow
│
│   ├── checker.py
│   │   Evaluates security headers
│
│   ├── database.py
│   │   Loads educational information
│
│   ├── learning.py
│   │   Formats learning content
│
│   ├── reports.py
│   │   Generates reports
│
│   └── models.py
│       Data models
│
├── data/
│   └── headers.yaml
│       Security header knowledge base
│
├── tests/
│   Automated tests
│
├── labs/
│   Educational exercises
│
├── examples/
│   Example data
│
├── Dockerfile
│
├── requirements.txt
│
└── README.md
```

---

# 🚀 Installation Guide

## Requirements

You need:

- Python 3.13+
- Git
- Terminal access

Recommended:

- VS Code
- macOS
- Linux
- Windows with WSL

---

# Step 1 — Clone the Repository

```bash
git clone https://github.com/ZeroTrustThreads/ztt-security-headers.git
```

Move into the project:

```bash
cd ztt-security-headers
```

---

# Step 2 — Create Virtual Environment

Create:

```bash
python3 -m venv .venv
```

Activate:

## macOS / Linux

```bash
source .venv/bin/activate
```

## Windows

```powershell
.venv\Scripts\activate
```

You should see:

```
(.venv)
```

---

# Step 3 — Install Dependencies

Run:

```bash
python -m pip install -r requirements.txt
```

---

# Step 4 — Run Tests

Verify everything works:

```bash
python -m pytest
```

Expected:

```
17 passed
```

---

# 🚀 Using The Tool

## Basic Scan

Example:

```bash
python -m src.cli https://example.com
```

Displays:

- Target website
- HTTP status
- Security header findings

---

## Learning Scan

Example:

```bash
python -m src.cli https://example.com --learn
```

Recommended for beginners.

---

## JSON Export

Example:

```bash
python -m src.cli https://example.com --json
```

---

## HTML Report

Example:

```bash
python -m src.cli https://example.com --report html
```

---

# 🧪 Learning Labs

The project includes educational exercises.

## Lab 01 — HTTP Basics

Learn:

- What HTTP is
- How browsers communicate
- What headers are

---

## Lab 02 — Security Headers

Learn:

- HSTS
- CSP
- Browser security controls

---

## Lab 03 — Python Testing

Learn:

- Unit testing
- Test-driven development
- Code quality

---

## Lab 04 — Contributing

Learn:

- Git workflows
- Pull requests
- Open-source collaboration

---

# 👩‍💻 Development Setup

Clone the project:

```bash
git clone https://github.com/ZeroTrustThreads/ztt-security-headers.git
```

Create environment:

```bash
python3 -m venv .venv
```

Activate:

```bash
source .venv/bin/activate
```

Install:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
pytest
```

---

# 🤝 Contributing

Contributions are welcome.

Good beginner contributions:

- Improving documentation
- Adding tests
- Adding educational explanations
- Fixing bugs
- Improving examples

Before contributing:

1. Read CONTRIBUTING.md
2. Create a branch
3. Add tests for changes
4. Submit a pull request

---

# ⚠️ Important Disclosures

## Educational Purpose Only

This project is provided for educational and learning purposes.

It is designed to help users understand:

- HTTP security headers
- Browser security concepts
- Defensive security practices

---

## No Security Guarantee

This tool does not guarantee that a website is secure.

Website security depends on many factors including:

- Application design
- Authentication controls
- Authorization logic
- Server configuration
- Infrastructure security
- Code quality
- Business requirements

A successful scan does not mean a website is secure.

---

## Not a Professional Security Assessment

This project is not intended to replace:

- Penetration testing
- Vulnerability assessments
- Security audits
- Professional security reviews

Organizations should work with qualified security professionals for formal assessments.

---

## Responsible Use

Only scan systems you own or have explicit permission to test.

Do not use this tool to:

- Access unauthorized systems
- Disrupt services
- Perform intrusive testing

Users are responsible for ensuring their activities comply with applicable laws and policies.

---

## Scope Limitations

This tool analyzes publicly available HTTP response headers.

It does not perform:

- Exploitation
- Vulnerability scanning
- Penetration testing
- Authentication testing
- Application security testing

---

# 🔗 External References

This project may reference educational resources including:

- OWASP documentation
- Mozilla Developer Network (MDN)

Zero Trust Threads is not affiliated with, sponsored by, or endorsed by these organizations.

References are provided for educational purposes.

---

# 📜 License

This project is licensed under the MIT License.

See:

```
LICENSE
```

for details.

---

# 🛡️ About Zero Trust Threads

Zero Trust Threads creates cybersecurity education content, tools, and resources designed to make security concepts approachable through:

- Practical projects
- Hands-on learning
- Security culture
- Community education

The mission:

**Learn. Build. Secure.**

🛡️ Zero Trust Threads