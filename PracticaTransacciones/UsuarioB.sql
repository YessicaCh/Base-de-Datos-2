$ sudo -u postgres psql
[sudo] password for yessica: 
psql (9.5.14)
Type "help" for help.

postgres=# \c desolation
You are now connected to database "desolation" as user "postgres".
desolation=# BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN
desolation=# update productos SET existencias = 222 where nombre ~* 'Peras';
UPDATE 1
desolation=#
desolation=#       select * from productos where nombre ~* 'Peras';
 id_producto | nombre | existencias 
-------------+--------+-------------
           1 | PERAS  |         222
(1 row)

desolation=# END TRANSACTION;
COMMIT
desolation=# BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN
desolation=# select * from productos where nombre ~* 'Peras';
 id_producto | nombre | existencias 
-------------+--------+-------------
           1 | PERAS  |         222
(1 row)

desolation=# select * from productos where nombre ~* 'Peras';
 id_producto | nombre | existencias 
-------------+--------+-------------
           1 | PERAS  |         222
(1 row)

desolation=# commit;
COMMIT
desolation=# select * from productos where nombre ~* 'Peras';
 id_producto | nombre | existencias 
-------------+--------+-------------
           1 | PERAS  |         333
(1 row)

desolation=# BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN
desolation=# select * from productos where nombre ~* 'Peras';
 id_producto | nombre | existencias 
-------------+--------+-------------
           1 | PERAS  |         333
(1 row)

desolation=#  update productos SET existencias = 555 where nombre ~* 'Peras';
select * from productos where nombre ~* 'Peras';




