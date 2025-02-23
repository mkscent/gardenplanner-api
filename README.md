# 🌱 Gardening API

A **FastAPI-based** backend for a gardening app, using **PostgreSQL** as the database and **SQLAlchemy** for ORM.  
It allows users to **manage gardens, track plants, and receive personalized growing recommendations.**  

## 🛠️ Features
✅ **User Authentication** (JWT-based)  
✅ **Create & Manage Gardens** (Specify size, shape, and plants)  
✅ **400+ Plant Database** with Grow Guides  
✅ **Personalized Planting Reminders**  
✅ **Crop Rotation & Companion Planting Warnings**  
✅ **Garden Journal** for tracking notes and harvests  

---

## 🚀 Tech Stack
- **Backend:** FastAPI (Python)
- **Database:** PostgreSQL (via SQLAlchemy)
- **Auth:** JWT (OAuth2 with Password Flow)
- **Async Support:** `asyncpg` + `SQLAlchemy`
- **Migrations:** Alembic
- **Environment Management:** `dotenv`
- **Testing:** Pytest

---

## ⚙️ Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/gardening-api.git
cd gardening-api
```

### **2️⃣ Set Up Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up the Database**
- Ensure **PostgreSQL is running** (or use Docker).
- Create a **`.env` file** and configure database credentials:

```ini
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/gardening_db
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
```

### **5️⃣ Run Migrations**
```bash
alembic upgrade head
```

---

## 🏃 Running the API
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
Access **Swagger UI** at:  
📌 [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🔑 Authentication (JWT)
### **Register**
```bash
curl -X 'POST' 'http://localhost:8000/auth/register' \
-H 'Content-Type: application/json' \
-d '{"email": "test@example.com", "password": "securepassword"}'
```

### **Login**
```bash
curl -X 'POST' 'http://localhost:8000/auth/login' \
-H 'Content-Type: application/json' \
-d '{"email": "test@example.com", "password": "securepassword"}'
```
Response:
```json
{
  "access_token": "your_jwt_token",
  "token_type": "bearer"
}
```

---

## 🌿 API Endpoints

### **Auth**
- `POST /auth/register` → Register a new user  
- `POST /auth/login` → Get JWT token  

### **Gardens**
- `POST /gardens/` → Create a new garden  
- `GET /gardens/` → List all gardens  
- `GET /gardens/{garden_id}` → Get garden details  
- `PUT /gardens/{garden_id}` → Update a garden  
- `DELETE /gardens/{garden_id}` → Remove a garden  

### **Plants**
- `GET /plants/` → Get plant database  
- `POST /plants/` → Add a plant to a garden  
- `DELETE /plants/{plant_id}` → Remove a plant  

---

## 🐳 Running with Docker
1. **Build the image**  
```bash
docker-compose up --build
```
2. **Run migrations inside the container**  
```bash
docker exec -it gardening-api alembic upgrade head
```
3. API will be available at:  
📌 `http://localhost:8000`

---

## 🔬 Running Tests
```bash
pytest
```

---

## 🚀 Future Enhancements
- 🌿 **AI-based plant care recommendations**  
- 📆 **Gardening calendar & reminders**  
- 📊 **Advanced analytics for tracking growth trends**  

---

## 🤝 Contributing
Want to contribute? **Fork, create a branch, and submit a PR!** 🚀  

```bash
git checkout -b feature-branch
git commit -m "Added new feature"
git push origin feature-branch
```

---

### **📬 Need Help?**
Reach out via [GitHub Issues](https://github.com/yourusername/gardening-api/issues).  

Happy Coding! 🌱🚀  

