#!/db/bin/perl
use strict;
use Data::Dumper;
use DBI;

$"="\n";
$ENV{ORACLE_HOME}    ='/db/pub/infra/ORCLclnt/product/8.1.7';
$ENV{PATH}           ="$ENV{'ORACLE_HOME'}/bin:$ENV{'PATH'}";
$ENV{LD_LIBRARY_PATH}="$ENV{'ORACLE_HOME'}/lib:$ENV{'LD_LIBRARY_PATH'}";

my $db		     ="smtm";
my $login            ="mabutali";
my $pass             ="mabutali";

my $dbh             = DBI->connect("dbi:Oracle:$db", $login, $pass) || 
	               die("Can't connect to Oracle : $!\n");


print "Enter sql statement -- Enter END to exit\n";
my $fetch;
my $sqlstmt=<STDIN>; chomp($sqlstmt);
my $tmp;
while ($sqlstmt) {

	   $fetch  = $dbh->prepare("$sqlstmt"); 
	   $tmp=$sqlstmt;
	   $fetch->execute;

	my(@rics, $count);
	while (my(@ric) = $fetch->fetchrow_array){
		print  join (',',@ric);
		print "\n";
	}		
	print "Enter sql statement -- Enter END to exit\n";
        $sqlstmt=<STDIN>; chomp($sqlstmt);

	if ($sqlstmt =~ /END/) {
		$fetch->finish;
		$fetch->disconnect;
		exit;
	}
        elsif ($sqlstmt eq "foo") {
		chomp($tmp);
		print $tmp;
       	 $sqlstmt=<STDIN>; chomp($sqlstmt);
	}
}

#-- This works
#my $fetch  = $dbh->prepare("select * from GELUSA.gq_order"); 


