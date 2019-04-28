


SET ECHO OFF
SET FEEDBACK OFF
SET VERIFY OFF
SET DEFINE ON
SET HEADING OFF

-- prompt user
ACCEPT basket_date varchar2(10) PROMPT 'Enter Date like: 15-May-02'
PROMPT



-- declare basket_date variable and set it to date you want, lets say Mar 15 2002
i  
var basket_date varchar2(10);

exec :basket_date := '14-MAR-02';

-- set the instruments you're interested in to what you want, below in
-- the line that says 
-- ins.symbol in ('MU', 'BBY', 'AES')

-- if the columns you're getting are too wide, format them to desired width, say
-- to set width of the column "basket_name" to 30 chars

col basket_name format a10
col side format a10
col symbol format a10
col shares_filled format a10
col price_filled format a10
col timestamp format a10
set newpage none

-- misc crap
-- break on basket_name  to take the pagebreak out
-- env set...SQLPATH so that it knows where to go look for scripts
-- show all ( for show all options
-- set pagesize (100/2000) whatever
-- spool filename (to apend /write the output of the sql stuff too)
-- set linesize 500(to give the result set of the query in one line



ddm all_tables
/





select
  eb.internal_desc basket_name,
  es.name side,
  ins.symbol,
  formatting_utils.format_integer(ef.shares_filled) shares_filled,
  formatting_utils.format_money_str(1, 2, ef.price_filled) price_filled,
  to_char(ef.order_attribs__timestamp, 'hh24:mi:ss') timestamp
from
  gelusa.g_exec_basket eb,
  gelusa.g_exec_wave ew,
  db_ge_side es,
  gelusa.g_exec_fill ef,
  gelusa.g_ins ins
where
  eb.basket_attribs__timestamp between to_date(:basket_date) and to_date(:basket_date) + 1 and
  eb.basket_attribs__is_removed = 0 and
  ew.gemsexecbasket_parent = eb.key and
  ew.basket_attribs__is_removed = 0 and
  ef.gemsexecwave_parent = ew.key and
  ef.order_attribs__is_removed = 0 and
  ef.order_attribs__ins_key = ins.key and
  ( ef.message_type is null or
    ef.message_type in (0, 3) ) and
  ins.gel_datestamp = to_date(:basket_date) and
  ins.symbol in ('HIBB') and
  es.value = eb.side
order by
  basket_name,
  side,
  symbol,
  timestamp,
  shares_filled,
  price_filled
/



select * from smtm_user
where name = 'SCHAO'
/

desc smtm_user;

set pagesize 10
select object_name from all_objects
where owner = 'SMTM'
/

