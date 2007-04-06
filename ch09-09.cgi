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

my $sth = $dbh->prepare('select title,lat,lng from ch08_simple');
$sth->execute();

while (my $row = $sth->fetchrow_hashref())
{
    printf('<marker lat="%f" lng="%f" title="%s"/>',
	   $row->{lat},
	   $row->{lng},
	   $row->{title});

}
$sth->finish();

print("</markers>\n");

