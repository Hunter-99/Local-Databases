import pandas as pd

from utils.postgres import get_pg_conn


def main():
    df = pd.read_parquet('migrations.parquet', engine='fastparquet')
    df.to_sql(
        name='migrations',
        con=get_pg_conn(),
        if_exists='replace',
        index=False
    )


if __name__ == '__main__':
    main()