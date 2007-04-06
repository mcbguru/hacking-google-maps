#!/usr/bin/perl

use DBI;
use strict;
use XML::Generator;
	     
my $dbh = DBI->connect( 'dbi:mysql:database=mapsbookex;host=db.maps.mcslp.com',
                        'mapsbookex',
                        'examples',
                        );

print<<EOF;
<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://earth.google.com/kml/2.0">
<Folder>
<name>Grantham features</name>
<open>1</open>
EOF

my $sth = $dbh->prepare(sprintf('select * from ch10 order by type'));

$sth->execute();

my ($currenttype,$count) = ('',0);

while (my $row = $sth->fetchrow_hashref())
{
    if ($currenttype ne $row->{type})
    {
        if ($count > 0)
        {
            print "</Folder>";
        }
        printf("<Folder>\n<name>%s</name>\n<open>0</open>\n",$row->{type});
        $currenttype = $row->{type};
    }
    
    $count++;

    printf("<Placemark>\n<name>%s</name>\n<address>%s,%s</address>\n<Point>\n<coordinates>%s,%s,0</coordinates>\n</Point></Placemark>\n",
           $row->{title},
           $row->{adda},
           $row->{addb},
           $row->{lng},
           $row->{lat},
           );
	
    }
$sth->finish();

print("</Folder></Folder>\n</kml>\n");



