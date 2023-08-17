set sql_safe_updates=0;

delimiter |
create function return_dest_id(dest_name varchar(30),dest_description varchar(255),
image_link varchar(255),max_elevation varchar(255),min_duration varchar(30),
difficulty varchar(30))
returns int deterministic
begin
	declare id int;
    
    insert into destination(dest_name,description,image_link,max_elevation,min_duration,difficulty)
	values (dest_name,dest_description,image_link,max_elevation,min_duration,difficulty);
    
	select dest_id into id
	from destination
    where destination.dest_name=dest_name;
    
return (id);
end|
delimiter ;

delimiter |
create function return_city_id(cname varchar(30),cdescription varchar(255))
returns int deterministic
begin
	declare id int;
    
    insert into city(city_name,city_description)
	values (cname,cdescription);
    
	select city_id into id
	from city
    where city.city_name=cname;
    
return (id);
end|
delimiter ;

delimiter |
create function add_r(rid int,city_id int)
returns int deterministic
begin

    insert into route(route_id,city_id)
	values (rid,city_id);
    
	return rid;
end|
delimiter ;

delimiter |
create procedure add_d_r(dest_id int,route_id int,rname varchar(30),
rdescription varchar(255),rpic varchar(255))
begin

    insert into destination_route(dest_id,route_id,route_name,route_description,route_pic)
	values (dest_id,route_id,rname,rdescription,rpic);

end|
delimiter ;

delimiter |
create procedure add_vp(city_id int,vp_name varchar(30),vp_details varchar(255))
begin

    insert into city_viewpoint(city_id,viewpoint_name,viewpoint_details)
	values (city_id,vp_name,vp_details);

end|
delimiter ;

delimiter |
create procedure add_acc(city_id int,h_name varchar(255),p_no varchar(10),e varchar(50),
p float)
begin

    insert into accomodation(city_id,hotel_name,phone_number,email,price)
	values (city_id,h_name,p_no,e,p);

end|
delimiter ;

delimiter |
create function add_months(m_name varchar(20))
returns int deterministic
begin
	declare mid int;
    insert into months(month_name)
	values (m_name);
    
    select month_id into mid
    from months
    where month_name=m_name;
	return (mid);
end|
delimiter ;

delimiter |
create procedure add_season(dest_id int, month_id int)
begin
	
    insert into season(dest_id,month_id)
	values (dest_id,month_id);
    
end|
delimiter ;

delimiter |
create function add_guide(g_name varchar(30),g_no varchar(10))
returns int deterministic
begin
	declare gid int;
    insert into guide(guide_name,phone_number)
	values (g_name,g_no);
    
    select guide_id into gid
    from guide
    where guide_name=g_name;
	return (gid);
end|
delimiter ;

delimiter |
create procedure add_package(p float,d int,guide_id int ,route_id int,p_name varchar(30),
p_description varchar(255))
begin
	
    insert into packages(price,days,guide_id,route_id,package_name,package_description)
	values (p,d,guide_id,route_id,p_name,p_description);
    
end|
delimiter ;
