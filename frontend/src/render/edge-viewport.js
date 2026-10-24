// Keep every route inside the SVG viewport, including negative graph coordinates.
export function edgeViewport(geometry,padding=24) {
  let left=Infinity,top=Infinity,right=-Infinity,bottom=-Infinity;
  const include=([x,y])=>{left=Math.min(left,x);top=Math.min(top,y);right=Math.max(right,x);bottom=Math.max(bottom,y);};
  for(const node of geometry.nodes.values()) {include([node.x,node.y]);include([node.x+node.width,node.y+node.height]);}
  for(const edge of geometry.edges)for(const point of edge.points)include(point);
  if(left===Infinity)include([0,0]);
  return {x:left-padding,y:top-padding,width:right-left+padding*2,height:bottom-top+padding*2};
}
