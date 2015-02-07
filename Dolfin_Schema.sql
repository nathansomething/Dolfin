create database if not exists dolfin;


create table USER (
	ID int primary key auto_increment,
    EMAIL varchar(250) not null unique,
    PASSWORD varchar(1000) not null
);

create table TOPIC (
	ID int primary key auto_increment,
	NAME varchar(250) not null unique,
    PARENT int,
    foreign key(PARENT) references TOPIC(ID)
);

create table USER_TOPIC (
	TIME_OF_DAY int not null default 12,
    NUM_PER_DAY int not null default 4,
    USER_ID int not null,
    TOPIC_ID int not null,
    NUM_CORRECT int not null default 0,
    foreign key (USER_ID) references USER(ID),
    foreign key (TOPIC_ID) references TOPIC(ID),
    primary key (USER_ID, TOPIC_ID)
);



