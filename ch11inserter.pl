#!/usr/bin/perl

use strict;
use LWP::UserAgent;
use URI::Escape;
use Data::Dumper;
use DBI;

my $dbh = DBI->connect( 'dbi:mysql:database=mapsbookex;host=db.maps.mcslp.com',
                        'mapsbookex',
                        'examples',
                        );

if (!defined($dbh))
{
    die "Couldn't open connection to database\n";
}

my $ua = LWP::UserAgent->new(
                             agent => "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.0.2) Gecko/20021120 Netscape/7.01",
                             );

my $response = $ua->get('http://maps.google.com/maps?q=' . uri_escape(sprintf('%s, %s',$ARGV[0],$ARGV[1])));

my $var = $response->{_content};

my @matches = ($var =~ m/<a href="\/maps(.*?)\&nbsp\;\-\&nbsp\;/g);

my $finds = [];

foreach my $entity (@matches)
{
    my ($lat,$lng,$title,$tel,$adda,$addb) = ($entity =~ m/latlng=(.*?),(.*?),.*?>(.*?)<.*<nobr>(.*?)<\/nobr>.*<font size=-1>(.*?)<\/font.*-1>(.*?)<\/font>/);

    ($lat,$lng) = getlatlng($addb);

    $dbh->do(sprintf('insert into ch10 values(0,%s,%s,%s,%s,%s,%s,%s)',
                     $dbh->quote($lat),
                     $dbh->quote($lng),
                     $dbh->quote($ARGV[0]),
                     $dbh->quote($title),
                     $dbh->quote($tel),
                     $dbh->quote($adda),
                     $dbh->quote($addb),
            ));
}

sub getlatlng
{
    my ($text) = @_;

    my $response = $ua->get('http://maps.google.com/maps?q=' . uri_escape($text));
    
    my $var = $response->{_content};
    
    my ($lat,$lng) = ( $var =~ m/GLatLng\(([-\d.]+).*?([-\d.]+)\)/ms );
    
    return ($lat,$lng);
}
