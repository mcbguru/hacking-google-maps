#!/usr/bin/perl

use DBI;

my $dbh = DBI->connect( 'dbi:mysql:database=mapsbookex;host=db.maps.mcslp.com',
                        'mapsbookex',
                        'examples',
                        );

if (defined($dbh))
{
    $dbh->do('create table ch12_routesimple (routeid int auto_increment not null primary key, ' .
	     'title varchar(80),description varchar(255))');
    $dbh->do('create table ch12_routepoints (routeid int,lat float,lng float)');
}
else
{
    die "Couldn't open connection to database\n";
}

