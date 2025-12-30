# WebApp Backend - Scalable Flask App with Docker Swarm

## Deskripsi
Project ini adalah aplikasi web sederhana menggunakan **Flask** sebagai backend, yang di-deploy menggunakan **Docker Swarm** agar bisa **scalable, reliable, dan aman** saat banyak user mengakses.  

Fitur utama:
- Login API (`/api/login`)
- Scalable backend dengan Docker Swarm
- Multi-container deployment
- Mendukung request simultan dari banyak user

---

## Prerequisites
Sebelum menjalankan project ini, pastikan sudah menginstall:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/) (opsional)
- Python 3.11+ (untuk development lokal)
- Git (untuk clone repo)

---

## Instalasi


1. Clone repository:
bash
git clone https://github.com/username/webapp_backend.git
cd webapp_backend

docker build -t backend_app:latest .

docker swarm init          # kalau belum inisialisasi swarm
docker stack deploy -c docker-compose.yml webapp




