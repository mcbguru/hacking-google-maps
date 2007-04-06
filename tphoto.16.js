// TPhoto() GMaps API extension copyright 2005 Tom Mangan (tmangan@gmail.com)
// http://gmaps.tommangan.us/tphoto.html
// free for non-commercial use
// the 'Made with TPhoto' bug must remain in place for free use
function TPhoto(){}
TPhoto.prototype.initialize=function(a){
  if (a.TBugged<1||typeof(a.TBugged=='undefined')){this.addTBug(a);}
  var photo=a.ownerDocument.createElement('img');
  this.setAttributes(photo);
  a.div.appendChild(photo);
  this.setOnce(a);
  this.reZoom(a);
  GEvent.bind(a,"zoom",this,function(){this.reZoom(a)});
  GEvent.bind(a,"moveend",this,function(){this.reZoom(a)});
}
TPhoto.prototype.setAttributes=function(a){
  a.setAttribute('id',this.id);
  a.setAttribute('src',this.src);
  if(this.size){
    var b=this.size;
    a.setAttribute('width',b.width);
    a.setAttribute('height',b.height);
  }
}
TPhoto.prototype.setOnce=function(a){
  var b=document.getElementById(this.id);
  b.style.position='absolute';
  b.style.zIndex=1;
  if(this.percentOpacity){
    this.setOpacity(this.percentOpacity);
  }
}
TPhoto.prototype.reZoom=function(a){
  if(this.anchorTopLeft&&this.anchorBottomRight){
    this.autoScaleAndPos(a);
  }else{
    var z=a.getZoomLevel();
    var b=(this.baseZoom?this.baseZoom:0);
    var m=1/Math.pow(2,z-b);
    var c=this.size;
    var zw=Math.floor(c.width*m);
    var zh=Math.floor(c.height*m);
    var x=document.getElementById(this.id);
    x.style.width=zw+'px';
    x.style.height=zh+'px';
    this.setPosition(a);
  }
}
TPhoto.prototype.setPosition=function(a){
  var d=this.anchorLatLng;
  var e=this.anchorPx;
  var bz=(this.baseZoom?this.baseZoom:0);
  var z=a.getZoomLevel();
  var m=1/Math.pow(2,z-bz);
  var zx=Math.floor(e.x*m);
  var zy=Math.floor(e.y*m);
  var b=this.getXY(a,d,z);
  var x=document.getElementById(this.id);
  x.style.top=b.y-zy+'px';
  x.style.left=b.x-zx+'px';
}
TPhoto.prototype.autoScaleAndPos=function(a){
  var b=this.anchorTopLeft;
  var c=this.anchorBottomRight;
  var z=a.getZoomLevel();
  var d=this.getXY(a,b,z);
  var e=this.getXY(a,c,z);
  var x=document.getElementById(this.id);
  x.style.top=d.y+'px';
  x.style.left=d.x+'px';
  x.style.width=e.x-d.x+'px';
  x.style.height=e.y-d.y+'px';
}
TPhoto.prototype.getXY=function(a,b,c){
  var e=a.spec.getBitmapCoordinate(b.y,b.x,c);
  return a.getDivCoordinate(e.x,e.y);
}
TPhoto.prototype.setOpacity=function(b){
  if(b<0){b=0;}  if(b>=100){b=100;}
  var c=b/100;
  var d=document.getElementById(this.id);
  if(typeof(d.style.filter)=='string'){d.style.filter='alpha(opacity:'+b+')';}
  if(typeof(d.style.KHTMLOpacity)=='string'){d.style.KHTMLOpacity=c;}
  if(typeof(d.style.MozOpacity)=='string'){d.style.MozOpacity=c;}
  if(typeof(d.style.opacity)=='string'){d.style.opacity=c;}
}
TPhoto.prototype.addTBug=function(a){
  if(a.TBugged==-1){
    document.getElementById('TPhotoBug').style.display='block';
  }else{
    var b=a.ownerDocument.createElement('div');
    b.id='TPhotoBug';
    b.style.position='absolute';
    b.style.right='0px';
    b.style.bottom='20px';
    b.style.backgroundColor='#f2efe9';
    b.style.zIndex=25500;
    b.innerHTML='<a href="http://gmaps.tommangan.us/tphoto.html" style="font: 10px verdana; text-decoration: none; padding: 2px; color: #000;">Made with TPhoto</a>';
    a.div.parentNode.appendChild(b);
    var c=0.7;
    var d=document.getElementById(b.id);
    if(typeof(d.style.filter)=='string'){d.style.filter='alpha(opacity:'+c*100+')';}
    if(typeof(d.style.KHTMLOpacity)=='string'){d.style.KHTMLOpacity=c;}
    if(typeof(d.style.MozOpacity)=='string'){d.style.MozOpacity=c;}
    if(typeof(d.style.opacity)=='string'){d.style.opacity=c;}
    a.TBugged=1;
  }
}
GMap.prototype.addTPhoto=function(a){
  a.initialize(this);
}
GMap.prototype.removeTPhoto=function(a){
  this.div.removeChild(document.getElementById(a.id));
  delete(a);
  if(this.TBugged){
    document.getElementById('TPhotoBug').style.display='none';
    this.TBugged=-1;
  }
}