^[[A^[[A^[[A^CCancel request sent
ERROR:  canceling statement due to user request
CONTEXT:  while updating tuple (0,4) in relation "productos"
desolation=# select * from productos where nombre ~* 'Peras';ERROR:  current transaction is aborted, commands ignored until end of transaction block
desolation=# COMMIT;
ROLLBACK
desolation=# ROLLBACK
desolation-# ;
WARNING:  there is no transaction in progress
ROLLBACK
desolation=# BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN
desolation=# update productos SET existencias = 777 where nombre ~* 'Peras';
^CCancel request sent
ERROR:  canceling statement due to user request
CONTEXT:  while updating tuple (0,4) in relation "productos"
desolation=# UPDATE 1
desolation-# ;
ERROR:  syntax error at or near "1"
LINE 1: UPDATE 1
               ^
desolation=# UPDATE 1
desolation-# select * from productos where nombre ~* 'Peras';
ERROR:  syntax error at or near "1"
LINE 1: UPDATE 1
               ^
desolation=# UPDATE 1
desolation-# select * from productos where nombre ~* 'Peras';ERROR:  syntax error at or near "1"
LINE 1: UPDATE 1
               ^
desolation=# UPDATE 1;
ERROR:  syntax error at or near "1"
LINE 1: UPDATE 1;
               ^
desolation=# UPDATE 1
desolation-# ;
ERROR:  syntax error at or near "1"
LINE 1: UPDATE 1
               ^
desolation=# select * from productos where nombre ~* 'Peras';ERROR:  current transaction is aborted, commands ignored until end of transaction block
desolation=#  BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
ERROR:  current transaction is aborted, commands ignored until end of transaction block
desolation=# commit;
ROLLBACK
desolation=# rollback
desolation-#  BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
ERROR:  syntax error at or near "BEGIN"
LINE 2:  BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
         ^
desolation=# rollback;
WARNING:  there is no transaction in progress
ROLLBACK
desolation=#          
 BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN
desolation=# update productos SET existencias = 777 where nombre ~* 'Peras';
UPDATE 1
desolation=# UPDATE 1
desolation-# select * from productos where nombre ~* 'Peras';      ERROR:  syntax error at or near "1"
LINE 1: UPDATE 1
               ^
desolation=# select * from productos where nombre ~* 'Peras';ERROR:  current transaction is aborted, commands ignored until end of transaction block
desolation=# select * from productos where nombre ~* 'Peras';
ERROR:  current transaction is aborted, commands ignored until end of transaction block
desolation=# select * from productos where nombre ~* 'Peras';
ERROR:  current transaction is aborted, commands ignored until end of transaction block
desolation=# ROLLBACK;
ROLLBACK
desolation=# select * from productos where nombre ~* 'Peras';
 id_producto | nombre | existencias 
-------------+--------+-------------
           1 | PERAS  |         333
(1 row)

desolation=#                                                         BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN
desolation=# update productos SET existencias = 777 where nombre ~* 'Peras';
UPDATE 1
desolation=# select * from productos where nombre ~* 'Peras';
 id_producto | nombre | existencias 
-------------+--------+-------------
           1 | PERAS  |         777
(1 row)

desolation=# COMMIT;
COMMIT
desolation=# BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN
desolation=# update productos SET existencias = 888 where nombre ~* 'Peras';
UPDATE 1
desolation=# 
desolation=# 
ABORT           DELETE FROM     LOCK            SELECT
ALTER           DISCARD         MOVE            SET
ANALYZE         DO              NOTIFY          SHOW
BEGIN           DROP            PREPARE         START
CHECKPOINT      END             REASSIGN        TABLE
CLOSE           EXECUTE         REFRESH         TRUNCATE
CLUSTER         EXPLAIN         REINDEX         UNLISTEN
COMMENT         FETCH           RELEASE         UPDATE
COMMIT          GRANT           RESET           VACUUM
COPY            IMPORT          REVOKE          VALUES
CREATE          INSERT          ROLLBACK        WITH
DEALLOCATE      LISTEN          SAVEPOINT       
DECLARE         LOAD            SECURITY LABEL  
desolation=# 
ABORT           DELETE FROM     LOCK            SELECT
ALTER           DISCARD         MOVE            SET
ANALYZE         DO              NOTIFY          SHOW
BEGIN           DROP            PREPARE         START
CHECKPOINT      END             REASSIGN        TABLE
CLOSE           EXECUTE         REFRESH         TRUNCATE
CLUSTER         EXPLAIN         REINDEX         UNLISTEN
COMMENT         FETCH           RELEASE         UPDATE
COMMIT          GRANT           RESET           VACUUM
COPY            IMPORT          REVOKE          VALUES
CREATE          INSERT          ROLLBACK        WITH
DEALLOCATE      LISTEN          SAVEPOINT       
DECLARE         LOAD            SECURITY LABEL  
desolation=# 
ABORT           DELETE FROM     LOCK            SELECT
ALTER           DISCARD         MOVE            SET
ANALYZE         DO              NOTIFY          SHOW
BEGIN           DROP            PREPARE         START
CHECKPOINT      END             REASSIGN        TABLE
CLOSE           EXECUTE         REFRESH         TRUNCATE
CLUSTER         EXPLAIN         REINDEX         UNLISTEN
COMMENT         FETCH           RELEASE         UPDATE
COMMIT          GRANT           RESET           VACUUM
COPY            IMPORT          REVOKE          VALUES
CREATE          INSERT          ROLLBACK        WITH
DEALLOCATE      LISTEN          SAVEPOINT       
DECLARE         LOAD            SECURITY LABEL  
desolation=# 
ABORT           DELETE FROM     LOCK            SELECT
ALTER           DISCARD         MOVE            SET
ANALYZE         DO              NOTIFY          SHOW
BEGIN           DROP            PREPARE         START
CHECKPOINT      END             REASSIGN        TABLE
CLOSE           EXECUTE         REFRESH         TRUNCATE
CLUSTER         EXPLAIN         REINDEX         UNLISTEN
COMMENT         FETCH           RELEASE         UPDATE
COMMIT          GRANT           RESET           VACUUM
COPY            IMPORT          REVOKE          VALUES
CREATE          INSERT          ROLLBACK        WITH
DEALLOCATE      LISTEN          SAVEPOINT       
DECLARE         LOAD            SECURITY LABEL  
desolation=# 
ABORT           DELETE FROM     LOCK            SELECT
ALTER           DISCARD         MOVE            SET
ANALYZE         DO              NOTIFY          SHOW
BEGIN           DROP            PREPARE         START
CHECKPOINT      END             REASSIGN        TABLE
CLOSE           EXECUTE         REFRESH         TRUNCATE
CLUSTER         EXPLAIN         REINDEX         UNLISTEN
COMMENT         FETCH           RELEASE         UPDATE
COMMIT          GRANT           RESET           VACUUM
COPY            IMPORT          REVOKE          VALUES
CREATE          INSERT          ROLLBACK        WITH
DEALLOCATE      LISTEN          SAVEPOINT       
DECLARE         LOAD            SECURITY LABEL  
desolation=#       Commit;
COMMIT
desolation=# 

