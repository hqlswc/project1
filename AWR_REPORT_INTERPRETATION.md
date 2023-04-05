## AWR REPORT INTERPRETATION

#### DB Time
The time used by the database sessions and processes during the period. For example, if there are 4 CPUs, then in 1 hour of elapsed time, there is maximum 240(4*60) minutes of DB time.

#### Host CPU
It is reflecting the CPU usage on the whole machine.

#### Instance CPU
It is reflecting the CPU usage by the instance itself.

#### Event : CPU + Wait for CPU
This wait show the time spent in the CPU run queue

#### Top Timed Foreground Events
It is ordered by percentage of the total database time used, the high percentage means it using the most database resource.

#### Parse calls
it is request to parse the SQL statement that have been presented to the database.

#### User calls
The call to the database by user sessions, Parse calls are subset of the user calls.

#### SQL ordered by Parse Calls
This lists SQL which has had the most parse calls (ie soft parses or hard parses)


