import os


def database_url() -> str:
    return (
        f"postgresql://{os.getenv('DB_USER', 'shop')}:{os.getenv('DB_PASS', 'shop')}"
        f"@{os.getenv('DB_HOST', 'db')}:{os.getenv('DB_PORT', '5432')}"
        f"/{os.getenv('DB_NAME', 'shop')}"
    )
