import psycopg2


conn = None

# Get information from base
def get_base():
    conn = psycopg2.connect(database="postgres", user="postgres", password="kostyazhuk")
    cur = conn.cursor()
    cur.execute("""
        SELECT
            user_id
        FROM
            state
        """,
        )
    # I'm not sure, but I hope, that we've got list of id_users
    id_row = cur.fetchall()
    print(id_row)
    id_row_norm = []
    for i in id_row:
        id_row_norm.append(i[0])
    cur.close()
    print(id_row_norm)
    full_full_row = []
    # get list of dicts. key is user_id mean is list of [user_id, user_name, right_tries, wrong_tries]. I hope
    cur = conn.cursor()
    for ii in id_row_norm:
        cur.execute("""
                SELECT
                    user_id, user_name, right_tries, wrong_tries
                FROM
                    state 
                WHERE
                    user_id=%s
                """,
                (ii,))
        full_row_1 = cur.fetchone()
        print(full_row_1)
        full_row = {full_row_1[0]: [full_row_1[1], full_row_1[2], full_row_1[3]]}
        full_full_row.append(full_row)
        print(full_full_row)
    cur.close()

    return full_full_row

