FROM python:3.11-slim
WORKDIR /app
COPY . /app
run pip install --no-cache-dir fastapi uvicorn[sNandard]
ENV APP_PORT=8080
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8080"]
