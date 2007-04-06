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

if (param('m') eq 'entitylist')
{
    entitylist();
}
elsif(param('m') eq 'getmarkers')
{
    getmarkers(param('entity'));
}

sub entitylist
{
    my $sth = $dbh->prepare('select distinct(type) from ch10');
    $sth->execute();

    print "<types>";
    while (my $row = $sth->fetchrow_hashref())
    {
	printf('<type typename="%s"/>',ucfirst($row->{type}));
    }
    print "</types>";
}

sub getmarkers
{
    my ($entity) = @_;

    print("<markers>\n");

    my $sth = $dbh->prepare(sprintf('select * from ch10 where type = %s',
				    $dbh->quote($entity)));
    $sth->execute();
    
    while (my $row = $sth->fetchrow_hashref())
    {
	printf('<marker lat="%f" lng="%f" title="%s"><infowindow><title>%s</title><address>%s</address><city>%s</city><phone>%s</phone></infowindow></marker>',
	       $row->{lat},
	       $row->{lng},
	       $row->{title},
	       $row->{title},
	       $row->{adda},
	       $row->{addb},
	       $row->{tel},
	       );
	
    }
    $sth->finish();
    
    print("</markers>\n");
}

