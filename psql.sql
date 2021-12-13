CREATE TABLE person (
	name varchar(30),
	uni varchar(10) unique not NULL,
	email varchar(50),
	Primary key (email)
);

CREATE TABLE diningHall (
id Serial,
	Primary key (id),
	name varchar(20)
);

CREATE TABLE foodItem (
	foodItemID Serial,
	foodName varchar(50) unique,
	imageURL varchar(200),
	Primary key (foodItemID),
	diningHall int references diningHall(id)
);

CREATE TABLE Review (
	reviewID Serial,
	text varchar(200),
	rating int,
	uni varchar(10),
	date timestamp,
	foodItemId int,
	Foreign key (foodItemId) references foodItem(foodItemId),
	Foreign key (uni) references person(uni),
	Primary key (reviewID)
);

insert into diningHall (name) values ('Ferris');
insert into diningHall (name) values ('John Jay');
insert into diningHall (name) values ('JJs');

insert into person(name, uni, email) values ('Ivan Chau', 'ic2504', 'ic2504@columbia.edu');




