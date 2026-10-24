"""Regenerate the editable behavioral overview from its documented transitions."""
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
file = ET.Element("mxfile", host="app.diagrams.net")
diagram = ET.SubElement(file, "diagram", id="behavior", name="Behavior")
model = ET.SubElement(diagram, "mxGraphModel", dx="1300", dy="1150", grid="1", page="1", pageWidth="1300", pageHeight="1320")
root = ET.SubElement(model, "root")
ET.SubElement(root, "mxCell", id="0")
ET.SubElement(root, "mxCell", id="1", parent="0")


def box(identity, title, x, y, link="state-machine.html", color="#dceaf7"):
    obj = ET.SubElement(root, "object", id=identity, label=title, link=link, linkTarget="_top")
    cell = ET.SubElement(obj, "mxCell", vertex="1", parent="1", style=f"rounded=1;whiteSpace=wrap;html=0;fillColor={color};strokeColor=#425466;fontSize=16;spacing=10;")
    ET.SubElement(cell, "mxGeometry", x=str(x), y=str(y), width="260", height="95", **{"as": "geometry"})


def edge(identity, source, target, title, points=()):
    cell = ET.SubElement(root, "mxCell", id=identity, value=title, source=source, target=target, edge="1", parent="1", style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=0;endArrow=block;fontSize=13;labelBackgroundColor=#ffffff;")
    geometry = ET.SubElement(cell, "mxGeometry", relative="1", **{"as": "geometry"})
    if points:
        array = ET.SubElement(geometry, "Array", **{"as": "points"})
        for x, y in points:
            ET.SubElement(array, "mxPoint", x=str(x), y=str(y))
    return cell


box("collection", "BUILD: collected invocations\nsource locations + distinct seeds", 30, 40, "elements-software.html#STV_SWE_DIRECTIVE")
box("pending", "BUILD: pending pages\nvalidated immutable snapshot", 490, 40, "elements-software.html#STV_SWE_GRAPH")
box("final", "BUILD: finalized bundle\ncontent-addressed graph + details", 950, 40, "elements-software.html#STV_SWE_BUNDLE")
box("buildfailed", "BUILD: failed\nno finalized new view", 490, 230, color="#f8dfdf")
edge("b1", "collection", "pending", "write-started\nvalid graph inputs")
edge("b2", "pending", "final", "build-finished\nfragments emitted")
edge("b3", "pending", "buildfailed", "extraction or write failure")
edge("b4", "collection", "buildfailed", "invalid builder, model or seed", [(160, 277)])
box("committed", "VIEW: committed\nseeds or active project page", 30, 450, "elements-software.html#STV_SWE_STATE")
box("candidate", "VIEW: candidate\nrooted reachability; cap <= 200", 490, 450, "requirements-software.html#STV_SWR_043")
box("layout", "VIEW: laying out\nfresh placement / stable slots", 950, 450, "elements-software.html#STV_SWE_LAYOUT")
edge("v1", "committed", "candidate", "group/root toggle, page,\nconfirmed seed or overview")
edge("v2", "candidate", "layout", "valid complete candidate")
v3 = edge("v3", "candidate", "committed", "reject / retain graph, page + focus", [(620, 610), (238, 610)])
v3.set("style", v3.get("style") + "exitX=0.5;exitY=1;entryX=0.8;entryY=1;")
v4 = edge("v4", "layout", "committed", "current result / commit; fit initial, seed, overview or page", [(1041, 670), (160, 670)])
v4.set("style", v4.get("style") + "exitX=0.35;exitY=1;entryX=0.5;entryY=1;")
v5 = edge("v5", "layout", "committed", "failure / preserve scene + announce retry", [(1145, 730), (82, 730)])
v5.set("style", v5.get("style") + "exitX=0.75;exitY=1;entryX=0.2;entryY=1;")
viewport = edge("v6", "committed", "committed", "pan / zoom / focus\nshared transform", [(360, 469), (360, 350), (160, 350)])
viewport.set("style", viewport.get("style") + "exitX=1;exitY=0.2;entryX=0.5;entryY=0;")
box("seedinput", "SEED INPUT: editing / matches\ninvalid ID retains committed view", 950, 230, "requirements-software.html#STV_SWR_057")
edge("s1", "seedinput", "candidate", "exact existing ID / fresh single seed", [(1080, 400), (620, 400)])
box("closed", "DETAILS: closed\nno panel or position listeners", 30, 880, "elements-software.html#STV_SWE_INSPECT")
box("loading", "DETAILS: loading\nlocal classic script; build-keyed cache", 490, 880, "requirements-software.html#STV_SWR_017")
box("open", "DETAILS: open or error\nstatic rich body / explicit failure", 950, 880, "requirements-software.html#STV_SWR_050")
box("hover", "DETAILS: hover pending\n1000 ms continuous node hover", 30, 1160, "requirements-software.html#STV_SWR_050")
hover_start = edge("dh1", "closed", "hover", "hover / start timer")
hover_start.find("mxGeometry").set("x", "-0.6")
edge("dh2", "hover", "closed", "cancel hover", [(10, 1207), (10, 927)])
dh3 = edge("dh3", "hover", "loading", "1000 ms or explicit Details", [(1300, 1207), (1300, 820), (620, 820)])
dh3.set("style", dh3.get("style") + "exitX=1;exitY=0.5;entryX=0.5;entryY=0;")
edge("d1", "closed", "loading", "explicit Details / immediate")
edge("d2", "loading", "open", "current token\nfragment or error")
d3 = edge("d3", "open", "closed", "Escape, Close, departure, scene or viewport change", [(1080, 1070), (238, 1070)])
d3.set("style", d3.get("style") + "exitX=0.5;exitY=1;entryX=0.8;entryY=1;")
d4 = edge("d4", "loading", "closed", "dismiss / invalidate pending completion", [(620, 1020), (277, 1020)])
d4.set("style", d4.get("style") + "exitX=0.5;exitY=1;entryX=0.95;entryY=1;")
ET.indent(file)
ET.ElementTree(file).write(ROOT / "docs/architecture/diagrams/state-machine.drawio", encoding="utf-8", xml_declaration=True)
