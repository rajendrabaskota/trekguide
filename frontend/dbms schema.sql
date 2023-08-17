create database trek;
use trek;

create table destination( dest_id int not null auto_increment,
dest_name varchar(30) not null,primary key(dest_id),dest_description varchar(200));

create table city(city_id int not null primary key auto_increment, 
city_name varchar(30) not null); 

create table route(route_id int not null, city_id int not null ,
primary key(route_id,city_id),foreign key(city_id) references city(city_id));

create table destination_route(dest_id int not null, route_id int not null, 
primary key(route_id,dest_id),foreign key(dest_id) references destination(dest_id),
foreign key(route_id) references route(route_id));

create table city_viewpoint(cvp_id int not null auto_increment, viewpoint_name varchar(30) not null, 
city_id int not null,primary key(cvp_id,city_id),foreign key(city_id) references city(city_id));

create table accomodation(acc_id int not null auto_increment, city_id int not null,primary key(acc_id,city_id),
hotel_name varchar(30) not null, phone_number integer(10),email varchar(50),price float not null );  

create table transport_medium(transport_medium_id int not null primary key auto_increment,
transport_medium_name varchar(30) not null);

create table transportation(transport_medium_id int not null,city_id_origin int not null,
city_id_destination int not null,foreign key(transport_medium_id) references transport_medium(transport_medium_id),
foreign key(city_id_origin) references city(city_id),foreign key(city_id_destination) references city(city_id),
price float not null);

create table months(month_id int not null primary key auto_increment,month_name varchar(20) not null);

create table season(dest_id int not null, month_id int not null,foreign key(month_id) references months(month_id));

create table guide(guide_id int not null auto_increment primary key,guide_name varchar(30) not null,
phone_number integer(10),dest_id int not null,foreign key(dest_id) references destination(dest_id));

create table packages(package_id int not null,guide_id int not null,primary key(package_id,guide_id),
foreign key(guide_id) references guide(guide_id),days int not null,price float not null,route_id int not null,
foreign key(route_id) references route(route_id));



