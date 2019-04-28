#!/bin/perl
use threads;
#
#
# mkDAOS.pl
#
# exit 0 - success
# exit 1 - error
#
#
#
sub usage {
        if ($_[0]) {
                print "\n$_[0]";
        }
        print "\nUsage:   $0 path levels num_dirs num_files file_size\n";
        print "         path      - full path to DAOS base directory\n";
        print "         num_dirs  - number of DAOS sub-dirs to create\n";
        print "         num_files - number of DAOS files to create in each DAOS dirs\n";
        print "         min_size  - max size of DAOS files to be created (size will be random) \n";
        print "         max_size  - min size of DAOS files to be created (size will be random) \n\n";
        print "Example: $0 /var/tmp/foo 3 4 10K 100M\n";
        print "         Create a 3 DAOS sub dirs, each contains 4 DAOS files. The DAOS's\n";
        print "         size is btw. 10KB - 100MB.\n\n";
        
        exit 1;
}

#
# make_tree_at_node will create the tree structure and populate it with the files
sub make_tree_at_node {
        local($current_path)  = $_[0];
#       local($current_level) = $_[1];
        local($current_level) = 0;
        local($i, $j, @dirs);

        $current_level++;
        for ( $i = 0, $j = 1; $i < $MAX_NODES; $i++, $j++ ) {
                #
                # DAOS sub-dirs are of the form, "0001,0002,...,0999,1000"
                #
                
                if ( $j < 10 ) {
                        $dirs[$i] = $current_path . $DIR_TAG . "000" . $j;              
                } elsif ( $j < 100 ) {
                        $dirs[$i] = $current_path . $DIR_TAG . "00" . $j;
                } elsif ( $j < 1000) {
                        $dirs[$i] = $current_path . $DIR_TAG . "0" . $j;
                } else {
                        $dirs[$i] = $current_path . $DIR_TAG . $j;
                }       
                
                if ( ! mkdir($dirs[$i], 0777) ) {
                        print "Failed to create directory \"$dirs[$i]\" - $!";
                        exit 1;
                }
                chdir ($dirs[$i]);
                # Create files in this directory.
                for ( $FileNum = 0; $FileNum < $NUM_FILES; $FileNum++ ) {

#                       $Filename = "File-".$FileNum.".nlo";
                        $Filename = "2376DD154FC3319999F0648CA88F55E792A06066000DA3EF".$j.$FileNum.".nlo";                      

                        open (OUTFILE, ">".$Filename) || die "Failed to open file <$Filename>";
                        $file_size = int(rand($MAX_SIZE-$MIN_SIZE)) + $MIN_SIZE;
                        $offset=int(rand(3 * $MAX_SIZE - $file_size));
                        print OUTFILE substr($RANDOM_DATA,$offset,$file_size);
                        close(OUTFILE);
                }
                chdir ($current_path);
        }
}


sub getSize {
  local ($fsize) = $_[0];
  if ( $fsize =~ m/([0-9]*)([kKmM]*)/ ) {
        $cnt = $1;
        ($type = $2) =~ tr/A-Z/a-z/;
        if ( $cnt == 0 ) {
                &usage ("Invalid size argument \"$fsize\"\n");
        }
  } else {
        &usage ("Invalid size argument \"$fsize\"\n");
  }

  if ( $type eq '' ) {
        # Bytes
        $size = $cnt;
  } elsif ( $type eq 'k' ) {
        # Kilobytes
        $size = $cnt * 1024;
  } elsif ( $type eq 'm' ) {
        # Megabytes
        $size = $cnt * 1024 * 1024;
  } else {
        &usage ("Invalid multiplier \"$type\"\n");  
  }
  return $size;
}
  

if ($#ARGV < 4) {
        &usage("Incorrect number of arguments\n");
}

$ROOT         = $ARGV[0];
$MAX_NODES    = $ARGV[1];
$NUM_FILES    = $ARGV[2];
$MIN_SIZE     = $ARGV[3];
$MAX_SIZE     = $ARGV[4];

$DIR_TAG      = "/";

if ( ! -d $ROOT ) {
        print "Directory \"$ROOT\" does not exist\n";
        exit 1;
} elsif ( ! -w $ROOT ) {
        print "Directory \"$ROOT\" is not writable\n";
        exit 1;
}
if (($MAX_NODES <= 0) or ($MAX_NODES > 1000))  {
  print "\nError: Number of dirs at each level should be greater than 0 and less than 1000\n";
  &usage("Check usage\n");
}
if (($NUM_FILES <= 0) or ($NUM_FILES > 40000)) {
  print "\nError: Number of files in each sub-directory should be greater than 0 and less than 40000\n";
  &usage("Check usage\n");
}
if ($MIN_SIZE <= 0) {
  print "\nError: Minimum size of files should be greater than 0\n";
  &usage("Check usage\n");
}
if ($MAX_SIZE <= 0) {
  print "\nError: Maximum size of files should be greater than 0\n";
  &usage("Check usage\n");
}

$MIN_SIZE = &getSize ($MIN_SIZE);
$MAX_SIZE = &getSize ($MAX_SIZE);

if ($MIN_SIZE >= $MAX_SIZE) {
  print "Maximum size must be greater than minimum size\n";
  &usage("Check usage\n");
}

# generate three times the amount of random data we'll ever need

srand(time|$$);
$RANDOM_DATA = "\0" x (3 * $MAX_SIZE);
for($l=0; $l < (3 * $MAX_SIZE); $l++){
    substr($RANDOM_DATA,$l,1)=chr(rand(127));
}

&make_tree_at_node( $ROOT, 0 );
exit 0;



