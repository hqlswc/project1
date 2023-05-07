### RMAN

`SQL> select * from v$backup_async_io;`

#### Corrupt DB block
`Shell> dd of=users.dbf bs=8192 conv=notrunc seek=139 <<EOF
XXX
EOF`

#### BlockRecover check 
`Shell> dbv file=users.dbf blocksize=8192`
#### BlockRecover repair
`Shell> blockrecover datafile <datafile number> block <block number>`

#### Validate datebase
`RMAN> backup validate database;`
