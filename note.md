### RMAN

`SQL> select * from v$backup_async_io;`

#### Corrupt DB block manually
`Shell> dd of=users.dbf bs=8192 conv=notrunc seek=139<<EOF`<br>
`xxx`<br>
`EOF`<br>

#### BlockRecover check 
`Shell> dbv file=users.dbf blocksize=8192`
#### BlockRecover repair
`Shell> blockrecover datafile <datafile number> block <block number>`

#### Validate datebase
`RMAN> backup validate database;`

#### Check DB corrupt block
`SQL> select * from v$database_block_corruption;`

#### Good post about block corruption
https://expertoracle.com/2018/03/10/physical-and-logical-block-corruption-in-oracle-database/

#### RMAN Recovery Advisor
`RMAN> list failure;`<br>
`RMAN> list failure <Failure ID> detail;`<br>
`RMAN> advise failure;`<br>
`RMAN> repair failure preview;`<br>
`RMAN> repair failure;`<br>
`RMAN> change failure all closed;`<br>
