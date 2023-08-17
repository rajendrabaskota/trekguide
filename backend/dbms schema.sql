create database trek;
use trek;

create table destination(dest_id int not null auto_increment,
dest_name varchar(30) not null, description varchar(255), image_link varchar(255), 
primary key(dest_id));
alter table destination
add max_elevation varchar(255), 
add min_duration varchar(30),
add difficulty varchar(30);

create table city(city_id int not null primary key auto_increment, 
city_name varchar(30) not null);
alter table city
add city_description varchar(255);

create table route(route_id int not null, city_id int not null,
primary key(route_id,city_id),foreign key(city_id) references city(city_id));

create table destination_route(dest_id int not null, route_id int not null, 
primary key(route_id,dest_id),foreign key(dest_id) references destination(dest_id),
foreign key(route_id) references route(route_id));
alter table destination_route
add route_name varchar(30),
add route_description varchar(255),
add route_pic varchar(255);

create table city_viewpoint(cvp_id int not null auto_increment, viewpoint_name varchar(30) not null,
city_id int not null,primary key(cvp_id),foreign key(city_id) references city(city_id));
alter table city_viewpoint
add viewpoint_details varchar(255);

create table accomodation(acc_id int not null auto_increment, city_id int not null,
hotel_name varchar(255) not null, phone_number varchar(10), email varchar(50), price float, primary key(acc_id));

create table transport_medium(transport_medium_id int not null primary key auto_increment,
transport_medium_name varchar(30) not null);

create table transportation(transport_medium_id int not null,city_id_origin int not null,
city_id_destination int not null, price float, foreign key(transport_medium_id) references transport_medium(transport_medium_id),
foreign key(city_id_origin) references city(city_id),foreign key(city_id_destination) references city(city_id));

create table months(month_id int not null primary key auto_increment,month_name varchar(20) not null);

create table season(dest_id int not null, month_id int not null,foreign key(month_id) references months(month_id),
foreign key(dest_id) references destination(dest_id), primary key(dest_id, month_id));

create table guide(guide_id int not null auto_increment primary key,guide_name varchar(30) not null,
phone_number varchar(10));

create table packages(package_id int not null auto_increment, price float, days int not null, guide_id int not null, route_id int not null, primary key(package_id),
foreign key(guide_id) references guide(guide_id),
foreign key(route_id) references route(route_id));
alter table packages
add package_name varchar(30),
add package_description varchar(255);

create table package_details(package_id int, package_description varchar(255), foreign key(package_id) references packages(package_id),
primary key(package_id, package_description));

create view destination_season as select dest_name, month_name
from season natural join months
natural join destination;

create view package_route as
select guide_name,phone_number,price,days,route_id
from guide natural join packages;

create view destination_route_city as
select dest_name,route_id,city_name
from destination_route natural join destination natural join route natural join city;

create view city_cvp as
select city_name, viewpoint_name
from city natural join city_viewpoint;

create view city_acc as
select city_name, hotel_name, phone_number, email, price
from city natural join accomodation;

select route_id, city_name
from destination_route natural join destination natural join route natural join city
where route_id=1;

select * from destination_route_city;