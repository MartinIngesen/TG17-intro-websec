drop table if exists users;
create table users (
    id integer primary key autoincrement,
    username text not null,
    password not null,
    description text not null
);

insert into users (username, password, description) VALUES ('admin', 'admin', 'Hello!, I am the admin!');
insert into users (username, password, description) VALUES ('user', 'user', 'I am the user!');
