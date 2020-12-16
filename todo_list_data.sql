BEGIN TRANSACTION;
insert into Student values (201801764,"201801764", '최준혁');
insert into Student values (201601798,"201601798", '최재이' );
insert into Student values (201601787,"201601787",'이승수' );


insert into Class values (1770001,30,"데이터베이스");
insert into Class values (6836001,30,"네트워크구조및설계");
insert into Class values (9494001,10,"제어시스템");

insert into Sugang VALUES (201801764,1770001);
insert into Sugang VALUES (201601787,1770001);
insert into Sugang VALUES (201601798,1770001);
insert into Sugang VALUES (201801764,6836001);
insert into Sugang VALUES (201601787,6836001);
insert into Sugang VALUES (201601798,6836001);
insert into Sugang VALUES (201801764,9494001);

insert into VideoAndHomework values (1770001,201801764 , '학기프로젝트', 7, 'N');
insert into VideoAndHomework values (6836001,201801764 ,'네트워크14-1 ', 5, 'N');
insert into VideoAndHomework values (6836001,201801764 ,'네트워크14-2 ', 5, 'N');
insert into VideoAndHomework values (6836001, 201801764,'네트워크14-3 ', 5, 'N');
insert into VideoAndHomework values (9494001,201801764 ,'5장 과제', 3, 'N');
insert into VideoAndHomework values (9494001,201801764 ,'7장 과제', 10,  'N');
insert into VideoAndHomework values (9494001,201801764 ,'제어 7장 Lead_lag(1)' ,4 ,  'N');
insert into VideoAndHomework values (9494001,201801764 ,'제어 7장 Lead_lag(2)', 4,   'N');

insert into VideoAndHomework values (1770001,201601787 , '학기프로젝트', 7,  'N');
insert into VideoAndHomework values (6836001,201601787 ,'네트워크14-1 ', 5,  'N');
insert into VideoAndHomework values (6836001, 201601787,'네트워크14-2 ', 5, 'N');
insert into VideoAndHomework values (6836001,201601787 ,'네트워크14-3 ', 5, 'N');


insert into VideoAndHomework values (1770001,201601798 , '학기프로젝트', 7, 'N');
insert into VideoAndHomework values (6836001,201601798 ,'네트워크14-1 ', 5, 'N');
insert into VideoAndHomework values (6836001,201601798 ,'네트워크14-2 ', 5, 'N');
insert into VideoAndHomework values (6836001,201601798 ,'네트워크14-3 ', 5,  'N');
COMMIT;
