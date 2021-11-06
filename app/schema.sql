drop table if exists contact;
create table contact (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    EMAIL TEXT NOT NULL
)