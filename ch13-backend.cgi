#!/usr/bin/perl

use DBI;
use Math::Trig;
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

if (param('m') eq 'saveroute')
{
    saveroute();
}
if (param('m') eq 'delroute')
{
    delroute(param('routeid'));
}
elsif(param('m') eq 'listroutes')
{
    listroutes();
}
elsif(param('m') eq 'getroute')
{
    getroute(param('routeid'));
}

sub delroute
{
    my ($routeid) = @_;

    $dbh->do(sprintf('delete from ch12_routesimple where routeid=%s',
		     $routeid));
    $dbh->do(sprintf('delete from ch12_routepoints where routeid=%s',
		     $routeid));
    
    xmlmessage('Route deleted');
}

sub listroutes
{
    my $sth = $dbh->prepare('select ch12_routesimple.routeid,title,lat,lng from ch12_routesimple,ch12_routepoints where ch12_routesimple.routeid = ch12_routepoints.routeid and seqid = 1 order by title');
    $sth->execute();

    print "<routes>";
    while (my $row = $sth->fetchrow_hashref())
    {
	printf('<route routeid="%s" title="%s" lat="%s" lng="%s"/>',
	       $row->{routeid},
	       $row->{title},
	       $row->{lat},
	       $row->{lng}
	       );
    }
    print "</routes>";
}

sub latlngdistance
{
    my ($xdeg1,$ydeg1,$xdeg2,$ydeg2) = @_;

    my ($x1,$y1,$x2,$y2) = (deg2rad($xdeg1),
			    deg2rad($ydeg1),
			    deg2rad($xdeg2),
			    deg2rad($ydeg2));

    my $radius = 6371; 
    my $latdistance = $x2 - $x1;
    my $lngdistance = $y2 - $y1;

    my $a = sin($latdistance/2) * sin($latdistance/2) +
          cos($x1) * cos($x2) * sin($lngdistance/2) * sin($lngdistance/2);
    my $c = 2 * atan2(sqrt($a), sqrt(1-$a));
    my $d = $radius * $c;

    return $d;
}

sub saveroute
{
    my $title = param('title');
    my $description = param('desc');
    my $points = param('points');

    my @pointlist = split(/,/,$points);
    my $routeid;

    if (defined(param('routeid')) && param('routeid') != 0)
    {
	$routeid = param('routeid');
	
	$dbh->do(sprintf('update ch12_routesimple set title=%s,description=%s where routeid=%s',
			 $dbh->quote($title),
			 $dbh->quote($description),
			 $routeid));
	$dbh->do(sprintf('delete from ch12_routepoints where routeid=%s',
			 $routeid));
    }
    else
    {
	$dbh->do(sprintf('insert into ch12_routesimple values(0,%s,%s)',
			 $dbh->quote($title),
			 $dbh->quote($description)));
	$routeid = $dbh->{mysql_insertid};
    }

    foreach my $point (@pointlist)
    {
	my ($seqid,$x,$y) = split(/:/,$point);
	$dbh->do(sprintf('insert into ch12_routepoints values(%s,%s,%s,%s)',
			 $dbh->quote($routeid),
			 $dbh->quote($x),
			 $dbh->quote($y),
			 $dbh->quote($seqid)));
    }
    xmlmessage('Route added',{routeid => $routeid});
}

sub getroute
{
    my ($reqrouteid) = @_;

    my $routedata = $dbh->selectrow_hashref('select routeid,title,description from ch12_routesimple where routeid = ' . 
					    $dbh->quote($reqrouteid));

    if ($routedata->{routeid} != $reqrouteid)
    {
	xmlmessage('Error: route not found');
	return();
    }

    printf('<route><routeinfo routeid="%s" title="%s" description="%s"/>',
	   $routedata->{routeid},
	   $routedata->{title},
	   $routedata->{description});

    my $sth = $dbh->prepare(sprintf('select lat,lng from ch12_routepoints where routeid = %s order by seqid',
				    $dbh->quote($routedata->{routeid})));
    $sth->execute();

    my $distance = 0;
    my $seq = 0;
    my ($lastx,$lasty) = (undef,undef);

    while (my $row = $sth->fetchrow_hashref())
    {
	$seq++;
	printf('<point lat="%f" lng="%f"/>',
	       $row->{lat},
	       $row->{lng},
	       );
	if ($seq >= 2)
	{
	    $distance += latlngdistance($lastx,$lasty,$row->{lat},$row->{lng});
	}
	($lastx,$lasty) = ($row->{lat},$row->{lng});
    }
    $sth->finish();
    printf('<distance km="%.2f" miles="%.2f"/>',$distance,($distance/1.609344));
    print("</route>\n");
}

sub xmlmessage
{
    my ($message,$attrib) = @_;

    printf('<msg><message text="%s" %s/></msg>',
	   $message,
	   join(' ',map {sprintf('%s="%s"',$_,$attrib->{$_}) } keys %{$attrib}));
}
