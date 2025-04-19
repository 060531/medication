import os

class Config:
    # ใช้ SQLite สำหรับพัฒนา พอขึ้น production เปลี่ยนเป็น Postgres/MySQL ตามต้องการ
    import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'sqlite:///' + os.path.join(basedir, 'app.db')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
