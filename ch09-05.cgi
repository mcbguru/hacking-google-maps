#!/usr/bin/perl

use CGI qw/:standard/;

print header(-type => 'text/xml');
	     
my $points = [
	      {x =>     -0.6394,
	       y =>     52.9114,
	       title => 'China Inn'},
	      {x =>     -0.64,
	       y =>     52.909444,
	       title => 'One on Wharf'},
	      {x =>     -0.64454,
	       y =>     52.91066,
	       title => 'Hop Sing'},
	      {x =>     -0.642743,
	       y =>     52.9123959,
	       title => 'Nicklebys'},
	      {x =>     -0.6376,
	       y =>     52.9073,
	       title => 'Siam Garden'},
	      ];


print '<markers>';

foreach my $point (@{$points})
{
    printf('<marker lat="%f" lng="%f" title="%s"/>',
	   $point->{y},
	   $point->{x},
	   $point->{title});
}

print '</markers>';


