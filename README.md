
## Frontend .env
NEXT_PUBLIC_API_URL=http://localhost:8000

## Backend .env
### App
ENV=development
### Database (LOCAL Postgres)
DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/sitesage
### OpenAI
OPENAI_API_KEY=sk-proj-

## With docker 
```bash
git clone
docker compose up
```

```bash
docker compose up --build
or 
docker compose down -v
docker compose build --no-cache
docker compose up
```

## Backend commands
```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Frontend commands
```bash
npm i
npm run dev
```