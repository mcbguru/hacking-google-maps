#!/usr/bin/perl

use DBI;
use strict;

my $dbh = DBI->connect( 'dbi:mysql:database=mapsbookex;host=db.maps.mcslp.com',
                        'mapsbookex',
                        'examples',
                        );

if (!defined($dbh))
{
    die "Couldn't open connection to database\n";
}

my @lines;

my $sth = $dbh->prepare('select title,lat,lng from ch08_simple');
$sth->execute();

while (my $row = $sth->fetchrow_hashref())
{
    push(@lines,
	 sprintf('<marker lat="%f" lng="%f" title="%s"/>',
		 $row->{lat},
		 $row->{lng},
		 $row->{title}));

}
$sth->finish();

if (scalar @lines > 0)
{
    print("<markers>\n",
	  join("\n",@lines),
	  "</markers>\n");
}
