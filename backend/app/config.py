from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://inventory_db_qeuc_user:KIbkMkE0dr2P8i4tNR3hPHdpmIANEZP8@dpg-d8ojbm77f7vs73eqs950-a.ohio-postgres.render.com/inventory_db_qeuc"
    FRONTEND_URL: str = "http://localhost:3000"

    class Config:
        env_file = ".env"

settings = Settings()
