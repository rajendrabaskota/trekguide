delimiter |
create procedure add_whole_data(
dest_name varchar(30),dest_description varchar(255),image_link varchar(255),
max_elevation varchar(255),min_duration varchar(30),difficulty varchar(30),
city_name varchar(30),city_description varchar(255),
r_id int,
route_name varchar(30),route_description varchar(255),route_pic varchar(255),
vp_name varchar(30),vp_details varchar(255),
hotel_name varchar(255),hotel_phone_no varchar(10),hotel_email varchar(50),acc_price float,
month_name varchar(20),
guide_name varchar(30),guide_no varchar(10),
package_price float,days int,package_name varchar(30),package_description varchar(255))
begin
    declare dest_id int;
    declare route_id int;
    declare city_id int;
    declare month_id int;
    declare guide_id int;
    
    select return_dest_id(dest_name,dest_description,image_link,max_elevation,min_duration,difficulty) into dest_id;
    select return_city_id(city_name,city_description) into city_id;
    select add_r(r_id,city_id) into route_id;
    call add_d_r(dest_id,route_id,route_name,route_description,route_pic);
    call add_vp(city_id,vp_name,vp_details);
    call add_acc(city_id,hotel_name,hotel_phone_no,hotel_email,acc_price);
    select add_months(month_name) into month_id;
    call add_season(dest_id,month_id);
    select add_guide(guide_name,guide_no) into guide_id;
    call add_package(package_price,days,guide_id,route_id,package_name,package_description);
end|
delimiter ;


call add_whole_data(
"Tilicho trek","Tilicho Lake is a lake located in the Manang district of Nepal.",
 "https://upload.wikimedia.org/wikipedia/commons/4/4c/Tilicho_Lake.jpg",
 "4949M","6 Days","Moderate",
"Manang","It is situated in the broad valley of the Marshyangdi River to the north of the Annapurna mountain range. 
",
1,
"Trecherous Path",
"Tilicho Lake trek is a journey to the world’s highest glacial lake Tilicho with an altitude of 4949 meters. Tlicho lake is part of Annapurna circuit trek and one of the best sight treks. Often trekkers do it when they are doing Annapurna circuit 
trek ",
"https://www.nepalmotherhousetreks.com/uploads/package/gallery/tilicho-lake-trail.jpg",
"Ice lake","Lake situated at the base of a snowy peak at 4600M",
"manang homestay","986562655","kasutub@gmail.com",1000,
"September",
"Aashish Pant","98625120",
"15000",7,"Economy","ramro package");

select return_city_id("Tilicho lake","Regarded as one of the highest lakes in the world, 
it rests in the stunning location in the Annapurna region at an altitude of 5,000 meters.
") as id;
select add_r(1,8) as id;
call add_vp(8,"lake,mountains","the vast lake and the glorous mountains are a sight to behold");
call add_acc(8,"homestay","986562655","kasutub@gmail.com",1000);

insert into package_details(package_id,package_description)
values (2,"Day 1: Besisahar"),
(2,"Day 2: Manang"),
(2,"Day 3: Shree Kharka")
,(2,"Day 4: Tilicho BAse Camp"),
(2,"Day 5: Return to shree kharka after visiting the lake"),
(2,"Day 6: Return Manang"),
(2,"Day 7: Return Home");

select * from destination;
select * from city;
select * from route;
select * from destination_route;
select * from city_viewpoint;
select * from accomodation;
select * from months;
select * from season;
select * from guide;
select * from packages;