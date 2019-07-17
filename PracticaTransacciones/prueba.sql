desolation=# BEGIN TRANSACTION ISOLATION
desolation-# LEVEL SERIALIZABLE;
BEGIN
desolation=# update productos 
desolation-# set existencias = 888
desolation-# where nombre ~* 'Peras'; 
UPDATE 1
desolation=# commit
desolation-# ;
COMMIT
desolation=#
