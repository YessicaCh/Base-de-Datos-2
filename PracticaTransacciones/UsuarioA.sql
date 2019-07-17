sudo -u postgres psql
[sudo] password for yessica: 
psql (9.5.14)
Type "help" for help.

postgres=# drop database desolation
postgres-# create database desolation;
ERROR:  syntax error at or near "create"
LINE 2: create database desolation;
        ^
postgres=# drop database desolation;
DROP DATABASE
postgres=# drop database desolation;
ERROR:  database "desolation" does not exist
postgres=# create database desolation;
CREATE DATABASE
postgres=# \c desolation
You are now connected to database "desolation" as user "postgres".
desolation=# create table productos (
desolation(# 
desolation(#   id_producto serial primary key,
desolation(# 
desolation(#   nombre text,
desolation(# 
desolation(#   existencias integer
desolation(# 
desolation(# );
CREATE TABLE
desolation=# 
desolation=# insert into productos (nombre,existencias) values
desolation-# 
desolation-# ('PERAS', 111),
desolation-# 
desolation-# ('UVAS', 999);
INSERT 0 2
desolation=# select * from productos
desolation-# ;
 id_producto | nombre | existencias 
-------------+--------+-------------
           1 | PERAS  |         111
           2 | UVAS   |         999
(2 rows)

desolation=# BEGIN TRANSACTION ISOLATION LEVEL READ COMMITTED;
BEGIN
desolation=# select * from productos where nombre ~* 'Peras';
 id_producto | nombre | existencias 
-------------+--------+-------------
           1 | PERAS  |         111
(1 row)

desolation=# select * from productos where nombre ~* 'Peras';
 id_producto | nombre | existencias 
-------------+--------+-------------
           1 | PERAS  |         111
(1 row)

desolation=# select * from productos where nombre ~* 'Peras';
 id_producto | nombre | existencias 
-------------+--------+-------------
           1 | PERAS  |         222
(1 row)

desolation=# update productos SET existencias = 333 
desolation-# where nombre ~* 'peras';
UPDATE 1
desolation=# COMMIT;
COMMIT
desolation=# BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN
desolation=# update productos SET existencias = 444 
desolation-# 
desolation-# where nombre ~* 'Peras';
UPDATE 1
desolation=# select * from productos where nombre ~* 'Peras';
 id_producto | nombre | existencias 
-------------+--------+-------------
           1 | PERAS  |         444
(1 row)

desolation=# COMMIT
desolation-# BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
ERROR:  syntax error at or near "BEGIN"
LINE 2: BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
        ^
desolation=# COMMIT;
ROLLBACK
desolation=# ROLLBACK
desolation-# COMMIT 
BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
ERROR:  syntax error at or near "COMMIT"
LINE 2: COMMIT
        ^
desolation=#         
BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN
desolation=# update productos SET existencias = 666 
desolation-# 
desolation-# where nombre ~* 'Peras';
UPDATE 1
desolation=# 
desolation=# select * from productos where nombre ~* 'Peras';
 id_producto | nombre | existencias 
-------------+--------+-------------
           1 | PERAS  |         666
(1 row)

desolation=# ROLLBACK
desolation-# ;
ROLLBACK
desolation=# rollback
desolation-# ;
WARNING:  there is no transaction in progress
ROLLBACK
desolation=# select * from productos where nombre ~* 'Peras';
 id_producto | nombre | existencias 
-------------+--------+-------------
           1 | PERAS  |         333
(1 row)

desolation=# BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN
desolation=# update productos SET existencias = 666 
desolation-# 
desolation-# where nombre ~* 'Peras';
UPDATE 1
desolation=# 
desolation=# select * from productos where nombre ~* 'Peras';
 id_producto | nombre | existencias 
-------------+--------+-------------
           1 | PERAS  |         666
(1 row)

desolation=# rollback;
ROLLBACK
desolation=# select * from productos where nombre ~* 'Peras';
 id_producto | nombre | existencias 
-------------+--------+-------------
           1 | PERAS  |         333
(1 row)

desolation=# COMMIT
desolation-# ROLLBACK
desolation-# rollback;
ERROR:  syntax error at or near "ROLLBACK"
LINE 2: ROLLBACK
        ^
desolation=# COMMIT;
WARNING:  there is no transaction in progress
COMMIT
desolation=# COMMIT;
WARNING:  there is no transaction in progress
COMMIT
desolation=# ROLLBACK
desolation-# ;
WARNING:  there is no transaction in progress
ROLLBACK
desolation=# select * from productos where nombre ~* 'Peras';
 id_producto | nombre | existencias 
-------------+--------+-------------
           1 | PERAS  |         333
(1 row)

desolation=# BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN
desolation=# update productos SET existencias = 666 
where nombre ~* 'Peras';
UPDATE 1
desolation=# select * from productos where nombre ~* 'Peras';
 id_producto | nombre | existencias 
-------------+--------+-------------
           1 | PERAS  |         666
(1 row)

desolation=# ROLLBACK
desolation-# ;
ROLLBACK
desolation=# select * from productos where nombre ~* 'Peras';
 id_producto | nombre | existencias 
-------------+--------+-------------
           1 | PERAS  |         333
(1 row)

desolation=# select * from productos where nombre ~* 'Peras';
 id_producto | nombre | existencias 
-------------+--------+-------------
           1 | PERAS  |         777
(1 row)

desolation=# BEGIN TRANSACTION ISOLATION LEVEL READ COMMITTED;
BEGIN
desolation=# select * from productos where existencias > 800;
 id_producto | nombre | existencias 
-------------+--------+-------------
           2 | UVAS   |         999
(1 row)

desolation=# select * from productos where existencias > 800;
 id_producto | nombre | existencias 
-------------+--------+-------------
           2 | UVAS   |         999
           1 | PERAS  |         888
(2 rows)

