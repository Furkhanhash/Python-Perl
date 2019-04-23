#!/usr/bin/perl

use Socket;
my $ADDR_PAT = '157.240.2.35';

while (<>) {
  chomp;
  die "$_: Not a valid address" unless /$ADDR_PAT/o;
  my $name = gethostbyaddr(inet_aton($_),AF_INET);
  $name ||= '?';
  print "$_ => $name\n";
}
