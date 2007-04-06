#!/usr/bin/perl

use CGI qw/:standard/;

print header(-type => 'text/html');
	     
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

page_header();
js_addmarker();
js_movemap();
js_onLoad();
page_footer();

sub page_header
{

print <<EOF;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
  <meta http-equiv="content-type" content="text/html; charset=UTF-8"/>

  <title>MCslp Maps Chapter 6, Ex 9</title>
  <script src="http://maps.google.com/maps?file=api&v=1&key=ABQIAAAAaN3cztBhhIJumioMt9V-TRQKCXCZYFcg34C5xfWZNrxIR2sIwhQQZgNXBZ-Lrr-KMRtSCzzweMqbWg"
      type="text/javascript">
  </script>

  <script type="text/javascript">
  //<![CDATA[

  var map;

  var points = [];
  var index = 0;

  var infopanel;
EOF
}

sub js_onLoad
{
    my @markers;

    foreach my $point (@{$points})
    {
	push @markers,sprintf("addmarker(%f,%f,'%s');",
			      $point->{x},
			      $point->{y},
			      $point->{title});
    }

    my $template = <<EOF;
  function onLoad() {
    if (GBrowserIsCompatible()) {
	infopanel = document.getElementById("infopanel");
	map = new GMap(document.getElementById("map"));
	map.centerAndZoom(new GPoint(-0.64,52.909444), 2);
	%s
    }
  }
EOF

    printf($template,join("\n",@markers));

}

sub js_addmarker
{
    print <<EOF;
  function addmarker(x,y,title) {
      var point = new GPoint(parseFloat(x),parseFloat(y));
      points.push(point);
      var marker = new GMarker(point);
      map.addOverlay(marker);
      infopanel.innerHTML = infopanel.innerHTML + 
	  '<a href="#" onClick="movemap(' + index + ');">' + 
	  title + 
	  '</a><br/>';
      index++;
  }    
EOF

}

sub js_movemap
{

    print <<EOF;
  function movemap(index) {
      map.recenterOrPanToLatLng(points[index]);
  }
EOF

}

sub page_footer
{
    print <<EOF;
  //]]>
  </script>
  </head>
  <body onload="onLoad()">
  <table cellspacing="15" cellpadding="0" border="0">
  <tr valign="top">
  <td><div id="map" style="width: 800px; height: 600px"></div></td>
  <td><h1>Restaurants</h1><div id="infopanel"></div></td>
  </tr>
  </table>
  </body>
  </html>
EOF

}
