import os
from ttutils.TTConfigHandler import confighandler

conf_dir = os.environ.get("CONF_DATA", "../conf")
conf_filename = os.path.join(conf_dir, 'app-conf.yml')
confighandler.load_config(conf_filename)

from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

from api.dbutils.database import Base
from api.dbutils import models
# from api.core import config as service_config
from datetime import datetime
from ttutils.TTConfigHandler import confighandler

DB_CON_STRING_ASSIGNMENT = confighandler.get_config("DB_CON_STRING_ASSIGNMENT", "")
# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config
# this will overwrite the ini-file sqlalchemy.url path with the path given in the config 
config.set_main_option('sqlalchemy.url', DB_CON_STRING_ASSIGNMENT)
config.set_main_option('file_template', datetime.now().strftime("%Y%m%d%H%M%S"))
config.set_main_option('script_location', './alembic')

# Interpret the config file for Python logging.
# This line sets up loggers basically.
# fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
