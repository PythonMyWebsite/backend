# syntax=docker/dockerfile:1

FROM python:3.10.12

# Tạo một người dùng không phải root
RUN useradd --create-home appuser
WORKDIR /app

# Sao chép tệp requirements.txt vào thư mục /app
COPY . .

# Cài đặt Django và các gói khác trong một môi trường ảo và sử dụng người dùng appuser
RUN python -m venv venv
RUN . venv/bin/activate && pip install -r requirements.txt


# Sao chép tất cả các tệp trong thư mục hiện tại vào thư mục /app trong container
COPY . .

# Thiết lập biến môi trường
ENV PYTHONUNBUFFERED=1

# Chạy ứng dụng với người dùng appuser
USER appuser

# Lệnh chạy ứng dụng
CMD [ "venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]
