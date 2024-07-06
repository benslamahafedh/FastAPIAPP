FROM python:3.9-slim AS builder

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir fastapi uvicorn pytest httpx

RUN pytest --maxfail=1 --disable-warnings && echo "Tests passed successfully" > /app/tests_passed

RUN ls -la /app && cat /app/tests_passed

FROM python:3.9-slim

WORKDIR /app

COPY --from=builder /app /app

RUN ls -la /app && cat /app/tests_passed

RUN pip install --no-cache-dir fastapi uvicorn

EXPOSE 8000

RUN test -f /app/tests_passed || (echo "Tests did not pass. Aborting build." && exit 1)

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
