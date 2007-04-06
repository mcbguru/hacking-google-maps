#!/usr/bin/perl

use DBI;

my $dbh = DBI->connect( 'dbi:mysql:database=mapsbookex;host=db.maps.mcslp.com',
                        'mapsbookex',
                        'examples',
                        );

if (defined($dbh))
{
    $dbh->do('create table ch08_simple (lat float,lng float,title varchar(80))');
}
else
{
    die "Couldn't open connection to database\n";
}

