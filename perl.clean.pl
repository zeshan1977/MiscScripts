use strict;
use Data::Dumper;

#Orig
#2009.06.16   12:14:28:670, -server 69.46.108.79 -port 7676 -performance -maxTPS 20 -runTime 20 -managedDepth 500 -xmlfile RandomO rderConfigurationMember002MU1.xml -statsFile RandomOrderConfigurationMember002MU1.xml.csv,RandomOrderConfigurationMember002MU1.xml ,20.159680638722556,2.0396039603960396,0.5181347150259067,0.039374359375 
# #2009.06.16,,,12:14:28:670,,-server,69.46.108.79,-port,7676,-performance,-maxTPS,20,-runTime,20,-managedDepth,500,-xmlfile,RandomO rderConfigurationMember002MU1.xml,-statsFile,RandomOrderConfigurationMember002MU1.xml.csv,RandomOrderConfigurationMember002MU1.xml ,20.159680638722556,2.0396039603960396,0.5181347150259067,0.039374359375

print "Date,Time,BrokerConfig,TPS,managedDepth,runTime(minutes),DoorToDoorEmapiResponseTime(ms),PrivateOrderBookEventTime(ms),Time
MGunisTaking(ms)\n";

while (<>) {
        my $line =$_;
                chomp($line);
                $line =~ s/\s+/,/g;
                my @arr=split(/\,/,$line);
#               print "DUMP ----- ",Dumper(@arr), "\n";

#DUMP ----- $VAR1 = '2009.06.16';
#VAR2 = '12:14:33:701';
#VAR3 = '';
#VAR4 = '-server';
#VAR5 = '69.46.108.79';
#VAR6 = '-port';
#VAR7 = '7676';
#VAR8 = '-performance';
#VAR9 = '-maxTPS';
#VAR10 = '20';
#VAR11 = '-runTime';
#VAR12 = '20';
#VAR13 = '-managedDepth';
#VAR14 = '500';
#VAR15 = '-xmlfile';
#VAR16 = 'RandomOrderConfigurationMember222MU1.xml';
#VAR17 = '-statsFile';
#VAR18 = 'RandomOrderConfigurationMember222MU1.xml.csv';
#VAR19 = 'RandomOrderConfigurationMember222MU1.xml';
#VAR20 = '28.50393700787402';
#VAR21 = '2.276243093922652';
#VAR22 = '369.0289855072464';
#VAR23 = '0.03924957362637362';

        print "$arr[0],$arr[1],$arr[15],$arr[9],$arr[13],$arr[11],$arr[20],$arr[21],$arr[22]\n";
}

