# rate variable
select @perkm = 1;

# station table
create table station(
	scode varchar(15) not null,
    sname varchar(100),
    slocation varchar(100),
    primary key (scode)
);


# Route table
create table route(
	rid int not null check(rid>0),
    start_scode varchar(20) not null,
    dest_scode varchar(20) not null,
    distance int,
    arr_time time,
    depart_time time,
    name varchar(20),
    primary key (rid),
    foreign key (start_scode) references station(scode) on delete cascade,
    foreign key (dest_scode) references station(scode) on delete cascade
);

# bus table
create table bus(
	bid int,
    name varchar(100),
    numplate varchar(20),
    type varchar(20),
    model int,
    seates int,
    rid int,
    scode varchar(20) ,
    primary key (bid),
    foreign key (scode) references station(scode) on delete set null,
    foreign key (rid) references route(rid) on delete set null    
);

# employee table
create table employee(
	eid int,
    name varchar(50),
    designation varchar(20),
    bid int,
    scode varchar(15),
    salary int,
    primary key (eid),
    foreign key (bid) references bus(bid) on delete set null,
    foreign key (scode) references station(scode) on delete set null
);


create table bushaults(
	rid int,
    start varchar(20) not null,
    end varchar(20) not null,
    primary key (rid)
);

create table ticket(
	tid int,
    bid int,
    rid int,
    fare float,
    pass_name varchar(50),	
    pass_mobno varchar(50),
    age int,
    gender varchar(10),
    start varchar(20),
    end varchar(20),
    tdate date,
    timestamp time,
    primary key (tid),
    foreign key (bid) references bus (bid) on delete set null,
    foreign key (rid) references route(rid) on delete set null
);


 ;

