
def test_fetch_data_from_database(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    print(result)

    assert result is not None


