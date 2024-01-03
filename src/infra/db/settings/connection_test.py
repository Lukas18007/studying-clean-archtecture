import pytest
from .connection import DBConnectionHandler

@pytest.mark.skip(reason="Sensive test")
def test_create_database_engine():
    db_connection_handle = DBConnectionHandler()

    engine = db_connection_handle.get_engine()

    conn = engine.connect()

    assert engine is not None
    assert conn is not None