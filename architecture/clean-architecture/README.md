# 🧱 Clean Architecture Project – Angular + NestJS

A scalable full-stack project following **Clean Architecture** principles, built with:

- 🧩 **Frontend**: Angular  
- ⚙️ **Backend**: NestJS  

This structure provides a **modular, testable, and maintainable** foundation for modern web applications.

---

## 🚀 Project Overview

This repository contains three main modules:

| Module     | Description |
|-------------|--------------|
| **Frontend** | Angular application structured with clean architecture principles. |
| **Backend**  | NestJS API layered into Domain, Infrastructure, and Presentation. |

Each module is **independent** and can be developed or deployed separately.

---

## 🧭 Folder Structure

### 🅰️ Frontend (Angular)
```
src/app/
├── core/               # Guards, interceptors, services, utils, state
├── domain/             # Business models, repositories, use-cases
├── infrastructure/     # Data sources, HTTP clients
├── presentation/       # UI components, modules, pages, layout, shared
├── assets/             # Static assets
├── environments/       # Environment configuration
└── test/               # Unit & acceptance tests
```

### ⚙️ Backend (NestJS)
```
src/
├── config/             # Environment and configuration files
├── constants/          # Global constants
├── decorators/         # Custom decorators
├── guards/             # Auth and access control guards
├── modules/            # Feature modules
│   ├── domain/         # Entities, services, use-cases
│   ├── infrastructure/ # Models, services, validations
│   └── presentation/   # Controllers, DTOs
├── pipes/              # Data validation and transformation
├── repositories/       # Data access layer
└── test/               # Unit, integration, acceptance tests
```

## 🧱 Clean Architecture Principles

This project follows **Clean Architecture** by **Robert C. Martin (Uncle Bob)**:

- **Domain Layer** → Business logic (Entities, Use Cases)
- **Infrastructure Layer** → Data access, external services, persistence
- **Presentation Layer** → UI (Angular) or Controllers (NestJS)
- **Core** → Shared utilities, guards, interceptors, configuration

Benefits:
- High testability 🔍  
- Independent of frameworks 🧩  
- Clear separation of concerns 🧠  
- Easy maintenance and scalability 🚀  

---

## 🧪 Testing

Each module includes its own test structure:

| Type | Description |
|------|--------------|
| `unit` | Tests individual components or services |
| `integration` | Tests interactions between modules |
| `acceptanceTests` | End-to-end functional tests |

## ⚙️ Environment Variables

Example `.env` for the backend:
```env
PORT=3000
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
JWT_SECRET=supersecretkey
```

Example environment file for the frontend (`src/environments/environment.ts`):
```ts
export const environment = {
  production: false,
  apiUrl: 'http://localhost:3000/api'
};
```

---

## 🧑‍💻 Contributing

1. Fork this repository  
2. Create a new branch (`feature/my-feature`)  
3. Commit your changes (`git commit -m 'Add new feature'`)  
4. Push the branch (`git push origin feature/my-feature`)  
5. Create a Pull Request 🚀

---

## 📜 License

This project is licensed under the **MIT License**. Feel free to use and modify it for your own projects.

---

## ✨ Author

👤 **IngAamira**  
💼 GitHub: [@ingaamira](https://github.com/ingaamira)  
🚀 Building clean, scalable, and AI-driven software.