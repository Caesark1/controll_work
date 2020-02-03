select firstname, lastname from developers where birth_date < "1995" and sex = "Male";


select firstname, lastname from project_manager union select lastname,firstname from developers;


select * from project_manager inner join developers on developers.manager_id = manager.id where project_manager.firstname = "Albert";


select * from developers inner join projects_developers on developers.id = projects.id;



select firstname, lastname from developers where birth_date > "1995";


select count(sex) from developers;


select birth_date as year from developers where birth_date > "1995" order by birth_date;

select firstname, count(firstname) from developers where sex = "female" group by firstname;
