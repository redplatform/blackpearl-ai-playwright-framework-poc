# AI-Powered Playwright Automation Framework (PoC)

An advanced, production-ready test automation framework utilizing **Python**, **Playwright**, and **pytest**. This project demonstrates enterprise-level testing patterns alongside an experimental AI healing layer designed to minimize script fragility and maintenance overhead.

---

## 🚀 Key Highlights for Recruiters
*   **Page Object Model (POM):** Clean separation of test logic from UI elements for maximum reusability.
*   **Data-Driven Automation:** Dynamic test data execution via isolated JSON datasets and reusable pytest fixtures.
*   **AI-Driven Self-Healing (PoC):** Integration with LLM APIs (OpenAI/Claude) to dynamically parse the DOM and heal broken selectors on failure.
*   **CI/CD Pipeline Integration:** Automated test execution and execution tracing via GitHub Actions.

---

## 🛠️ Tech Stack & Core Tools
*   **Language:** Python 3.x
*   **Execution Engine:** pytest-playwright
*   **Design Pattern:** Page Object Model (POM)
*   **Reporting:** pytest-html / Allure Reporting
*   **CI/CD Platform:** GitHub Actions
*   **AI Engine:** OpenAI / Claude API Client

---

## 📅 Project Implementation Timeline

### 🛠️ Week 1: Setup & Core Infrastructure (Completed)
*   Isolated virtual environment configured (`venv`).
*   Playwright core engine and browser binaries deployed.
*   Version control baseline integrated with secure tracking barriers (`.gitignore`).

### 🏗️ Week 2: Scalable Architecture (In Progress)
*   Modular directory structure layout (`pages/`, `tests/`, `utils/`).
*   Object abstraction mappings (`LoginPage`, `HomePage`).
*   Data tokenization utilizing JSON file providers.

### 🧠 Week 3: Cognitive & Self-Healing Layer
*   Deployment of async LLM client infrastructure inside `utils/ai_client.py`.
*   Development of an autonomous element router mapping user intent prompts directly to targeted actions.
*   Implementation of an active runtime engine parser to automatically find alternative selectors during DOM degradation.

### 📊 Week 4: Deployment & Portfolio Polish
*   Integration of automated runtime schedules inside GitHub Actions workflows.
*   Packaging rich artifact reports including visual tracking execution video playbacks.
*   Final system demonstration build.
