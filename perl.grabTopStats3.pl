#!/bin/env perl

# Quick little thing
# to grab and keep stats of space and other things chronologically
# so we can pump the output to excel and then graph it out
#
# Will make this into a neat little general purpose util with env vars, and all clasiic OO
#

use strict;
use Data::Dumper;


$SIG{'INT'} = 'INT_handler';


my $sTOP='/bin/top';
my $sProc=$ARGV[0];
my $dInterval=$ARGV[1];

chomp($sProc);
if (scalar(@ARGV) != 2) {
	die "Usage: $0 nsr|orauser Interval\n".
            " example : $0 nsr 10 \n".
            "   means poll every 10 seconds grab proc information for nsr etc \n".
            "   and pump the output out to output file \n".
            "   which can then be pulled into excel and then graphed \n";
}

if ( $dInterval !~ /\d+/ ) {
	die "Interval: $dInterval should be digits in seconds like 5  \n";
}
if ( ! -e "$sTOP") {
	die "where is top it is not in $sTOP \n";
}


my $dPID=$$;

my $dtPID1=$dPID - 1;
my $dtPID2=$dPID - 2;

open (WH_topMemStat , " > /tmp/topProcOutput.$dtPID1") || die " Can't write to this file: /tmp/topProcOutput.$dtPID1 ";
open (WH_topProcStat , " > /tmp/topProcOutput.$dtPID2") || die " Can't write to this file: /tmp/topProcOutput.$dtPID2 ";


my $sTopCmd="$sTOP -b  300 > /tmp/topout.$dPID";
`$sTopCmd`;

open (RH,"/tmp/topout.$dPID")|| die "Can't read the output of the top commands output file:/tmp/topout.$dPID \n";
my @aTopOutput=<RH>;
close (RH); 


print "$0: Output will be written to /tmp/topProcOutput.$dtPID1 and /tmp/topProcOutput.$dtPID2 \n";

my @aFormatted;
my @aFormatted2;
my $sTime;

#print "Time,CPUIdle,CPUKernel,CPUIowait,CPUswap,MEMTot,MEMfree,MEMSwap,MEMFreeSwap\n";
#print "Time,ProcName,MEM,MEM RES,STATE,CPUUsage\n";

#print WH_topMemStat "Time,CPUIdle,CPUKernel,CPUIowait,CPUswap,MEMTot,MEMfree,MEMSwap,MEMFreeSwap\n";
print WH_topMemStat "Time,CPUUser,CPUSystem,CPUInice,CPUIdle,MEMTot,MEMUsed,Memfree,SWAPTotal,SWAPfree\n";
print WH_topProcStat "Time,ProcName,VirtMEM,ResMEM,ShrMEM,CPUUsage,MEMUsage\n";

while (1) {

for (my $i=0;$i <= $#aTopOutput;$i++) {
  
	chomp($aTopOutput[$i]);
	
 if ($aTopOutput[$i] =~ /load avera*/) {
        my @atemp=split(/\s+/,$aTopOutput[$i]);
	push(@aFormatted,$atemp[$#atemp]); #push(@aFormatted,"Time",$atemp[$#atemp]);
        $sTime=$atemp[$#atemp];
	chomp($sTime);
 }
 elsif ($aTopOutput[$i] =~ /CPU states/) {
        my @atemp=split(/,/,$aTopOutput[$i]);
        my ($one,$two)= split(/:/,$atemp[0]);
        $two=~ s/idle//;
	push(@aFormatted,$two);

	$atemp[1] =~ s/user//g;
	push(@aFormatted,$atemp[1]); #CPUIdle

	$atemp[2] =~ s/kernel//g;
	push(@aFormatted,$atemp[2]); #CPUKernel

	$atemp[3] =~ s/iowait//g;
	push(@aFormatted,$atemp[3]); #CPUIowait

	$atemp[4] =~ s/swap//g;
	push(@aFormatted,,$atemp[4]); #CPUSwap
	
 }
 elsif ($aTopOutput[$i] =~ /Memory/) {
  my @atemp=split(/,/,$aTopOutput[$i]);
        my ($one,$two)= split(/:/,$atemp[0]);
        $two=~ s/phys mem//;
        push(@aFormatted,$two); #push(@aFormatted,"MEMTot",$two);

        $atemp[1] =~ s/free mem//g;
        push(@aFormatted,$atemp[1]); #push(@aFormatted,"MEMfree",$atemp[1]);

        $atemp[2] =~ s/total swap//g;
        push(@aFormatted,$atemp[2]); #push(@aFormatted,"MEMSwap",$atemp[2]);

        $atemp[3] =~ s/free swap//g;
        push(@aFormatted,$atemp[3]); #push(@aFormatted,"MEMFreeSwap",$atemp[3]);

 }
 elsif ($aTopOutput[$i] =~ /$sProc/) {
        my @atemp=split(/\s+/,$aTopOutput[$i]);
        #push(@aFormatted,$atemp[$#atemp],$atemp[5],$atemp[6],$atemp[9]);
        #push(@aFormatted,"ProcName " . $atemp[$#atemp],"MEM " . $atemp[6],"MEM RES ". $atemp[7],"STATE " . $atemp[8], "CPU usage ".$atemp[10]);

        #push(@aFormatted2,"ProcName " . $atemp[$#atemp].
        #                 ",MEM " . $atemp[6].",MEM RES ". $atemp[7].
        #                 ",STATE " . $atemp[8]. ",CPU usage ".$atemp[10]);

        push(@aFormatted2,$sTime,$atemp[$#atemp],$atemp[6],$atemp[7],$atemp[8], $atemp[10]."\n"); 

}

}

#print join(",",@aFormatted),"\n";
#print Dumper(@aFormatted2),"\n";

print WH_topMemStat join(",",@aFormatted),"\n";
#print WH_topProcStat join(",",@aFormatted2),"\n";
#print "foo Str ",join(",",@aFormatted2),"\n";
print WH_topProcStat join(",",@aFormatted2);

sleep ($dInterval);

$sTopCmd="$sTOP -b  300 > /tmp/topout.$dPID";
`$sTopCmd`;

@aTopOutput=();
$sTime="";
open (RH,"/tmp/topout.$dPID") || die "Can't read the output of the top commands output file:/tmp/topout.$dPID \n";
@aTopOutput=<RH>;
close (RH);

@aFormatted=();
@aFormatted2=();
}

#####################################################
#
#####################################################
sub INT_handler {
    # close all files.
    # send error message to log file.
    close (RH);
    close (WH_topProcStat); 
    close (WH_topMemStat); 
    print "Exiting Cleanly, closed all File Handles \n";
    exit(0);
}
