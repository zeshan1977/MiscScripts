use threads;
use threads::shared;    
use strict;
my $total : shared = 0;    

sub calc {
        for (;;) {
            my $result;
            # (...  calculations and result $result .for latencyu periodic check..)
            {
                lock($total); # block until  lock released
                $total += $result;
            } # haha perl magick lock implicitly released at end of scope
            last if $result == 0;
        }
 }
    my $thr1 = threads->new(\&calc);
    my $thr2 = threads->new(\&calc);
    my $thr3 = threads->new(\&calc);
    $thr1->join;
    $thr2->join;
    $thr3->join;
    print "total=$total\n";

#
#################################
################################
use Thread::Queue;    
my $DataQueue = Thread::Queue->new; 
    my $thr = threads->new(sub { 
        while (my $DataElement = $DataQueue->dequeue) { 
            print "Popped $DataElement off the queue\n";
        } 
    });
    $DataQueue->enqueue(12); 
    $DataQueue->enqueue("A", "B", "C"); 
    $DataQueue->enqueue(\$thr); 
    sleep 10; 
    $DataQueue->enqueue(undef);
    $thr->join;

############################
##### Looper find prime number
##### act when time and random factor is prime 
################################
    my $DataQueue2 = new Thread::Queue;
    my $kinder    = new threads(\&check_num, $DataQueue2, 2);
    for my $i ( 3 .. 1000 ) {
      $DataQueue2->enqueue($i);
    } 
   
  $DataQueue2->enqueue(undef);
  $kinder->join;
  
 sub check_num {
    my ($upstream, $cur_prime) = @_;
    my $kinder;
    my $downstream = new Thread::Queue;
    while (my $num = $upstream->dequeue) {
       next unless $num % $cur_prime;
          if ($kinder) {
                $downstream->enqueue($num);
          } else {
             #print    "Ich habe es gefunden,Hier ist die prime zahl $num\n";
                $kinder = new threads(\&check_num, $downstream, $num);
          }
       } 
    $downstream->enqueue(undef) if $kinder;
    $kinder->join if $kinder;
 }
