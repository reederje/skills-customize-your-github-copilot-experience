# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build simple, well-structured REST APIs using the FastAPI framework. This assignment covers defining routes, request/response models, validation, and running a development server.

## 📝 Tasks

### 🛠️ Create a Small REST API with FastAPI

#### Description
Implement a small REST API that provides CRUD-like endpoints for a simple resource (for example, `Item`). Use `pydantic` models for request validation and return appropriate HTTP status codes and errors.

#### Requirements
Completed program should:

- Define at least three endpoints: `GET /items/{id}`, `POST /items`, and `GET /` (health or welcome).
- Use `pydantic` models for request and response validation.
- Handle missing resources with proper HTTP status codes (e.g., 404).
- Include clear instructions for running the app locally.

You can use the provided `starter-code.py` to get started.

## 📎 Deliverables

- `starter-code.py` (in this folder) with a working FastAPI app.
- A short README explaining how to run the server and test the endpoints.

## ✅ Evaluation

- Correct use of FastAPI route decorators and `pydantic` models.
- Clear, working instructions to run the app.
- Proper handling of errors and HTTP status codes.

## 💡 Tips

- Run locally with `uvicorn starter-code:app --reload` after installing dependencies.
- Use `curl` or an API client (Postman / HTTPie) to test endpoints.
