drop table if exists users;
create table users (
    id integer primary key autoincrement,
    username text not null,
    password not null
);
insert into users (username, password) VALUES ('user', 'user');
insert into users (username, password) VALUES ('admin', 'admin');


drop table if exists guestbook;
create table guestbook (
    id integer primary key autoincrement,
    entry text not null
);
insert into guestbook (entry) VALUES ('Such code, much hacker!');
insert into guestbook (entry) VALUES ('OMG liksom! Bare #TG17 hype much!');
