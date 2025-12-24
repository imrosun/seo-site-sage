from alembic import context
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig
import os

from app.db.base import Base  # import models

config = context.config

# Logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Inject DATABASE_URL from Railway
database_url = os.getenv("DATABASE_URL")
if not database_url:
    raise RuntimeError("DATABASE_URL is not set")

config.set_main_option("sqlalchemy.url", database_url)

target_metadata = Base.metadata
