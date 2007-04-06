#!/usr/bin/perl

use DBI;

my $dbh = DBI->connect( 'dbi:mysql:database=mapsbookex;host=db.maps.mcslp.com',
                        'mapsbookex',
                        'examples',
                        );

if (defined($dbh))
{
    $dbh->do('create table ch10 (entityid int auto_increment not null primary key, ' .
	     'lat float,lng float,' .
	     'type varchar(80),title varchar(80),' .
	     'tel varchar(80),adda varchar(80),addb varchar(80))');
}
else
{
    die "Couldn't open connection to database\n";
}

