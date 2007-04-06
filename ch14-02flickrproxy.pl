#!/usr/bin/perl

use strict;
use CGI qw/:standard/;
use LWP::UserAgent;

my $ua = LWP::UserAgent->new(env_proxy => 1,
                             keep_alive => 1,
                             timeout => 30,
                             agent => "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.0.2) Gecko/20021120 Netscape/7.\
01",
                             );
print header(-type => 'text/xml');

my @query;

foreach my $param (param())
{
    push @query,sprintf('%s=%s',$param,param($param));
}

my $query = 'http://www.flickr.com/services/rest/?' . join('&',@query);

my $response = $ua->get($query);

print $response->{_content};

