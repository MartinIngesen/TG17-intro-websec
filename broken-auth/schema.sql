drop table if exists users;
create table users (
    id integer primary key autoincrement,
    username text not null,
    password not null
);
insert into users (username, password) VALUES ('admin', 'admin');
insert into users (username, password) VALUES ('user', 'user');
