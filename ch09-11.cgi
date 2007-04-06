#!/usr/bin/perl

use DBI;
use strict;
use CGI qw/:standard/;

print header(-type => 'text/xml');
	     
my $dbh = DBI->connect( 'dbi:mysql:database=mapsbookex;host=db.maps.mcslp.com',
                        'mapsbookex',
                        'examples',
                        );

if (!defined($dbh))
{
    die "Couldn't open connection to database\n";
}

print("<markers>\n");

my $sth = $dbh->prepare('select * from ch08_cplx');
$sth->execute();

while (my $row = $sth->fetchrow_hashref())
{
    printf('<marker lat="%f" lng="%f" title="%s"><infowindow><title>%s</title><address>%s</address><city>%s</city><postcode>%s</postcode><phone>%s</phone></infowindow></marker>',
	   $row->{lat},
	   $row->{lng},
	   $row->{title},
	   $row->{title},
	   $row->{street},
	   $row->{city},
	   $row->{postcode},
	   $row->{phone},
	   );

}
$sth->finish();

print("</markers>\n");

