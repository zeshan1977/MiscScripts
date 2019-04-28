#!/nw/dev/usr/bin/perl 
use strict;
use IO::File;
use Fatal qw(open);
use Env;
use File::Basename;
use Date::Manip;
use vars qw ($k $v $tlw $o $ofh $ffh);
use Data::Dumper;
#
#Das ist mein FIX Parser ja
#

while (<>) {
    my $l = {map {($k, $v) = split (/=/,$_); (lc($k),$v)} grep {/.=./} split(/:/,$_)};


    #next if $l->{mt}=~/A|X|J/i;

    if ($l->{mt} =~/R/i) {
    for my $f (qw(bskn upriv bn sy sh x xp ttim)) {

        if ($f eq "ttim"){
	   $l->{$f}=scalar localtime($l->{$f});
	}
        printf ("%-15s",$l->{$f});
	$tlw->{$l->{mt}}->{$l->{oid}}->{$l->{id}}->{$f}=$l->{$f};
	if ($l->{mt} eq 'O') {
	    $o->{$l->{oid}}->{$f}=$l->{$f};
	}
        
    }
    print "\n";
    
#    warn "Message: ".$l->{mt}." Order: ".$l->{oid}." fill: ".$l->{id}." Symbol: ".$l->{sy}. " Qty: ".$l->{sh};
   } 
}
#warn Dumper($tlw);

    #next if ($l->{mt} !~ /R/i && length($l->{xp})) ;
