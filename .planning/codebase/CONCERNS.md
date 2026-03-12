# Concerns

Key architectural and technical risks.

- **Maintainability:** Large `style.css` (~2000 lines) makes it difficult to navigate and manage styles.
- **Organization:** Flat directory structure may become cluttered as the project grows.
- **Security:** HTML string injection risks in the Python-based `review-server`.
- **Documentation:** Documentation is bundled directly with the implementation, blurring the line between design system core and user guides.
