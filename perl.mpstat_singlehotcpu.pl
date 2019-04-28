# 
# We cycle # thru the vmstat output piped into awk and grab the %usr 
# command output  mpstat -P ALL
# If we have a a single hot cpu then we have an issue
#mpstat -P ALL |awk '{print $3" "$4}' |xargs |sed -e "s/ /|/g"
#(centos7-Master)|02/16/2019|CPU|%usr|all|0.50|0|0.45|1|0.56
#[zesham2@centos7-Master SupportGeneric]$
#
