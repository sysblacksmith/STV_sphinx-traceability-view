from bs4 import BeautifulSoup
import pytest
from sphinx_traceability_view.details import transform, portable_url


@pytest.mark.requirements("STV_SWR_015", "STV_SWR_017", "STV_SWR_018", "STV_SWR_048", "STV_SWR_049")
def test_static_details_and_remote_fallback():
    markup = '''<table id="NEED"><tr><td><b>Rich text</b><script>bad()</script>
    <img src="../images/local.png" onerror="bad()"><img src="//example.org/picture.png">
    <video poster="https://example.org/poster.png"><source src="https://example.org/movie.mp4"></video>
    <svg><use href="https://example.org/symbol.svg#x"/></svg>
    <iframe src="https://example.org/widget"></iframe><object data="https://example.org/document"></object>
    <span style="background:url(https://example.org/background)">Static widget</span>
    <span class="traces"><a href="../other.html#HIDDEN">hidden reference</a></span><a href="javascript:bad()">unsafe</a>
    <a href="https://example.org/other.html#HIDDEN">Deliberately published prose reference</a>
    <a href="https://example.org/original">Original</a><label for="field">Name</label><input id="field">
    </td></tr></table>'''
    result = BeautifulSoup(transform(markup, "nested/needs.html", {"HIDDEN"}, {"traces"}), "html.parser")
    assert result.find("b").text == "Rich text"
    assert "Static widget" in result.text
    assert not result.find_all(["script", "iframe", "object"])
    assert not result.select("[onerror]")
    assert 'https:' not in ''.join(tag.get('style','') for tag in result.find_all(True))
    assert "hidden reference" not in result.text
    assert 'Deliberately published prose reference' in result.text
    assert result.find("img")["data-stv-src"] == "images/local.png"
    assert not result.find_all(src=lambda s: s and s.startswith("http"))
    assert "Resource unavailable offline" in result.text
    assert result.find("a", string="Original")["href"] == "https://example.org/original"
    assert not result.find("a", string="unsafe").has_attr("href")


@pytest.mark.requirements("STV_SWR_018")
def test_portable_paths_preserve_queries_and_fragments():
    assert portable_url("../images/a.png?v=1#part", "nested/page.html") == "images/a.png?v=1#part"
    assert portable_url("#section", "nested/page.html") == "nested/page.html#section"
    assert portable_url("../../outside.png", "page.html") is None


@pytest.mark.requirements('STV_SWR_015','STV_SWR_017','STV_SWR_018')
def test_srcset_data_images_and_css_resources():
    markup='''<div style="color:red;background-image:url(../images/local.png)"><img srcset="data:image/png;base64,AAAA 1x, ../images/two.png 2x, https://example.org/three.png 3x"><style>@import "https://example.org/remote.css"; .image {background: url(//example.org/remote.png)}</style></div>'''
    result=BeautifulSoup(transform(markup,'nested/page.html',set()),'html.parser')
    assert result.div['data-stv-style']=='color:red;background-image:url("images/local.png")'
    assert result.img['data-stv-srcset']=='data:image/png;base64,AAAA 1x, images/two.png 2x'
    assert '@import' not in result.style.text
    assert 'https:' not in result.style.text
    assert result.find('a',href='https://example.org/three.png')


@pytest.mark.requirements('STV_SWR_015','STV_SWR_017','STV_SWR_049')
def test_active_embed_urls_are_not_retained_as_navigation():
    markup='''<iframe src="data:text/html,&lt;script&gt;bad()&lt;/script&gt;"></iframe><script src="data:text/javascript,bad()"></script><object data="javascript:bad()"></object><img src="data:image/png;base64,AAAA">'''
    result=BeautifulSoup(transform(markup,'page.html',set()),'html.parser')
    assert not result.find_all(['iframe','script','object','a'])
    assert result.img['src']=='data:image/png;base64,AAAA'
