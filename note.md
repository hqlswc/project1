### RMAN

`SQL> select * from v$backup_async_io;`

#### BlockRecover check 
`Shell> dbv file=users.dbf blocksize=8192`
#### BlockRecover repair
`Shell> blockrecover datafile <datafile number> block <block number>`

#### Validate datebase
`RMAN> backup validate database;`
