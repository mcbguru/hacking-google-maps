// TLabel() GMaps API extension copyright 2005 Tom Mangan (tmangan@gmail.com)
// http://gmaps.tommangan.us/tlabel.html
// free for non-commercial use
// the 'Made with TLabel' bug must remain in place for free use
function TLabel(){}
TLabel.prototype.initialize=function(a){
  if (typeof(a.TLabelBugged=='undefined')){this.addTBug(a);}
  this.parentMap=a;
  var b=a.ownerDocument.createElement('span');
  b.setAttribute('id',this.id);
  b.innerHTML=this.content;
  document.body.appendChild(b);
  b.style.position='absolute';
  b.style.zIndex=1;
  if(this.percentOpacity){this.setOpacity(this.percentOpacity);}
  this.w = document.getElementById(this.id).offsetWidth;
  this.h = document.getElementById(this.id).offsetHeight;
  a.div.appendChild(b);
  if(!this.markerOffset){this.markerOffset=new GSize(0,0);}
  this.setPosition();
  GEvent.bind(a,"zoom",this,function(){this.setPosition()});
  GEvent.bind(a,"moveend",this,function(){this.setPosition()});
}
TLabel.prototype.setPosition=function(c){
  if(c){this.anchorLatLng=c;}
  var a=this.parentMap;
  var b=this.getXY(a,this.anchorLatLng,a.getZoomLevel());
  with(Math){switch(this.anchorPoint){
    case 'topLeft':break;
    case 'topCenter':b.x-=floor(this.w/2);break;
    case 'topRight':b.x-=this.w;break;
    case 'midRight':b.x-=this.w;b.y-=floor(this.h/2);break;
    case 'bottomRight':b.x-=this.w;b.y-=this.h;break;
    case 'bottomCenter':b.x-=floor(this.w/2);b.y-=this.h;break;
    case 'bottomLeft':b.y-=this.h;break;
    case 'midLeft':b.y-=floor(this.h/2);break;
    case 'center':b.x-=floor(this.w/2);b.y-=floor(this.h/2);break;
    default:break;
  }}
  var offsetX=0;var offsetY=0;
  var x=document.getElementById(this.id);
  x.style.left=b.x-this.markerOffset.width+'px';
  x.style.top=b.y-this.markerOffset.height+'px';
}
TLabel.prototype.getXY=function(a,b,c){
  var e=a.spec.getBitmapCoordinate(b.y,b.x,c);
  return a.getDivCoordinate(e.x,e.y);
}
TLabel.prototype.setOpacity=function(b){
  if(b<0){b=0;} if(b>=100){b=100;}
  var c=b/100;
  var d=document.getElementById(this.id);
  if(typeof(d.style.filter)=='string'){d.style.filter='alpha(opacity:'+b+')';}
  if(typeof(d.style.KHTMLOpacity)=='string'){d.style.KHTMLOpacity=c;}
  if(typeof(d.style.MozOpacity)=='string'){d.style.MozOpacity=c;}
  if(typeof(d.style.opacity)=='string'){d.style.opacity=c;}
}
TLabel.prototype.addTBug=function(a){
  if(typeof(a.TLabelBugged)=='undefined'){
    var b=a.ownerDocument.createElement('div');
    b.id='TLabelBug';
    b.style.position='absolute';
    b.style.right='0px';
    if(a.TBugged>0){b.style.bottom='32px';}else{b.style.bottom='20px';}
    b.style.backgroundColor='#f2efe9';
    b.style.zIndex=25500;
    b.innerHTML='<a href="http://gmaps.tommangan.us/tlabel.html" style="font:10px verdana;text-decoration:none;padding:2px;color:#000;">Made with TLabel</a>';
    a.div.parentNode.appendChild(b);
    var c=0.7;
    var d=document.getElementById(b.id);
    if(typeof(d.style.filter)=='string'){d.style.filter='alpha(opacity:'+c*100+')';}
    if(typeof(d.style.KHTMLOpacity)=='string'){d.style.KHTMLOpacity=c;}
    if(typeof(d.style.MozOpacity)=='string'){d.style.MozOpacity=c;}
    if(typeof(d.style.opacity)=='string'){d.style.opacity=c;}
    a.TLabelBugged=1;
  }
}
GMap.prototype.addTLabel=function(a){
  a.initialize(this);
}
GMap.prototype.removeTLabel=function(a){
  this.div.removeChild(document.getElementById(a.id));
  delete(a);
}

