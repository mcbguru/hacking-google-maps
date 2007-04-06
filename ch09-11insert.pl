#!/usr/bin/perl

use DBI;

my $dbh = DBI->connect( 'dbi:mysql:database=mapsbookex;host=db.maps.mcslp.com',
                        'mapsbookex',
                        'examples',
                        );

if (!defined($dbh))
{
    die "Couldn't open connection to database\n";
}

open(DATA,$ARGV[0]) or die "Couldn't open file; did you forget it?";

my $counter = 0;

while(<DATA>)
{
    chomp;
    my ($title,$lng,$lat,$street,$city,$postcode,$phone) = split /:/;

    $dbh->do(sprintf('insert into ch08_cplx values(%s,%s,%s,%s,%s,%s,%s)',
		     $dbh->quote($lat),
		     $dbh->quote($lng),
		     $dbh->quote($title),
		     $dbh->quote($street),
		     $dbh->quote($city),
		     $dbh->quote($postcode),
		     $dbh->quote($phone),
		     ));
    $counter++;
}
close(DATA);

print "$counter records inserted\n";
